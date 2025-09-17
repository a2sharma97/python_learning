"""The yield keyword in Python is used to create generator functions. Unlike a regular function that uses return to send a value and terminate, a generator function uses yield to produce a sequence of values iteratively.
A function containing yield automatically becomes a generator function"""
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        # print(i)
        yield i

print(even_generator(10)) # <generator object even_generator at 0x0000020977F102E0>
for num in even_generator(10):
    print(num, end=" ")

print()
for num in even_generator(5):
    print(num, end=" ")