from db_config import get_connection


def add_car(model, brand, year, price_per_day, status):
    conn = get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO Car (Model, Brand, Year, PricePerDay, Status) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql, (model, brand, year, price_per_day, status))
    conn.commit()
    cur.close()
    conn.close()


def get_all_cars():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Car ORDER BY CarID ASC")
    cars = cur.fetchall()
    cur.close()
    conn.close()
    return cars


def update_car_status(car_id, new_status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Car SET Status = %s WHERE CarID = %s", (new_status, car_id))
    conn.commit()
    cur.close()
    conn.close()


def update_car(car_id, model, brand, year, price_per_day, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Car
        SET Model = %s, Brand = %s, Year = %s, PricePerDay = %s, Status = %s
        WHERE CarID = %s
    """, (model, brand, year, price_per_day, status, car_id))
    conn.commit()
    cur.close()
    conn.close()


def delete_car(car_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Car WHERE CarID = %s", (car_id,))
    conn.commit()
    cur.close()
    conn.close()
