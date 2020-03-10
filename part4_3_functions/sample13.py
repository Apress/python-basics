def swap(x, y):
    return y, x

a, b = swap(10, 5)
print(a, b)
a_and_b = swap(10, 5)
type(a_and_b)
a, b = a_and_b
print(a, b)
