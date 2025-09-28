# jb bhi hm shell m programming krte h and kisi file ko import krte h to uske sare methods(attributes) import ho jate h
# but after importing agr hmne uss file m kuch b changes kre to changes import nhi hoge unko import krne k liye ya to 
# shell ko again start krna hoga ya "from importlib import reload" krna hoga isse ek reload library import hoti h and
# iss library m ek reload method hota h jisme hm hmari file ka name likhte h and vo file reload ho jati h and uske sare
# attributes b aa jate h reload(hello_world)
# mutable data type(changeable)-list, set ,dictionary, bytearray, array
# immutable data type(unchangeable)-integers, floating-point, boolean, string, tuples, frozen set, bytes

### data types
#  list- y ek data type h jo contiguous memory allocate krta h just like array []. it start with 0 idexing.
#  Tuple- y bhi list jese hote h bs () s denote hote h.
# Dict (dictionary)- isme values 0 s start nhi hoti h and denoted as {} and isme values key: value k pair m hoti h.
# set- y unique values store krta h.
# Boolean- y true/false m value rkhte h.
# >>> mylist = [1, 3, 5]
# >>> mylist
# [1, 3, 5]
# >>> mylist[0]
# 1
# >>> 12 + 12
# 24  
# >>> 2.5 * 5
# 12.5
# >>> 2 ** 100
# 1267650600228229401496703205376
# >>> import math
# >>> math.pi
# 3.141592653589793
# >>> import random 
# >>> random.random()
# 0.3236464981212366
# >>> random.random()
# 0.09752222551998935
# >>> random.choice([1,2 ,3, 5, 3])
# 3
# >>> random.choice([1,2 ,3, 5, 3])
# 3
# >>> random.choice([1,2 ,3, 5, 3])
# 1
# >>> random.choice([1,2 ,3, 5,t ,3])
# Traceback (most recent call last):
#   File "<python-input-14>", line 1, in <module>
#     random.choice([1,2 ,3, 5,t ,3])
#                              ^
# NameError: name 't' is not defined
# dir(name of datatype) returns all the methods eg: dir(username), dir(mylist)

#### some internal concepts (memory)

# python k andr ek garbage collector hota h jo unn values ko collect krta h jinka koi variable nhi hota and vo kafi time
# s use nhi ho r hoti h. But y ek dm nhi chlta h kuch time baad chlta h in case of number and string. 
# jitna b memory allocation hota h un sb k sath ek ref_count ka variable bnta h but vo dhikta nhi h and iss variable m
# sare variables jo ek particular memory ko point kr r hote h un sb variables k counting hoti h. 
# note:- jitne b data ka type hota h vo sb memory m jata h na k variable m i.e varible ko kbi koi type nhi milta h uski
# value ko type milta h. memory k andr k value ka data type hota h variable ka n hota h.
#  list mutable hoti h i.e agr hm do list bnate h and ek list m dusri list assign krte h and then first list m kuch or value
# assign krte h to second list m kuch changes nhi hoge vo same memory ko point krti rhegi. but agr first list m h changes krege
# to vo changes second list m bhi reflect hoge. 
# eg:- l1 = [1, 2, 3]
# >>> l2 = l1
# >>> l1
# [1, 2, 3]
# >>> l2   
# [1, 2, 3]
# >>> l1[0] = 44
# >>> l2
# [44, 2, 3]

# with new values assign
#  p1 = [3, 6, 7]
# >>> p2 = p1
# >>> p2 = [3, 6, 7]
# >>> p1[0] = 55
# >>> p2
# [3, 6, 7]
# >>> p1
# [55, 6, 7]

# slicing from start to end h1 = [1, 2, 3]
# h2 = h1[:] h2 m h1 k copy aa gi h. to h2 m copy aai h to ab hm h1 m kuch b change krege to vo h1 m reflect nhi hoge vice versa.
# 

# loop behind the scene
# python m kuch iteration tools hote h like for, comprehension, while etc
# y tools only uni p use hote h jo chij iterable ho or iterable objects p like lists, file
# iterable tools iter objects s query krte h and use iter() method bhejta h jise uspe loop lga ske and then y iter object __next__ or next() ko bhejte h as a response it means memory ka first element ka address ayega and sath m next aayega jo btayega k aage or bhi values h ya end ho gi list. Last value aane p ek exception aata h jo btata h k ab aage loop n chlana.

# file.readline()
# 'import time\n'
# >>>
# >>> file.readline()
# 'print("abhishek")\n'
# >>> file.readline()
# '\n'
# >>> file.readline()
# 'username = "abhishek"\n'
# >>> file.readline()
# 'print(username)'
# >>> file.readline()
# ''
# >>> file.readline()
# ''
# >>> file = open('script.py')
# >>> file.__next__()
# 'import time\n'
# >>> file.__next__()
# 'print("abhishek")\n'
# >>> file.__next__()
# '\n'
# >>> file.__next__()
# 'username = "abhishek"\n'
# >>> file.__next__()
# 'print(username)'
# >>> file.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     file.__next__()
#     ~~~~~~~~~~~~~^^
# StopIteration


# for line in open('script.py'): 
# ...     print(line)
# ... 
# import time

# print("abhishek")

# username = "abhishek"

# print(username)

# myList = [1, 2, 3, 4]
# >>> ref = iter(myList)
# >>> ref
# <list_iterator object at 0x0000015014E71E70>
# >>> ref.__next__()
# 1
# >>> ref.__next__()
# 2
# >>> ref.__next__()
# 3
# >>> ref.__next__()
# 4
# >>> ref.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     ref.__next__()
#     ~~~~~~~~~~~~^^
# StopIteration

# jitni b chijo m loop lg skta h vo sb iterable hoti h

### OOPs ###
# """classes and objects""" 

# class Car:  # syntax to create a class
#    def __init__(self, brand, model): # it is a constructor. self is like this keyword
#         self.brand = brand
#         self.model = model


# my_car = Car("Toyota", "Corolla") # syntax to create an object

# **kwargs(keyword arguments) it use only in fns and accept key-value pair as values and return dict {}
# eg:- def show_info(**kwargs):
#     print("kwargs inside function:", kwargs)
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# show_info(name="Alice", age=30, city="Delhi")
# Since show_info has a parameter **kwargs, all these keyword arguments are captured into a dict:
# kwargs = {"name": "Alice", "age": 30, "city": "Delhi"}

