def print_grid(width=5, height=5):
    print(width, '(w) by', height, '(h) grid')
    for _ in range(height):
        print('x' * width)
print_grid()
print_grid(2)
print_grid(height=2)
