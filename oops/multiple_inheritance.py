class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def fuel_type(self): #polymorphism
        return "Petrol or Diesel"


class Battery:
    def batter_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass



my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.batter_info())