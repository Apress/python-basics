open('some_file.txt')
with open('some_file.txt') as input_file:
    contents = input_file.read()
print(contents)
