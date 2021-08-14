import unittest
from main import app


class TestCaseGetNoCars(unittest.TestCase):

    # Check for response 200
    def test_response_status(self):
        tester = app.test_client(self)
        response = tester.get("/api/all_cars")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for data returned
    def test_response_data(self):
        tester = app.test_client(self)
        response = tester.get("/api/all_cars")
        self.assertEqual(response.get_json(), [])


class TestCaseGetSingleCar(unittest.TestCase):

    # Check for response 200
    def test_response_status(self):
        tester = app.test_client(self)
        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 1})
        response = tester.get("/api/all_cars")
        self.assertEqual(response.status_code, 200)

    # check for data returned
    def test_response_data(self):
        tester = app.test_client(self)
        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 1})
        response = tester.get("/api/all_cars")
        self.assertEqual(response.get_json(), [{'Manufacture': 'Toyota',
                                                'Manufacture price': 100,
                                                'Manufacture year': 1980,
                                                'car id': 1}])


class TestCaseGetManyCars(unittest.TestCase):

    # Check for response 200
    def test_response_status(self):
        tester = app.test_client(self)
        tester.post("/api/purchase_car", json={'Manufacture': 'Ford',
                                               'Manufacture price': 20,
                                               'Manufacture year': 1995,
                                               'car id': 2})

        tester.post("/api/purchase_car", json={'Manufacture': 'Audi',
                                               'Manufacture price': 500,
                                               'Manufacture year': 2013,
                                               'car id': 3})

        tester.post("/api/purchase_car", json={'Manufacture': 'Subaru',
                                               'Manufacture price': 400,
                                               'Manufacture year': 2015,
                                               'car id': 4})

        tester.post("/api/purchase_car", json={'Manufacture': 'Subaru',
                                               'Manufacture price': 400,
                                               'Manufacture year': 2015,
                                               'car id': 5})

        tester.post("/api/purchase_car", json={'Manufacture': 'Subaru',
                                               'Manufacture price': 400,
                                               'Manufacture year': 2015,
                                               'car id': 6})

        tester.post("/api/purchase_car", json={'Manufacture': 'Subaru',
                                               'Manufacture price': 400,
                                               'Manufacture year': 2015,
                                               'car id': 7})
        response = tester.get("/api/all_cars")
        self.assertEqual(response.status_code, 200)

    # check for data returned
    def test_response_data(self):
        tester = app.test_client(self)
        tester.post("/api/purchase_car", json={'Manufacture': 'Ford',
                                               'Manufacture price': 20,
                                               'Manufacture year': 1995,
                                               'car id': 2})

        tester.post("/api/purchase_car", json={'Manufacture': 'Audi',
                                               'Manufacture price': 500,
                                               'Manufacture year': 2013,
                                               'car id': 3})

        tester.post("/api/purchase_car", json={'Manufacture': 'Subaru',
                                               'Manufacture price': 400,
                                               'Manufacture year': 2015,
                                               'car id': 4})

        tester.post("/api/purchase_car", json={'Manufacture': 'Subaru',
                                               'Manufacture price': 400,
                                               'Manufacture year': 2015,
                                               'car id': 5})

        tester.post("/api/purchase_car", json={'Manufacture': 'Subaru',
                                               'Manufacture price': 400,
                                               'Manufacture year': 2015,
                                               'car id': 6})

        tester.post("/api/purchase_car", json={'Manufacture': 'Subaru',
                                               'Manufacture price': 400,
                                               'Manufacture year': 2015,
                                               'car id': 7})

        response = tester.get("/api/all_cars")
        self.assertEqual(response.get_json(), [{'Manufacture': 'Toyota',
                                                'Manufacture price': 100,
                                                'Manufacture year': 1980,
                                                'car id': 1},
                                               {'Manufacture': 'Ford',
                                                'Manufacture price': 20,
                                                'Manufacture year': 1995,
                                                'car id': 2},
                                               {'Manufacture': 'Audi',
                                                'Manufacture price': 500,
                                                'Manufacture year': 2013,
                                                'car id': 3},
                                               {'Manufacture': 'Subaru',
                                                'Manufacture price': 400,
                                                'Manufacture year': 2015,
                                                'car id': 4},
                                               {'Manufacture': 'Subaru',
                                                'Manufacture price': 400,
                                                'Manufacture year': 2015,
                                                'car id': 5},
                                               {'Manufacture': 'Subaru',
                                                'Manufacture price': 400,
                                                'Manufacture year': 2015,
                                                'car id': 6},
                                               {'Manufacture': 'Subaru',
                                                'Manufacture price': 400,
                                                'Manufacture year': 2015,
                                                'car id': 7}
                                               ])


if __name__ == '__main__':
    unittest.main()
