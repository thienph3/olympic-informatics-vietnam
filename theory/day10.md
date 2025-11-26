# Day 10: DP on Sequences

## Longest Common Subsequence (LCS)

### Khái niệm
LCS là subsequence dài nhất chung của 2 sequences. Subsequence không cần liên tiếp nhưng phải giữ thứ tự.

### Basic LCS Implementation
```python
def lcs_length(text1, text2):
    """
    Tính độ dài LCS
    Time: O(mn), Space: O(mn)
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

def lcs_string(text1, text2):
    """
    Trả về LCS string thực tế
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct LCS
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

# Test
text1 = "ABCDGH"
text2 = "AEDFHR"
print(f"LCS length: {lcs_length(text1, text2)}")  # 3
print(f"LCS string: {lcs_string(text1, text2)}")  # "ADH"
```

### Space Optimized LCS
```python
def lcs_space_optimized(text1, text2):
    """
    LCS với O(min(m,n)) space
    """
    # Đảm bảo text2 là string ngắn hơn
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    
    m, n = len(text1), len(text2)
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

def lcs_rolling_array(text1, text2):
    """LCS với rolling array technique"""
    m, n = len(text1), len(text2)
    dp = [0] * (n + 1)
    
    for i in range(1, m + 1):
        prev_diag = 0
        for j in range(1, n + 1):
            temp = dp[j]
            if text1[i-1] == text2[j-1]:
                dp[j] = prev_diag + 1
            else:
                dp[j] = max(dp[j], dp[j-1])
            prev_diag = temp
    
    return dp[n]
```

## Longest Increasing Subsequence (LIS)

### Basic LIS - O(n²)
```python
def lis_dp(nums):
    """
    LIS với DP cơ bản
    Time: O(n²), Space: O(n)
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # dp[i] = LIS length ending at index i
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def lis_with_sequence(nums):
    """LIS với trả về sequence thực tế"""
    if not nums:
        return 0, []
    
    n = len(nums)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    # Find max length and its ending index
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # Reconstruct sequence
    lis = []
    current = max_index
    while current != -1:
        lis.append(nums[current])
        current = parent[current]
    
    return max_length, lis[::-1]

# Test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
length, sequence = lis_with_sequence(nums)
print(f"LIS length: {length}")  # 4
print(f"LIS sequence: {sequence}")  # [2, 3, 7, 18]
```

### Optimized LIS - O(n log n)
```python
import bisect

def lis_binary_search(nums):
    """
    LIS với binary search
    Time: O(n log n), Space: O(n)
    """
    if not nums:
        return 0
    
    # tails[i] = smallest ending element of LIS with length i+1
    tails = []
    
    for num in nums:
        # Binary search for position to insert/replace
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            tails.append(num)  # Extend LIS
        else:
            tails[pos] = num   # Replace with smaller element
    
    return len(tails)

def lis_binary_search_with_sequence(nums):
    """LIS O(n log n) với reconstruct sequence"""
    if not nums:
        return 0, []
    
    n = len(nums)
    tails = []
    predecessors = [-1] * n
    tail_indices = []  # indices of elements in tails
    
    for i, num in enumerate(nums):
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            tails.append(num)
            tail_indices.append(i)
        else:
            tails[pos] = num
            tail_indices[pos] = i
        
        # Set predecessor
        if pos > 0:
            predecessors[i] = tail_indices[pos - 1]
    
    # Reconstruct sequence
    lis = []
    current = tail_indices[-1] if tail_indices else -1
    
    while current != -1:
        lis.append(nums[current])
        current = predecessors[current]
    
    return len(tails), lis[::-1]
```

### LIS Variants
```python
def lis_non_decreasing(nums):
    """LIS cho phép equal elements"""
    tails = []
    
    for num in nums:
        pos = bisect.bisect_right(tails, num)  # bisect_right thay vì bisect_left
        
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)

def longest_decreasing_subsequence(nums):
    """Longest Decreasing Subsequence"""
    # Reverse array và tìm LIS
    return lis_binary_search(nums[::-1])

def lis_with_difference_constraint(nums, max_diff):
    """LIS với constraint: nums[j] - nums[i] <= max_diff"""
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] >= nums[j] and nums[i] - nums[j] <= max_diff:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

## Edit Distance Algorithm

### Basic Edit Distance
```python
def edit_distance(word1, word2):
    """
    Minimum edit distance (Levenshtein distance)
    Operations: insert, delete, replace
    Time: O(mn), Space: O(mn)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from word1
    
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters to get word2
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete from word1
                    dp[i][j-1],    # Insert to word1
                    dp[i-1][j-1]   # Replace in word1
                )
    
    return dp[m][n]

def edit_distance_with_operations(word1, word2):
    """Edit distance với trace back operations"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    # Trace back operations
    operations = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            operations.append(f"Replace '{word1[i-1]}' with '{word2[j-1]}'")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            operations.append(f"Delete '{word1[i-1]}'")
            i -= 1
        else:
            operations.append(f"Insert '{word2[j-1]}'")
            j -= 1
    
    return dp[m][n], operations[::-1]

# Test
word1 = "horse"
word2 = "ros"
distance, ops = edit_distance_with_operations(word1, word2)
print(f"Edit distance: {distance}")
print("Operations:", ops)
```

### Space Optimized Edit Distance
```python
def edit_distance_optimized(word1, word2):
    """
    Edit distance với O(min(m,n)) space
    """
    # Ensure word2 is shorter
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
        
        prev, curr = curr, prev
    
    return prev[n]
```

## DP on Strings và Arrays

### Palindrome Problems
```python
def longest_palindromic_subsequence(s):
    """
    Longest Palindromic Subsequence
    LPS(s) = LCS(s, reverse(s))
    """
    return lcs_length(s, s[::-1])

def longest_palindromic_substring(s):
    """
    Longest Palindromic Substring
    Time: O(n²), Space: O(n²)
    """
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for 2-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]

def count_palindromic_substrings(s):
    """Đếm số palindromic substrings"""
    n = len(s)
    count = 0
    
    # Expand around centers
    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    
    for i in range(n):
        expand_around_center(i, i)      # Odd length palindromes
        expand_around_center(i, i + 1)  # Even length palindromes
    
    return count
```

### String Matching DP
```python
def is_subsequence(s, t):
    """
    Kiểm tra s có phải subsequence của t không
    Time: O(n), Space: O(1)
    """
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)

def num_distinct_subsequences(s, t):
    """
    Đếm số cách t xuất hiện như subsequence trong s
    """
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Empty string is subsequence of any string in 1 way
    for i in range(m + 1):
        dp[i][0] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j]  # Don't use s[i-1]
            
            if s[i-1] == t[j-1]:
                dp[i][j] += dp[i-1][j-1]  # Use s[i-1]
    
    return dp[m][n]

def wildcard_matching(s, p):
    """
    Wildcard pattern matching
    '?' matches any single character
    '*' matches any sequence of characters
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    dp[0][0] = True
    
    # Handle patterns like a* or *a* etc.
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]
```

### Array DP Problems
```python
def max_subarray_sum(nums):
    """
    Maximum Subarray Sum (Kadane's Algorithm)
    """
    max_ending_here = max_so_far = nums[0]
    
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def max_product_subarray(nums):
    """Maximum Product Subarray"""
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)
    
    return result

def longest_arithmetic_subsequence(nums):
    """Longest Arithmetic Subsequence"""
    n = len(nums)
    if n <= 2:
        return n
    
    max_length = 2
    
    # dp[i][d] = length of arithmetic subsequence ending at i with difference d
    dp = [{}] * n
    
    for i in range(n):
        dp[i] = {}
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            max_length = max(max_length, dp[i][diff])
    
    return max_length
```

## Advanced Sequence DP

### Multiple Sequences
```python
def shortest_common_supersequence(str1, str2):
    """
    Shortest Common Supersequence
    SCS length = len(str1) + len(str2) - LCS(str1, str2)
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill LCS table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Construct SCS
    scs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            scs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            scs.append(str1[i-1])
            i -= 1
        else:
            scs.append(str2[j-1])
            j -= 1
    
    # Add remaining characters
    while i > 0:
        scs.append(str1[i-1])
        i -= 1
    
    while j > 0:
        scs.append(str2[j-1])
        j -= 1
    
    return ''.join(reversed(scs))

def interleaving_string(s1, s2, s3):
    """
    Kiểm tra s3 có phải interleaving của s1 và s2 không
    """
    m, n, l = len(s1), len(s2), len(s3)
    
    if m + n != l:
        return False
    
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    # Fill first row
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    
    # Fill first column
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
    # Fill rest of table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = ((dp[i-1][j] and s1[i-1] == s3[i+j-1]) or
                       (dp[i][j-1] and s2[j-1] == s3[i+j-1]))
    
    return dp[m][n]
```