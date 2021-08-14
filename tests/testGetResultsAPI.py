import unittest
from main import app


class TestCaseZeroResult(unittest.TestCase):


    # Check for response 200
    def test_response_status(self):
        tester = app.test_client(self)
        response = tester.get("/api/results")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # check for data returned
    def test_response_data(self):
        tester = app.test_client(self)
        response = tester.get("/api/results")
        self.assertEqual(response.data, b'0')


class TestCaseNegativeResult(unittest.TestCase):

    # Check for response 200
    def test_response_status(self):
        tester = app.test_client(self)
        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 1})
        response = tester.get("/api/results")
        self.assertEqual(response.status_code, 200)

    # check for data returned
    def test_response_data(self):
        tester = app.test_client(self)
        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 2})
        response = tester.get("/api/results")
        self.assertEqual(response.data, b'-100')

    # check for data returned after many purchases
    def test_response_data_complex(self):
        tester = app.test_client(self)
        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 3})

        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 4})

        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 5})

        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 6})

        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 7})
        response = tester.get("/api/results")
        self.assertEqual(response.data, b'-600')



class TestCasePositiveResult(unittest.TestCase):

    # Check for response 200
    def test_response_status(self):
        tester = app.test_client(self)
        tester.put("/api/sell_car/1", json={'car selling price': 1000})
        response = tester.get("/api/results")
        self.assertEqual(response.status_code, 200)

    # check for data returned
    def test_response_data(self):
        tester = app.test_client(self)
        tester.put("/api/sell_car/2", json={'car selling price': 1000})
        response = tester.get("/api/results")
        self.assertEqual(response.data, b'300')

    # check for data returned after many purchases and sells
    def test_response_data_complex(self):
        tester = app.test_client(self)
        tester.put("/api/sell_car/3", json={'car selling price': 1000})
        tester.put("/api/sell_car/4", json={'car selling price': 1000})
        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 10})
        tester.put("/api/sell_car/5", json={'car selling price': 1000})
        tester.put("/api/sell_car/6", json={'car selling price': 1000})
        tester.post("/api/purchase_car", json={'Manufacture': 'Toyota',
                                               'Manufacture price': 100,
                                               'Manufacture year': 1980,
                                               'car id': 11})
        tester.put("/api/sell_car/7", json={'car selling price': 1000})
        tester.put("/api/sell_car/10", json={'car selling price': 1000})
        response = tester.get("/api/results")
        self.assertEqual(response.data, b'6100')



if __name__ == '__main__':
    unittest.main()

