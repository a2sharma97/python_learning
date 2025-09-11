total_numbers = int(input('Enter the range of numbers '))

even_number_sum = 0

for num in range(1, total_numbers + 1):
    if num % 2 == 0:
        even_number_sum += num
   

print('Sum of even numbers is ', even_number_sum) 

