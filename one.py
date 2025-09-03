rows = int(input("Enter row: "))
cols = int(input("Enter col: "))
search = int(input("Search: "))

for row in range(1, rows + 1):
    for col in range(1, cols + 1):
        value = row * col
        if value == search:
            print(f"[{value}]", end=" ")
        else:
            print(value, end=" ")
    print()