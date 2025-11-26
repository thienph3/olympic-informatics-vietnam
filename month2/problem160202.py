"""
Day 16 - Problem 4: Selection sort optimizations
Thời gian: 25 phút
"""

def selection_sort_bidirectional(arr):
    """
    Bidirectional selection sort - tìm min và max từ 2 đầu
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement bidirectional selection sort
    pass

def selection_sort_with_heap_property(arr):
    """
    Selection sort sử dụng heap property để optimize finding min
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement selection sort với heap optimization
    pass

def tournament_selection_sort(arr):
    """
    Tournament selection sort - sử dụng tournament tree
    Input: arr - list of comparable elements
    Output: sorted list
    """
    # TODO: Implement tournament selection sort
    pass

def selection_sort_with_early_termination(arr):
    """
    Selection sort với early termination khi array đã sorted
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement selection sort với early termination
    pass

def adaptive_selection_sort(arr):
    """
    Adaptive selection sort - detect patterns và optimize
    Input: arr - list of comparable elements
    Output: tuple (sorted_arr, optimizations_used)
    """
    # TODO: Implement adaptive selection sort
    pass

def selection_sort_for_linked_list(head):
    """
    Selection sort optimized cho linked list
    Input: head - head of linked list
    Output: head of sorted linked list
    """
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    # TODO: Implement selection sort for linked list
    pass

def selection_sort_with_memory_optimization(arr):
    """
    Selection sort với memory access optimization
    Input: arr - list of comparable elements
    Output: sorted list với minimized memory accesses
    """
    # TODO: Implement memory-optimized selection sort
    pass

def parallel_selection_sort_simulation(arr, num_threads=2):
    """
    Simulate parallel selection sort
    Input: arr - list, num_threads - number of parallel threads
    Output: sorted list
    """
    # TODO: Implement simulated parallel selection sort
    pass

# Helper functions
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    """Create linked list from array"""
    if not arr:
        return None
    
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

def is_sorted(arr):
    """Check if array is sorted"""
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# Test cases
if __name__ == "__main__":
    # Test bidirectional selection sort
    print("=== BIDIRECTIONAL SELECTION SORT ===")
    
    bidirectional_arrays = [
        [3, 7, 1, 9, 4, 6, 2, 8, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 9, 2, 8, 3, 7, 4, 6, 5]
    ]
    
    for arr in bidirectional_arrays:
        original = arr.copy()
        selection_sort_bidirectional(arr)
        print(f"Bidirectional: {original} -> {arr}")
    
    # Test heap property optimization
    print(f"\n=== HEAP PROPERTY OPTIMIZATION ===")
    
    heap_test_arrays = [
        [4, 1, 3, 2, 16, 9, 10, 14, 8, 7],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for arr in heap_test_arrays:
        original = arr.copy()
        selection_sort_with_heap_property(arr)
        print(f"Heap optimized: {original} -> {arr}")
    
    # Test tournament selection sort
    print(f"\n=== TOURNAMENT SELECTION SORT ===")
    
    tournament_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [1, 3, 2, 4, 6, 5, 8, 7]
    ]
    
    for arr in tournament_arrays:
        original = arr.copy()
        sorted_arr = tournament_selection_sort(arr)
        print(f"Tournament: {original} -> {sorted_arr}")
    
    # Test early termination
    print(f"\n=== EARLY TERMINATION ===")
    
    early_term_arrays = [
        [1, 2, 3, 4, 5],           # Already sorted
        [1, 3, 2, 4, 5],           # Nearly sorted
        [2, 1, 3, 4, 5],           # One element out of place
        [5, 4, 3, 2, 1]            # Reverse sorted
    ]
    
    for arr in early_term_arrays:
        original = arr.copy()
        selection_sort_with_early_termination(arr)
        print(f"Early termination: {original} -> {arr}")
    
    # Test adaptive selection sort
    print(f"\n=== ADAPTIVE SELECTION SORT ===")
    
    adaptive_test_cases = [
        [1, 2, 3, 4, 5],           # Already sorted
        [5, 4, 3, 2, 1],           # Reverse sorted
        [1, 3, 2, 4, 6, 5],        # Nearly sorted
        [5, 1, 4, 2, 8, 0, 2]      # Random
    ]
    
    for arr in adaptive_test_cases:
        original = arr.copy()
        sorted_arr, optimizations = adaptive_selection_sort(arr)
        print(f"Array: {original}")
        print(f"  Sorted: {sorted_arr}")
        print(f"  Optimizations: {optimizations}")
    
    # Test linked list selection sort
    print(f"\n=== LINKED LIST SELECTION SORT ===")
    
    linked_list_arrays = [
        [4, 2, 1, 3],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6]
    ]
    
    for arr in linked_list_arrays:
        head = create_linked_list(arr)
        sorted_head = selection_sort_for_linked_list(head)
        sorted_arr = linked_list_to_array(sorted_head)
        
        print(f"Linked list: {arr} -> {sorted_arr}")
    
    # Test memory optimization
    print(f"\n=== MEMORY OPTIMIZATION ===")
    
    memory_test_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    
    for arr in memory_test_arrays:
        original = arr.copy()
        selection_sort_with_memory_optimization(arr)
        print(f"Memory optimized: {original} -> {arr}")
    
    # Test parallel selection sort simulation
    print(f"\n=== PARALLEL SELECTION SORT ===")
    
    parallel_arrays = [
        [8, 3, 1, 7, 0, 10, 2],
        [5, 2, 8, 1, 9, 3, 7, 4, 6],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ]
    
    for arr in parallel_arrays:
        original = arr.copy()
        sorted_arr = parallel_selection_sort_simulation(arr, num_threads=2)
        print(f"Parallel (2 threads): {original} -> {sorted_arr}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    import time
    import random
    
    # Compare optimization techniques
    sizes = [200, 500, 1000]
    
    for size in sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\nArray size: {size}")
        
        # Basic selection sort (from previous problem)
        def basic_selection_sort(arr):
            n = len(arr)
            for i in range(n):
                min_idx = i
                for j in range(i + 1, n):
                    if arr[j] < arr[min_idx]:
                        min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
            return arr
        
        # Test basic version
        arr1 = test_data.copy()
        start = time.time()
        basic_selection_sort(arr1)
        basic_time = time.time() - start
        
        # Test bidirectional version
        arr2 = test_data.copy()
        start = time.time()
        selection_sort_bidirectional(arr2)
        bidirectional_time = time.time() - start
        
        # Test adaptive version
        arr3 = test_data.copy()
        start = time.time()
        adaptive_selection_sort(arr3)
        adaptive_time = time.time() - start
        
        print(f"  Basic selection sort: {basic_time:.4f}s")
        print(f"  Bidirectional: {bidirectional_time:.4f}s")
        print(f"  Adaptive: {adaptive_time:.4f}s")
        
        # Calculate improvements
        if basic_time > 0:
            bidirectional_improvement = (basic_time - bidirectional_time) / basic_time * 100
            adaptive_improvement = (basic_time - adaptive_time) / basic_time * 100
            
            print(f"  Bidirectional improvement: {bidirectional_improvement:.1f}%")
            print(f"  Adaptive improvement: {adaptive_improvement:.1f}%")
    
    # Test với different data patterns
    print(f"\n=== PATTERN-SPECIFIC PERFORMANCE ===")
    
    patterns = {
        'Random': lambda n: [random.randint(1, n) for _ in range(n)],
        'Sorted': lambda n: list(range(n)),
        'Reverse': lambda n: list(range(n, 0, -1)),
        'Nearly sorted': lambda n: list(range(n)) + [random.randint(1, n) for _ in range(n//20)]
    }
    
    size = 300
    
    for pattern_name, pattern_func in patterns.items():
        test_arr = pattern_func(size)
        
        # Test adaptive selection sort
        start = time.time()
        sorted_arr, optimizations = adaptive_selection_sort(test_arr.copy())
        end = time.time()
        
        print(f"{pattern_name} data:")
        print(f"  Time: {end-start:.4f}s")
        print(f"  Optimizations: {optimizations}")
    
    print(f"\n=== SELECTION SORT OPTIMIZATIONS SUMMARY ===")
    print("Optimization Techniques:")
    print("  - Bidirectional: Find min and max simultaneously")
    print("  - Heap property: Use heap structure for efficient min finding")
    print("  - Tournament: Use tournament tree for selection")
    print("  - Early termination: Stop when array becomes sorted")
    print("  - Adaptive: Detect patterns and apply appropriate optimizations")
    print("  - Memory optimization: Minimize cache misses")
    print("  - Parallel: Distribute work across multiple threads")
    
    print("\\nComplexity Improvements:")
    print("  - Bidirectional: ~50% fewer iterations")
    print("  - Tournament: O(n log n) comparisons vs O(n²)")
    print("  - Early termination: O(n) best case for sorted data")
    print("  - Adaptive: Varies based on input pattern")
    
    print("\\nPractical Benefits:")
    print("  - Reduced number of comparisons")
    print("  - Better cache locality")
    print("  - Improved performance on specific patterns")
    print("  - Maintained simplicity of basic algorithm")