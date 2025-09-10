age = int(input("Enter the age: \n"))

if age < 13:
    print("Child")
elif age >= 13 and age < 19:
    print("Teenage")
elif age < 60:
    print("Adult")
else:
    print("Senior")

