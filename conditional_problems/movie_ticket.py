# age = int(input("Please Enter your age for the ticket \n"))
# day = input("Enter the day: ")

# if age >= 18:
#     if day.lower() == "wednesday":
#         print("you get our wednesday discount of $2 and now the total amount is ", 12 - 2 )
#     else:
#         print("your total amount is ", 12)
# elif day.lower() == "wednesday":
#     print("you get our wednesday discount of $2 and now the total amount is ", 8 - 2 )
# else:
#     print("your total amount is ", 8)

# another way

age = int(input("Please Enter your age for the ticket \n"))
day = input("Enter the day: ") 

price = 12 if age >= 18 else 8

if day.lower() == "wednesday":
    price -= 2

print(f"Ticket price for you is ${price}") # for string literal use f