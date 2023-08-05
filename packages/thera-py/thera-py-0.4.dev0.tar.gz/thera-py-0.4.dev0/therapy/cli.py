"""This module provides a CLI util to make updates to normalizer database."""
from os import environ
import logging
from timeit import default_timer as timer
from typing import List, Optional

import click
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from disease.database import Database as DiseaseDatabase
from disease.cli import CLI as DiseaseCLI
from disease.schemas import SourceName as DiseaseSources

from therapy import SOURCES_CLASS, SOURCES
from therapy.schemas import SourceName
from therapy.database import Database, confirm_aws_db_use
from therapy.etl.merge import Merge

logger = logging.getLogger("therapy")
logger.setLevel(logging.DEBUG)


class CLI:
    """Class for updating the normalizer database via Click"""

    @staticmethod
    @click.command()
    @click.option(
        "--normalizer",
        help="The normalizer(s) you wish to update separated by spaces."
    )
    @click.option(
        "--prod",
        is_flag=True,
        help="Working in production environment."
    )
    @click.option(
        "--db_url",
        help="URL endpoint for the application database."
    )
    @click.option(
        "--update_all",
        is_flag=True,
        help="Update all normalizer sources."
    )
    @click.option(
        "--update_merged",
        is_flag=True,
        help="Update concepts for normalize endpoint from accepted sources."
    )
    @click.option(
        "--use_existing",
        is_flag=True,
        default=False,
        help="Use most recent existing source data instead of fetching latest version"
    )
    def update_normalizer_db(normalizer: str, prod: bool, db_url: str,
                             update_all: bool, update_merged: bool,
                             use_existing: bool) -> None:
        """Update selected normalizer source(s) in the therapy database.
        \f  # noqa: D301
        :param str normalizer: comma-separated string listing source names
        :param bool prod: if true, utilize production environment settings
        :param str db_url: DynamoDB endpoint URL (usually only needed locally)
        :param bool update_all: if true, update all sources
        :param bool update_merged: if true, update normalized group results
        :param bool use_existing: if true, don't try to fetch latest source data
        """
        # Sometimes THERAPY_NORM_EB_PROD is accidentally set. We should verify that
        # it should actually be used in CLI
        if "THERAPY_NORM_EB_PROD" in environ:
            confirm_aws_db_use("PROD")

        endpoint_url = None
        if prod:
            environ["THERAPY_NORM_PROD"] = "TRUE"
            environ["DISEASE_NORM_PROD"] = "TRUE"
            db: Database = Database()
        else:
            if db_url:
                endpoint_url = db_url
            elif "THERAPY_NORM_DB_URL" in environ.keys():
                endpoint_url = environ["THERAPY_NORM_DB_URL"]
            else:
                endpoint_url = "http://localhost:8000"
            db = Database(db_url=endpoint_url)

        if update_all:
            normalizers = list(src for src in SOURCES)
            CLI()._check_disease_normalizer(normalizers, endpoint_url)
            CLI()._update_normalizers(normalizers, db, update_merged, use_existing)
        elif not normalizer:
            if update_merged:
                CLI()._update_merged(db, [])
            else:
                CLI()._help_msg()
        else:
            normalizers = str(normalizer).lower().split()

            if len(normalizers) == 0:
                CLI()._help_msg()

            non_sources = set(normalizers) - {src for src in SOURCES}

            if len(non_sources) != 0:
                raise Exception(f"Not valid source(s): {non_sources}")

            CLI()._check_disease_normalizer(normalizers, endpoint_url)
            CLI()._update_normalizers(normalizers, db, update_merged, use_existing)

    def _check_disease_normalizer(self, normalizers: List[str],
                                  endpoint_url: Optional[str]) -> None:
        """When loading HemOnc source, perform rudimentary check of Disease Normalizer
        tables, and reload them if necessary. This reload method should never be used
        (and is restricted from use) in a production setting.

        :param List[str] normalizers: List of sources to load
        :param Optional[str] endpoint_url: Therapy endpoint URL. This should always be
            a local address.
        """
        if "hemonc" in normalizers and "THERAPY_NORM_PROD" not in environ:
            db = DiseaseDatabase(db_url=endpoint_url)  # type: ignore
            current_tables = {table.name for table in db.dynamodb.tables.all()}
            if ("disease_concepts" not in current_tables) or \
                    ("disease_metadata" not in current_tables) or \
                    (db.diseases.scan()["Count"] == 0) or \
                    (db.metadata.scan()["Count"] < len(DiseaseSources)):

                msg = "Disease Normalizer not loaded. Loading now..."
                logger.debug(msg)
                click.echo(msg)
                try:
                    DiseaseCLI().update_normalizer_db(
                        ["--update_all", "--update_merged", "--db_url", endpoint_url]
                    )
                except Exception as e:
                    logger.error(e)
                    raise Exception(e)
                except:  # noqa: E722
                    # TODO: what does this do?
                    pass
                msg = "Disease Normalizer reloaded successfully."
                logger.debug(msg)
                click.echo(msg)

    @staticmethod
    def _help_msg() -> None:
        """Display help message."""
        ctx = click.get_current_context()
        click.echo(
            "Must either enter 1 or more sources, or use `--update_all` parameter")
        click.echo(ctx.get_help())
        ctx.exit()

    @staticmethod
    def _update_normalizers(normalizers: List[str], db: Database,
                            update_merged: bool, use_existing: bool) -> None:
        """Update selected normalizer sources.
        :param List[str] normalizers: list of source names to update
        :param Database db: database instance to use
        :param bool update_merged: if true, store concept IDs as they're processed and
            produce normalized records
        :param bool use_existing: if true, don't try to fetch latest source data in
            source perform_etl methods
        """
        processed_ids = list()
        for n in normalizers:
            msg = f"Deleting {n}..."
            click.echo(f"\n{msg}")
            logger.info(msg)

            start_delete = timer()
            CLI()._delete_data(n, db)
            end_delete = timer()
            delete_time = end_delete - start_delete

            msg = f"Deleted {n} in {delete_time:.5f} seconds."
            click.echo(f"{msg}\n")
            logger.info(msg)

            msg = f"Loading {n}..."
            click.echo(msg)
            logger.info(msg)

            start_load = timer()
            source = SOURCES_CLASS[n](database=db)
            try:
                processed_ids += source.perform_etl(use_existing)
            except FileNotFoundError as e:
                if use_existing:
                    if click.confirm(
                        f"Encountered FileNotFoundError while loading {n}: "
                        f"{e.args[0] if len(e.args) > 0 else ''}\n"
                        "Attempt to retrieve latest version from source? "
                    ):
                        processed_ids += source.perform_etl()
                    else:
                        raise e
            end_load = timer()
            load_time = end_load - start_load

            msg = f"Loaded {n} in {load_time:.5f} seconds."
            click.echo(msg)
            logger.info(msg)

            msg = f"Total time for {n}: " \
                  f"{(delete_time + load_time):.5f} seconds."
            click.echo(msg)
            logger.info(msg)

        if update_merged:
            CLI()._update_merged(db, processed_ids)

    def _update_merged(self, db: Database, processed_ids: List[str]) -> None:
        """Build and upload merged records. Will construct list of IDs if given an empty
        processed_ids list.
        :param Database db: DB instance to use
        :param List[str] processed_ids: List of IDs to create merged groups from
        """
        start_merge = timer()
        if not processed_ids:
            CLI()._delete_normalized_data(db)
            processed_ids = db.get_ids_for_merge()
        merge = Merge(database=db)
        click.echo("Constructing normalized records...")
        merge.create_merged_concepts(set(processed_ids))
        end_merge = timer()
        click.echo(f"Merged concept generation completed in"
                   f" {(end_merge - start_merge):.5f} seconds.")

    @staticmethod
    def _delete_normalized_data(database: Database) -> None:
        click.echo("\nDeleting normalized records...")
        start_delete = timer()
        try:
            while True:
                with database.therapies.batch_writer(
                        overwrite_by_pkeys=["label_and_type", "concept_id"]) \
                        as batch:
                    response = database.therapies.query(
                        IndexName="item_type_index",
                        KeyConditionExpression=Key("item_type").eq("merger"),
                    )
                    records = response["Items"]
                    if not records:
                        break
                    for record in records:
                        batch.delete_item(Key={
                            "label_and_type": record["label_and_type"],
                            "concept_id": record["concept_id"]
                        })
        except ClientError as e:
            click.echo(e.response["Error"]["Message"])
        end_delete = timer()
        delete_time = end_delete - start_delete
        click.echo(f"Deleted normalized records in {delete_time:.5f} seconds.")

    @staticmethod
    def _delete_data(source: str, database: Database) -> None:
        """Delete all data (records + metadata) from given source in database.
        :param str source: name of source to delete
        :param Database database: db instance
        """
        source_name = SourceName[f"{source.upper()}"].value
        # Delete source"s metadata first
        try:
            metadata = database.metadata.query(
                KeyConditionExpression=Key(
                    "src_name").eq(source_name)
            )
            if metadata["Items"]:
                database.metadata.delete_item(
                    Key={"src_name": metadata["Items"][0]["src_name"]},
                    ConditionExpression="src_name = :src",
                    ExpressionAttributeValues={
                        ":src": source_name}
                )
        except ClientError as e:
            click.echo(e.response["Error"]["Message"])

        try:
            while True:
                response = database.therapies.query(
                    IndexName="src_index",
                    KeyConditionExpression=Key("src_name").eq(
                        source_name),
                )

                records = response["Items"]
                if not records:
                    break

                with database.therapies.batch_writer(
                        overwrite_by_pkeys=["label_and_type", "concept_id"]) as batch:

                    for record in records:
                        batch.delete_item(
                            Key={
                                "label_and_type": record["label_and_type"],
                                "concept_id": record["concept_id"]
                            }
                        )
        except ClientError as e:
            click.echo(e.response["Error"]["Message"])


if __name__ == "__main__":
    CLI().update_normalizer_db()  # type: ignore
