def print_grid(width, height):
    for _ in range(height):
        print('x' * width)

print_grid(2, 5)
print_grid(5, 2)
print_grid(width=5, height=2)
print_grid(height=2, width=5)
