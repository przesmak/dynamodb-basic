from botocore.exceptions import ClientError


def query_movies(table, year):
    """
    Queries for movies that were released in the specified year.
    :param year: The year to query.
    :return: The list of movies that were released in the specified year.
    """
    try:
        response = table.query(KeyConditionExpression=Key('year').eq(year))
    except ClientError as err:
        logger.error(
            "Couldn't query for movies released in %s. Here's why: %s: %s", year,
            err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    else:
        return response['Items']