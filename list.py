heros = ["hulk", "spiderman", "superman", "ironman"]
print(heros)

print(heros[2])

print(heros[-1]) # gives last index value

print(heros[1:3]) # start from 1 and end at 2 or 3 - 1 = 2 
print(heros[:3]) # start from 0 and end at 2 or 3 - 0 = 3 
print(heros[2:]) # start from 2 and end at last or 2 - last index 
print(heros)  

heros[3] = "antman"
print(heros)

print(heros[1:2])
heros[1:2] = "hawkeye"
print(heros) #['hulk', 'h', 'a', 'w', 'k', 'e', 'y', 'e', 'superman', 'antman']

heros[1:2] = ["hawkeye"]
print(heros) #['hulk', 'hawkeye', 'a', 'w', 'k', 'e', 'y', 'e', 'superman', 'antman']

heros = ["hulk", "spiderman", "superman", "ironman"]
print(heros)

heros[1:2] = ["hawkeye"]
print(heros) #['hulk', 'hawkeye', 'superman', 'ironman']

heros[1:3] = ["wolverine", "flash"]
print(heros)

heros[1:1] = ["spiderman", "superman"]
print(heros)

for hero in heros:
        print(hero)

for hero in heros:
        print(hero, end=",")

if "abhishek" in heros:
    print("No abhishek is not a hero he is a superhero")

if "spiderman" in heros:
    print("\nyes spiderman is a hero")

heros.append("groot")
print(heros)

print(heros.pop()) #remove last element 

heros.remove("flash")
# heros.remove("groot") not in list
print(heros)

heros.insert(1, "thor")
print(heros)

# heros_copy = heros ## now heros_copy point to same place as pointed by heros or both points to the same memory.

heros_copy = heros.copy() # points to different memory location or have differnt references

heros_copy.append("rocket")
print(heros) #['hulk', 'thor', 'spiderman', 'superman', 'wolverine', 'ironman']
print(heros_copy) #['hulk', 'thor', 'spiderman', 'superman', 'wolverine', 'ironman', 'rocket']

squared_nums = [square ** 2 for square in range(10) ] #list comprehension range is from 0 to 10(exclusive)
print(squared_nums) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_nums = [cube ** 3 for cube in range(5)]
print(cube_nums)

print("list items ")
names = ["abhishek", 'chanchal', 'radhika', 'raju', 'babubhiya']

for item in zip(range(1, len(names) + 1), names):
    print(item)


names = ["abhishek", 'chanchal', 'radhika', 'raju', 'babubhiya']
pay = [5000, 50000, 5000000, 50, 5]

for item in zip(pay, names):
    print(item)