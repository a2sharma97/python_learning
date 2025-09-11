input_string = input()

reverse_string = ""
for i in range(0, len(input_string)):
   reverse_string += input_string[len(input_string) - 1 - i ]

print("reverse of the string is: ", reverse_string)