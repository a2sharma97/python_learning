file = open('youtube.txt', 'w')

try:
    file.write('abhishek sharma')
finally:
    file.close()

# or another modern way to handle file errors

with open('youtube.txt', 'w') as file:
    file.write("open file using modern syntax")