username = "abhishek"
print(username)

username = "Abhishek Sharma"
first_char = username[0]
print(first_char)

firstName = username[0:8]
print(firstName)
firstName = username[-1]
print(firstName)

num_list = "0123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[0:7:3])
print(num_list[1:-7:3])

print(username.lower())
print(username.upper())

fullName = " Abhishek Sharma  "
print(fullName.strip())

username = "abhishek sharma"
print(username.replace("abhishek", "Abhishek"))

names = "Abhishek, Radhika, Khushi, Chanchal"
print(names.split())
print(names.split(", "))

print(username.find("sharma"))
print(username.find("ram"))

wrong_name = "abhishek sharma sharma sharma"
print(wrong_name.count("sharma"))

firstName = "abhishek"
age = 20
order = "Write your name: {} and  age: {}"
print(order.format(firstName, age))

all_names = ["abhishek", "radhika", "khushi", "chanchal"]
print("".join(all_names))
print(" ".join(all_names))
print(", ".join(all_names))

print(len(username))

for letter in username:
        print(letter)

paragraph = "He said, \"ghar pr sab shi hai\" "
print(paragraph)

fullName = "abhishek\nsharma"
print(fullName)
fullName = r"abhishek\nsharma"
print(fullName)

path = r"c:\user\pwd"
print(path)
path = "c:\\user\\pwd"
print(path)

print("abhishek" in firstName)