with open('f3.txt', 'r') as file:
    contents = file.readlines()

my_dict = {}

for line in contents:
    key, value = line.strip().split(':')  

    my_dict[key.strip()] = value.strip()

print(my_dict)
