from botocore.exceptions import ClientError
import logging


logger = logging.getLogger(__name__)


def add_config(table, meter_size: str, project: str, config: dict):
    try:
        table.put_item(
            Item={
                'meterSize': meter_size,
                'projectName': project,
                'configuration': config})
    except ClientError as err:
        logger.error(
            "Couldn't add movie %s to table %s. Here's why: %s: %s",
            meter_size, table.name,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise
