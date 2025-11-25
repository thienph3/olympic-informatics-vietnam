# Problem 06.02.02: Ma trận đặc biệt

print("=== MA TRẬN ĐẶC BIỆT ===")

def print_matrix(matrix):
    """In ma trận đẹp"""
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(f"{matrix[i][j]:4d}", end=" ")
        print()

# Bài 1: Ma trận xoắn ốc
def create_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # Đi từ trái sang phải (hàng trên)
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1
        
        # Đi từ trên xuống dưới (cột phải)
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Đi từ phải sang trái (hàng dưới)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
        
        # Đi từ dưới lên trên (cột trái)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    return matrix

n = int(input("Nhập kích thước ma trận xoắn ốc: "))
spiral = create_spiral_matrix(n)
print(f"\nMa trận xoắn ốc {n}×{n}:")
print_matrix(spiral)

# Bài 2: Ma phương (Magic Square) - chỉ với n lẻ
def create_magic_square(n):
    if n % 2 == 0:
        print("Ma phương chỉ tạo được với n lẻ!")
        return None
    
    magic_square = [[0] * n for _ in range(n)]
    
    # Bắt đầu từ giữa hàng đầu
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        
        # Di chuyển lên trên và sang phải
        next_i, next_j = (i - 1) % n, (j + 1) % n
        
        # Nếu ô đã có số, di chuyển xuống dưới
        if magic_square[next_i][next_j] != 0:
            i = (i + 1) % n
        else:
            i, j = next_i, next_j
    
    return magic_square

def verify_magic_square(matrix):
    """Kiểm tra ma phương có hợp lệ không"""
    n = len(matrix)
    magic_sum = n * (n * n + 1) // 2
    
    # Kiểm tra tổng các hàng
    for i in range(n):
        if sum(matrix[i]) != magic_sum:
            return False
    
    # Kiểm tra tổng các cột
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
    
    # Kiểm tra đường chéo chính
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    
    # Kiểm tra đường chéo phụ
    if sum(matrix[i][n-1-i] for i in range(n)) != magic_sum:
        return False
    
    return True

if n % 2 == 1:
    magic = create_magic_square(n)
    if magic:
        print(f"\nMa phương {n}×{n}:")
        print_matrix(magic)
        
        magic_sum = n * (n * n + 1) // 2
        print(f"Tổng ma thuật: {magic_sum}")
        print(f"Hợp lệ: {'Có' if verify_magic_square(magic) else 'Không'}")

# Bài 3: Ma trận đối xứng
def create_symmetric_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # Tạo pattern đối xứng
            matrix[i][j] = min(i, j, n-1-i, n-1-j) + 1
    
    return matrix

print(f"\nMa trận đối xứng {n}×{n}:")
symmetric = create_symmetric_matrix(n)
print_matrix(symmetric)

# Bài 4: Ma trận đường chéo
def create_diagonal_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = i + 1  # Đường chéo chính
            elif i + j == n - 1:
                matrix[i][j] = n - i  # Đường chéo phụ
    
    return matrix

print(f"\nMa trận đường chéo {n}×{n}:")
diagonal = create_diagonal_matrix(n)
print_matrix(diagonal)