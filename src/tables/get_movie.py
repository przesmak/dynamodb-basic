from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def get_movie(table, title, year):
    """
    Gets movie data from the table for a specific movie.
    :param title: The title of the movie.
    :param year: The release year of the movie.
    :return: The data about the requested movie.
    """
    try:
        response = table.get_item(Key={'year': year, 'title': title})
    except ClientError as err:
        logger.error(
            "Couldn't get movie %s from table %s. Here's why: %s: %s",
            title, table.name,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    else:
        return response['Item']