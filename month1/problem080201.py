# Problem 08.02.01: Nested comprehension và ma trận

print("=== NESTED COMPREHENSION VÀ MA TRẬN ===")

# Bài 1: Tạo ma trận với nested comprehension
print("1. Tạo ma trận:")

# Ma trận đơn vị 4x4
identity = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
print("Ma trận đơn vị 4x4:")
for row in identity:
    print(row)

# Ma trận nhân
size = 3
multiplication_matrix = [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]
print(f"\nMa trận nhân {size}x{size}:")
for row in multiplication_matrix:
    print(row)

# Ma trận khoảng cách Manhattan
distance_matrix = [[abs(i - j) for j in range(5)] for i in range(5)]
print("\nMa trận khoảng cách Manhattan 5x5:")
for row in distance_matrix:
    print(row)

# Bài 2: Xử lý nested lists
print("\n2. Xử lý nested lists:")

# Flatten nested list
nested_data = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
flattened = [item for sublist in nested_data for item in sublist]
print(f"Nested: {nested_data}")
print(f"Flattened: {flattened}")

# Tổng từng sublist
sums = [sum(sublist) for sublist in nested_data]
print(f"Tổng từng sublist: {sums}")

# Lọc sublist có độ dài > 2
long_sublists = [sublist for sublist in nested_data if len(sublist) > 2]
print(f"Sublist dài > 2: {long_sublists}")

# Bài 3: Bảng cửu chương
print("\n3. Bảng cửu chương:")
multiplication_table = [[i * j for j in range(1, 11)] for i in range(1, 11)]

print("Bảng cửu chương 1-10:")
print("   ", end="")
for j in range(1, 11):
    print(f"{j:4}", end="")
print()

for i in range(10):
    print(f"{i+1:2}:", end="")
    for j in range(10):
        print(f"{multiplication_table[i][j]:4}", end="")
    print()

# Bài 4: Ma trận tam giác
print("\n4. Ma trận tam giác:")

# Tam giác Pascal
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

pascal = pascal_triangle(6)
print("Tam giác Pascal:")
for i, row in enumerate(pascal):
    print(" " * (6 - i), end="")
    for num in row:
        print(f"{num:3}", end=" ")
    print()

# Bài 5: Reshape và transform
print("\n5. Reshape và transform:")

# Tạo list 1D và reshape thành 2D
data_1d = list(range(1, 13))  # 1 đến 12
print(f"Dữ liệu 1D: {data_1d}")

# Reshape thành 3x4
rows, cols = 3, 4
reshaped = [[data_1d[i * cols + j] for j in range(cols)] for i in range(rows)]
print(f"Reshape 3x4:")
for row in reshaped:
    print(row)

# Reshape thành 4x3
rows, cols = 4, 3
reshaped2 = [[data_1d[i * cols + j] for j in range(cols)] for i in range(rows)]
print(f"Reshape 4x3:")
for row in reshaped2:
    print(row)

# Bài 6: Chuyển vị ma trận
print("\n6. Chuyển vị ma trận:")
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Ma trận gốc:")
for row in original:
    print(row)

# Chuyển vị
transposed = [[original[i][j] for i in range(len(original))] 
              for j in range(len(original[0]))]
print("Ma trận chuyển vị:")
for row in transposed:
    print(row)

# Bài 7: Ma trận với điều kiện
print("\n7. Ma trận với điều kiện:")

# Ma trận checker (bàn cờ)
size = 5
checker = [["B" if (i + j) % 2 == 0 else "W" for j in range(size)] for i in range(size)]
print(f"Ma trận checker {size}x{size}:")
for row in checker:
    print(" ".join(row))

# Ma trận khoảng cách từ tâm
center = size // 2
distance_from_center = [[max(abs(i - center), abs(j - center)) 
                        for j in range(size)] for i in range(size)]
print(f"\nKhoảng cách từ tâm:")
for row in distance_from_center:
    print(row)

# Bài 8: Xử lý ma trận số
print("\n8. Xử lý ma trận số:")
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("Ma trận gốc:")
for row in matrix:
    print(row)

# Tổng từng hàng
row_sums = [sum(row) for row in matrix]
print(f"Tổng hàng: {row_sums}")

# Tổng từng cột
col_sums = [sum(matrix[i][j] for i in range(len(matrix))) 
           for j in range(len(matrix[0]))]
print(f"Tổng cột: {col_sums}")

# Phần tử lớn nhất từng hàng
row_max = [max(row) for row in matrix]
print(f"Max hàng: {row_max}")

# Tất cả phần tử chẵn
even_elements = [element for row in matrix for element in row if element % 2 == 0]
print(f"Phần tử chẵn: {even_elements}")

# Ma trận nhân với scalar
scalar = 2
scaled_matrix = [[element * scalar for element in row] for row in matrix]
print(f"Ma trận × {scalar}:")
for row in scaled_matrix:
    print(row)