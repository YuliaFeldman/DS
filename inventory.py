from car import *
from typing import ValuesView


class Inventory:

    __profit: int
    __available_cars: {int , Car}

    def __init__(self):
        self.__profit = 0
        self.__available_cars = {}

    def purchase_car(self, car: Car) -> None:
        """
        Add a car to the inventory
        """
        self.__available_cars[car.get_car_id()] = car
        self.__profit -= car.get_manufacture_price()

    def sell_car(self, car_id: int, selling_price: int) -> None:
        """
        Sell a car from the inventory
        """
        self.__available_cars.pop(car_id)
        self.__profit += selling_price

    def get_total_profit(self) -> int:
        """
        Return the current total profit of this inventory
        """
        return self.__profit

    def get_all_cars(self) -> ValuesView:
        """
        Return all cars in the inventory
        """
        return self.__available_cars.values()
