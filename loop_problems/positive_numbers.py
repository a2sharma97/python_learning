total_numbers = input()
numbers = [int(num) for num in total_numbers.split() ]



# for i in range(10):
#     numbers.append(int(input(' ')))

positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1

print(f"Total postitive numbers are {positive_number_count}")