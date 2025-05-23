from db_config import get_connection


def add_payment(rental_id, amount, method, status):
    conn = get_connection()
    cur = conn.cursor()
    sql = """
        INSERT INTO Payment (RentalID, Amount, PaymentMethod, PaymentStatus)
        VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (rental_id, amount, method, status))
    conn.commit()
    cur.close()
    conn.close()


def get_all_payments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT PaymentID, Rental.RentalID, Customer.Name, Amount, PaymentMethod, PaymentStatus
        FROM Payment
        JOIN Rental ON Payment.RentalID = Rental.RentalID
        JOIN Customer ON Rental.CustomerID = Customer.CustomerID
        ORDER BY PaymentID ASC
    """)
    payments = cur.fetchall()
    cur.close()
    conn.close()
    return payments


def get_rentals_for_payment():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Rental.RentalID, Car.Model, Customer.Name, Rental.TotalCost
        FROM Rental
        JOIN Car ON Rental.CarID = Car.CarID
        JOIN Customer ON Rental.CustomerID = Customer.CustomerID
        ORDER BY RentalID DESC
    """)
    rentals = cur.fetchall()
    cur.close()
    conn.close()
    return rentals


def update_payment_status(payment_id, new_status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Payment SET PaymentStatus = %s WHERE PaymentID = %s", (new_status, payment_id))
    conn.commit()
    cur.close()
    conn.close()
