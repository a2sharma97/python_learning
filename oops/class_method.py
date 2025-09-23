class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullName(self): #self must be used for the connection with attributes 
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Carolla")
car_fullName = my_car.fullName()
print("fullName:", car_fullName)