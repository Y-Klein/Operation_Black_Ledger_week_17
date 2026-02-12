import json
from  mysql_connection import *
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "kafka:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

mydb = connect()
my_cursor = mydb.cursor()
create_tables(my_cursor)
consumer = Consumer(consumer_config)

consumer.subscribe(["orders_and_customers"])

print("🟢 Consumer is running and subscribed to orders_and_customers topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        unit = json.loads(value)
        if unit["type"] == "customer":
            insert_customer(my_cursor,mydb,unit["customerNumber"],unit["customerName"],unit["contactLastName"],unit["contactFirstName"],unit["phone"],unit["addressLine1"],unit["addressLine2"],unit["city"],unit["state"],unit["postalCode"],unit["country"],unit["salesRepEmployeeNumber"],unit["creditLimit"])
        elif unit["type"] == "order":
            insert_order(my_cursor,mydb,unit["orderNumber"],unit["orderDate"],unit["requiredDate"],unit["shippedDate"],unit["status"],unit["comments"],unit["customerNumber"])

except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()
