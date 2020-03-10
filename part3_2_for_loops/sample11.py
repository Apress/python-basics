shopping_list = ['carrots', 'potatoes', 'milk', 'eggs', 'bread', 'onions']
i = 1
for item in shopping_list:
    print(i, item)
    i = i + 1
for i, item in enumerate(shopping_list):
    print(i + 1, item)
