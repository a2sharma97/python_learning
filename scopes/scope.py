"""scopes are similar to other languages. In python the scope of a varible is depend on the indentation of fns. Global varibles can be accessed from anywhere in the program."""

username = "abhishek"

def func():
    # username = "Abhishek"
    print(username) # if we do not intialized the varible inside the fns it access the global variable

func()
print(username)

x = 99
def func2(y):
    z = x + y
    return z

result = func2(1)
print(result)

# def func3():
#     global x #sets the values globally but it is not a good practice.
#     x = 88

# func3()
# print(x)

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()

# f1() # f2 uses the value of x 

def f1():
    x = 88
    def f2():
        print(x)
    return f2 #returns fns definition

myResult = f1() #f1 retrun a fns (f2) definition and myResult stores that definition and work as a f2() and as per definition it has accessed all varibles of its parent fns and this is called closure.
myResult()

def pythonCode(num):
    def actual (x):
        return x ** num
    return actual

f = pythonCode(2)
g = pythonCode(3)
print(f(2))
print(g(3))