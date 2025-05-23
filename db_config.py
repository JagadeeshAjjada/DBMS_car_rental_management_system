import mysql.connector
from mysql.connector import Error


def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='car_rental_management_system',
            user='root',
            password='Root@1234'
        )
        return connection
    except Error as e:
        print("❌ Error connecting to MySQL:", e)
        return None
