
class Car:
    __manufacture: str
    __manufacture_price: int
    __manufacture_year: int
    __car_id: int

    def __init__(self, manufacture: str, manufacture_price: int, manufacture_year: int, car_id: int):
        self.__manufacture = manufacture
        self.__manufacture_price = manufacture_price
        self.__manufacture_year = manufacture_year
        self.__car_id = car_id

    def to_json(self) -> dict:
        """
        Return json representation of this car
        """
        return {"Manufacture": self.__manufacture,
                "Manufacture price": self.__manufacture_price,
                "Manufacture year": self.__manufacture_year,
                "car id": self.__car_id}

    def get_car_id(self) -> int:
        """
        Return id of this car
        """
        return self.__car_id

    def get_manufacture_price(self) -> int:
        """
        Return manufacture price of this car
        """
        return self.__manufacture_price


def from_json(values: dict) -> Car:
    """
    Convert from json to Car object
    :param values: json representation of a car
    :return: a car object with the given values
    """
    return Car(values["Manufacture"], values["Manufacture price"], values["Manufacture year"], values["car id"])
