order = input("Enter the order ").lower()
option = input("extra option ").lower()

if option == "yes":
    option = True
elif option == "no":
    option = False
else:
    exit()

if order == "small":
    if option:
        print("Small coffee with an option of Extra Shot of espresso.")
    else:
        print("Small coffee.")
elif order == "medium":
    if option:
        print("Medium coffee with an option of Extra Shot of espresso.")
    else:
        print("Medium coffee.")
elif order == "large":
    if option:
        print("Large coffee with an option of Extra Shot of espresso.")
    else:
        print("Large coffee.")
