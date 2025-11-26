"""
Day 16 - Problem 2: Bubble sort applications
Thời gian: 30 phút
"""

def sort_by_frequency(arr):
    """
    Sắp xếp array theo frequency của elements (tăng dần)
    Input: arr - list of elements
    Output: sorted list by frequency
    """
    # TODO: Implement sorting by frequency using bubble sort
    pass

def sort_students_by_grades(students):
    """
    Sắp xếp students theo grades, nếu bằng nhau thì theo tên
    Input: students - list of (name, grade) tuples
    Output: sorted list
    """
    # TODO: Implement multi-key sorting using bubble sort
    pass

def bubble_sort_with_custom_comparison(arr, compare_func):
    """
    Bubble sort với custom comparison function
    Input: arr - list, compare_func - function(a, b) returns True if a > b
    Output: sorted list
    """
    # TODO: Implement bubble sort với custom comparison
    pass

def find_kth_largest_bubble(arr, k):
    """
    Tìm kth largest element bằng partial bubble sort
    Input: arr - list, k - position (1-indexed)
    Output: kth largest element
    """
    # TODO: Implement partial bubble sort để tìm kth largest
    pass

def sort_colors_bubble(colors):
    """
    Sort colors (0=red, 1=white, 2=blue) - Dutch flag problem
    Input: colors - list of 0s, 1s, 2s
    Output: sorted list
    """
    # TODO: Implement Dutch flag problem using bubble sort approach
    pass

def bubble_sort_linked_list(head):
    """
    Bubble sort cho linked list
    Input: head - head of linked list
    Output: head of sorted linked list
    """
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    # TODO: Implement bubble sort for linked list
    pass

def sort_intervals_by_start(intervals):
    """
    Sắp xếp intervals theo start time
    Input: intervals - list of [start, end] pairs
    Output: sorted intervals
    """
    # TODO: Implement interval sorting using bubble sort
    pass

def adaptive_bubble_sort(arr):
    """
    Adaptive bubble sort - detect patterns và optimize accordingly
    Input: arr - list of elements
    Output: tuple (sorted_arr, algorithm_used)
    """
    # TODO: Implement adaptive bubble sort
    pass

# Helper functions
def create_linked_list(arr):
    """Create linked list from array"""
    if not arr:
        return None
    
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_array(head):
    """Convert linked list to array"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

# Test cases
if __name__ == "__main__":
    # Test sort_by_frequency
    print("=== SORT BY FREQUENCY ===")
    
    frequency_arrays = [
        [4, 5, 6, 5, 4, 3],           # Expected: [6, 3, 4, 4, 5, 5]
        [1, 1, 1, 2, 2, 3],           # Expected: [3, 2, 2, 1, 1, 1]
        [1, 2, 3, 4, 5],              # Expected: [1, 2, 3, 4, 5] (all same frequency)
    ]
    
    for arr in frequency_arrays:
        original = arr.copy()
        sorted_arr = sort_by_frequency(arr)
        print(f"Original: {original}")
        print(f"By frequency: {sorted_arr}")
        print()
    
    # Test sort_students_by_grades
    print("=== SORT STUDENTS BY GRADES ===")
    
    students = [
        ("Alice", 85),
        ("Bob", 90),
        ("Charlie", 85),
        ("David", 92),
        ("Eve", 90)
    ]
    
    sorted_students = sort_students_by_grades(students)
    print("Students sorted by grade (then by name):")
    for name, grade in sorted_students:
        print(f"  {name}: {grade}")
    
    # Test custom comparison
    print(f"\n=== CUSTOM COMPARISON ===")
    
    # Sort strings by last character
    words = ["hello", "world", "python", "java", "code"]
    
    def compare_by_last_char(a, b):
        return a[-1] > b[-1]
    
    original = words.copy()
    bubble_sort_with_custom_comparison(words, compare_by_last_char)
    print(f"Sort by last character:")
    print(f"  Original: {original}")
    print(f"  Sorted: {words}")
    
    # Test find_kth_largest_bubble
    print(f"\n=== KTH LARGEST ELEMENT ===")
    
    kth_arrays = [
        ([3, 2, 1, 5, 6, 4], 2),     # Expected: 5
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),  # Expected: 4
        ([1], 1),                     # Expected: 1
    ]
    
    for arr, k in kth_arrays:
        kth_largest = find_kth_largest_bubble(arr.copy(), k)
        print(f"Array: {arr}, k={k}")
        print(f"  {k}th largest: {kth_largest}")
    
    # Test sort_colors_bubble
    print(f"\n=== SORT COLORS (DUTCH FLAG) ===")
    
    color_arrays = [
        [2, 0, 2, 1, 1, 0],          # Expected: [0, 0, 1, 1, 2, 2]
        [2, 0, 1],                   # Expected: [0, 1, 2]
        [0],                         # Expected: [0]
        [1, 1, 1, 0, 0, 2, 2]        # Expected: [0, 0, 1, 1, 1, 2, 2]
    ]
    
    for colors in color_arrays:
        original = colors.copy()
        sort_colors_bubble(colors)
        print(f"Colors: {original} -> {colors}")
    
    # Test bubble_sort_linked_list
    print(f"\n=== BUBBLE SORT LINKED LIST ===")
    
    linked_list_arrays = [
        [4, 2, 1, 3],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [1]
    ]
    
    for arr in linked_list_arrays:
        head = create_linked_list(arr)
        sorted_head = bubble_sort_linked_list(head)
        sorted_arr = linked_list_to_array(sorted_head)
        
        print(f"Linked list: {arr} -> {sorted_arr}")
    
    # Test sort_intervals_by_start
    print(f"\n=== SORT INTERVALS ===")
    
    intervals_list = [
        [[1, 3], [6, 9], [2, 5], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 2], [3, 4], [5, 6]],
        [[2, 3], [1, 4], [3, 6]]
    ]
    
    for intervals in intervals_list:
        original = intervals.copy()
        sort_intervals_by_start(intervals)
        print(f"Intervals: {original}")
        print(f"  Sorted: {intervals}")
    
    # Test adaptive_bubble_sort
    print(f"\n=== ADAPTIVE BUBBLE SORT ===")
    
    adaptive_test_cases = [
        [1, 2, 3, 4, 5],             # Already sorted
        [5, 4, 3, 2, 1],             # Reverse sorted
        [1, 3, 2, 4, 6, 5],          # Nearly sorted
        [5, 1, 4, 2, 8, 0, 2]        # Random
    ]
    
    for arr in adaptive_test_cases:
        original = arr.copy()
        sorted_arr, algorithm = adaptive_bubble_sort(arr)
        print(f"Array: {original}")
        print(f"  Sorted: {sorted_arr}")
        print(f"  Algorithm used: {algorithm}")
    
    # Performance analysis
    print(f"\n=== PERFORMANCE ANALYSIS ===")
    
    import time
    import random
    
    # Test performance với different data patterns
    patterns = {
        'Random': lambda n: [random.randint(1, n) for _ in range(n)],
        'Sorted': lambda n: list(range(n)),
        'Reverse': lambda n: list(range(n, 0, -1)),
        'Nearly sorted': lambda n: list(range(n)) + [random.randint(1, n) for _ in range(n//10)]
    }
    
    size = 200
    
    for pattern_name, pattern_func in patterns.items():
        test_arr = pattern_func(size)
        
        start = time.time()
        bubble_sort_optimized(test_arr.copy())  # Assuming this exists from previous problem
        end = time.time()
        
        print(f"{pattern_name} data (size {size}): {end-start:.4f}s")
    
    print(f"\n=== BUBBLE SORT APPLICATIONS SUMMARY ===")
    print("Practical Applications:")
    print("  - Educational demonstrations")
    print("  - Small dataset sorting")
    print("  - Custom comparison requirements")
    print("  - Linked list sorting")
    print("  - Partial sorting (kth element)")
    
    print("\\nAdvantages:")
    print("  - Simple implementation")
    print("  - Stable sorting")
    print("  - In-place sorting")
    print("  - Adaptive (với optimizations)")
    
    print("\\nDisadvantages:")
    print("  - O(n²) time complexity")
    print("  - Poor performance on large datasets")
    print("  - Many unnecessary comparisons")
    
    print("\\nWhen to use:")
    print("  - Learning sorting concepts")
    print("  - Very small datasets (< 10 elements)")
    print("  - When code simplicity is priority")
    print("  - Custom comparison logic needed")