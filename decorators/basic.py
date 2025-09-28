"""without changing the actual code, decorator modifiy or extend behaviour of functions.
Calling fns inside a fns.A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality. add additional functionality to existing functions or methods in a clean, reusable way."""

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet():
    print("Hello, World!")
    
greet()



# we create a function name decorator which takes greet() as a parameter. when we use '@' it means we create a decorator '@decorator' so here it means is greet = decorator(greet) which means whatever decorator fns returns greet() refers to that. Here greet() refers to the wrapper() so whenever the greet calls wrapper() calls and inside wrapper original fns i.e greet() calls which comes from decorator fns.
# So when we call greet(), we are actually calling wrapper().
# And inside wrapper, there is a line func() that invokes the original greet logic.

