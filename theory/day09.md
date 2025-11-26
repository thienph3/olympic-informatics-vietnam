# Day 9: Advanced Dynamic Programming

## 0/1 Knapsack Problem

### Khái niệm
Cho n đồ vật, mỗi đồ vật có trọng lượng w[i] và giá trị v[i]. Túi có sức chứa W. Tìm cách chọn đồ vật để tối đa hóa giá trị mà không vượt quá sức chứa.

### Basic 0/1 Knapsack
```python
def knapsack_01(weights, values, W):
    """
    0/1 Knapsack - mỗi đồ vật chỉ chọn 1 lần
    Time: O(nW), Space: O(nW)
    """
    n = len(weights)
    # dp[i][w] = max value với i đồ vật đầu và sức chứa w
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            # Không chọn đồ vật i-1
            dp[i][w] = dp[i-1][w]
            
            # Chọn đồ vật i-1 nếu có thể
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w - weights[i-1]] + values[i-1])
    
    return dp[n][W]

# Test
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7
print(knapsack_01(weights, values, W))  # 9
```

### Space Optimized Knapsack
```python
def knapsack_01_optimized(weights, values, W):
    """
    Space optimized: O(W) thay vì O(nW)
    """
    n = len(weights)
    dp = [0] * (W + 1)
    
    for i in range(n):
        # Duyệt ngược để tránh sử dụng giá trị đã update
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[W]

def knapsack_with_items(weights, values, W):
    """Knapsack với trace back items được chọn"""
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w - weights[i-1]] + values[i-1])
    
    # Trace back
    w = W
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)  # Item index
            w -= weights[i-1]
    
    return dp[n][W], selected[::-1]

# Test
max_value, items = knapsack_with_items(weights, values, W)
print(f"Max value: {max_value}, Items: {items}")
```

## Unbounded Knapsack

### Khái niệm
Tương tự 0/1 knapsack nhưng mỗi đồ vật có thể chọn nhiều lần.

### Implementation
```python
def unbounded_knapsack(weights, values, W):
    """
    Unbounded Knapsack - có thể chọn mỗi item nhiều lần
    Time: O(nW), Space: O(W)
    """
    dp = [0] * (W + 1)
    
    for w in range(1, W + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[W]

def unbounded_knapsack_with_count(weights, values, W):
    """Unbounded knapsack với đếm số lượng mỗi item"""
    n = len(weights)
    dp = [0] * (W + 1)
    count = [[0] * n for _ in range(W + 1)]
    
    for w in range(1, W + 1):
        for i in range(n):
            if weights[i] <= w:
                new_value = dp[w - weights[i]] + values[i]
                if new_value > dp[w]:
                    dp[w] = new_value
                    # Copy count từ state trước
                    count[w] = count[w - weights[i]][:]
                    count[w][i] += 1
    
    return dp[W], count[W]

# Test
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7
max_val, item_count = unbounded_knapsack_with_count(weights, values, W)
print(f"Max value: {max_val}, Item counts: {item_count}")
```

## DP State Design

### Multi-dimensional DP States
```python
def edit_distance(word1, word2):
    """
    Edit Distance (Levenshtein Distance)
    State: dp[i][j] = min operations để chuyển word1[:i] thành word2[:j]
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]

def longest_common_subsequence(text1, text2):
    """
    LCS với 2D state
    State: dp[i][j] = LCS length của text1[:i] và text2[:j]
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

### Complex State Design
```python
def max_profit_with_cooldown(prices):
    """
    Stock với cooldown - phức tạp state design
    State: held[i], sold[i], rest[i]
    """
    if not prices:
        return 0
    
    n = len(prices)
    # held[i] = max profit khi hold stock ở ngày i
    # sold[i] = max profit khi bán stock ở ngày i  
    # rest[i] = max profit khi rest ở ngày i
    
    held = [0] * n
    sold = [0] * n
    rest = [0] * n
    
    held[0] = -prices[0]  # Mua ngày đầu
    
    for i in range(1, n):
        held[i] = max(held[i-1], rest[i-1] - prices[i])
        sold[i] = held[i-1] + prices[i]
        rest[i] = max(rest[i-1], sold[i-1])
    
    return max(sold[n-1], rest[n-1])

def max_profit_k_transactions(prices, k):
    """
    Stock với tối đa k transactions
    State: buy[i][j], sell[i][j] = max profit với i transactions ở ngày j
    """
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # Nếu k >= n//2, có thể trade không giới hạn
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
    # DP với k transactions
    buy = [[-float('inf')] * n for _ in range(k + 1)]
    sell = [[0] * n for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        buy[i][0] = -prices[0]
        for j in range(1, n):
            buy[i][j] = max(buy[i][j-1], sell[i-1][j-1] - prices[j])
            sell[i][j] = max(sell[i][j-1], buy[i][j-1] + prices[j])
    
    return sell[k][n-1]
```

## Space Optimization Techniques

### Rolling Array
```python
def longest_palindromic_subsequence(s):
    """
    LPS với space optimization
    Từ O(n²) xuống O(n)
    """
    n = len(s)
    prev = [0] * n
    curr = [0] * n
    
    # Base case: single characters
    for i in range(n):
        prev[i] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                if length == 2:
                    curr[i] = 2
                else:
                    curr[i] = prev[i + 1] + 2
            else:
                curr[i] = max(prev[i], prev[i + 1])
        
        prev, curr = curr, prev
    
    return prev[0]

def coin_change_space_optimized(coins, amount):
    """
    Coin change với O(amount) space thay vì O(n * amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

### State Compression
```python
def unique_paths_with_obstacles(grid):
    """
    Unique paths với obstacles - state compression
    """
    if not grid or grid[0][0] == 1:
        return 0
    
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]
    
    return dp[n-1]

def min_path_sum_optimized(grid):
    """Min path sum với O(min(m,n)) space"""
    m, n = len(grid), len(grid[0])
    
    # Chọn dimension nhỏ hơn để optimize
    if m > n:
        grid = list(zip(*grid))  # Transpose
        m, n = n, m
    
    dp = [float('inf')] * m
    dp[0] = grid[0][0]
    
    # Initialize first column
    for i in range(1, m):
        dp[i] = dp[i-1] + grid[i][0]
    
    # Process remaining columns
    for j in range(1, n):
        dp[0] += grid[0][j]
        for i in range(1, m):
            dp[i] = min(dp[i], dp[i-1]) + grid[i][j]
    
    return dp[m-1]
```

## Advanced DP Patterns

### Interval DP
```python
def matrix_chain_multiplication(matrices):
    """
    Matrix Chain Multiplication
    State: dp[i][j] = min cost để nhân matrices từ i đến j
    """
    n = len(matrices)
    if n < 2:
        return 0
    
    # dp[i][j] = min cost to multiply matrices from i to j
    dp = [[0] * n for _ in range(n)]
    
    # length = chain length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k+1][j] + 
                       matrices[i][0] * matrices[k][1] * matrices[j][1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n-1]

def palindrome_partitioning_min_cuts(s):
    """
    Min cuts để partition string thành palindromes
    """
    n = len(s)
    
    # Precompute palindrome check
    is_palindrome = [[False] * n for _ in range(n)]
    for i in range(n):
        is_palindrome[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or is_palindrome[i+1][j-1]:
                    is_palindrome[i][j] = True
    
    # DP for min cuts
    dp = [float('inf')] * n
    
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_palindrome[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
    
    return dp[n-1]
```

### Digit DP
```python
def count_numbers_with_digit_sum(n, target_sum):
    """
    Đếm số có n chữ số với tổng chữ số = target_sum
    """
    memo = {}
    
    def dp(pos, current_sum, tight, started):
        if pos == n:
            return 1 if current_sum == target_sum and started else 0
        
        if (pos, current_sum, tight, started) in memo:
            return memo[(pos, current_sum, tight, started)]
        
        limit = 9 if not tight else int(str(10**n - 1)[pos])
        result = 0
        
        for digit in range(0, limit + 1):
            new_tight = tight and (digit == limit)
            new_started = started or (digit > 0)
            new_sum = current_sum + digit if new_started else current_sum
            
            if new_sum <= target_sum:
                result += dp(pos + 1, new_sum, new_tight, new_started)
        
        memo[(pos, current_sum, tight, started)] = result
        return result
    
    return dp(0, 0, True, False)
```

## Practice Problems

### House Robber Variants
```python
def rob_circular(nums):
    """House Robber II - houses arranged in circle"""
    if len(nums) == 1:
        return nums[0]
    
    def rob_linear(houses):
        prev2 = prev1 = 0
        for money in houses:
            curr = max(prev1, prev2 + money)
            prev2, prev1 = prev1, curr
        return prev1
    
    # Case 1: Rob house 0, can't rob house n-1
    # Case 2: Don't rob house 0, can rob house n-1
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

def rob_tree(root):
    """House Robber III - houses in binary tree"""
    def dfs(node):
        if not node:
            return (0, 0)  # (rob, not_rob)
        
        left_rob, left_not_rob = dfs(node.left)
        right_rob, right_not_rob = dfs(node.right)
        
        # Rob current node
        rob = node.val + left_not_rob + right_not_rob
        
        # Don't rob current node
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return (rob, not_rob)
    
    return max(dfs(root))
```

### Partition Problems
```python
def can_partition_equal_sum(nums):
    """Partition array into 2 equal sum subsets"""
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

def min_subset_sum_difference(nums):
    """Minimize difference between 2 subset sums"""
    total = sum(nums)
    target = total // 2
    
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    # Find largest sum <= target that's achievable
    for i in range(target, -1, -1):
        if dp[i]:
            return total - 2 * i
    
    return total
```

## Debugging DP

### Common Mistakes
```python
def debug_knapsack():
    """Common debugging techniques for DP"""
    
    # 1. Print DP table
    def print_dp_table(dp, weights, values):
        print("DP Table:")
        for i in range(len(dp)):
            print(f"Item {i}: {dp[i]}")
    
    # 2. Verify base cases
    def verify_base_cases(dp):
        assert dp[0][0] == 0, "Base case failed"
        print("Base cases verified")
    
    # 3. Check transitions
    def check_transition(dp, i, w, weights, values):
        expected = dp[i-1][w]
        if weights[i-1] <= w:
            expected = max(expected, dp[i-1][w-weights[i-1]] + values[i-1])
        
        assert dp[i][w] == expected, f"Transition error at ({i}, {w})"
    
    # 4. Trace back solution
    def trace_solution(dp, weights, values, W):
        n = len(weights)
        w = W
        items = []
        
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                items.append(i-1)
                w -= weights[i-1]
        
        return items[::-1]
```