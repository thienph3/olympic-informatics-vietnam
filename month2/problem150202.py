"""
Day 15 - Problem 4: Infinite array problems
Thời gian: 25 phút
"""

class InfiniteArrayReader:
    """
    Interface for reading infinite sorted array
    """
    def __init__(self, arr):
        self.arr = arr
    
    def get(self, index):
        """Get element at index, return infinity if out of bounds"""
        if index >= len(self.arr):
            return float('inf')
        return self.arr[index]

def search_in_infinite_array(reader, target):
    """
    Tìm kiếm trong infinite sorted array
    Input: reader - InfiniteArrayReader, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement search in infinite array
    pass

def find_first_occurrence_infinite(reader, target):
    """
    Tìm first occurrence trong infinite array
    Input: reader - InfiniteArrayReader, target - giá trị cần tìm
    Output: index đầu tiên của target, -1 nếu không có
    """
    # TODO: Implement first occurrence in infinite array
    pass

def count_occurrences_infinite(reader, target):
    """
    Đếm số lần xuất hiện trong infinite array
    Input: reader - InfiniteArrayReader, target - giá trị cần đếm
    Output: số lần xuất hiện
    """
    # TODO: Implement counting in infinite array
    pass

def find_kth_element_infinite(reader, k):
    """
    Tìm phần tử thứ k trong infinite array (1-indexed)
    Input: reader - InfiniteArrayReader, k - vị trí cần tìm
    Output: phần tử thứ k
    """
    # TODO: Implement kth element finding
    pass

def search_in_infinite_matrix(matrix_reader, target):
    """
    Tìm kiếm trong infinite 2D matrix
    Input: matrix_reader - function(row, col) -> value, target - giá trị cần tìm
    Output: (row, col) nếu tìm thấy, (-1, -1) nếu không
    """
    # TODO: Implement 2D infinite matrix search
    pass

class StreamingArray:
    """
    Simulate streaming array where elements arrive over time
    """
    def __init__(self, arr, chunk_size=10):
        self.arr = arr
        self.chunk_size = chunk_size
        self.loaded_size = 0
    
    def get(self, index):
        """Get element, loading more data if needed"""
        if index >= len(self.arr):
            return float('inf')
        
        # Simulate loading data in chunks
        if index >= self.loaded_size:
            self.loaded_size = min(len(self.arr), index + self.chunk_size)
        
        return self.arr[index]
    
    def get_loaded_size(self):
        """Return currently loaded size"""
        return self.loaded_size

def search_in_streaming_array(streaming_arr, target):
    """
    Tìm kiếm trong streaming array
    Input: streaming_arr - StreamingArray, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement search in streaming array
    pass

def find_boundary_in_infinite_array(reader, condition_func):
    """
    Tìm boundary trong infinite array where condition changes
    Input: reader - InfiniteArrayReader, condition_func - function to test
    Output: index where condition first becomes True
    """
    # TODO: Implement boundary finding
    # Example: find first index where arr[i] >= target
    pass

# Test cases
if __name__ == "__main__":
    # Test search_in_infinite_array
    print("=== INFINITE ARRAY SEARCH ===")
    
    # Create test infinite arrays
    test_arrays = [
        list(range(1, 1000, 2)),      # Odd numbers
        list(range(2, 1000, 2)),      # Even numbers
        [i*i for i in range(1, 100)], # Perfect squares
        list(range(100, 10000, 100))  # Multiples of 100
    ]
    
    for i, arr in enumerate(test_arrays):
        reader = InfiniteArrayReader(arr)
        
        # Test some targets
        if i == 0:  # Odd numbers
            targets = [1, 99, 501, 1000]
        elif i == 1:  # Even numbers
            targets = [2, 100, 500, 999]
        elif i == 2:  # Perfect squares
            targets = [1, 25, 81, 150]
        else:  # Multiples of 100
            targets = [100, 500, 1000, 1050]
        
        print(f"\\nArray {i+1} (first few: {arr[:5]}...):")
        for target in targets:
            result = search_in_infinite_array(reader, target)
            print(f"  Tìm {target}: {result}")
    
    # Test find_first_occurrence_infinite
    print(f"\n=== FIRST OCCURRENCE IN INFINITE ARRAY ===")
    
    # Array with duplicates
    arr_with_dups = []
    for i in range(1, 100):
        arr_with_dups.extend([i] * (i % 3 + 1))  # Each number appears 1-3 times
    
    reader_dups = InfiniteArrayReader(arr_with_dups)
    
    targets = [5, 10, 25, 50, 100]
    for target in targets:
        first_idx = find_first_occurrence_infinite(reader_dups, target)
        print(f"First occurrence của {target}: {first_idx}")
    
    # Test count_occurrences_infinite
    print(f"\n=== COUNT OCCURRENCES ===")
    
    for target in [5, 10, 15]:
        count = count_occurrences_infinite(reader_dups, target)
        print(f"Count của {target}: {count}")
    
    # Test find_kth_element_infinite
    print(f"\n=== KTH ELEMENT ===")
    
    simple_reader = InfiniteArrayReader(list(range(1, 1000)))
    
    k_values = [1, 10, 100, 500, 999]
    for k in k_values:
        kth_element = find_kth_element_infinite(simple_reader, k)
        print(f"{k}th element: {kth_element}")
    
    # Test search_in_infinite_matrix
    print(f"\n=== INFINITE MATRIX SEARCH ===")
    
    def matrix_reader(row, col):
        """Infinite matrix: matrix[i][j] = i*10 + j"""
        if row >= 100 or col >= 100:  # Simulate finite but large matrix
            return float('inf')
        return row * 10 + col
    
    matrix_targets = [0, 25, 99, 150]
    for target in matrix_targets:
        result = search_in_infinite_matrix(matrix_reader, target)
        print(f"Tìm {target} trong infinite matrix: {result}")
    
    # Test search_in_streaming_array
    print(f"\n=== STREAMING ARRAY SEARCH ===")
    
    streaming_data = list(range(0, 1000, 5))  # [0, 5, 10, 15, ...]
    streaming_arr = StreamingArray(streaming_data, chunk_size=20)
    
    streaming_targets = [0, 25, 100, 500, 1000]
    for target in streaming_targets:
        result = search_in_streaming_array(streaming_arr, target)
        loaded_size = streaming_arr.get_loaded_size()
        print(f"Tìm {target}: index={result}, loaded_size={loaded_size}")
    
    # Test find_boundary_in_infinite_array
    print(f"\n=== BOUNDARY FINDING ===")
    
    # Array: [1, 2, 3, ..., 50, 100, 101, 102, ...]
    boundary_arr = list(range(1, 51)) + list(range(100, 200))
    boundary_reader = InfiniteArrayReader(boundary_arr)
    
    # Find first element >= 100
    def condition_ge_100(x):
        return x >= 100
    
    boundary_idx = find_boundary_in_infinite_array(boundary_reader, condition_ge_100)
    print(f"First element >= 100 tại index: {boundary_idx}")
    
    # Find first element >= 150
    def condition_ge_150(x):
        return x >= 150
    
    boundary_idx = find_boundary_in_infinite_array(boundary_reader, condition_ge_150)
    print(f"First element >= 150 tại index: {boundary_idx}")
    
    # Performance analysis
    print(f"\n=== PERFORMANCE ANALYSIS ===")
    
    import time
    
    # Test performance với large infinite array
    large_arr = list(range(0, 1000000, 7))  # Multiples of 7
    large_reader = InfiniteArrayReader(large_arr)
    
    # Test targets at different positions
    test_positions = [0, 1000, 10000, 50000]
    
    for pos in test_positions:
        if pos < len(large_arr):
            target = large_arr[pos]
            
            start = time.time()
            result = search_in_infinite_array(large_reader, target)
            end = time.time()
            
            print(f"Target at position {pos}: {end-start:.6f}s")
    
    print(f"\n=== INFINITE ARRAY TECHNIQUES SUMMARY ===")
    print("Key Techniques:")
    print("  - Exponential search for range finding")
    print("  - Binary search within found range")
    print("  - Boundary detection for condition changes")
    print("  - Streaming data handling")
    
    print("\\nApplications:")
    print("  - Database queries on large datasets")
    print("  - Log file searching")
    print("  - Real-time data streams")
    print("  - Memory-mapped files")
    print("  - Network-based data access")
    
    print("\\nComplexity:")
    print("  - Time: O(log n) where n is position of target")
    print("  - Space: O(1)")
    print("  - Network calls: O(log n)")
    
    print("\\nAdvantages:")
    print("  - Works without knowing array size")
    print("  - Efficient for early targets")
    print("  - Handles streaming data")
    print("  - Memory efficient")
    
    print("\\nChallenges:")
    print("  - Network latency for remote data")
    print("  - Error handling for infinite sources")
    print("  - Caching strategies")
    print("  - Timeout management")