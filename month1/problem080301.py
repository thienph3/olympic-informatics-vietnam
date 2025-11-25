# Problem 08.03.01: Thao tác ma trận cơ bản

print("=== THAO TÁC MA TRẬN CƠ BẢN ===")

# Bài 1: Tạo ma trận
print("1. Tạo ma trận:")

def create_matrix(rows, cols, default_value=0):
    """Tạo ma trận với giá trị mặc định"""
    return [[default_value for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix, title="Ma trận"):
    """In ma trận đẹp"""
    print(f"{title}:")
    for row in matrix:
        print([f"{x:3}" for x in row])

# Ma trận 3x4 với giá trị 0
matrix_zeros = create_matrix(3, 4, 0)
print_matrix(matrix_zeros, "Ma trận 3x4 toàn 0")

# Ma trận với giá trị tăng dần
matrix_sequential = [[i * 4 + j + 1 for j in range(4)] for i in range(3)]
print_matrix(matrix_sequential, "Ma trận 3x4 tăng dần")

# Ma trận đơn vị 4x4
identity_matrix = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
print_matrix(identity_matrix, "Ma trận đơn vị 4x4")

# Bài 2: Truy cập và duyệt ma trận
print("\n2. Truy cập và duyệt ma trận:")
test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(test_matrix, "Ma trận test")

# Truy cập phần tử
print(f"Phần tử [0][0]: {test_matrix[0][0]}")
print(f"Phần tử [1][2]: {test_matrix[1][2]}")
print(f"Phần tử [2][1]: {test_matrix[2][1]}")

# Duyệt tất cả phần tử
print("Duyệt theo hàng:")
for i in range(len(test_matrix)):
    for j in range(len(test_matrix[i])):
        print(f"[{i}][{j}] = {test_matrix[i][j]}", end="  ")
    print()

# Duyệt với enumerate
print("Duyệt với enumerate:")
for i, row in enumerate(test_matrix):
    for j, value in enumerate(row):
        print(f"({i},{j}): {value}", end="  ")
    print()

# Bài 3: Tính tổng hàng và cột
print("\n3. Tính tổng hàng và cột:")

def sum_rows(matrix):
    """Tính tổng từng hàng"""
    return [sum(row) for row in matrix]

def sum_cols(matrix):
    """Tính tổng từng cột"""
    if not matrix:
        return []
    return [sum(matrix[i][j] for i in range(len(matrix))) 
            for j in range(len(matrix[0]))]

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print_matrix(matrix, "Ma trận gốc")

row_sums = sum_rows(matrix)
col_sums = sum_cols(matrix)
print(f"Tổng hàng: {row_sums}")
print(f"Tổng cột: {col_sums}")
print(f"Tổng toàn ma trận: {sum(row_sums)}")

# Bài 4: Chuyển vị ma trận
print("\n4. Chuyển vị ma trận:")

def transpose(matrix):
    """Chuyển vị ma trận"""
    if not matrix:
        return []
    return [[matrix[i][j] for i in range(len(matrix))] 
            for j in range(len(matrix[0]))]

original = [[1, 2, 3], [4, 5, 6]]
transposed = transpose(original)
print_matrix(original, "Ma trận gốc 2x3")
print_matrix(transposed, "Ma trận chuyển vị 3x2")

# Kiểm tra ma trận vuông
square_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
square_transposed = transpose(square_matrix)
print_matrix(square_matrix, "Ma trận vuông gốc")
print_matrix(square_transposed, "Ma trận vuông chuyển vị")

# Bài 5: Tìm kiếm trong ma trận
print("\n5. Tìm kiếm trong ma trận:")

def find_in_matrix(matrix, target):
    """Tìm vị trí đầu tiên của target"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return i, j
    return -1, -1

def find_all_in_matrix(matrix, target):
    """Tìm tất cả vị trí của target"""
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                positions.append((i, j))
    return positions

search_matrix = [[1, 2, 3], [2, 5, 6], [7, 2, 9]]
print_matrix(search_matrix, "Ma trận tìm kiếm")

target = 2
first_pos = find_in_matrix(search_matrix, target)
all_pos = find_all_in_matrix(search_matrix, target)
print(f"Tìm số {target}:")
print(f"  Vị trí đầu tiên: {first_pos}")
print(f"  Tất cả vị trí: {all_pos}")

# Bài 6: Min/Max trong ma trận
print("\n6. Min/Max trong ma trận:")

def matrix_min_max(matrix):
    """Tìm min/max và vị trí"""
    if not matrix:
        return None
    
    min_val = max_val = matrix[0][0]
    min_pos = max_pos = (0, 0)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_pos = (i, j)
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)
    
    return min_val, min_pos, max_val, max_pos

test_matrix = [[15, 3, 8], [7, 12, 1], [9, 6, 20]]
print_matrix(test_matrix, "Ma trận test min/max")

min_val, min_pos, max_val, max_pos = matrix_min_max(test_matrix)
print(f"Min: {min_val} tại vị trí {min_pos}")
print(f"Max: {max_val} tại vị trí {max_pos}")

# Bài 7: Đường chéo ma trận
print("\n7. Đường chéo ma trận:")

def get_diagonals(matrix):
    """Lấy đường chéo chính và phụ (ma trận vuông)"""
    n = len(matrix)
    if n != len(matrix[0]):
        return None, None
    
    main_diagonal = [matrix[i][i] for i in range(n)]
    anti_diagonal = [matrix[i][n-1-i] for i in range(n)]
    
    return main_diagonal, anti_diagonal

square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(square, "Ma trận vuông")

main_diag, anti_diag = get_diagonals(square)
print(f"Đường chéo chính: {main_diag}")
print(f"Đường chéo phụ: {anti_diag}")
print(f"Tổng đường chéo chính: {sum(main_diag)}")
print(f"Tổng đường chéo phụ: {sum(anti_diag)}")

# Bài 8: Phép toán ma trận
print("\n8. Phép toán ma trận:")

def matrix_add(A, B):
    """Cộng hai ma trận"""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] 
            for i in range(len(A))]

def matrix_scalar_multiply(matrix, scalar):
    """Nhân ma trận với số"""
    return [[element * scalar for element in row] for row in matrix]

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print_matrix(A, "Ma trận A")
print_matrix(B, "Ma trận B")

C = matrix_add(A, B)
print_matrix(C, "A + B")

A_scaled = matrix_scalar_multiply(A, 3)
print_matrix(A_scaled, "A × 3")