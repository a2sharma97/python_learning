# dictionary m (key value) k pair m storage hota h. It is just like object in js.
user = {
    "firstName" : "Abhishek",
    "lastName" : "Sharma",
    "age" : 25,
}

print(user)

print(user["firstName"])
print(user.get("lastName"))
print(user.get("middleName")) # None

user["age"] = 28
print(user)

for single_user in user:
        print(single_user) #show only keys not values

for single_user in user:
        print(single_user, user[single_user])

for key, value in user.items():
        print(key, value)

if "firstName" in user:
        print("firstName is :", user.get("firstName"))

print(len(user)) # 3

user["Education"] = "MCA"
print(user)

# user.popitem() remove last element
user.pop("Education")
print(user)

del user["age"]
print(user)

user_copy = user.copy()
user_copy["age"] = 28
print(user_copy)

register = {
    "fullName" : {"firstName": "Abhishek", "lastName": "Sharma"},
    "Education" : {"graduation" : "BCA", "post-graduation": "MCA"}
}

print(register)

print(register["fullName"]) # {'firstName': 'Abhishek', 'lastName': 'Sharma'}
print(register["fullName"]["firstName"])

squared_nums = {square: square ** 2 for square in range(10)}
print(squared_nums) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

squared_nums.clear()
print(squared_nums) #{}

keys = ["firstName", "lastName", "age"]
default_value = "user Details"

new_Dict = dict.fromkeys(keys, default_value)

print(new_Dict) # {'firstName': 'user Details', 'lastName': 'user Details', 'age': 'user Details'}

new_Dict = dict.fromkeys(keys, keys)
print(new_Dict) #{'firstName': ['firstName', 'lastName', 'age'], 'lastName': ['firstName', 'lastName', 'age'], 'age': ['firstName', 'lastName', 'age']}

# dict keyword
user = dict(username= "abhishek42", gender= "male")
print(f'user info: {user}')
del user["gender"]
print(f'after deleting {user}')