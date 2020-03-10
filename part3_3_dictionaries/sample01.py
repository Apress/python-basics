definitions = {
    'a': 'First letter',
    'b': 'Second letter',
    'c': 'Third letter',
    'do': 'First note',
    're': 'Second note',
    'mi': 'Third note'
}
print(list(definitions.keys()))
for key in definitions.keys():
    print(key)
print(definitions)
for key in definitions.keys():
    print(key * 5)
for key in definitions:
    print(key * 5)
print(list(definitions.values()))
for value in definitions.values():
    print(value)
print(list(definitions.items()))
for item in definitions.items():
    print(type(item), item)
for word, definition in definitions.items():
    print('Word:', word, '- Definition:', definition)

