"""
Day 15 - Problem 1: Ternary search implementations
Thời gian: 30 phút
"""

def ternary_search_array(arr, target):
    """
    Ternary search trong sorted array
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target, -1 nếu không tìm thấy
    Time complexity: O(log₃ n)
    """
    # TODO: Implement ternary search cho array
    pass

def ternary_search_recursive(arr, target, left=0, right=None):
    """
    Ternary search đệ quy
    Input: arr - sorted array, target, left/right - bounds
    Output: index của target, -1 nếu không tìm thấy
    """
    # TODO: Implement recursive ternary search
    pass

def ternary_search_maximum(func, left, right, epsilon=1e-9):
    """
    Tìm maximum của unimodal function bằng ternary search
    Input: func - unimodal function, left/right - bounds, epsilon - precision
    Output: x tại đó func(x) maximum
    """
    # TODO: Implement ternary search for maximum
    pass

def ternary_search_minimum(func, left, right, epsilon=1e-9):
    """
    Tìm minimum của unimodal function bằng ternary search
    Input: func - unimodal function, left/right - bounds, epsilon - precision
    Output: x tại đó func(x) minimum
    """
    # TODO: Implement ternary search for minimum
    pass

def find_peak_ternary(arr):
    """
    Tìm peak element bằng ternary search
    Input: arr - array có peak element
    Output: index của peak element
    """
    # TODO: Implement peak finding using ternary search
    pass

def ternary_search_first_occurrence(arr, target):
    """
    Tìm first occurrence bằng ternary search
    Input: arr - sorted array có duplicates, target - giá trị cần tìm
    Output: index đầu tiên của target, -1 nếu không có
    """
    # TODO: Implement first occurrence với ternary search
    pass

def compare_ternary_vs_binary(arr, target):
    """
    So sánh hiệu suất ternary vs binary search
    Input: arr - sorted array, target - giá trị cần tìm
    Output: dictionary với results và timing
    """
    import time
    
    # TODO: Implement comparison
    # Binary search
    def binary_search(arr, target):
        # TODO: Implement binary search
        pass
    
    # Measure binary search
    start = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start
    
    # Measure ternary search
    start = time.time()
    ternary_result = ternary_search_array(arr, target)
    ternary_time = time.time() - start
    
    return {
        'binary': {'result': binary_result, 'time': binary_time},
        'ternary': {'result': ternary_result, 'time': ternary_time}
    }

# Test cases
if __name__ == "__main__":
    # Test ternary_search_array
    print("=== TERNARY SEARCH ARRAY ===")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    targets = [1, 5, 10, 11, 0]
    
    for target in targets:
        result = ternary_search_array(arr, target)
        print(f"Tìm {target} trong {arr}: {result}")
    
    # Test ternary_search_recursive
    print(f"\n=== TERNARY SEARCH RECURSIVE ===")
    for target in [3, 7, 12]:
        result = ternary_search_recursive(arr, target)
        print(f"Recursive tìm {target}: {result}")
    
    # Test ternary_search_maximum
    print(f"\n=== TERNARY SEARCH MAXIMUM ===")
    
    # Test với parabola: f(x) = -(x-3)² + 10
    def parabola_max(x):
        return -(x - 3) ** 2 + 10
    
    max_x = ternary_search_maximum(parabola_max, 0, 6)
    max_value = parabola_max(max_x)
    print(f"Maximum của parabola tại x = {max_x:.6f}, f(x) = {max_value:.6f}")
    
    # Test với sin function
    import math
    def sin_func(x):
        return math.sin(x)
    
    max_x = ternary_search_maximum(sin_func, 0, math.pi)
    max_value = sin_func(max_x)
    print(f"Maximum của sin(x) tại x = {max_x:.6f}, sin(x) = {max_value:.6f}")
    
    # Test ternary_search_minimum
    print(f"\n=== TERNARY SEARCH MINIMUM ===")
    
    # Test với parabola: f(x) = (x-2)² + 1
    def parabola_min(x):
        return (x - 2) ** 2 + 1
    
    min_x = ternary_search_minimum(parabola_min, 0, 4)
    min_value = parabola_min(min_x)
    print(f"Minimum của parabola tại x = {min_x:.6f}, f(x) = {min_value:.6f}")
    
    # Test find_peak_ternary
    print(f"\n=== PEAK FINDING ===")
    
    peak_arrays = [
        [1, 3, 8, 12, 4, 2],
        [0, 1, 0],
        [0, 2, 1, 0],
        [1, 2, 3, 1]
    ]
    
    for arr in peak_arrays:
        peak_idx = find_peak_ternary(arr)
        if peak_idx != -1:
            print(f"Peak trong {arr}: index {peak_idx}, value {arr[peak_idx]}")
        else:
            print(f"No peak found trong {arr}")
    
    # Test ternary_search_first_occurrence
    print(f"\n=== FIRST OCCURRENCE ===")
    
    arr_with_dups = [1, 2, 2, 2, 3, 4, 4, 5]
    targets = [2, 4, 1, 6]
    
    for target in targets:
        first_idx = ternary_search_first_occurrence(arr_with_dups, target)
        print(f"First occurrence của {target} trong {arr_with_dups}: {first_idx}")
    
    # Test performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    large_arr = list(range(10000))
    target = 7500
    
    comparison = compare_ternary_vs_binary(large_arr, target)
    
    print(f"Binary search: result={comparison['binary']['result']}, time={comparison['binary']['time']:.8f}s")
    print(f"Ternary search: result={comparison['ternary']['result']}, time={comparison['ternary']['time']:.8f}s")
    
    if comparison['binary']['time'] > 0:
        speedup = comparison['binary']['time'] / comparison['ternary']['time']
        print(f"Speedup ratio: {speedup:.2f}x")
    
    # Edge cases
    print(f"\n=== EDGE CASES ===")
    
    edge_cases = [
        ([], 5, "Empty array"),
        ([1], 1, "Single element - found"),
        ([1], 2, "Single element - not found"),
        ([1, 2], 1, "Two elements - first"),
        ([1, 2], 2, "Two elements - second")
    ]
    
    for arr, target, description in edge_cases:
        result = ternary_search_array(arr, target)
        print(f"{description}: {result}")
    
    print(f"\n=== COMPLEXITY ANALYSIS ===")
    print("Ternary Search:")
    print("  - Time: O(log₃ n) ≈ 0.63 * O(log₂ n)")
    print("  - Space: O(1) iterative, O(log n) recursive")
    print("  - Comparisons per iteration: 2 (vs 1 for binary)")
    print("  - Total comparisons: ~1.26 * log₂(n)")
    
    print("\\nWhen to use Ternary Search:")
    print("  - Unimodal function optimization")
    print("  - When function evaluation is expensive")
    print("  - Alternative to binary search (theoretical interest)")
    print("  - Peak finding problems")