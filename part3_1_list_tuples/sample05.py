shopping_list = ['bread', 'milk', 'eggs', 'butter']
shopping_list[1] = 'crisps'
print(shopping_list)
name = 'Fred'
# The following line has a deliberate error. See the video for details
# To get this script working, put a # in front of it to turn it into a comment
name[1] = 's'
shopping_list.append('ham')
print(shopping_list)
list_of_numbers = list(range(20))
print(list_of_numbers)
list_of_numbers.insert(9, 38)
print(list_of_numbers)
print(shopping_list)
buy_now = shopping_list.pop()
print(buy_now)
print(shopping_list)
del shopping_list[2]
print(shopping_list)
