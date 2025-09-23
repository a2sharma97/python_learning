class Car():
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1 # self.total_car += 1 both are same
    
    def fullName(self): #self must be used for the connection with attributes 
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Carolla")
my_car_two = Car("test", "test")
# my_car_three = Car("test2", "test2")
test = Car("test2", "test2")

print(Car.total_car)
