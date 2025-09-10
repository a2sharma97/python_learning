# tuple is immutable i.e it is not changeable just like strings. () for tuples.

marvel_heors = ("spiderman", "antman", "thor", "loki")
print(marvel_heors)
print(marvel_heors[0])
print(marvel_heors[-1])
print(marvel_heors[1:3])

# marvel_heors[0] = "ironman" # error becoz tuple is immutable so it does not support assigment
# print(marvel_heors) 

print(len(marvel_heors))

dc_heros = ("superman", "batman", "flash", "shazam")
print(dc_heros)

all_heros = marvel_heors + dc_heros
print(all_heros)

if "batman" in all_heros:
    print("yes")

user = ("abhishek", "abhishek.sharma@gmail.com", "12456")

(username, email, password) = user
print(username + " " + email + " " + password)

print(type(all_heros))