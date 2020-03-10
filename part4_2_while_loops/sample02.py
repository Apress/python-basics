name = ''
while name != 'stop':
    name = input('Name> ')
    if not name or name == 'stop':
        continue
    print('Hello', name, 'how are you?')
