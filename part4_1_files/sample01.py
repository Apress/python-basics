with open('some_file.txt') as input_file:
    lines = input_file.readlines()

print(lines)
for line in lines:
    print(line)
print(lines[2])
