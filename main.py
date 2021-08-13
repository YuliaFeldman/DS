from inventory import *
from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = Inventory()

"""This is a small service which will help car agencies to manage their inventory"""


@app.post("/api/purchase_car")
def purchase_car():
    """
    Purchase a car with the following parameters: manufacture (string), manufacture price (integer),
    manufacture year (integer), car id (integer)
    :return: response status 200
    """
    car = from_json(request.get_json())
    inventory.purchase_car(car)
    resp = jsonify(success=True)
    return resp


@app.put("/api/sell_car/<car_id>")
def sell_car(car_id):
    """
    Sell a car with the following parameters: car id(string), selling price(integer)
    :param car_id: id of a sold car
    :return: response status 200
    """
    sold_car_id = int(f'{car_id}')
    selling_price = request.get_json()["car selling price"]
    inventory.sell_car(sold_car_id, selling_price)
    resp = jsonify(success=True)
    return resp


@app.get("/api/all_cars")
def get_all_cars():
    """
    Return a sorted list (by purchase date) of all the cars which are currently found in
    the inventory (Excluding the cars we sold).
    :return: response status 200. The response contains a list of cars.
    """
    cars = inventory.get_all_cars()
    return jsonify([car.to_json() for car in cars])


@app.get("/api/results")
def get_results():
    """
    Get total profit
    :return: response status 200. The response is the total profit
    """
    return str(inventory.get_total_profit())
