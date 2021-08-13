from inventory import *
import requests

inventory = Inventory()
url = "http://127.0.0.1:5000/api/all_cars"


def test_get_no_cars():
    response = requests.get(url)
    assert response.json() == []


def test_get_cars():
    requests.post("http://127.0.0.1:5000/api/purchase_car", json={'Manufacture': 'Toyota',
                                                                  'Manufacture price': 100,
                                                                  'Manufacture year': 1980,
                                                                  'car id': 465})

    requests.post("http://127.0.0.1:5000/api/purchase_car", json={'Manufacture': 'Ford',
                                                                  'Manufacture price': 20,
                                                                  'Manufacture year': 1995,
                                                                  'car id': 57})

    requests.post("http://127.0.0.1:5000/api/purchase_car", json={'Manufacture': 'Audi',
                                                                  'Manufacture price': 500,
                                                                  'Manufacture year': 2013,
                                                                  'car id': 4})

    requests.post("http://127.0.0.1:5000/api/purchase_car", json={'Manufacture': 'Subaru',
                                                                  'Manufacture price': 400,
                                                                  'Manufacture year': 2015,
                                                                  'car id': 22})
    response = requests.get(url)
    assert response.json() == [{'Manufacture': 'Toyota',
                                'Manufacture price': 100,
                                'Manufacture year': 1980,
                                'car id': 465},
                               {'Manufacture': 'Ford',
                                'Manufacture price': 20,
                                'Manufacture year': 1995,
                                'car id': 57},
                               {'Manufacture': 'Audi',
                                'Manufacture price': 500,
                                'Manufacture year': 2013,
                                'car id': 4},
                               {'Manufacture': 'Subaru',
                                'Manufacture price': 400,
                                'Manufacture year': 2015,
                                'car id': 22}]
