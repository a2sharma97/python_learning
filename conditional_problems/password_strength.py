password = (input("Enter the password ")).lower()
total_characters = len(password)

if total_characters < 6:
    print("Weak")
elif total_characters <= 10:
    print("Medium")
else:
    print("Strong")