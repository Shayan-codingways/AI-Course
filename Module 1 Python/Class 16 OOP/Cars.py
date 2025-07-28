class Car():
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def describe_car(self):
       long_name = f"{self.__year} {self.__make} {self.__model}"
       return long_name


    def set_make(self, new_make):
        self.__make = new_make
    def get_make(self):
        return self.__make
        
    def set_model(self, new_model):
        self.__model = new_model
    def get_model(self):
        return self.__model

    def set_year(self, new_year):
        self.__year = new_year
    def get_year(self):
        return self.__year