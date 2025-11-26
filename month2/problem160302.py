"""
Day 16 - Problem 6: Insertion sort applications
Thời gian: 30 phút
"""

def insertion_sort_linked_list(head):
    """
    Insertion sort cho linked list
    Input: head - head of linked list
    Output: head of sorted linked list
    """
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    # TODO: Implement insertion sort for linked list
    pass

def online_insertion_sort():
    """
    Online insertion sort - sort elements as they arrive
    Returns a class that can add elements và maintain sorted order
    """
    class OnlineSorter:
        def __init__(self):
            # TODO: Initialize online sorter
            pass
        
        def add_element(self, element):
            """Add element và maintain sorted order"""
            # TODO: Implement online element addition
            pass
        
        def get_sorted_list(self):
            """Get current sorted list"""
            # TODO: Return current sorted state
            pass
        
        def get_median(self):
            """Get current median"""
            # TODO: Return current median
            pass
    
    return OnlineSorter()

def insertion_sort_with_duplicates_handling(arr):
    """
    Insertion sort với special handling cho duplicates
    Input: arr - list có thể có duplicates
    Output: tuple (sorted_arr, duplicate_info)
    """
    # TODO: Implement insertion sort với duplicate tracking
    pass

def insertion_sort_for_strings(strings):
    """
    Insertion sort optimized cho strings
    Input: strings - list of strings
    Output: sorted list of strings
    """
    # TODO: Implement string-optimized insertion sort
    pass

def insertion_sort_with_early_termination(arr):
    """
    Insertion sort với early termination cho sorted subarrays
    Input: arr - list of comparable elements
    Output: sorted list với optimization info
    """
    # TODO: Implement insertion sort với early termination
    pass

def cocktail_insertion_sort(arr):
    """
    Cocktail insertion sort - bidirectional insertion
    Input: arr - list of comparable elements
    Output: sorted list (in-place)
    """
    # TODO: Implement bidirectional insertion sort
    pass

def insertion_sort_with_binary_tree(arr):
    """
    Insertion sort sử dụng binary search tree
    Input: arr - list of comparable elements
    Output: sorted list
    """
    # TODO: Implement insertion sort using BST
    pass

def parallel_insertion_sort_simulation(arr, num_threads=2):
    """
    Simulate parallel insertion sort
    Input: arr - list, num_threads - number of threads
    Output: sorted list
    """
    # TODO: Implement simulated parallel insertion sort
    pass

# Helper classes và functions
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def inorder_traversal(root):
    """Inorder traversal of BST"""
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

# Test cases
if __name__ == "__main__":
    # Test insertion_sort_linked_list
    print("=== INSERTION SORT LINKED LIST ===")
    
    linked_list_arrays = [
        [4, 2, 1, 3],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6]
    ]
    
    for arr in linked_list_arrays:
        head = create_linked_list(arr)
        sorted_head = insertion_sort_linked_list(head)
        sorted_arr = linked_list_to_array(sorted_head)
        
        print(f"Linked list: {arr} -> {sorted_arr}")
    
    # Test online insertion sort
    print(f"\n=== ONLINE INSERTION SORT ===")
    
    online_sorter = online_insertion_sort()
    
    # Simulate stream of data
    stream_data = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    
    print("Adding elements to online sorter:")
    for element in stream_data:
        online_sorter.add_element(element)
        current_list = online_sorter.get_sorted_list()
        median = online_sorter.get_median()
        print(f"  Added {element}: sorted={current_list}, median={median}")
    
    # Test duplicates handling
    print(f"\n=== DUPLICATES HANDLING ===")
    
    duplicate_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        [1, 1, 1, 1, 1],
        [1, 2, 1, 3, 2, 4, 3, 5],
        [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
    ]
    
    for arr in duplicate_arrays:
        original = arr.copy()
        sorted_arr, duplicate_info = insertion_sort_with_duplicates_handling(arr)
        print(f"Array: {original}")
        print(f"  Sorted: {sorted_arr}")
        print(f"  Duplicate info: {duplicate_info}")
    
    # Test string insertion sort
    print(f"\n=== STRING INSERTION SORT ===")
    
    string_arrays = [
        ["banana", "apple", "cherry", "date"],
        ["python", "java", "c++", "javascript", "go"],
        ["hello", "world", "programming", "algorithm"],
        ["a", "aa", "aaa", "b", "bb"]
    ]
    
    for strings in string_arrays:
        original = strings.copy()
        insertion_sort_for_strings(strings)
        print(f"Strings: {original} -> {strings}")
    
    # Test early termination
    print(f"\n=== EARLY TERMINATION ===")
    
    early_term_arrays = [
        [1, 2, 3, 4, 5],           # Already sorted
        [1, 3, 2, 4, 5, 6, 7],     # Nearly sorted
        [5, 1, 2, 3, 4],           # One element out of place
        [1, 2, 6, 3, 4, 5]         # Small disruption
    ]
    
    for arr in early_term_arrays:
        original = arr.copy()
        sorted_arr = insertion_sort_with_early_termination(arr)
        print(f"Early termination: {original} -> {sorted_arr}")
    
    # Test cocktail insertion sort
    print(f"\n=== COCKTAIL INSERTION SORT ===")
    
    cocktail_arrays = [
        [3, 7, 1, 9, 4, 6, 2, 8, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 9, 2, 8, 3, 7, 4, 6, 5]
    ]
    
    for arr in cocktail_arrays:
        original = arr.copy()
        cocktail_insertion_sort(arr)
        print(f"Cocktail insertion: {original} -> {arr}")
    
    # Test binary tree insertion sort
    print(f"\n=== BINARY TREE INSERTION SORT ===")
    
    tree_arrays = [
        [4, 2, 6, 1, 3, 5, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6]
    ]
    
    for arr in tree_arrays:
        original = arr.copy()
        sorted_arr = insertion_sort_with_binary_tree(arr)
        print(f"BST insertion sort: {original} -> {sorted_arr}")
    
    # Test parallel insertion sort
    print(f"\n=== PARALLEL INSERTION SORT ===")
    
    parallel_arrays = [
        [8, 3, 1, 7, 0, 10, 2],
        [5, 2, 8, 1, 9, 3, 7, 4, 6],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ]
    
    for arr in parallel_arrays:
        original = arr.copy()
        sorted_arr = parallel_insertion_sort_simulation(arr, num_threads=2)
        print(f"Parallel (2 threads): {original} -> {sorted_arr}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    import time
    import random
    
    # Compare different insertion sort applications
    sizes = [100, 300, 500]
    
    for size in sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        print(f"\nArray size: {size}")
        
        # Basic insertion sort
        def basic_insertion_sort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return arr
        
        # Test basic version
        arr1 = test_data.copy()
        start = time.time()
        basic_insertion_sort(arr1)
        basic_time = time.time() - start
        
        # Test BST version
        arr2 = test_data.copy()
        start = time.time()
        insertion_sort_with_binary_tree(arr2)
        bst_time = time.time() - start
        
        # Test cocktail version
        arr3 = test_data.copy()
        start = time.time()
        cocktail_insertion_sort(arr3)
        cocktail_time = time.time() - start
        
        print(f"  Basic insertion sort: {basic_time:.4f}s")
        print(f"  BST insertion sort: {bst_time:.4f}s")
        print(f"  Cocktail insertion sort: {cocktail_time:.4f}s")
    
    # Test online sorting performance
    print(f"\n=== ONLINE SORTING PERFORMANCE ===")
    
    online_sorter = online_insertion_sort()
    
    # Simulate adding many elements
    num_elements = 1000
    start = time.time()
    
    for i in range(num_elements):
        element = random.randint(1, 1000)
        online_sorter.add_element(element)
    
    end = time.time()
    
    final_list = online_sorter.get_sorted_list()
    print(f"Added {num_elements} elements online: {end-start:.4f}s")
    print(f"Final list size: {len(final_list)}")
    print(f"Is sorted: {all(final_list[i] <= final_list[i+1] for i in range(len(final_list)-1))}")
    
    print(f"\n=== INSERTION SORT APPLICATIONS SUMMARY ===")
    print("Application Areas:")
    print("  - Linked list sorting")
    print("  - Online/streaming data sorting")
    print("  - Small dataset sorting")
    print("  - Nearly sorted data optimization")
    print("  - Stable sorting requirements")
    
    print("\\nSpecialized Variants:")
    print("  - Binary insertion: Reduce comparisons")
    print("  - Online sorting: Handle streaming data")
    print("  - BST-based: O(n log n) average case")
    print("  - Cocktail: Bidirectional optimization")
    print("  - Early termination: Detect sorted regions")
    
    print("\\nPractical Benefits:")
    print("  - Simple implementation")
    print("  - Stable sorting")
    print("  - Adaptive behavior")
    print("  - Good for small datasets")
    print("  - Excellent for nearly sorted data")
    
    print("\\nReal-world Usage:")
    print("  - Subroutine in hybrid algorithms (Timsort, Introsort)")
    print("  - Small array optimization in quicksort")
    print("  - Online data processing")
    print("  - Embedded systems với memory constraints")