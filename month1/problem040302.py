# Problem 04.03.02: Ma trận và bảng 2D

print("=== THAO TÁC MA TRẬN ===")

# Nhập kích thước ma trận
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

# Tạo ma trận
matrix = []
print("Nhập các phần tử ma trận:")
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Phần tử [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# In ma trận
print("\nMa trận vừa nhập:")
for i in range(rows):
    for j in range(cols):
        print(f"{matrix[i][j]:4d}", end=" ")
    print()

# Tính tổng các hàng
print("\nTổng các hàng:")
for i in range(rows):
    row_sum = 0
    for j in range(cols):
        row_sum += matrix[i][j]
    print(f"Hàng {i}: {row_sum}")

# Tính tổng các cột
print("\nTổng các cột:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Cột {j}: {col_sum}")

# Tìm phần tử lớn nhất và nhỏ nhất
max_val = min_val = matrix[0][0]
max_pos = min_pos = (0, 0)

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_pos = (i, j)
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_pos = (i, j)

print(f"\nGiá trị lớn nhất: {max_val} tại vị trí {max_pos}")
print(f"Giá trị nhỏ nhất: {min_val} tại vị trí {min_pos}")

# Kiểm tra ma trận vuông và tính tổng đường chéo
if rows == cols:
    print("\nĐây là ma trận vuông!")
    
    # Tổng đường chéo chính
    main_diagonal_sum = 0
    for i in range(rows):
        main_diagonal_sum += matrix[i][i]
    print(f"Tổng đường chéo chính: {main_diagonal_sum}")
    
    # Tổng đường chéo phụ
    anti_diagonal_sum = 0
    for i in range(rows):
        anti_diagonal_sum += matrix[i][rows - 1 - i]
    print(f"Tổng đường chéo phụ: {anti_diagonal_sum}")