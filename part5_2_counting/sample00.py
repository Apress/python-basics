with open('tempest_extract.txt') as input_file:
    lines = input_file.readlines()
print(len(lines))
for line in lines:
    print(len(line.split()), line.strip())
print('hello.there'.split())
word_count = 0
for line in lines:
    word_count = word_count + len(line.split())
print(word_count)
character_count = 0
for line in lines:
    character_count = character_count + len(line)
print(character_count)
print('Line count:', len(lines))
print('Word count:', sum(len(line.split()) for line in lines))
print('Character count:', sum(len(line) for line in lines))
