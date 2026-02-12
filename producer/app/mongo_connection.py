import pymongo
def connect():
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["mydatabase"]
    my_col = my_db["customers"]
    return my_col

def insert(my_col):
    with open("suspicious_customers_orders.json", "r") as file:
        my_list = file.read()
        my_col.insert_many(my_list)

