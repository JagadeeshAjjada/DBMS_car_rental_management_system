from db_config import get_connection
from datetime import datetime
from car_module import update_car_status


def add_rental(car_id, customer_id, start_date, end_date, price_per_day):
    conn = get_connection()
    cur = conn.cursor()

    # Calculate total cost
    fmt = "%Y-%m-%d"
    days = (datetime.strptime(end_date, fmt) - datetime.strptime(start_date, fmt)).days
    total_cost = float(price_per_day) * days

    # Insert into Rental table
    sql = """
        INSERT INTO Rental (CarID, CustomerID, StartDate, EndDate, TotalCost)
        VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(sql, (car_id, customer_id, start_date, end_date, total_cost))

    # Update car status to 'Rented'
    cur.execute("UPDATE Car SET Status = 'Rented' WHERE CarID = %s", (car_id,))

    conn.commit()
    cur.close()
    conn.close()


def get_all_rentals():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Rental.RentalID, Car.Model, Customer.Name, StartDate, EndDate, TotalCost, RentalStatus
        FROM Rental
        JOIN Car ON Rental.CarID = Car.CarID
        JOIN Customer ON Rental.CustomerID = Customer.CustomerID
        ORDER BY RentalID ASC
    """)
    rentals = cur.fetchall()
    cur.close()
    conn.close()
    return rentals


def update_rental_status(rental_id, new_status):
    conn = get_connection()
    cur = conn.cursor()

    # Update rental status
    cur.execute("UPDATE Rental SET RentalStatus = %s WHERE RentalID = %s", (new_status, rental_id))

    # If finished, update car to Available
    if new_status.lower() == "finished":
        # Get CarID linked to this rental
        cur.execute("SELECT CarID FROM Rental WHERE RentalID = %s", (rental_id,))
        car_id = cur.fetchone()[0]
        update_car_status(car_id, "Available")

    # If ongoing, update car to Rented
    if new_status.lower() == "ongoing":
        # Get CarID linked to this rental
        cur.execute("SELECT CarID FROM Rental WHERE RentalID = %s", (rental_id,))
        car_id = cur.fetchone()[0]
        update_car_status(car_id, "Rented")

    conn.commit()
    cur.close()
    conn.close()

