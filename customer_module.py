from db_config import get_connection


def add_customer(name, contact, license_number):
    conn = get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO Customer (Name, Contact, LicenseNumber) VALUES (%s, %s, %s)"
    cur.execute(sql, (name, contact, license_number))
    conn.commit()
    cur.close()
    conn.close()


def get_all_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Customer ORDER BY CustomerID ASC")
    customers = cur.fetchall()
    cur.close()
    conn.close()
    return customers


def update_customer(customer_id, name, contact, license_number):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Customer
        SET Name = %s, Contact = %s, LicenseNumber = %s
        WHERE CustomerID = %s
    """, (name, contact, license_number, customer_id))
    conn.commit()
    cur.close()
    conn.close()


def delete_customer(customer_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Customer WHERE CustomerID = %s", (customer_id,))
    conn.commit()
    cur.close()
    conn.close()
