# Problem 04.03.01: Pattern printing nâng cao

print("=== PATTERN PRINTING ===")

n = int(input("Nhập kích thước pattern: "))

print("\n1. Tam giác vuông:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\n2. Tam giác vuông ngược:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\n3. Tam giác cân:")
for i in range(1, n + 1):
    # In khoảng trắng
    for j in range(n - i):
        print(" ", end="")
    # In sao
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print("\n4. Hình thoi:")
# Nửa trên
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Nửa dưới
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print("\n5. Tam giác số Pascal:")
for i in range(n):
    # In khoảng trắng
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Tính và in số Pascal
    num = 1
    for j in range(i + 1):
        print(f"{num:2d}", end="")
        num = num * (i - j) // (j + 1)
    print()

print("\n6. Pattern số:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()