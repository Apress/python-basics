name = ''
while True:
    name = input('Name> ')
    if name == 'stop':
        break
    if name:
        print('Hello', name, 'how are you?')
