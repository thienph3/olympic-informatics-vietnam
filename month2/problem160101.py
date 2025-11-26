"""
Day 16 - Problem 1: Bubble sort implementations
Thời gian: 30 phút
"""

def bubble_sort(arr):
    """
    Basic bubble sort implementation
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    Time complexity: O(n²)
    """
    # TODO: Implement basic bubble sort
    pass

def bubble_sort_optimized(arr):
    """
    Optimized bubble sort với early termination
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement optimized bubble sort với flag
    pass

def cocktail_shaker_sort(arr):
    """
    Cocktail Shaker Sort - bidirectional bubble sort
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement cocktail shaker sort
    pass

def bubble_sort_custom(arr, key=None, reverse=False):
    """
    Bubble sort với custom key function và reverse order
    Input: arr - list, key - function, reverse - boolean
    Output: sorted list (in-place)
    """
    # TODO: Implement custom bubble sort
    pass

def bubble_sort_with_tracking(arr):
    """
    Bubble sort với tracking comparisons và swaps
    Input: arr - list of comparable elements
    Output: tuple (sorted_arr, comparisons, swaps)
    """
    # TODO: Implement bubble sort với performance tracking
    pass

def bubble_sort_recursive(arr, n=None):
    """
    Recursive bubble sort implementation
    Input: arr - list, n - size (optional)
    Output: sorted list (in-place)
    """
    # TODO: Implement recursive bubble sort
    pass

def bubble_sort_range(arr, start, end):
    """
    Bubble sort chỉ trong range [start, end]
    Input: arr - list, start/end - indices
    Output: partially sorted list
    """
    # TODO: Implement range-specific bubble sort
    pass

# Test cases
if __name__ == "__main__":
    # Test basic bubble_sort
    print("=== BASIC BUBBLE SORT ===")
    
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [5, 4, 3, 2, 1]
    ]
    
    for arr in test_arrays:
        original = arr.copy()
        bubble_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted:   {arr}")
        print()
    
    # Test optimized bubble sort
    print("=== OPTIMIZED BUBBLE SORT ===")
    
    # Test với already sorted array
    sorted_arr = [1, 2, 3, 4, 5]
    original = sorted_arr.copy()
    bubble_sort_optimized(sorted_arr)
    print(f"Already sorted: {original} -> {sorted_arr}")
    
    # Test với reverse sorted
    reverse_arr = [5, 4, 3, 2, 1]
    original = reverse_arr.copy()
    bubble_sort_optimized(reverse_arr)
    print(f"Reverse sorted: {original} -> {reverse_arr}")
    
    # Test cocktail_shaker_sort
    print(f"\n=== COCKTAIL SHAKER SORT ===")
    
    test_arr = [5, 1, 4, 2, 8, 0, 2]
    original = test_arr.copy()
    cocktail_shaker_sort(test_arr)
    print(f"Cocktail shaker: {original} -> {test_arr}")
    
    # Test bubble_sort_custom
    print(f"\n=== CUSTOM BUBBLE SORT ===")
    
    # Sort by string length
    words = ["python", "java", "c", "javascript", "go"]
    original = words.copy()
    bubble_sort_custom(words, key=len)
    print(f"Sort by length: {original} -> {words}")
    
    # Sort tuples by second element
    pairs = [(1, 3), (2, 1), (3, 2), (4, 0)]
    original = pairs.copy()
    bubble_sort_custom(pairs, key=lambda x: x[1])
    print(f"Sort by 2nd element: {original} -> {pairs}")
    
    # Reverse sort
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    original = numbers.copy()
    bubble_sort_custom(numbers, reverse=True)
    print(f"Reverse sort: {original} -> {numbers}")
    
    # Test bubble_sort_with_tracking
    print(f"\n=== BUBBLE SORT WITH TRACKING ===")
    
    tracking_arrays = [
        [3, 2, 1],           # Worst case
        [1, 2, 3],           # Best case
        [2, 1, 3],           # One swap needed
        [3, 1, 4, 1, 5, 9]   # Random case
    ]
    
    for arr in tracking_arrays:
        original = arr.copy()
        sorted_arr, comparisons, swaps = bubble_sort_with_tracking(arr)
        print(f"Array: {original}")
        print(f"  Sorted: {sorted_arr}")
        print(f"  Comparisons: {comparisons}, Swaps: {swaps}")
    
    # Test recursive bubble sort
    print(f"\n=== RECURSIVE BUBBLE SORT ===")
    
    recursive_test = [4, 3, 2, 1, 5]
    original = recursive_test.copy()
    bubble_sort_recursive(recursive_test)
    print(f"Recursive: {original} -> {recursive_test}")
    
    # Test range bubble sort
    print(f"\n=== RANGE BUBBLE SORT ===")
    
    range_arr = [9, 5, 2, 7, 1, 8, 3, 6, 4]
    original = range_arr.copy()
    
    # Sort only middle portion [2:7]
    bubble_sort_range(range_arr, 2, 6)
    print(f"Original: {original}")
    print(f"Range [2:7] sorted: {range_arr}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    import time
    import random
    
    # Generate test data
    sizes = [100, 500, 1000]
    
    for size in sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\nArray size: {size}")
        
        # Test basic bubble sort
        arr1 = test_data.copy()
        start = time.time()
        bubble_sort(arr1)
        basic_time = time.time() - start
        
        # Test optimized bubble sort
        arr2 = test_data.copy()
        start = time.time()
        bubble_sort_optimized(arr2)
        optimized_time = time.time() - start
        
        # Test cocktail shaker
        arr3 = test_data.copy()
        start = time.time()
        cocktail_shaker_sort(arr3)
        cocktail_time = time.time() - start
        
        print(f"  Basic bubble sort: {basic_time:.4f}s")
        print(f"  Optimized bubble sort: {optimized_time:.4f}s")
        print(f"  Cocktail shaker: {cocktail_time:.4f}s")
        
        # Verify all results are same
        assert arr1 == arr2 == arr3, "Results should be identical"
    
    print(f"\n=== BUBBLE SORT ANALYSIS ===")
    print("Time Complexity:")
    print("  - Best case: O(n) - already sorted với optimization")
    print("  - Average case: O(n²)")
    print("  - Worst case: O(n²) - reverse sorted")
    
    print("\\nSpace Complexity:")
    print("  - O(1) - in-place sorting")
    
    print("\\nStability:")
    print("  - Stable - equal elements maintain relative order")
    
    print("\\nOptimizations:")
    print("  - Early termination flag")
    print("  - Cocktail shaker (bidirectional)")
    print("  - Range-specific sorting")
    
    print("\\nBest Use Cases:")
    print("  - Educational purposes")
    print("  - Small datasets")
    print("  - Nearly sorted data (với optimization)")
    print("  - When simplicity is preferred over efficiency")