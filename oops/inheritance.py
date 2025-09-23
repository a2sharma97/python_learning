class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_fullName(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
ev_car = ElectricCar("Tesla", "Model S", "85kWh")
print(ev_car.brand)
print(ev_car.model)
print(ev_car.battery_size)
print(ev_car.car_fullName())
