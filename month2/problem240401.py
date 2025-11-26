"""
Problem 240401: Kỹ thuật debug và tối ưu code
Học cách debug hiệu quả và tối ưu hóa code cho Olympic

Debug techniques:
- Print debugging
- Assert statements  
- Test case generation
- Edge case handling

Optimization techniques:
- Time complexity reduction
- Space optimization
- Constant factor optimization
- Algorithm selection
"""

def debug_example_1():
    """Ví dụ debug: Tìm lỗi trong binary search"""
    def buggy_binary_search(arr, target):
        left, right = 0, len(arr)  # BUG: right should be len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print(f"Debug: left={left}, right={right}, mid={mid}")  # Debug print
            
            if mid >= len(arr):  # Handle the bug temporarily
                right = mid - 1
                continue
                
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    # TODO: Fix the bug and implement correct binary search
    def fixed_binary_search(arr, target):
        pass

def debug_example_2():
    """Ví dụ debug: Tìm lỗi trong merge sort"""
    def buggy_merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = buggy_merge_sort(arr[:mid])
        right = buggy_merge_sort(arr[mid:])
        
        return buggy_merge(left, right)
    
    def buggy_merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # BUG: Missing remaining elements
        return result
    
    # TODO: Fix the merge function
    def fixed_merge(left, right):
        pass

def debug_techniques():
    """Các kỹ thuật debug hiệu quả"""
    
    def print_debugging():
        """Sử dụng print để debug"""
        def debug_function(arr):
            print(f"Input: {arr}")
            
            # Debug từng bước
            for i, val in enumerate(arr):
                print(f"Step {i}: processing {val}")
                # Process val
            
            result = "processed"
            print(f"Output: {result}")
            return result
    
    def assert_debugging():
        """Sử dụng assert để kiểm tra"""
        def safe_divide(a, b):
            assert b != 0, f"Division by zero: {a}/{b}"
            assert isinstance(a, (int, float)), f"Invalid type for a: {type(a)}"
            assert isinstance(b, (int, float)), f"Invalid type for b: {type(b)}"
            
            return a / b
    
    def boundary_testing():
        """Test các trường hợp biên"""
        def test_boundaries(func):
            # Test empty input
            try:
                result = func([])
                print(f"Empty input: {result}")
            except Exception as e:
                print(f"Empty input error: {e}")
            
            # Test single element
            try:
                result = func([1])
                print(f"Single element: {result}")
            except Exception as e:
                print(f"Single element error: {e}")
            
            # Test large input
            try:
                result = func(list(range(1000)))
                print(f"Large input: success")
            except Exception as e:
                print(f"Large input error: {e}")

def optimization_example_1():
    """Ví dụ tối ưu: Từ O(n²) xuống O(n)"""
    
    def slow_two_sum(arr, target):
        """O(n²) solution"""
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == target:
                    return [i, j]
        return []
    
    def fast_two_sum(arr, target):
        """O(n) solution using hash map"""
        # TODO: Implement O(n) solution
        pass

def optimization_example_2():
    """Ví dụ tối ưu: Space optimization"""
    
    def space_inefficient_fibonacci(n):
        """O(n) space"""
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    def space_efficient_fibonacci(n):
        """O(1) space"""
        # TODO: Implement O(1) space solution
        pass

def performance_measurement():
    """Đo hiệu suất thuật toán"""
    import time
    
    def measure_time(func, *args):
        """Đo thời gian chạy function"""
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    
    def compare_algorithms():
        """So sánh hiệu suất các thuật toán"""
        import random
        
        # Generate test data
        arr = [random.randint(1, 1000) for _ in range(1000)]
        
        # Compare sorting algorithms
        arr1 = arr.copy()
        measure_time(sorted, arr1)  # Built-in sort
        
        arr2 = arr.copy()
        # measure_time(bubble_sort, arr2)  # Custom sort
        
        # Compare search algorithms
        sorted_arr = sorted(arr)
        target = random.choice(arr)
        
        measure_time(linear_search, sorted_arr, target)
        measure_time(binary_search, sorted_arr, target)

def linear_search(arr, target):
    """Linear search for comparison"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    """Binary search for comparison"""
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

def code_optimization_checklist():
    """Checklist tối ưu code cho Olympic"""
    
    checklist = [
        "1. Chọn thuật toán có độ phức tạp thấp nhất",
        "2. Sử dụng built-in functions khi có thể",
        "3. Tránh nested loops không cần thiết", 
        "4. Sử dụng appropriate data structures",
        "5. Tối ưu constant factors",
        "6. Xử lý edge cases",
        "7. Kiểm tra memory usage",
        "8. Profile code với large inputs"
    ]
    
    for item in checklist:
        print(item)

def common_optimization_patterns():
    """Các pattern tối ưu thường gặp"""
    
    def memoization_pattern():
        """Pattern: Memoization cho đệ quy"""
        memo = {}
        
        def fibonacci_memo(n):
            if n in memo:
                return memo[n]
            
            if n <= 1:
                result = n
            else:
                result = fibonacci_memo(n-1) + fibonacci_memo(n-2)
            
            memo[n] = result
            return result
    
    def two_pointers_pattern():
        """Pattern: Two pointers"""
        def two_sum_sorted(arr, target):
            left, right = 0, len(arr) - 1
            
            while left < right:
                current_sum = arr[left] + arr[right]
                if current_sum == target:
                    return [left, right]
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
            
            return []
    
    def sliding_window_pattern():
        """Pattern: Sliding window"""
        def max_sum_subarray(arr, k):
            if len(arr) < k:
                return 0
            
            # Calculate sum of first window
            window_sum = sum(arr[:k])
            max_sum = window_sum
            
            # Slide the window
            for i in range(k, len(arr)):
                window_sum = window_sum - arr[i-k] + arr[i]
                max_sum = max(max_sum, window_sum)
            
            return max_sum

# Test and debug functions
def test_debug_optimization():
    """Test các kỹ thuật debug và tối ưu"""
    
    print("=== TESTING DEBUG TECHNIQUES ===")
    
    # Test debug examples
    debug_example_1()
    debug_example_2()
    
    print("\n=== TESTING OPTIMIZATION ===")
    
    # Test optimization examples
    optimization_example_1()
    optimization_example_2()
    
    print("\n=== PERFORMANCE MEASUREMENT ===")
    performance_measurement()
    
    print("\n=== OPTIMIZATION CHECKLIST ===")
    code_optimization_checklist()

if __name__ == "__main__":
    test_debug_optimization()