class Car:  # syntax to create a class
   def __init__(self, brand, model): # it is a constructor. self is like this keyword
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla") # syntax to create an object
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)