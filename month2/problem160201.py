"""
Day 16 - Problem 3: Selection sort implementations
Thời gian: 25 phút
"""

def selection_sort(arr):
    """
    Basic selection sort implementation
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    Time complexity: O(n²)
    """
    # TODO: Implement basic selection sort
    pass

def selection_sort_stable(arr):
    """
    Stable version của selection sort
    Input: arr - list of comparable elements
    Output: sorted list (in-place, stable)
    """
    # TODO: Implement stable selection sort
    pass

def double_selection_sort(arr):
    """
    Double selection sort - tìm min và max cùng lúc
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement double selection sort
    pass

def selection_sort_recursive(arr, start=0):
    """
    Recursive selection sort implementation
    Input: arr - list, start - starting index
    Output: sorted list (in-place)
    """
    # TODO: Implement recursive selection sort
    pass

def selection_sort_k_smallest(arr, k):
    """
    Chỉ sort k phần tử nhỏ nhất
    Input: arr - list, k - number of smallest elements to sort
    Output: partially sorted list
    """
    # TODO: Implement partial selection sort
    pass

def selection_sort_with_tracking(arr):
    """
    Selection sort với tracking comparisons và swaps
    Input: arr - list of comparable elements
    Output: tuple (sorted_arr, comparisons, swaps)
    """
    # TODO: Implement selection sort với performance tracking
    pass

def selection_sort_custom(arr, key=None, reverse=False):
    """
    Selection sort với custom key function
    Input: arr - list, key - function, reverse - boolean
    Output: sorted list (in-place)
    """
    # TODO: Implement custom selection sort
    pass

# Test cases
if __name__ == "__main__":
    # Test basic selection_sort
    print("=== BASIC SELECTION SORT ===")
    
    test_arrays = [
        [64, 25, 12, 22, 11],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [5, 4, 3, 2, 1]
    ]
    
    for arr in test_arrays:
        original = arr.copy()
        selection_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted:   {arr}")
        print()
    
    # Test stable selection sort
    print("=== STABLE SELECTION SORT ===")
    
    # Test với objects có same key để verify stability
    class Student:
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade
        
        def __lt__(self, other):
            return self.grade < other.grade
        
        def __repr__(self):
            return f"{self.name}({self.grade})"
    
    students = [
        Student("Alice", 85),
        Student("Bob", 90),
        Student("Charlie", 85),  # Same grade as Alice
        Student("David", 90)     # Same grade as Bob
    ]
    
    print("Original order:", students)
    
    # Test unstable selection sort
    students_unstable = students.copy()
    selection_sort(students_unstable)
    print("Unstable result:", students_unstable)
    
    # Test stable selection sort
    students_stable = students.copy()
    selection_sort_stable(students_stable)
    print("Stable result:", students_stable)
    
    # Test double_selection_sort
    print(f"\n=== DOUBLE SELECTION SORT ===")
    
    double_test_arrays = [
        [3, 7, 1, 9, 4, 6, 2, 8, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 1, 1, 1]
    ]
    
    for arr in double_test_arrays:
        original = arr.copy()
        double_selection_sort(arr)
        print(f"Double selection: {original} -> {arr}")
    
    # Test recursive selection sort
    print(f"\n=== RECURSIVE SELECTION SORT ===")
    
    recursive_test = [4, 3, 2, 1, 5]
    original = recursive_test.copy()
    selection_sort_recursive(recursive_test)
    print(f"Recursive: {original} -> {recursive_test}")
    
    # Test k smallest selection sort
    print(f"\n=== K SMALLEST SELECTION SORT ===")
    
    k_test_cases = [
        ([7, 10, 4, 3, 20, 15], 3),  # Sort first 3 smallest
        ([1, 2, 3, 4, 5], 2),        # Already sorted
        ([5, 4, 3, 2, 1], 4),        # Reverse sorted
    ]
    
    for arr, k in k_test_cases:
        original = arr.copy()
        selection_sort_k_smallest(arr, k)
        print(f"Array: {original}, k={k}")
        print(f"  Result: {arr} (first {k} elements sorted)")
    
    # Test selection_sort_with_tracking
    print(f"\n=== SELECTION SORT WITH TRACKING ===")
    
    tracking_arrays = [
        [3, 2, 1],           # Worst case
        [1, 2, 3],           # Best case
        [2, 1, 3],           # Mixed case
        [3, 1, 4, 1, 5, 9]   # Random case
    ]
    
    for arr in tracking_arrays:
        original = arr.copy()
        sorted_arr, comparisons, swaps = selection_sort_with_tracking(arr)
        print(f"Array: {original}")
        print(f"  Sorted: {sorted_arr}")
        print(f"  Comparisons: {comparisons}, Swaps: {swaps}")
    
    # Test custom selection sort
    print(f"\n=== CUSTOM SELECTION SORT ===")
    
    # Sort by string length
    words = ["python", "java", "c", "javascript", "go"]
    original = words.copy()
    selection_sort_custom(words, key=len)
    print(f"Sort by length: {original} -> {words}")
    
    # Sort tuples by second element
    pairs = [(1, 3), (2, 1), (3, 2), (4, 0)]
    original = pairs.copy()
    selection_sort_custom(pairs, key=lambda x: x[1])
    print(f"Sort by 2nd element: {original} -> {pairs}")
    
    # Reverse sort
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    original = numbers.copy()
    selection_sort_custom(numbers, reverse=True)
    print(f"Reverse sort: {original} -> {numbers}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    import time
    import random
    
    # Compare different selection sort variants
    sizes = [100, 500, 1000]
    
    for size in sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\nArray size: {size}")
        
        # Test basic selection sort
        arr1 = test_data.copy()
        start = time.time()
        selection_sort(arr1)
        basic_time = time.time() - start
        
        # Test double selection sort
        arr2 = test_data.copy()
        start = time.time()
        double_selection_sort(arr2)
        double_time = time.time() - start
        
        # Test stable selection sort
        arr3 = test_data.copy()
        start = time.time()
        selection_sort_stable(arr3)
        stable_time = time.time() - start
        
        print(f"  Basic selection sort: {basic_time:.4f}s")
        print(f"  Double selection sort: {double_time:.4f}s")
        print(f"  Stable selection sort: {stable_time:.4f}s")
        
        # Verify all results are same
        assert arr1 == arr2 == arr3, "Results should be identical"
    
    # Analyze swap counts
    print(f"\n=== SWAP ANALYSIS ===")
    
    swap_test_arrays = [
        [1, 2, 3, 4, 5],      # Already sorted
        [5, 4, 3, 2, 1],      # Reverse sorted
        [3, 1, 4, 1, 5, 9, 2, 6]  # Random
    ]
    
    for arr in swap_test_arrays:
        original = arr.copy()
        _, comparisons, swaps = selection_sort_with_tracking(arr)
        print(f"Array: {original}")
        print(f"  Comparisons: {comparisons}")
        print(f"  Swaps: {swaps}")
        print(f"  Theoretical max swaps: {len(original) - 1}")
    
    print(f"\n=== SELECTION SORT ANALYSIS ===")
    print("Time Complexity:")
    print("  - Best case: O(n²) - always same number of comparisons")
    print("  - Average case: O(n²)")
    print("  - Worst case: O(n²)")
    
    print("\\nSpace Complexity:")
    print("  - O(1) - in-place sorting")
    
    print("\\nStability:")
    print("  - Unstable by default")
    print("  - Can be made stable với shifting instead of swapping")
    
    print("\\nSwap Count:")
    print("  - Maximum: n-1 swaps")
    print("  - Minimum: 0 swaps (already sorted)")
    print("  - Always ≤ n-1 swaps (good for expensive swap operations)")
    
    print("\\nOptimizations:")
    print("  - Double selection (find min and max together)")
    print("  - Partial sorting (k smallest elements)")
    print("  - Stable version (shifting instead of swapping)")
    
    print("\\nBest Use Cases:")
    print("  - When swap operations are expensive")
    print("  - Memory-constrained environments")
    print("  - When you need exactly n-1 swaps")
    print("  - Small datasets where simplicity matters")