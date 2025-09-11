input_string = input("Enter the string ")

flag = True

for char in input_string:
    if input_string.count(char) == 1:
       print("Non-repeated character is:", char)
       flag = False
       break

if flag:
    print("No character repeat")
    
