import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper
       
@timer
def example_function(n):
    time.sleep(n)

example_function(2)

# here timer() calls and in this example_function() pass as an argument and timer() return the wrapper() and
# it recive the result of original fns i.e example_function() and it refers to as example_function()