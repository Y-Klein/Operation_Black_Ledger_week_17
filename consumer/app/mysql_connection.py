import mysql.connector


def connect():
    mydb = mysql.connector.connect(
      host="mysql",
      user="admin",
      database="project"
    )
    return mydb




def create_tables(my_cursor):
    my_cursor.execute("""CREATE TABLE customers (
    customerNumber INT,
    customerName VARCHAR(255),
    contactLastName VARCHAR(255),
    contactFirstName VARCHAR(255),
    phone VARCHAR(255),
    addressLine1 VARCHAR(255),
    addressLine2 VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    postalCode VARCHAR(255),
    country VARCHAR(255),
    salesRepEmployeeNumber INT ,
    creditLimit VARCHAR(255),
    PRIMARY KEY (customerNumber)
    );
    
    CREATE TABLE orders (
    orderNumber INT,
    orderDate VARCHAR(255),
    requiredDate VARCHAR(255),
    shippedDate VARCHAR(255),
    status VARCHAR(255),
    comments VARCHAR(255),
    customerNumber INT,
    PRIMARY KEY (orderNumber),
    FOREIGN KEY (customerNumber) REFERENCES customers (customerNumber)
    );

    """)
def insert_customer(my_cursor,mydb,customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit):
    my_cursor.execute("""
    INSERT INTO customers (
    customerNumber, customerName,contactLastName,contactFirstName,
    phone,addressLine1,addressLine2,city,state,postalCode,
    country,salesRepEmployeeNumber,creditLimit) 
    VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,[customerNumber,customerName,contactLastName,contactFirstName,
         phone,addressLine1,addressLine2,city,state,postalCode,
         country,salesRepEmployeeNumber,creditLimit])
    mydb.commit()

def insert_order(my_cursor,mydb,orderNumber,orderDate,requiredDate,shippedDate,status,comments,customerNumber):
    my_cursor.execute("""INSERT INTO orders (
    orderNumber,orderDate,requiredDate,shippedDate,
    status,comments,customerNumber)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """,[orderNumber,orderDate,requiredDate,shippedDate,
         status,comments,customerNumber])
    mydb.commit()



