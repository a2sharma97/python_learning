items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    # if items.count(item) != 1:
    #     print("Duplicate item is ", item)
    #     break
    if item in unique_items:
        print("Duplicate: ", item)
        break
    unique_items.add(item)