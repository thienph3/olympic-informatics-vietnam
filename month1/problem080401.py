# Problem 08.04.01: Dynamic Programming với ma trận

print("=== DYNAMIC PROGRAMMING VỚI MA TRẬN ===")

# Bài 1: Fibonacci với memoization
print("1. Fibonacci với memoization:")

def fibonacci_dp(n):
    """Fibonacci sử dụng Dynamic Programming"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def fibonacci_sequence_dp(n):
    """Tạo dãy Fibonacci n số đầu tiên"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# Test Fibonacci
n = 15
print(f"Fibonacci({n}) = {fibonacci_dp(n)}")
fib_sequence = fibonacci_sequence_dp(n)
print(f"Dãy Fibonacci {n} số đầu: {fib_sequence}")

# Bài 2: Tam giác Pascal
print("\n2. Tam giác Pascal:")

def pascal_triangle(n):
    """Tạo tam giác Pascal n hàng"""
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle

def print_pascal_triangle(triangle):
    """In tam giác Pascal đẹp"""
    n = len(triangle)
    for i, row in enumerate(triangle):
        # In khoảng trắng để căn giữa
        spaces = " " * (n - i - 1) * 2
        print(spaces, end="")
        
        # In các số trong hàng
        for num in row:
            print(f"{num:3d} ", end="")
        print()

pascal = pascal_triangle(8)
print_pascal_triangle(pascal)

# Tính tổng từng hàng (luôn là lũy thừa của 2)
row_sums = [sum(row) for row in pascal]
print(f"Tổng từng hàng: {row_sums}")

# Bài 3: Longest Common Subsequence (LCS)
print("\n3. Longest Common Subsequence:")

def lcs_length(text1, text2):
    """Tính độ dài LCS của 2 chuỗi"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def lcs_string(text1, text2):
    """Tìm chuỗi LCS thực tế"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Tính bảng DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Truy vết để tìm chuỗi LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# Test LCS
str1 = "ABCDGH"
str2 = "AEDFHR"
print(f"Chuỗi 1: {str1}")
print(f"Chuỗi 2: {str2}")
print(f"Độ dài LCS: {lcs_length(str1, str2)}")
print(f"LCS: {lcs_string(str1, str2)}")

# Bài 4: Minimum Path Sum
print("\n4. Minimum Path Sum:")

def min_path_sum(grid):
    """Tìm đường đi có tổng nhỏ nhất từ góc trái trên đến góc phải dưới"""
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    # Khởi tạo
    dp[0][0] = grid[0][0]
    
    # Hàng đầu tiên
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Cột đầu tiên
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Điền bảng DP
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]

def print_grid_with_path(grid, title="Grid"):
    """In grid đẹp"""
    print(f"{title}:")
    for row in grid:
        print([f"{x:3d}" for x in row])

# Test Min Path Sum
path_grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print_grid_with_path(path_grid, "Grid gốc")
min_sum = min_path_sum(path_grid)
print(f"Tổng đường đi nhỏ nhất: {min_sum}")

# Bài 5: Unique Paths
print("\n5. Unique Paths:")

def unique_paths(m, n):
    """Đếm số đường đi duy nhất từ (0,0) đến (m-1,n-1)"""
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

def unique_paths_with_obstacles(grid):
    """Đếm đường đi với chướng ngại vật (1 = chướng ngại)"""
    if not grid or grid[0][0] == 1:
        return 0
    
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    # Hàng đầu tiên
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] if grid[0][j] == 0 else 0
    
    # Cột đầu tiên
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] if grid[i][0] == 0 else 0
    
    # Điền bảng DP
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0
    
    return dp[m-1][n-1]

# Test Unique Paths
print(f"Số đường đi trong lưới 3x7: {unique_paths(3, 7)}")

# Test với chướng ngại vật
obstacle_grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print_grid_with_path(obstacle_grid, "Grid với chướng ngại (1 = chướng ngại)")
paths_with_obstacles = unique_paths_with_obstacles(obstacle_grid)
print(f"Số đường đi với chướng ngại: {paths_with_obstacles}")

# Bài 6: Edit Distance
print("\n6. Edit Distance:")

def edit_distance(word1, word2):
    """Tính khoảng cách chỉnh sửa (Levenshtein distance)"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Khởi tạo
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Điền bảng DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Xóa
                    dp[i][j-1],    # Chèn
                    dp[i-1][j-1]   # Thay thế
                )
    
    return dp[m][n]

# Test Edit Distance
word1 = "horse"
word2 = "ros"
print(f"Từ 1: {word1}")
print(f"Từ 2: {word2}")
print(f"Edit Distance: {edit_distance(word1, word2)}")

word1 = "intention"
word2 = "execution"
print(f"Từ 1: {word1}")
print(f"Từ 2: {word2}")
print(f"Edit Distance: {edit_distance(word1, word2)}")