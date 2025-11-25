# Problem 06.01.02: Pattern với chữ cái

print("=== PATTERN VỚI CHỮ CÁI ===")

n = int(input("Nhập kích thước pattern: "))

print("\n1. Tam giác chữ cái:")
for i in range(n):
    for j in range(i + 1):
        print(chr(ord('A') + j), end="")
    print()

print("\n2. Tam giác chữ cái cân đối:")
for i in range(n):
    # In khoảng trắng
    for j in range(n - i - 1):
        print(" ", end="")
    
    # In chữ cái tăng
    for j in range(i + 1):
        print(chr(ord('A') + j), end="")
    
    # In chữ cái giảm
    for j in range(i - 1, -1, -1):
        print(chr(ord('A') + j), end="")
    
    print()

print("\n3. Pattern chữ cái lặp:")
for i in range(n):
    char = chr(ord('A') + i)
    for j in range(i + 1):
        print(char, end="")
    print()

print("\n4. Hình thoi chữ cái:")
# Nửa trên
for i in range(n):
    # Khoảng trắng
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Chữ cái tăng
    for j in range(i + 1):
        print(chr(ord('A') + j), end="")
    
    # Chữ cái giảm
    for j in range(i - 1, -1, -1):
        print(chr(ord('A') + j), end="")
    
    print()

# Nửa dưới
for i in range(n - 2, -1, -1):
    # Khoảng trắng
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Chữ cái tăng
    for j in range(i + 1):
        print(chr(ord('A') + j), end="")
    
    # Chữ cái giảm
    for j in range(i - 1, -1, -1):
        print(chr(ord('A') + j), end="")
    
    print()

print("\n5. Pattern ABC lặp lại:")
for i in range(n):
    for j in range(i + 1):
        # Lặp lại A, B, C
        print(chr(ord('A') + (j % 3)), end="")
    print()