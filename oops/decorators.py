class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    def fuel_type(self): #polymorphism
        return "Petrol or Diesel"

    @staticmethod
    def general_description(): # it doesn't need self becoz of the static method
        return "Explaining cars using static method"

    
    @property
    def model(self):
        return self.__model


my_car = Car("Toyota", "Corolla")
# my_car.model = "city"

# print(my_car.model())
print(my_car.model)