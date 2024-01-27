with open('f1.txt', 'r') as file:
    contents = file.read()

reversed_contents = contents[::-1]

with open('f1.txt', 'w') as file:
    file.write(reversed_contents)
