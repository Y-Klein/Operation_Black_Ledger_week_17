import pymongo
import json



def connect():
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["mydatabase"]
    my_col = my_db["customers"]
    return my_col

def insert(my_col,file):
        my_list = json.loads(file.read())
        my_col.insert_many(my_list)

