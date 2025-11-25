# Problem 06.01.01: Các pattern cơ bản

print("=== CÁC PATTERN CƠ BẢN ===")

n = int(input("Nhập kích thước pattern: "))

print("\n1. Hình vuông rỗng:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n2. Tam giác số tăng dần:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n3. Tam giác số giảm dần:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n4. Tam giác cân với số:")
for i in range(1, n + 1):
    # In khoảng trắng
    for j in range(n - i):
        print(" ", end="")
    # In số tăng
    for j in range(1, i + 1):
        print(j, end="")
    # In số giảm
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print("\n5. Hình thoi:")
# Nửa trên (bao gồm giữa)
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

print("\n6. Pattern chữ X:")
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()