definitions = {
    'snake': 'long thin reptile',
    'plant': 'green growing thing',
    'dinosaur': 'large and extinct',
    'amoeba': 'single cell creature'
}
print(definitions['plant'])
another_dictionary = {
    'hello': 'some string',
    15: 'another string',
    (1, 2): 'and one more string'
}
print(another_dictionary[15])
print(another_dictionary[(1, 2)])
one_more_dictionary = {
    'plant': 'green growing thing',
    'amoebas': 5
}
print(one_more_dictionary['amoebas'])
one_more_dictionary['nonsense'] = another_dictionary
one_more_dictionary['some key'] = [1, 3, 7, 15]
print(one_more_dictionary)
print(definitions['snake'])
# The following line has a deliberate error. See the video for details
# To get this script working, put a # in front of it to turn it into a comment
print(definitions['monkey'])
print(definitions.get('plant'))
print(definitions.get('monkey'))
print(definitions.get('plant', 'Not found'))
print(definitions.get('monkey', 'Not found'))
print(definitions['snake'])
definitions['snake'] = 'elongated, legless, carnivorous reptiles'
print(definitions['snake'])
definitions['apple'] = 'Round-ish fruit'
print(definitions)
del definitions['snake']
# The following line has a deliberate error. See the video for details
# To get this script working, put a # in front of it to turn it into a comment
print(definitions['snake'])
