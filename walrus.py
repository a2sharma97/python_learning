# walrus operator(:=) example in Python, it allows assignment within an expression

value  = 16
remainder = value % 3

if remainder:
    print(f"{value} is not divisible by 3, remainder is {remainder}")


# Using walrus operator
if (remainder := value % 3):
    print(f"{value} is not divisible by 3, remainder is {remainder}")