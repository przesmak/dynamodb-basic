from tables.create_table import create_movie_table
from tables.add_movie import add_movie, update_movie
import boto3
from tables.get_movie import get_movie

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
    try: 
        movie_table = create_movie_table(dynamodb)
        print("Table status:", movie_table.table_status)
    except: 
        movie_table = dynamodb.Table("Movies")
        movie_table.load()
    add_movie(movie_table, "some title", 220, {"key": "value", "key2": "value2"}, 2222)
    update_movie(movie_table, "some title", 220, {"key": "value", "key2": "value2", "key3": "value3"}, 5)
    response = get_movie(movie_table, "some title", 220)
    print(response)