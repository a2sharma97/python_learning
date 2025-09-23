class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def fuel_type(self): #polymorphism
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self): #polymorphism
        return "Electric charge"


ev_car = ElectricCar("Tesla", "Model s", "85kWh")
print(ev_car.fuel_type())

my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())