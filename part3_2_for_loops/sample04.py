shopping_list = ['carrots v', 'potatoes v', 'milk', 'eggs', 'bread', 'onions v']
for item in shopping_list:
    if item[-1] == 'v':
        item = item[:-2]
        print(item)

for item in shopping_list:
    if item[-1] != 'v':
        continue
    item = item[:-2]
    print(item)
