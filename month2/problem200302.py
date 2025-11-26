"""
Problem 200302: Algorithm Comparison
So sánh độ phức tạp của các thuật toán giải cùng một bài toán

Topics: Algorithm comparison, trade-offs, optimization strategies
"""

def compare_sorting_algorithms():
    """
    So sánh complexity của các thuật toán sắp xếp
    """
    def bubble_sort(arr):
        # Time: O(n²), Space: O(1)
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def merge_sort(arr):
        # Time: O(n log n), Space: O(n)
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def counting_sort(arr):
        # Time: O(n + k), Space: O(k) where k is range
        if not arr:
            return arr
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1
        
        count = [0] * range_val
        for num in arr:
            count[num - min_val] += 1
        
        result = []
        for i in range(range_val):
            result.extend([i + min_val] * count[i])
        return result
    
    # TODO: So sánh và phân tích khi nào dùng thuật toán nào
    pass

def compare_search_algorithms():
    """
    So sánh complexity của các thuật toán tìm kiếm
    """
    def linear_search(arr, target):
        # Time: O(n), Space: O(1)
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    def binary_search(arr, target):
        # Time: O(log n), Space: O(1)
        # Requires sorted array
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
    
    def hash_search(arr, target):
        # Time: O(1) average, Space: O(n)
        # Preprocessing: O(n)
        hash_map = {val: i for i, val in enumerate(arr)}
        return hash_map.get(target, -1)
    
    # TODO: Phân tích trade-offs giữa preprocessing và search time
    pass

def compare_fibonacci_implementations():
    """
    So sánh các cách implement Fibonacci
    """
    def fibonacci_recursive(n):
        # Time: O(2ⁿ), Space: O(n)
        if n <= 1:
            return n
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
    def fibonacci_memoized(n, memo=None):
        # Time: O(n), Space: O(n)
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
        return memo[n]
    
    def fibonacci_iterative(n):
        # Time: O(n), Space: O(1)
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def fibonacci_matrix(n):
        # Time: O(log n), Space: O(1)
        # Using matrix exponentiation
        if n <= 1:
            return n
        
        def matrix_multiply(A, B):
            return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                    [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]
        
        def matrix_power(matrix, power):
            if power == 1:
                return matrix
            if power % 2 == 0:
                half = matrix_power(matrix, power // 2)
                return matrix_multiply(half, half)
            else:
                return matrix_multiply(matrix, matrix_power(matrix, power - 1))
        
        base_matrix = [[1, 1], [1, 0]]
        result_matrix = matrix_power(base_matrix, n)
        return result_matrix[0][1]
    
    # TODO: So sánh 4 approaches và trade-offs
    pass

def compare_duplicate_finding():
    """
    So sánh các cách tìm duplicate trong array
    """
    def find_duplicate_nested_loop(arr):
        # Time: O(n²), Space: O(1)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    return arr[i]
        return None
    
    def find_duplicate_sorting(arr):
        # Time: O(n log n), Space: O(1) if in-place sort
        arr_copy = sorted(arr)
        for i in range(len(arr_copy) - 1):
            if arr_copy[i] == arr_copy[i + 1]:
                return arr_copy[i]
        return None
    
    def find_duplicate_hash_set(arr):
        # Time: O(n), Space: O(n)
        seen = set()
        for num in arr:
            if num in seen:
                return num
            seen.add(num)
        return None
    
    def find_duplicate_floyd_cycle(arr):
        # Time: O(n), Space: O(1)
        # Only works if array contains numbers 1 to n-1 with one duplicate
        slow = fast = arr[0]
        
        # Find intersection point in cycle
        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break
        
        # Find start of cycle
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        
        return slow
    
    # TODO: Phân tích từng approach và constraints
    pass

def compare_string_matching():
    """
    So sánh các thuật toán string matching
    """
    def naive_string_match(text, pattern):
        # Time: O(n * m), Space: O(1)
        n, m = len(text), len(pattern)
        for i in range(n - m + 1):
            if text[i:i + m] == pattern:
                return i
        return -1
    
    def kmp_string_match(text, pattern):
        # Time: O(n + m), Space: O(m)
        def compute_lps(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0
            i = 1
            
            while i < m:
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
        
        n, m = len(text), len(pattern)
        if m == 0:
            return 0
        
        lps = compute_lps(pattern)
        i = j = 0
        
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == m:
                return i - j
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1
    
    def python_builtin_find(text, pattern):
        # Time: O(n * m) worst case, but optimized in practice
        return text.find(pattern)
    
    # TODO: So sánh performance trong different scenarios
    pass

def analyze_space_time_tradeoffs():
    """
    Phân tích trade-offs giữa space và time complexity
    """
    examples = {
        'Caching/Memoization': {
            'No Cache': 'Time: High, Space: Low',
            'With Cache': 'Time: Low, Space: High'
        },
        'Preprocessing': {
            'No Preprocessing': 'Setup: O(1), Query: O(n)',
            'With Preprocessing': 'Setup: O(n), Query: O(1)'
        },
        'Data Structure Choice': {
            'Array': 'Access: O(1), Search: O(n), Space: O(n)',
            'Hash Table': 'Access: O(1), Search: O(1), Space: O(n) + overhead'
        }
    }
    
    # TODO: Provide concrete examples và analysis
    pass

# Test cases
def test_algorithm_comparison():
    print("Algorithm Comparison Analysis")
    print("=" * 40)
    
    # Compare sorting algorithms
    print("1. Sorting Algorithms Comparison:")
    compare_sorting_algorithms()
    
    # Compare search algorithms
    print("\n2. Search Algorithms Comparison:")
    compare_search_algorithms()
    
    # Compare Fibonacci implementations
    print("\n3. Fibonacci Implementations:")
    compare_fibonacci_implementations()
    
    # Compare duplicate finding
    print("\n4. Duplicate Finding Methods:")
    compare_duplicate_finding()
    
    # Compare string matching
    print("\n5. String Matching Algorithms:")
    compare_string_matching()
    
    # Analyze trade-offs
    print("\n6. Space-Time Trade-offs:")
    analyze_space_time_tradeoffs()

if __name__ == "__main__":
    test_algorithm_comparison()