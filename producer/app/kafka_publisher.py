import json
from confluent_kafka import Producer
from mongo_connection import *

my_col = connect()
insert(my_col)



producer = Producer({"bootstrap.servers": "producer:9092"})

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode("utf-8")}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

counter = 0
while my_col.find():
    mongo_list = my_col.find().skip(counter).limit(30)
    counter += 30
    for order in mongo_list:
        value = json.dumps(order).encode("utf-8")
        producer.produce(
            topic="orders_and_customers",
            value=value,
            callback=delivery_report
        )
        producer.flush()
