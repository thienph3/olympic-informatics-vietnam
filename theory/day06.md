# Day 6: Dynamic Programming Cơ bản

## DP Concept: Overlapping Subproblems

### Khái niệm Dynamic Programming
Dynamic Programming (DP) là kỹ thuật giải quyết bài toán tối ưu bằng cách:
1. Chia bài toán thành các bài toán con nhỏ hơn
2. Lưu trữ kết quả của các bài toán con (tránh tính lại)
3. Sử dụng kết quả đã lưu để giải bài toán lớn hơn

### Điều kiện áp dụng DP
1. **Optimal Substructure**: Lời giải tối ưu chứa lời giải tối ưu của bài toán con
2. **Overlapping Subproblems**: Các bài toán con được tính lại nhiều lần

### Ví dụ: Fibonacci Problem
```python
# Recursion thuần (không hiệu quả)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)
# Time: O(2^n), Space: O(n)

# DP Solution
def fib_dp(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
# Time: O(n), Space: O(n)
```

## Memoization Technique

### Top-down Approach (Memoization)
```python
def fib_memo(n, memo={}):
    """Fibonacci với memoization"""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Sử dụng decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n-1) + fib_cached(n-2)
```

### Manual Memoization
```python
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        
        result = self.func(*args)
        self.cache[args] = result
        return result

@Memoize
def expensive_function(n):
    # Simulate expensive computation
    if n <= 1:
        return n
    return expensive_function(n-1) + expensive_function(n-2)
```

## Top-down vs Bottom-up Approach

### Top-down (Memoization)
```python
def climb_stairs_topdown(n, memo={}):
    """
    Số cách leo n bậc cầu thang (1 hoặc 2 bậc mỗi lần)
    Top-down approach
    """
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return n
    
    memo[n] = climb_stairs_topdown(n-1, memo) + climb_stairs_topdown(n-2, memo)
    return memo[n]
```

### Bottom-up (Tabulation)
```python
def climb_stairs_bottomup(n):
    """
    Bottom-up approach
    Xây dựng từ bài toán nhỏ nhất
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

### Space Optimized Bottom-up
```python
def climb_stairs_optimized(n):
    """
    Tối ưu không gian - chỉ cần 2 biến
    """
    if n <= 2:
        return n
    
    prev2 = 1  # dp[i-2]
    prev1 = 2  # dp[i-1]
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1
```

## Simple DP Examples

### 1. Minimum Cost Climbing Stairs
```python
def min_cost_climbing_stairs(cost):
    """
    Tìm chi phí tối thiểu để leo hết cầu thang
    Có thể bắt đầu từ bậc 0 hoặc 1
    """
    n = len(cost)
    if n <= 2:
        return min(cost)
    
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    # Có thể kết thúc ở bậc n-1 hoặc n-2
    return min(dp[n-1], dp[n-2])

# Test
cost = [10, 15, 20]
print(min_cost_climbing_stairs(cost))  # 15
```

### 2. House Robber
```python
def rob(nums):
    """
    Trộm nhà sao cho không trộm 2 nhà liền kề
    Tối đa hóa số tiền trộm được
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# Space optimized
def rob_optimized(nums):
    if not nums:
        return 0
    
    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]
    
    for num in nums:
        current = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = current
    
    return prev1

# Test
nums = [2, 7, 9, 3, 1]
print(rob_optimized(nums))  # 12 (2 + 9 + 1)
```

### 3. Coin Change Problem
```python
def coin_change(coins, amount):
    """
    Tìm số lượng coin tối thiểu để tạo thành amount
    Trả về -1 nếu không thể
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Test
coins = [1, 3, 4]
amount = 6
print(coin_change(coins, amount))  # 2 (3 + 3)
```

### 4. Unique Paths
```python
def unique_paths(m, n):
    """
    Số đường đi từ góc trên trái đến góc dưới phải
    Chỉ được đi xuống hoặc sang phải
    """
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Space optimized (1D array)
def unique_paths_optimized(m, n):
    dp = [1] * n
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    
    return dp[n-1]

# Test
print(unique_paths_optimized(3, 7))  # 28
```

## DP Pattern Recognition

### 1. Linear DP
```python
def max_subarray(nums):
    """
    Maximum Subarray Sum (Kadane's Algorithm)
    """
    max_ending_here = max_so_far = nums[0]
    
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
```

### 2. Grid DP
```python
def min_path_sum(grid):
    """
    Tìm đường đi có tổng nhỏ nhất từ góc trên trái đến góc dưới phải
    """
    m, n = len(grid), len(grid[0])
    
    # Initialize first row and column
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    
    # Fill the rest
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[m-1][n-1]
```

### 3. Decision DP
```python
def can_partition(nums):
    """
    Kiểm tra có thể chia mảng thành 2 tập con có tổng bằng nhau
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]
```

## Common DP Optimizations

### 1. Space Optimization
```python
# From 2D to 1D
def longest_common_subsequence_optimized(text1, text2):
    m, n = len(text1), len(text2)
    
    # Chỉ cần 2 rows thay vì m x n matrix
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        
        prev, curr = curr, prev
    
    return prev[n]
```

### 2. Rolling Array
```python
def unique_paths_rolling(m, n):
    """Sử dụng rolling array để tối ưu không gian"""
    dp = [1] * n
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    
    return dp[n-1]
```

## Debugging DP Solutions

### 1. Print DP Table
```python
def debug_dp_table(dp, title="DP Table"):
    print(f"\n{title}:")
    for i, row in enumerate(dp):
        if isinstance(row, list):
            print(f"Row {i}: {row}")
        else:
            print(f"dp[{i}] = {row}")
```

### 2. Trace Back Solution
```python
def coin_change_with_path(coins, amount):
    """Coin change với trace back path"""
    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return -1, []
    
    # Reconstruct path
    path = []
    curr = amount
    while curr > 0:
        coin = parent[curr]
        path.append(coin)
        curr -= coin
    
    return dp[amount], path

# Test
coins = [1, 3, 4]
amount = 6
min_coins, path = coin_change_with_path(coins, amount)
print(f"Min coins: {min_coins}, Path: {path}")  # Min coins: 2, Path: [3, 3]
```

## Practice Problems

### 1. Triangle Minimum Path Sum
```python
def minimum_total(triangle):
    """
    Tìm đường đi có tổng nhỏ nhất từ đỉnh xuống đáy tam giác
    """
    n = len(triangle)
    dp = triangle[-1][:]  # Copy last row
    
    # Bottom-up approach
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    
    return dp[0]
```

### 2. Decode Ways
```python
def num_decodings(s):
    """
    Số cách decode string thành letters (A=1, B=2, ..., Z=26)
    """
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n + 1):
        # Single digit
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        
        # Two digits
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]
```

## Best Practices

1. **Identify the state**: Xác định trạng thái DP cần lưu trữ
2. **Define recurrence relation**: Thiết lập công thức truy hồi
3. **Handle base cases**: Xử lý các trường hợp cơ sở
4. **Choose approach**: Top-down (memoization) vs Bottom-up (tabulation)
5. **Optimize space**: Giảm không gian nếu có thể
6. **Test with examples**: Kiểm tra với các ví dụ nhỏ