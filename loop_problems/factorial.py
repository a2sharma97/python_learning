num = int(input("Enter a number "))

factorial = 1

# i = 1

# while i <= num: 
#     factorial *= i
#     i += 1

while num > 0:
    factorial *= num
    num -= 1

print(f"Factorial is: ", factorial)
