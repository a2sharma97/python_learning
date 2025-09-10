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
