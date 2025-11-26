"""
Day 14 - Problem 5: Search variants implementation
Thời gian: 30 phút
"""

import math

def interpolation_search(arr, target):
    """
    Interpolation search - tốt hơn binary search cho uniformly distributed data
    Input: arr - sorted array với uniform distribution, target - giá trị cần tìm
    Output: index của target hoặc -1
    Time complexity: O(log log n) average, O(n) worst case
    """
    # TODO: Implement interpolation search
    pass

def exponential_search(arr, target):
    """
    Exponential search - tốt cho unbounded/infinite arrays
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target hoặc -1
    Time complexity: O(log n)
    """
    # TODO: Implement exponential search
    pass

def fibonacci_search(arr, target):
    """
    Fibonacci search - không cần division, tốt cho systems không có division
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target hoặc -1
    Time complexity: O(log n)
    """
    # TODO: Implement fibonacci search
    pass

def jump_search(arr, target):
    """
    Jump search - nhảy theo bước sqrt(n)
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target hoặc -1
    Time complexity: O(√n)
    """
    # TODO: Implement jump search
    pass

def ternary_search_iterative(arr, target):
    """
    Ternary search iterative - chia array thành 3 phần
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target hoặc -1
    Time complexity: O(log₃ n)
    """
    # TODO: Implement iterative ternary search
    pass

def ternary_search_recursive(arr, target, left=0, right=None):
    """
    Ternary search recursive
    Input: arr - sorted array, target - giá trị cần tìm, left/right - bounds
    Output: index của target hoặc -1
    """
    # TODO: Implement recursive ternary search
    pass

def compare_search_algorithms(arr, target):
    """
    So sánh hiệu suất các thuật toán search
    Input: arr - sorted array, target - giá trị cần tìm
    Output: dictionary với results và timing
    """
    import time
    
    algorithms = {
        'linear': lambda: linear_search(arr, target),
        'binary': lambda: binary_search(arr, target),
        'interpolation': lambda: interpolation_search(arr, target),
        'exponential': lambda: exponential_search(arr, target),
        'fibonacci': lambda: fibonacci_search(arr, target),
        'jump': lambda: jump_search(arr, target),
        'ternary_iter': lambda: ternary_search_iterative(arr, target),
        'ternary_rec': lambda: ternary_search_recursive(arr, target)
    }
    
    results = {}
    
    for name, func in algorithms.items():
        try:
            start = time.time()
            result = func()
            end = time.time()
            
            results[name] = {
                'result': result,
                'time': end - start,
                'found': result != -1
            }
        except Exception as e:
            results[name] = {
                'result': -1,
                'time': float('inf'),
                'found': False,
                'error': str(e)
            }
    
    return results

# Helper functions for comparison
def linear_search(arr, target):
    """Linear search for comparison"""
    for i in range(len(arr)):
        if arr[i] == target:
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

# Test cases
if __name__ == "__main__":
    # Test với uniform distributed data
    print("=== UNIFORM DISTRIBUTED DATA ===")
    uniform_arr = list(range(0, 1000, 10))  # [0, 10, 20, ..., 990]
    target = 500
    
    print(f"Array size: {len(uniform_arr)}")
    print(f"Target: {target}")
    
    results = compare_search_algorithms(uniform_arr, target)
    
    print(f"{'Algorithm':<15} {'Result':<8} {'Time(s)':<12} {'Found':<8}")
    print("-" * 50)
    for name, data in results.items():
        if 'error' not in data:
            print(f"{name:<15} {data['result']:<8} {data['time']:<12.8f} {data['found']:<8}")
        else:
            print(f"{name:<15} ERROR: {data['error']}")
    
    # Test với non-uniform data
    print(f"\n=== NON-UNIFORM DATA ===")
    non_uniform_arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    target = 64
    
    print(f"Array: {non_uniform_arr}")
    print(f"Target: {target}")
    
    results = compare_search_algorithms(non_uniform_arr, target)
    
    print(f"{'Algorithm':<15} {'Result':<8} {'Time(s)':<12} {'Found':<8}")
    print("-" * 50)
    for name, data in results.items():
        if 'error' not in data:
            print(f"{name:<15} {data['result']:<8} {data['time']:<12.8f} {data['found']:<8}")
        else:
            print(f"{name:<15} ERROR: {data['error']}")
    
    # Test edge cases
    print(f"\n=== EDGE CASES ===")
    
    edge_cases = [
        ([], 5, "Empty array"),
        ([1], 1, "Single element - found"),
        ([1], 2, "Single element - not found"),
        ([1, 2], 1, "Two elements - first"),
        ([1, 2], 2, "Two elements - second"),
        ([1, 2], 3, "Two elements - not found")
    ]
    
    for arr, target, description in edge_cases:
        print(f"\n{description}: arr={arr}, target={target}")
        
        # Test a few key algorithms
        algorithms_to_test = ['binary', 'interpolation', 'exponential', 'fibonacci']
        
        for alg_name in algorithms_to_test:
            try:
                if alg_name == 'binary':
                    result = binary_search(arr, target)
                elif alg_name == 'interpolation':
                    result = interpolation_search(arr, target)
                elif alg_name == 'exponential':
                    result = exponential_search(arr, target)
                elif alg_name == 'fibonacci':
                    result = fibonacci_search(arr, target)
                
                print(f"  {alg_name}: {result}")
            except Exception as e:
                print(f"  {alg_name}: ERROR - {e}")
    
    # Performance analysis
    print(f"\n=== PERFORMANCE ANALYSIS ===")
    
    sizes = [100, 1000, 10000]
    
    for size in sizes:
        print(f"\nArray size: {size}")
        test_arr = list(range(size))
        target = size // 2
        
        # Test key algorithms
        key_algorithms = {
            'Binary': lambda: binary_search(test_arr, target),
            'Interpolation': lambda: interpolation_search(test_arr, target),
            'Exponential': lambda: exponential_search(test_arr, target),
            'Jump': lambda: jump_search(test_arr, target)
        }
        
        for name, func in key_algorithms.items():
            try:
                import time
                start = time.time()
                for _ in range(1000):  # Multiple runs for better timing
                    result = func()
                end = time.time()
                
                avg_time = (end - start) / 1000
                print(f"  {name}: {avg_time:.8f}s per search")
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    print(f"\n=== ALGORITHM CHARACTERISTICS ===")
    print("Binary Search:")
    print("  - Always O(log n)")
    print("  - Works on any sorted array")
    print("  - Most reliable choice")
    
    print("\\nInterpolation Search:")
    print("  - O(log log n) for uniform data")
    print("  - O(n) worst case for skewed data")
    print("  - Best for uniformly distributed data")
    
    print("\\nExponential Search:")
    print("  - O(log n)")
    print("  - Good for unbounded arrays")
    print("  - Finds range then binary search")
    
    print("\\nFibonacci Search:")
    print("  - O(log n)")
    print("  - No division operations")
    print("  - Good for systems without division")
    
    print("\\nJump Search:")
    print("  - O(√n)")
    print("  - Simple implementation")
    print("  - Better than linear, worse than binary")
    
    print("\\nTernary Search:")
    print("  - O(log₃ n) ≈ 0.63 * O(log₂ n)")
    print("  - More comparisons per iteration")
    print("  - Theoretical improvement over binary")