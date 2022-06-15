from decimal import Decimal
from botocore.exceptions import ClientError
import logging


logger = logging.getLogger(__name__)

def add_movie(table, title, year, plot, rating):
    """
    Adds a movie to the table.
    :param title: The title of the movie.
    :param year: The release year of the movie.
    :param plot: The plot summary of the movie.
    :param rating: The quality rating of the movie.
    """
    try:
        table.put_item(
            Item={
                'year': year,
                'title': title,
                'info': {'plot': plot, 'rating': Decimal(str(rating))}})
    except ClientError as err:
        logger.error(
            "Couldn't add movie %s to table %s. Here's why: %s: %s",
            title, table.name,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise


def update_movie(table, title, year, plot, rating):
    """
    Updates rating and plot data for a movie in the table.
    :param title: The title of the movie to update.
    :param year: The release year of the movie to update.
    :param rating: The updated rating to the give the movie.
    :param plot: The updated plot summary to give the movie.
    :return: The fields that were updated, with their new values.
    """
    try:
        response = table.update_item(
            Key={'year': year, 'title': title},
            UpdateExpression="set info.rating=:r, info.plot=:p",
            ExpressionAttributeValues={
                ':r': Decimal(str(rating)), ':p': plot},
            ReturnValues="UPDATED_NEW")
    except ClientError as err:
        logger.error(
            "Couldn't update movie %s in table %s. Here's why: %s: %s",
            title, table.name,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    else:
        return response['Attributes']