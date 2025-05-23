from flask import Flask, render_template, request, redirect
from car_module import add_car, get_all_cars, update_car, delete_car
from customer_module import add_customer, get_all_customers, update_customer, delete_customer
from rental_module import add_rental, get_all_rentals
from payment_module import add_payment, get_all_payments, get_rentals_for_payment, update_payment_status
from rental_module import update_rental_status

app = Flask(__name__)


@app.route('/')
def index():
    cars = get_all_cars()
    available_cars = [car for car in cars if car[5] == "Available"]
    customers = get_all_customers()
    rentals = get_all_rentals()
    payments = get_all_payments()
    rental_options = get_rentals_for_payment()
    return render_template('index.html', cars=cars, customers=customers,
                           available_cars=available_cars, rentals=rentals,
                           payments=payments, rental_options=rental_options)


@app.route('/add_car', methods=['POST'])
def add_car_route():
    model = request.form['model']
    brand = request.form['brand']
    year = int(request.form['year'])
    price = float(request.form['price_per_day'])
    status = request.form['status']
    add_car(model, brand, year, price, status)
    return redirect('/')


@app.route('/edit_car', methods=['POST'])
def edit_car():
    data = request.form
    update_car(data['car_id'], data['model'], data['brand'], data['year'], data['price_per_day'], data['status'])
    return redirect('/')


@app.route('/delete_car/<int:car_id>')
def delete_car_route(car_id):
    delete_car(car_id)
    return redirect('/')


@app.route('/add_customer', methods=['POST'])
def add_customer_route():
    name = request.form['name']
    contact = request.form['contact']
    license_number = request.form['license_number']
    add_customer(name, contact, license_number)
    return redirect('/')


@app.route('/edit_customer', methods=['POST'])
def edit_customer():
    data = request.form
    update_customer(data['customer_id'], data['name'], data['contact'], data['license_number'])
    return redirect('/')


@app.route('/delete_customer/<int:customer_id>')
def delete_customer_route(customer_id):
    delete_customer(customer_id)
    return redirect('/')


@app.route('/add_rental', methods=['POST'])
def add_rental_route():
    car_id = request.form['car_id']
    customer_id = request.form['customer_id']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    price_per_day = request.form['price_per_day']
    add_rental(car_id, customer_id, start_date, end_date, price_per_day)
    return redirect('/')


@app.route('/update_rental_status', methods=['POST'])
def update_rental_status_route():
    rental_id = request.form['rental_id']
    new_status = request.form['new_status']
    update_rental_status(rental_id, new_status)
    return redirect('/')


@app.route('/add_payment', methods=['POST'])
def add_payment_route():
    rental_id = request.form['rental_id']
    amount = request.form['amount']
    method = request.form['method']
    status = request.form['status']
    add_payment(rental_id, amount, method, status)
    return redirect('/')


@app.route('/update_payment_status', methods=['POST'])
def update_payment_status_route():
    payment_id = request.form['payment_id']
    new_status = request.form['new_status']
    update_payment_status(payment_id, new_status)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
