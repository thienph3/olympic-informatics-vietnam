"""
Problem 110402: Backtracking và divide-and-conquer
Solve problems using backtracking và divide-and-conquer techniques

Bài 1: Backtracking Problems
- N-Queens problem
- Sudoku solver
- Subset sum problem
- Permutation generation

Bài 2: Divide-and-Conquer Algorithms
- Binary search variants
- Maximum subarray problem
- Closest pair of points
- Matrix multiplication
"""

# Backtracking Problems

def solve_n_queens(n):
    """Solve N-Queens problem using backtracking"""
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        
        # Check diagonals
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        
        return True
    
    def backtrack(board, row):
        if row == n:
            return [board[:]]  # Found a solution
        
        solutions = []
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solutions.extend(backtrack(board, row + 1))
                board[row] = -1  # backtrack
        
        return solutions
    
    return backtrack([-1] * n, 0)

def print_chess_board(solution, n):
    """Print chess board với queens"""
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_sudoku(board):
    """Solve Sudoku puzzle using backtracking"""
    def is_valid(board, row, col, num):
        # Check row
        for j in range(9):
            if board[row][j] == num:
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = 0  # backtrack
                    return False
        return True
    
    return solve()

def subset_sum_backtrack(numbers, target):
    """Find all subsets that sum to target using backtracking"""
    def backtrack(index, current_subset, current_sum):
        if current_sum == target:
            return [current_subset[:]]
        
        if index >= len(numbers) or current_sum > target:
            return []
        
        solutions = []
        
        # Include current number
        current_subset.append(numbers[index])
        solutions.extend(backtrack(index + 1, current_subset, current_sum + numbers[index]))
        current_subset.pop()
        
        # Exclude current number
        solutions.extend(backtrack(index + 1, current_subset, current_sum))
        
        return solutions
    
    return backtrack(0, [], 0)

def generate_permutations_backtrack(arr):
    """Generate all permutations using backtracking"""
    def backtrack(current_perm, remaining):
        if not remaining:
            return [current_perm[:]]
        
        result = []
        for i in range(len(remaining)):
            # Choose
            current_perm.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            
            # Explore
            result.extend(backtrack(current_perm, new_remaining))
            
            # Unchoose (backtrack)
            current_perm.pop()
        
        return result
    
    return backtrack([], arr)

def solve_maze(maze):
    """Solve maze using backtracking"""
    rows, cols = len(maze), len(maze[0])
    path = []
    
    def is_safe(x, y):
        return (0 <= x < rows and 0 <= y < cols and 
                maze[x][y] == 0)  # 0 = path, 1 = wall
    
    def backtrack(x, y, target_x, target_y):
        if x == target_x and y == target_y:
            path.append((x, y))
            return True
        
        if not is_safe(x, y):
            return False
        
        # Mark as visited
        maze[x][y] = 2
        path.append((x, y))
        
        # Try all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if backtrack(x + dx, y + dy, target_x, target_y):
                return True
        
        # Backtrack
        path.pop()
        maze[x][y] = 0  # Unmark
        return False
    
    if backtrack(0, 0, rows-1, cols-1):
        return path
    return []

def word_search(board, word):
    """Find word in 2D board using backtracking"""
    rows, cols = len(board), len(board[0])
    
    def backtrack(x, y, index):
        if index == len(word):
            return True
        
        if (x < 0 or x >= rows or y < 0 or y >= cols or 
            board[x][y] != word[index]):
            return False
        
        # Mark as visited
        temp = board[x][y]
        board[x][y] = '#'
        
        # Try all 4 directions
        found = (backtrack(x+1, y, index+1) or
                backtrack(x-1, y, index+1) or
                backtrack(x, y+1, index+1) or
                backtrack(x, y-1, index+1))
        
        # Restore
        board[x][y] = temp
        
        return found
    
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False

# Divide-and-Conquer Algorithms

def binary_search_first_occurrence(arr, target):
    """Find first occurrence of target using divide-and-conquer"""
    def search(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Check if this is the first occurrence
            if mid == 0 or arr[mid-1] != target:
                return mid
            else:
                return search(left, mid-1)
        elif arr[mid] < target:
            return search(mid+1, right)
        else:
            return search(left, mid-1)
    
    return search(0, len(arr)-1)

def binary_search_last_occurrence(arr, target):
    """Find last occurrence of target using divide-and-conquer"""
    def search(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Check if this is the last occurrence
            if mid == len(arr)-1 or arr[mid+1] != target:
                return mid
            else:
                return search(mid+1, right)
        elif arr[mid] < target:
            return search(mid+1, right)
        else:
            return search(left, mid-1)
    
    return search(0, len(arr)-1)

def maximum_subarray_divide_conquer(arr):
    """Find maximum subarray sum using divide-and-conquer"""
    def max_crossing_sum(arr, left, mid, right):
        # Left side
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left-1, -1):
            current_sum += arr[i]
            left_sum = max(left_sum, current_sum)
        
        # Right side
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid+1, right+1):
            current_sum += arr[i]
            right_sum = max(right_sum, current_sum)
        
        return left_sum + right_sum
    
    def max_subarray_rec(arr, left, right):
        if left == right:
            return arr[left]
        
        mid = (left + right) // 2
        
        left_sum = max_subarray_rec(arr, left, mid)
        right_sum = max_subarray_rec(arr, mid+1, right)
        cross_sum = max_crossing_sum(arr, left, mid, right)
        
        return max(left_sum, right_sum, cross_sum)
    
    return max_subarray_rec(arr, 0, len(arr)-1)

def closest_pair_of_points(points):
    """Find closest pair of points using divide-and-conquer"""
    import math
    
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def closest_pair_rec(px, py):
        n = len(px)
        
        # Base case
        if n <= 3:
            min_dist = float('inf')
            closest = None
            for i in range(n):
                for j in range(i+1, n):
                    dist = distance(px[i], px[j])
                    if dist < min_dist:
                        min_dist = dist
                        closest = (px[i], px[j])
            return min_dist, closest
        
        # Divide
        mid = n // 2
        midpoint = px[mid]
        
        pyl = [point for point in py if point[0] <= midpoint[0]]
        pyr = [point for point in py if point[0] > midpoint[0]]
        
        # Conquer
        dl, pair_l = closest_pair_rec(px[:mid], pyl)
        dr, pair_r = closest_pair_rec(px[mid:], pyr)
        
        # Find minimum of the two
        if dl <= dr:
            min_dist, closest_pair = dl, pair_l
        else:
            min_dist, closest_pair = dr, pair_r
        
        # Check points near the dividing line
        strip = [point for point in py if abs(point[0] - midpoint[0]) < min_dist]
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
                dist = distance(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (strip[i], strip[j])
                j += 1
        
        return min_dist, closest_pair
    
    # Sort points
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    
    return closest_pair_rec(px, py)

def matrix_multiply_divide_conquer(A, B):
    """Matrix multiplication using divide-and-conquer (Strassen-like)"""
    n = len(A)
    
    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Initialize result matrix
    C = [[0] * n for _ in range(n)]
    
    if n == 2:
        # Direct multiplication for 2x2
        C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
        C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
        C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
        C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]
        return C
    
    # Divide matrices into quadrants
    mid = n // 2
    
    # Extract quadrants
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    # Recursive multiplication
    C11 = matrix_add(matrix_multiply_divide_conquer(A11, B11),
                     matrix_multiply_divide_conquer(A12, B21))
    C12 = matrix_add(matrix_multiply_divide_conquer(A11, B12),
                     matrix_multiply_divide_conquer(A12, B22))
    C21 = matrix_add(matrix_multiply_divide_conquer(A21, B11),
                     matrix_multiply_divide_conquer(A22, B21))
    C22 = matrix_add(matrix_multiply_divide_conquer(A21, B12),
                     matrix_multiply_divide_conquer(A22, B22))
    
    # Combine results
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    
    return C

def matrix_add(A, B):
    """Add two matrices"""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def power_divide_conquer(base, exp):
    """Fast exponentiation using divide-and-conquer"""
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    if exp % 2 == 0:
        half_power = power_divide_conquer(base, exp // 2)
        return half_power * half_power
    else:
        return base * power_divide_conquer(base, exp - 1)

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Backtracking Problems ===")
    
    # Test N-Queens
    print("N-Queens (n=4):")
    solutions = solve_n_queens(4)
    print(f"Found {len(solutions)} solutions:")
    for i, solution in enumerate(solutions[:2]):  # Show first 2
        print(f"Solution {i+1}:")
        print_chess_board(solution, 4)
    
    # Test Sudoku
    print("Sudoku solver:")
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    if solve_sudoku(sudoku_board):
        print("Sudoku solved!")
        for row in sudoku_board[:3]:  # Show first 3 rows
            print(row)
        print("...")
    
    # Test subset sum
    print(f"\nSubset sum:")
    numbers = [1, 2, 3, 4, 5]
    target = 5
    subsets = subset_sum_backtrack(numbers, target)
    print(f"Subsets of {numbers} that sum to {target}: {subsets}")
    
    # Test maze solving
    print(f"\nMaze solving:")
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    
    path = solve_maze([row[:] for row in maze])  # Copy maze
    print(f"Path through maze: {path}")
    
    print("\n=== Bài 2: Divide-and-Conquer Algorithms ===")
    
    # Test binary search variants
    arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    target = 2
    print(f"Array: {arr}")
    print(f"First occurrence of {target}: {binary_search_first_occurrence(arr, target)}")
    print(f"Last occurrence of {target}: {binary_search_last_occurrence(arr, target)}")
    
    # Test maximum subarray
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = maximum_subarray_divide_conquer(arr)
    print(f"\nMaximum subarray sum in {arr}: {max_sum}")
    
    # Test closest pair of points
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    min_dist, closest = closest_pair_of_points(points)
    print(f"\nClosest pair in {points}:")
    print(f"Distance: {min_dist:.2f}, Pair: {closest}")
    
    # Test fast exponentiation
    result = power_divide_conquer(2, 10)
    print(f"\n2^10 = {result}")
    
    # Test matrix multiplication
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = matrix_multiply_divide_conquer(A, B)
    print(f"\nMatrix multiplication:")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"A × B = {C}")

    print("\n=== Bài tập thực hành ===")
    print("1. Solve cryptarithmetic puzzles với backtracking")
    print("2. Implement quickselect algorithm")
    print("3. Solve graph coloring problem")
    print("4. Build expression tree evaluator với divide-and-conquer")