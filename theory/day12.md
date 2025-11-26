# Day 12: Backtracking

## Backtracking Concept

### Khái niệm
Backtracking là kỹ thuật giải quyết bài toán bằng cách thử tất cả các khả năng có thể, và quay lại (backtrack) khi gặp đường cụt.

### Template Backtracking
```python
def backtrack(solution, choices):
    """
    Template cơ bản cho backtracking
    """
    # Base case - found complete solution
    if is_complete(solution):
        process_solution(solution)
        return
    
    # Try all possible choices
    for choice in get_choices(solution):
        # Make choice
        solution.append(choice)
        
        # Check if choice is valid
        if is_valid(solution):
            # Recurse with this choice
            backtrack(solution, choices)
        
        # Backtrack - undo choice
        solution.pop()

def is_complete(solution):
    """Kiểm tra solution đã hoàn thành chưa"""
    pass

def is_valid(solution):
    """Kiểm tra solution hiện tại có hợp lệ không"""
    pass

def get_choices(solution):
    """Lấy danh sách choices có thể từ state hiện tại"""
    pass

def process_solution(solution):
    """Xử lý solution hoàn chỉnh"""
    pass
```

## N-Queens Problem Solution

### Basic N-Queens
```python
def solve_n_queens(n):
    """
    Giải bài toán N-Queens
    Đặt n quân hậu trên bàn cờ n×n sao cho không tấn công nhau
    """
    def is_safe(board, row, col):
        """Kiểm tra có thể đặt quân hậu tại (row, col) không"""
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        
        # Check diagonal (top-left to bottom-right)
        for i in range(row):
            if board[i] - i == col - row:
                return False
        
        # Check anti-diagonal (top-right to bottom-left)
        for i in range(row):
            if board[i] + i == col + row:
                return False
        
        return True
    
    def backtrack(board, row):
        """Backtrack để tìm solution"""
        if row == n:
            # Found complete solution
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place queen
                backtrack(board, row + 1)
                # No need to explicitly remove - will be overwritten
    
    solutions = []
    board = [-1] * n  # board[i] = column of queen in row i
    backtrack(board, 0)
    
    return solutions

def print_n_queens_solution(solution):
    """In solution N-Queens dưới dạng bàn cờ"""
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

# Test N-Queens
solutions = solve_n_queens(4)
print(f"Found {len(solutions)} solutions for 4-Queens:")
for i, sol in enumerate(solutions):
    print(f"Solution {i+1}:")
    print_n_queens_solution(sol)
```

### Optimized N-Queens
```python
def solve_n_queens_optimized(n):
    """
    N-Queens tối ưu với bit manipulation
    """
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            solutions.append(board[:])
            return
        
        # Available positions = positions not attacked
        available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
        
        while available:
            # Get rightmost available position
            pos = available & -available
            available ^= pos  # Remove this position
            
            col = bin(pos).count('0') - 1  # Convert bit position to column
            board[row] = col
            
            backtrack(row + 1,
                     cols | pos,
                     (diag1 | pos) << 1,
                     (diag2 | pos) >> 1)
    
    solutions = []
    board = [-1] * n
    backtrack(0, 0, 0, 0)
    return solutions

def count_n_queens(n):
    """Chỉ đếm số solutions, không lưu trữ"""
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            return 1
        
        count = 0
        available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
        
        while available:
            pos = available & -available
            available ^= pos
            
            count += backtrack(row + 1,
                             cols | pos,
                             (diag1 | pos) << 1,
                             (diag2 | pos) >> 1)
        
        return count
    
    return backtrack(0, 0, 0, 0)

# Test optimized version
for n in range(1, 9):
    count = count_n_queens(n)
    print(f"{n}-Queens: {count} solutions")
```

## Generating Permutations

### Basic Permutations
```python
def generate_permutations(nums):
    """
    Sinh tất cả hoán vị của nums
    """
    def backtrack(current_perm):
        if len(current_perm) == len(nums):
            result.append(current_perm[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in current_perm:
                current_perm.append(nums[i])
                backtrack(current_perm)
                current_perm.pop()
    
    result = []
    backtrack([])
    return result

def generate_permutations_optimized(nums):
    """
    Permutations tối ưu với swap
    """
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            # Swap
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            # Backtrack
            nums[start], nums[i] = nums[i], nums[start]
    
    result = []
    backtrack(0)
    return result

# Test permutations
nums = [1, 2, 3]
perms = generate_permutations_optimized(nums)
print(f"Permutations of {nums}:")
for perm in perms:
    print(perm)
```

### Permutations with Duplicates
```python
def permutations_with_duplicates(nums):
    """
    Sinh permutations khi có duplicate elements
    """
    def backtrack(current_perm, used):
        if len(current_perm) == len(nums):
            result.append(current_perm[:])
            return
        
        for i in range(len(nums)):
            # Skip used elements
            if used[i]:
                continue
            
            # Skip duplicates: if current element equals previous
            # and previous is not used, skip current
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            used[i] = True
            current_perm.append(nums[i])
            backtrack(current_perm, used)
            current_perm.pop()
            used[i] = False
    
    nums.sort()  # Sort to handle duplicates
    result = []
    used = [False] * len(nums)
    backtrack([], used)
    return result

# Test with duplicates
nums_dup = [1, 1, 2]
perms_dup = permutations_with_duplicates(nums_dup)
print(f"Permutations of {nums_dup} (with duplicates):")
for perm in perms_dup:
    print(perm)
```

## Pruning Techniques

### Early Termination
```python
def subset_sum_backtrack(nums, target):
    """
    Tìm subset có tổng = target với pruning
    """
    def backtrack(index, current_sum, current_subset):
        # Pruning: if current sum exceeds target
        if current_sum > target:
            return False
        
        # Base case: found target sum
        if current_sum == target:
            result.append(current_subset[:])
            return True
        
        # Base case: no more elements
        if index >= len(nums):
            return False
        
        # Pruning: if remaining sum cannot reach target
        remaining_sum = sum(nums[index:])
        if current_sum + remaining_sum < target:
            return False
        
        # Choice 1: Include current element
        current_subset.append(nums[index])
        if backtrack(index + 1, current_sum + nums[index], current_subset):
            return True
        current_subset.pop()
        
        # Choice 2: Exclude current element
        return backtrack(index + 1, current_sum, current_subset)
    
    nums.sort()  # Sort for better pruning
    result = []
    backtrack(0, 0, [])
    return result

# Test subset sum
nums = [2, 3, 6, 7]
target = 7
subsets = subset_sum_backtrack(nums, target)
print(f"Subsets with sum {target}: {subsets}")
```

### Constraint Propagation
```python
def sudoku_solver(board):
    """
    Sudoku solver với constraint propagation
    """
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
    
    def get_candidates(board, row, col):
        """Get possible values for cell (row, col)"""
        if board[row][col] != '.':
            return []
        
        candidates = []
        for num in '123456789':
            if is_valid(board, row, col, num):
                candidates.append(num)
        return candidates
    
    def find_best_cell(board):
        """Find empty cell with minimum candidates (MRV heuristic)"""
        min_candidates = 10
        best_cell = None
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    candidates = get_candidates(board, i, j)
                    if len(candidates) < min_candidates:
                        min_candidates = len(candidates)
                        best_cell = (i, j, candidates)
        
        return best_cell
    
    def solve():
        cell_info = find_best_cell(board)
        if not cell_info:
            return True  # No empty cells - solved!
        
        row, col, candidates = cell_info
        
        for num in candidates:
            board[row][col] = num
            if solve():
                return True
            board[row][col] = '.'  # Backtrack
        
        return False
    
    solve()
    return board

# Test Sudoku (simplified example)
def print_sudoku(board):
    for row in board:
        print(' '.join(row))
    print()
```

### Branch and Bound
```python
def traveling_salesman_backtrack(graph):
    """
    TSP với branch and bound
    """
    n = len(graph)
    
    def calculate_lower_bound(path, visited):
        """Calculate lower bound for current partial path"""
        bound = 0
        
        # Add cost of current path
        for i in range(len(path) - 1):
            bound += graph[path[i]][path[i + 1]]
        
        # Add minimum outgoing edge for each unvisited vertex
        for i in range(n):
            if i not in visited:
                min_edge = min(graph[i][j] for j in range(n) if j != i)
                bound += min_edge
        
        return bound
    
    def backtrack(path, visited, current_cost):
        nonlocal best_cost, best_path
        
        if len(path) == n:
            # Complete tour - return to start
            total_cost = current_cost + graph[path[-1]][path[0]]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path + [path[0]]
            return
        
        # Pruning: if lower bound exceeds best known solution
        lower_bound = calculate_lower_bound(path, visited)
        if lower_bound >= best_cost:
            return
        
        # Try all unvisited cities
        for city in range(n):
            if city not in visited:
                new_cost = current_cost + graph[path[-1]][city]
                
                # Pruning: if current cost already exceeds best
                if new_cost >= best_cost:
                    continue
                
                path.append(city)
                visited.add(city)
                backtrack(path, visited, new_cost)
                path.pop()
                visited.remove(city)
    
    best_cost = float('inf')
    best_path = []
    
    # Start from city 0
    visited = {0}
    backtrack([0], visited, 0)
    
    return best_path, best_cost
```

## Advanced Backtracking Problems

### Word Search
```python
def word_search(board, word):
    """
    Tìm word trong 2D board
    """
    def backtrack(row, col, index):
        # Base case: found complete word
        if index == len(word):
            return True
        
        # Boundary check
        if (row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or
            board[row][col] != word[index]):
            return False
        
        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Try all 4 directions
        found = (backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1))
        
        # Backtrack
        board[row][col] = temp
        
        return found
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    
    return False

# Test word search
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print(word_search(board, "ABCCED"))  # True
print(word_search(board, "SEE"))     # True
print(word_search(board, "ABCB"))    # False
```

### Combination Sum
```python
def combination_sum(candidates, target):
    """
    Tìm tất cả combinations có tổng = target
    Có thể sử dụng số nhiều lần
    """
    def backtrack(start, current_combination, current_sum):
        if current_sum == target:
            result.append(current_combination[:])
            return
        
        if current_sum > target:
            return
        
        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            # Can reuse same number (start from i, not i+1)
            backtrack(i, current_combination, current_sum + candidates[i])
            current_combination.pop()
    
    candidates.sort()  # Sort for optimization
    result = []
    backtrack(0, [], 0)
    return result

def combination_sum_unique(candidates, target):
    """
    Combination sum với mỗi số chỉ dùng 1 lần
    """
    def backtrack(start, current_combination, current_sum):
        if current_sum == target:
            result.append(current_combination[:])
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            if current_sum + candidates[i] > target:
                break  # Pruning
            
            current_combination.append(candidates[i])
            backtrack(i + 1, current_combination, current_sum + candidates[i])
            current_combination.pop()
    
    candidates.sort()
    result = []
    backtrack(0, [], 0)
    return result

# Test combination sum
candidates = [2, 3, 6, 7]
target = 7
combinations = combination_sum(candidates, target)
print(f"Combination sum for target {target}: {combinations}")
```

### Palindrome Partitioning
```python
def palindrome_partitioning(s):
    """
    Partition string thành palindromes
    """
    def is_palindrome(string):
        return string == string[::-1]
    
    def backtrack(start, current_partition):
        if start >= len(s):
            result.append(current_partition[:])
            return
        
        for end in range(start, len(s)):
            substring = s[start:end + 1]
            if is_palindrome(substring):
                current_partition.append(substring)
                backtrack(end + 1, current_partition)
                current_partition.pop()
    
    result = []
    backtrack(0, [])
    return result

# Optimized with precomputed palindrome check
def palindrome_partitioning_optimized(s):
    """
    Palindrome partitioning với precomputed palindrome table
    """
    n = len(s)
    
    # Precompute palindrome table
    is_palindrome = [[False] * n for _ in range(n)]
    
    # Single characters are palindromes
    for i in range(n):
        is_palindrome[i][i] = True
    
    # Check for 2-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palindrome[i][i + 1] = True
    
    # Check for palindromes of length 3+
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
    
    def backtrack(start, current_partition):
        if start >= n:
            result.append(current_partition[:])
            return
        
        for end in range(start, n):
            if is_palindrome[start][end]:
                current_partition.append(s[start:end + 1])
                backtrack(end + 1, current_partition)
                current_partition.pop()
    
    result = []
    backtrack(0, [])
    return result

# Test palindrome partitioning
s = "aab"
partitions = palindrome_partitioning_optimized(s)
print(f"Palindrome partitions of '{s}': {partitions}")
```

## Optimization Techniques

### Memoization in Backtracking
```python
def word_break_backtrack(s, word_dict):
    """
    Word break với memoization
    """
    memo = {}
    
    def backtrack(start):
        if start in memo:
            return memo[start]
        
        if start >= len(s):
            return True
        
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_dict and backtrack(end):
                memo[start] = True
                return True
        
        memo[start] = False
        return False
    
    return backtrack(0)
```

### Iterative Deepening
```python
def iterative_deepening_search(problem, max_depth):
    """
    Iterative deepening search
    """
    for depth in range(max_depth + 1):
        result = depth_limited_search(problem, depth)
        if result is not None:
            return result
    return None

def depth_limited_search(problem, limit):
    """
    Depth-limited search
    """
    def dls(state, depth):
        if problem.is_goal(state):
            return state
        
        if depth <= 0:
            return None
        
        for action in problem.get_actions(state):
            child = problem.get_result(state, action)
            result = dls(child, depth - 1)
            if result is not None:
                return result
        
        return None
    
    return dls(problem.initial_state, limit)
```

## Best Practices

1. **Define Clear Base Cases**: Khi nào dừng recursion
2. **Implement Proper Backtracking**: Undo changes khi quay lại
3. **Use Pruning**: Cắt bỏ branches không cần thiết
4. **Choose Good Variable Ordering**: Thử variables có ít choices trước
5. **Implement Constraint Checking**: Kiểm tra constraints sớm
6. **Consider Memoization**: Cache results để tránh recomputation
7. **Optimize Data Structures**: Sử dụng efficient data structures