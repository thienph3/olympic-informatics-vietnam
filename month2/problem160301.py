"""
Day 16 - Problem 5: Insertion sort implementations
Thời gian: 30 phút
"""

def insertion_sort(arr):
    """
    Basic insertion sort implementation
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    Time complexity: O(n²) worst case, O(n) best case
    """
    # TODO: Implement basic insertion sort
    pass

def binary_insertion_sort(arr):
    """
    Binary insertion sort - sử dụng binary search để tìm vị trí chèn
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement binary insertion sort
    pass

def insertion_sort_with_sentinel(arr):
    """
    Insertion sort với sentinel để giảm boundary checking
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement insertion sort với sentinel
    pass

def insertion_sort_recursive(arr, n=None):
    """
    Recursive insertion sort implementation
    Input: arr - list, n - size (optional)
    Output: sorted list (in-place)
    """
    # TODO: Implement recursive insertion sort
    pass

def insertion_sort_with_gap(arr, gap=1):
    """
    Insertion sort với gap (shell sort building block)
    Input: arr - list, gap - gap size
    Output: sorted list (in-place)
    """
    # TODO: Implement insertion sort với gap
    pass

def insertion_sort_with_tracking(arr):
    """
    Insertion sort với tracking comparisons và shifts
    Input: arr - list of comparable elements
    Output: tuple (sorted_arr, comparisons, shifts)
    """
    # TODO: Implement insertion sort với performance tracking
    pass

def insertion_sort_custom(arr, key=None, reverse=False):
    """
    Insertion sort với custom key function
    Input: arr - list, key - function, reverse - boolean
    Output: sorted list (in-place)
    """
    # TODO: Implement custom insertion sort
    pass

def adaptive_insertion_sort(arr):
    """
    Adaptive insertion sort - optimize based on input characteristics
    Input: arr - list of comparable elements
    Output: tuple (sorted_arr, optimizations_used)
    """
    # TODO: Implement adaptive insertion sort
    pass

# Test cases
if __name__ == "__main__":
    # Test basic insertion_sort
    print("=== BASIC INSERTION SORT ===")
    
    test_arrays = [
        [12, 11, 13, 5, 6],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]  # Already sorted
    ]
    
    for arr in test_arrays:
        original = arr.copy()
        insertion_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted:   {arr}")
        print()
    
    # Test binary insertion sort
    print("=== BINARY INSERTION SORT ===")
    
    binary_test_arrays = [
        [4, 3, 2, 10, 12, 1, 5, 6],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for arr in binary_test_arrays:
        original = arr.copy()
        binary_insertion_sort(arr)
        print(f"Binary insertion: {original} -> {arr}")
    
    # Test insertion sort với sentinel
    print(f"\n=== INSERTION SORT WITH SENTINEL ===")
    
    sentinel_arrays = [
        [4, 2, 1, 3, 5],
        [10, 5, 2, 8, 1, 9],
        [3, 1, 4, 1, 5, 9, 2, 6]
    ]
    
    for arr in sentinel_arrays:
        original = arr.copy()
        insertion_sort_with_sentinel(arr)
        print(f"Sentinel: {original} -> {arr}")
    
    # Test recursive insertion sort
    print(f"\n=== RECURSIVE INSERTION SORT ===")
    
    recursive_test = [4, 3, 2, 1, 5]
    original = recursive_test.copy()
    insertion_sort_recursive(recursive_test)
    print(f"Recursive: {original} -> {recursive_test}")
    
    # Test insertion sort với gap
    print(f"\n=== INSERTION SORT WITH GAP ===")
    
    gap_test_arrays = [
        ([9, 8, 3, 7, 5, 6, 4, 1], 1),  # Normal insertion sort
        ([9, 8, 3, 7, 5, 6, 4, 1], 2),  # Gap of 2
        ([9, 8, 3, 7, 5, 6, 4, 1], 3),  # Gap of 3
    ]
    
    for arr, gap in gap_test_arrays:
        original = arr.copy()
        insertion_sort_with_gap(arr, gap)
        print(f"Gap {gap}: {original} -> {arr}")
    
    # Test insertion_sort_with_tracking
    print(f"\n=== INSERTION SORT WITH TRACKING ===")
    
    tracking_arrays = [
        [1, 2, 3, 4, 5],      # Best case - already sorted
        [5, 4, 3, 2, 1],      # Worst case - reverse sorted
        [2, 1, 3, 4, 5],      # Nearly sorted
        [3, 1, 4, 1, 5, 9]    # Random case
    ]
    
    for arr in tracking_arrays:
        original = arr.copy()
        sorted_arr, comparisons, shifts = insertion_sort_with_tracking(arr)
        print(f"Array: {original}")
        print(f"  Sorted: {sorted_arr}")
        print(f"  Comparisons: {comparisons}, Shifts: {shifts}")
    
    # Test custom insertion sort
    print(f"\n=== CUSTOM INSERTION SORT ===")
    
    # Sort by string length
    words = ["python", "java", "c", "javascript", "go"]
    original = words.copy()
    insertion_sort_custom(words, key=len)
    print(f"Sort by length: {original} -> {words}")
    
    # Sort tuples by second element
    pairs = [(1, 3), (2, 1), (3, 2), (4, 0)]
    original = pairs.copy()
    insertion_sort_custom(pairs, key=lambda x: x[1])
    print(f"Sort by 2nd element: {original} -> {pairs}")
    
    # Reverse sort
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    original = numbers.copy()
    insertion_sort_custom(numbers, reverse=True)
    print(f"Reverse sort: {original} -> {numbers}")
    
    # Test adaptive insertion sort
    print(f"\n=== ADAPTIVE INSERTION SORT ===")
    
    adaptive_test_cases = [
        [1, 2, 3, 4, 5],           # Already sorted
        [5, 4, 3, 2, 1],           # Reverse sorted
        [1, 3, 2, 4, 6, 5],        # Nearly sorted
        [5, 1, 4, 2, 8, 0, 2]      # Random
    ]
    
    for arr in adaptive_test_cases:
        original = arr.copy()
        sorted_arr, optimizations = adaptive_insertion_sort(arr)
        print(f"Array: {original}")
        print(f"  Sorted: {sorted_arr}")
        print(f"  Optimizations: {optimizations}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    import time
    import random
    
    # Compare different insertion sort variants
    sizes = [100, 500, 1000]
    
    for size in sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\nArray size: {size}")
        
        # Test basic insertion sort
        arr1 = test_data.copy()
        start = time.time()
        insertion_sort(arr1)
        basic_time = time.time() - start
        
        # Test binary insertion sort
        arr2 = test_data.copy()
        start = time.time()
        binary_insertion_sort(arr2)
        binary_time = time.time() - start
        
        # Test sentinel insertion sort
        arr3 = test_data.copy()
        start = time.time()
        insertion_sort_with_sentinel(arr3)
        sentinel_time = time.time() - start
        
        print(f"  Basic insertion sort: {basic_time:.4f}s")
        print(f"  Binary insertion sort: {binary_time:.4f}s")
        print(f"  Sentinel insertion sort: {sentinel_time:.4f}s")
        
        # Verify all results are same
        assert arr1 == arr2 == arr3, "Results should be identical"
    
    # Test với different data patterns
    print(f"\n=== PATTERN-SPECIFIC PERFORMANCE ===")
    
    patterns = {
        'Random': lambda n: [random.randint(1, n) for _ in range(n)],
        'Sorted': lambda n: list(range(n)),
        'Reverse': lambda n: list(range(n, 0, -1)),
        'Nearly sorted': lambda n: list(range(n)) + [random.randint(1, n) for _ in range(n//20)]
    }
    
    size = 500
    
    for pattern_name, pattern_func in patterns.items():
        test_arr = pattern_func(size)
        
        # Test basic insertion sort
        start = time.time()
        insertion_sort(test_arr.copy())
        basic_time = time.time() - start
        
        # Test adaptive insertion sort
        start = time.time()
        sorted_arr, optimizations = adaptive_insertion_sort(test_arr.copy())
        adaptive_time = time.time() - start
        
        print(f"{pattern_name} data (size {size}):")
        print(f"  Basic: {basic_time:.4f}s")
        print(f"  Adaptive: {adaptive_time:.4f}s, optimizations: {optimizations}")
        
        if basic_time > 0:
            improvement = (basic_time - adaptive_time) / basic_time * 100
            print(f"  Improvement: {improvement:.1f}%")
    
    # Analyze shifts vs comparisons
    print(f"\n=== SHIFTS VS COMPARISONS ANALYSIS ===")
    
    shift_test_cases = [
        ([1, 2, 3, 4, 5], "Already sorted"),
        ([5, 4, 3, 2, 1], "Reverse sorted"),
        ([2, 1, 3, 4, 5], "One element out of place"),
        ([1, 3, 2, 4, 5], "Nearly sorted")
    ]
    
    for arr, description in shift_test_cases:
        original = arr.copy()
        _, comparisons, shifts = insertion_sort_with_tracking(arr)
        
        print(f"{description}: {original}")
        print(f"  Comparisons: {comparisons}")
        print(f"  Shifts: {shifts}")
        print(f"  Ratio (shifts/comparisons): {shifts/comparisons if comparisons > 0 else 0:.2f}")
    
    print(f"\n=== INSERTION SORT ANALYSIS ===")
    print("Time Complexity:")
    print("  - Best case: O(n) - already sorted")
    print("  - Average case: O(n²)")
    print("  - Worst case: O(n²) - reverse sorted")
    
    print("\\nSpace Complexity:")
    print("  - O(1) - in-place sorting")
    
    print("\\nStability:")
    print("  - Stable - equal elements maintain relative order")
    
    print("\\nOptimizations:")
    print("  - Binary search for insertion position")
    print("  - Sentinel to reduce boundary checks")
    print("  - Gap-based sorting (shell sort building block)")
    print("  - Adaptive behavior for different patterns")
    
    print("\\nBest Use Cases:")
    print("  - Small datasets (< 50 elements)")
    print("  - Nearly sorted data")
    print("  - Online algorithms (sorting as data arrives)")
    print("  - When stability is required")
    print("  - As subroutine in hybrid algorithms")