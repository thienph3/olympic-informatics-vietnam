"""
Day 15 - Problem 3: Exponential search implementations
Thời gian: 25 phút
"""

def exponential_search(arr, target):
    """
    Exponential search - tốt cho unbounded arrays
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target hoặc -1
    Time complexity: O(log n)
    """
    # TODO: Implement exponential search
    pass

def exponential_search_first_occurrence(arr, target):
    """
    Tìm first occurrence bằng exponential search
    Input: arr - sorted array có duplicates, target - giá trị cần tìm
    Output: index đầu tiên của target, -1 nếu không có
    """
    # TODO: Implement first occurrence với exponential search
    pass

def exponential_search_insertion_point(arr, target):
    """
    Tìm insertion point bằng exponential search
    Input: arr - sorted array, target - giá trị cần insert
    Output: index để insert target
    """
    # TODO: Implement insertion point với exponential search
    pass

def exponential_search_range(arr, target):
    """
    Tìm range [first, last] của target bằng exponential search
    Input: arr - sorted array, target - giá trị cần tìm
    Output: [first_index, last_index], [-1, -1] nếu không có
    """
    # TODO: Implement range finding với exponential search
    pass

class InfiniteArray:
    """Simulate infinite sorted array"""
    def __init__(self, arr):
        self.arr = arr
    
    def get(self, index):
        """Get element at index, return infinity if out of bounds"""
        if index >= len(self.arr):
            return float('inf')
        return self.arr[index]
    
    def size_hint(self):
        """Return actual size for testing purposes"""
        return len(self.arr)

def exponential_search_infinite(infinite_arr, target):
    """
    Exponential search cho infinite array
    Input: infinite_arr - InfiniteArray object, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement exponential search for infinite array
    pass

def exponential_search_2d_matrix(matrix, target):
    """
    Exponential search trong sorted 2D matrix
    Input: matrix - 2D sorted matrix, target - giá trị cần tìm
    Output: (row, col) nếu tìm thấy, (-1, -1) nếu không
    """
    # TODO: Implement exponential search for 2D matrix
    pass

def compare_exponential_vs_binary(arr, target):
    """
    So sánh hiệu suất exponential vs binary search
    Input: arr - sorted array, target - giá trị cần tìm
    Output: dictionary với results và timing
    """
    import time
    
    def binary_search(arr, target):
        # TODO: Implement binary search for comparison
        pass
    
    # TODO: Implement comparison
    results = {}
    
    # Measure binary search
    start = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start
    
    # Measure exponential search
    start = time.time()
    exp_result = exponential_search(arr, target)
    exp_time = time.time() - start
    
    return {
        'binary': {'result': binary_result, 'time': binary_time},
        'exponential': {'result': exp_result, 'time': exp_time}
    }

# Test cases
if __name__ == "__main__":
    # Test exponential_search
    print("=== EXPONENTIAL SEARCH ===")
    
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
    targets = [1, 15, 30, 35, 0]
    
    for target in targets:
        result = exponential_search(arr, target)
        print(f"Tìm {target} trong array: {result}")
    
    # Test exponential_search_first_occurrence
    print(f"\n=== FIRST OCCURRENCE ===")
    
    arr_with_dups = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
    targets = [2, 4, 5, 6]
    
    for target in targets:
        first_idx = exponential_search_first_occurrence(arr_with_dups, target)
        print(f"First occurrence của {target}: {first_idx}")
    
    # Test exponential_search_insertion_point
    print(f"\n=== INSERTION POINT ===")
    
    arr_insert = [1, 3, 5, 7, 9]
    values_to_insert = [0, 2, 4, 6, 8, 10]
    
    for value in values_to_insert:
        insert_pos = exponential_search_insertion_point(arr_insert, value)
        print(f"Insert {value} tại position: {insert_pos}")
    
    # Test exponential_search_range
    print(f"\n=== RANGE FINDING ===")
    
    arr_range = [1, 2, 2, 2, 3, 4, 4, 4, 4, 5]
    targets = [2, 4, 1, 6]
    
    for target in targets:
        range_result = exponential_search_range(arr_range, target)
        print(f"Range của {target}: {range_result}")
    
    # Test exponential_search_infinite
    print(f"\n=== INFINITE ARRAY SEARCH ===")
    
    # Create infinite array simulation
    finite_arr = list(range(1, 1000000, 2))  # Odd numbers up to 1M
    infinite_arr = InfiniteArray(finite_arr)
    
    infinite_targets = [999, 1001, 999999, 1000000]
    
    for target in infinite_targets:
        result = exponential_search_infinite(infinite_arr, target)
        print(f"Tìm {target} trong infinite array: {result}")
    
    # Test exponential_search_2d_matrix
    print(f"\n=== 2D MATRIX SEARCH ===")
    
    matrix = [
        [1,  4,  7,  11],
        [2,  5,  8,  12],
        [3,  6,  9,  16],
        [10, 13, 14, 17]
    ]
    
    matrix_targets = [5, 14, 20]
    
    for target in matrix_targets:
        result = exponential_search_2d_matrix(matrix, target)
        print(f"Tìm {target} trong 2D matrix: {result}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    # Test với different array sizes
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        test_arr = list(range(size))
        target = size // 4  # Target near beginning
        
        comparison = compare_exponential_vs_binary(test_arr, target)
        
        print(f"\\nArray size: {size}, target: {target}")
        print(f"Binary search: {comparison['binary']['time']:.8f}s")
        print(f"Exponential search: {comparison['exponential']['time']:.8f}s")
        
        if comparison['exponential']['time'] > 0:
            ratio = comparison['binary']['time'] / comparison['exponential']['time']
            print(f"Speed ratio (binary/exponential): {ratio:.2f}")
    
    # Test với target positions khác nhau
    print(f"\n=== TARGET POSITION ANALYSIS ===")
    
    large_arr = list(range(100000))
    positions = [10, 100, 1000, 10000, 50000, 99999]
    
    for pos in positions:
        target = large_arr[pos]
        comparison = compare_exponential_vs_binary(large_arr, target)
        
        print(f"Target at position {pos}:")
        print(f"  Binary: {comparison['binary']['time']:.8f}s")
        print(f"  Exponential: {comparison['exponential']['time']:.8f}s")
    
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
        result = exponential_search(arr, target)
        print(f"{description}: {result}")
    
    print(f"\n=== EXPONENTIAL SEARCH ANALYSIS ===")
    print("Time Complexity:")
    print("  - Finding range: O(log n)")
    print("  - Binary search in range: O(log n)")
    print("  - Total: O(log n)")
    
    print("\\nSpace Complexity:")
    print("  - O(1) for iterative implementation")
    
    print("\\nBest Use Cases:")
    print("  - Unbounded/infinite arrays")
    print("  - Target likely to be near beginning")
    print("  - Unknown array size")
    print("  - Streaming data")
    
    print("\\nAdvantages:")
    print("  - Works with unbounded data")
    print("  - Good performance when target is near start")
    print("  - Same worst-case complexity as binary search")
    
    print("\\nDisadvantages:")
    print("  - Slightly more complex than binary search")
    print("  - May be slower for targets near end")
    print("  - Requires sorted data")