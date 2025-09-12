number = int(input("Enter a number: "))
flag = True

for i in range(2, number):
    if (number % i) == 0:
        flag = False
        break

if flag and number != 1:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")