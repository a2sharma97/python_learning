class Car():
    def __init__(self, brand, model):
        self.__brand = brand #by using __ the attribute become private
        self.model = model
    
    def get_brand(self):
        return self.__brand + "!"

    def set_model(self, model):
        self.model = model
 
my_car = Car("xyz", "z")
# print(my_car.__brand) error becoz we can't acces it from outside of the class 
print(my_car.get_brand())
my_car.set_model("k")
print(my_car.model)
