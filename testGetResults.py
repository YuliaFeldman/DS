from inventory import *
import requests

inventory = Inventory()
url = "http://127.0.0.1:5000/api/results"


def test_get_result_zero():
    response = requests.get(url)
    assert response.json() == 0


def test_get_result_negative():
    requests.post("http://127.0.0.1:5000/api/purchase_car", json={'Manufacture': 'Toyota',
                                                                  'Manufacture price': 100,
                                                                  'Manufacture year': 1980,
                                                                  'car id': 465})
    response = requests.get(url)
    assert response.json() == -100


def test_get_result_positive():
    requests.put("http://127.0.0.1:5000/api/sell_car/465", json={'car selling price': 500})
    response = requests.get(url)
    assert response.json() == 400


def test_get_result_complex():
    requests.post("http://127.0.0.1:5000/api/purchase_car", json={'Manufacture': 'Toyota',
                                                                  'Manufacture price': 700,
                                                                  'Manufacture year': 2020,
                                                                  'car id': 1})

    requests.post("http://127.0.0.1:5000/api/purchase_car", json={'Manufacture': 'Toyota',
                                                                  'Manufacture price': 1000,
                                                                  'Manufacture year': 2020,
                                                                  'car id': 2})

    requests.put("http://127.0.0.1:5000/api/sell_car/1", json={'car selling price': 1500})
    requests.post("http://127.0.0.1:5000/api/purchase_car", json={'Manufacture': 'Toyota',
                                                                  'Manufacture price': 100,
                                                                  'Manufacture year': 1980,
                                                                  'car id': 3})
    requests.put("http://127.0.0.1:5000/api/sell_car/2", json={'car selling price': 2000})

    response = requests.get(url)
    assert response.json() == 2100


