"""
Problem 100402: Algorithm functions cho competitive programming
Viết functions cho thuật toán: binary search, array processing, string algorithms

Bài 1: Search và Sort Algorithms
- Binary search variants
- Sorting algorithms

Bài 2: String Algorithms và Array Processing
- Pattern matching
- Array manipulation techniques
"""

# Search Algorithms
def binary_search(arr, target):
    """Binary search cơ bản"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_leftmost(arr, target):
    """Tìm vị trí leftmost của target"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left if left < len(arr) and arr[left] == target else -1

def binary_search_rightmost(arr, target):
    """Tìm vị trí rightmost của target"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left - 1 if left > 0 and arr[left - 1] == target else -1

def ternary_search(arr, target):
    """Ternary search cho array unimodal"""
    left, right = 0, len(arr) - 1
    
    while right - left > 2:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
            
        if arr[mid1] < target:
            left = mid1 + 1
        elif arr[mid2] > target:
            right = mid2 - 1
        else:
            left, right = mid1 + 1, mid2 - 1
    
    for i in range(left, right + 1):
        if arr[i] == target:
            return i
    return -1

# Sorting Algorithms
def bubble_sort(arr):
    """Bubble sort"""
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

def selection_sort(arr):
    """Selection sort"""
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def insertion_sort(arr):
    """Insertion sort"""
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def merge_sort(arr):
    """Merge sort"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge_sorted_arrays(left, right)

def merge_sorted_arrays(arr1, arr2):
    """Merge hai array đã sort"""
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

def quick_sort(arr):
    """Quick sort"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Array Processing
def kadane_algorithm(arr):
    """Kadane's algorithm - maximum subarray sum"""
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0
    
    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end

def sliding_window_maximum(arr, k):
    """Sliding window maximum"""
    if not arr or k <= 0:
        return []
    
    result = []
    for i in range(len(arr) - k + 1):
        window_max = max(arr[i:i + k])
        result.append(window_max)
    
    return result

def two_sum(arr, target):
    """Two sum problem"""
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def three_sum(arr, target):
    """Three sum problem"""
    arr.sort()
    result = []
    
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                result.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result

def longest_increasing_subsequence(arr):
    """Longest Increasing Subsequence length"""
    if not arr:
        return 0
    
    dp = [1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# String Algorithms
def naive_string_match(text, pattern):
    """Naive string matching"""
    positions = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            positions.append(i)
    
    return positions

def kmp_search(text, pattern):
    """KMP string matching algorithm"""
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    if not pattern:
        return []
    
    lps = compute_lps(pattern)
    positions = []
    i = j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return positions

def longest_common_subsequence(text1, text2):
    """Longest Common Subsequence"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def edit_distance(str1, str2):
    """Edit distance (Levenshtein distance)"""
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # deletion
                    dp[i][j - 1],      # insertion
                    dp[i - 1][j - 1]   # substitution
                )
    
    return dp[m][n]

def is_palindrome(s):
    """Check if string is palindrome"""
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def longest_palindromic_substring(s):
    """Find longest palindromic substring"""
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    for i in range(len(s)):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    
    return s[start:start + max_len]

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Search và Sort Algorithms ===")
    
    # Test binary search
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(f"Array: {arr}")
    print(f"Binary search for {target}: {binary_search(arr, target)}")
    
    # Test with duplicates
    arr_dup = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    print(f"Array with duplicates: {arr_dup}")
    print(f"Leftmost {target}: {binary_search_leftmost(arr_dup, target)}")
    print(f"Rightmost {target}: {binary_search_rightmost(arr_dup, target)}")
    
    # Test sorting algorithms
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nUnsorted: {unsorted}")
    print(f"Bubble sort: {bubble_sort(unsorted)}")
    print(f"Selection sort: {selection_sort(unsorted)}")
    print(f"Insertion sort: {insertion_sort(unsorted)}")
    print(f"Merge sort: {merge_sort(unsorted)}")
    print(f"Quick sort: {quick_sort(unsorted)}")
    
    print("\n=== Bài 2: Array Processing ===")
    
    # Test Kadane's algorithm
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start, end = kadane_algorithm(arr)
    print(f"Array: {arr}")
    print(f"Max subarray sum: {max_sum} from index {start} to {end}")
    print(f"Subarray: {arr[start:end+1]}")
    
    # Test sliding window
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sliding_window_maximum(arr, k)
    print(f"\nSliding window max (k={k}): {result}")
    
    # Test two sum and three sum
    arr = [2, 7, 11, 15]
    target = 9
    print(f"Two sum in {arr} for target {target}: {two_sum(arr, target)}")
    
    arr = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(f"Three sum in {arr} for target {target}: {three_sum(arr, target)}")
    
    # Test LIS
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"LIS length in {arr}: {longest_increasing_subsequence(arr)}")
    
    print("\n=== String Algorithms ===")
    
    # Test string matching
    text = "ABABDABACDABABCABCABCABCABC"
    pattern = "ABABCABCABCABC"
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Naive search: {naive_string_match(text, pattern)}")
    print(f"KMP search: {kmp_search(text, pattern)}")
    
    # Test string algorithms
    str1 = "ABCDGH"
    str2 = "AEDFHR"
    print(f"\nLCS of '{str1}' and '{str2}': {longest_common_subsequence(str1, str2)}")
    print(f"Edit distance: {edit_distance(str1, str2)}")
    
    # Test palindrome
    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
    for s in test_strings:
        print(f"'{s}' is palindrome: {is_palindrome(s)}")
    
    s = "babad"
    print(f"Longest palindromic substring in '{s}': '{longest_palindromic_substring(s)}'")

    print("\n=== Bài tập thực hành ===")
    print("1. Implement binary search on answer technique")
    print("2. Solve maximum rectangle in histogram")
    print("3. Implement Z-algorithm for string matching")
    print("4. Solve longest common substring problem")