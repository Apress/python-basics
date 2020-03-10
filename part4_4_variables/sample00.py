list_a = list(range(10))
print(list_a)
list_b = list_a
print(list_b)
id(list_a)
id(list_b)
list_a is list_b
list_a = list(range(10))
list_c = list(range(10))
print(list_a)
print(list_c)
list_a is list_c
id(list_a)
id(list_c)
list_a == list_c
list_a = list(range(10))
list_b = list_a
list_c = list(range(10))
print(list_a)
print(list_b)
print(list_c)
list_a[0] = 25
print(list_a)
print(list_b)
print(list_c)
print(list_a)
print(list_b)
print(list_c)
list_a = list(range(20))
print(list_a)
print(list_b)
