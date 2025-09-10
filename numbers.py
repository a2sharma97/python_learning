x = 2
y = 4
z = 6
print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(z / x)  # 3.0
print(z // x) # 3

# x + y * z not good practice use always ()
print(x + ( y * z )) 
x = 45
y = 2.23
print (x + y) #not a good practice, both datatypes should be same
print(int(y)) # 2
print(float(x)) # 45.0
print ('abhishek' + 'sharma') # concat
print(x, y, z)
print(x + 1, y * 2)
print(z % x) # 6
print(100 ** 2)
print(2 ** 100)
print(2 ** 1000)
result = 1/3.0 # not a good practice

print(result)
str1 = repr('Abhishek') #return in string with quotes
print(str1)
str1 = str('Abhishek') # creates new string object.
print(str1)

print(1 < 2) #True
print(5.0 == 5.0) #True
print(4.0 != 5.0) #True
print(x < y and y < z) #False
print(x < y or y < z) #True

import math
print(math.floor(3.5))  #3
print(math.floor(-3.5)) # -4
print(math.trunc(2.8)) # 2
print(math.trunc(-2.8)) # -2

print(0o20) #16
print(0xFF) #255
print(0b1000) #8

print(oct(64))
print(hex(64))
print(bin(64))

print(int('64', 8)) #octal value of 64
print(int('64', 16)) #hex value of 64
print(int('10000', 2)) #binary value of 10000 == 16

#bitwise
x = 1
print(x << 1) # 2
print(x | 1) # 1
print(x & 1) # 1

import random
print(random.random())
print(random.randint(1, 10)) # give random value from 1 to 10
print(random.randint(1, 100)) # give random value from 1 to 100

l1 = ['abhishek', 'khushi', 'sharma']
print(random.choice(l1)) # choose random from list
print(random.choice(l1)) 
random.shuffle(l1) #shuffle the list
print(l1) 

print(0.1 + 0.1 + 0.1)
print((0.1 + 0.1 + 0.1) - 0.3) #gives some random answer which is wrong decimal precision is a problem in python so we import Decimal

setone = {1, 2, 3, 5}
print(setone & {1, 3}) #intersection
print(setone | {1, 3, 7}) #union
print(setone - {1, 3}) #difference
print(setone - {1, 2, 3, 5}) #set()

print(type({})) #dict
print(type(())) #tuple
print(type([])) #list

print(True == 1)
print(False == 1)
print(True is 1) #false
print(True + 1) #2







