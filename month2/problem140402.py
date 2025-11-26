"""
Day 14 - Problem 8: Advanced Olympic problems
Thời gian: 30 phút
"""

def split_array_largest_sum(nums, m):
    """
    Split array thành m subarrays để minimize largest sum
    Input: nums - array, m - số subarrays
    Output: minimum possible largest sum
    """
    # TODO: Implement using binary search on answer
    def can_split(max_sum):
        # TODO: Check if có thể split thành m parts với max_sum
        pass
    
    # TODO: Binary search on sum range
    pass

def find_minimum_in_rotated_sorted_array_ii(nums):
    """
    Tìm minimum trong rotated sorted array có duplicates
    Input: nums - rotated sorted array với duplicates
    Output: minimum value
    Time complexity: O(log n) average, O(n) worst case
    """
    # TODO: Implement với handling duplicates
    pass

def search_for_range_in_infinite_array(reader, target):
    """
    Tìm range của target trong infinite sorted array
    Input: reader - object với get(index) method, target - giá trị cần tìm
    Output: [start_index, end_index] của target range
    """
    # TODO: Implement exponential search + binary search for range
    pass

def find_k_closest_elements(arr, k, x):
    """
    Tìm k elements gần x nhất trong sorted array
    Input: arr - sorted array, k - số elements, x - target value
    Output: k elements gần x nhất (sorted order)
    """
    # TODO: Implement using binary search + two pointers
    pass

def count_complete_tree_nodes(root):
    """
    Đếm nodes trong complete binary tree
    Input: root - root của complete binary tree
    Output: số nodes
    Time complexity: O(log²n)
    """
    # TODO: Implement using binary search on tree levels
    # Note: Cần define TreeNode class trước
    pass

def find_duplicate_number_binary_search(nums):
    """
    Tìm duplicate number trong array [1,n] có n+1 elements
    Input: nums - array chứa numbers từ 1 đến n, có 1 duplicate
    Output: duplicate number
    Time complexity: O(n log n), Space: O(1)
    """
    # TODO: Implement using binary search on value range
    pass

def median_of_two_sorted_arrays(nums1, nums2):
    """
    Tìm median của 2 sorted arrays
    Input: nums1, nums2 - sorted arrays
    Output: median value
    Time complexity: O(log(min(m,n)))
    """
    # TODO: Implement using binary search
    pass

def find_peak_element_ii(matrix):
    """
    Tìm peak element trong 2D matrix
    Input: matrix - 2D matrix
    Output: [row, col] của peak element
    Time complexity: O(m log n)
    """
    # TODO: Implement 2D peak finding
    pass

def capacity_to_ship_packages(weights, D):
    """
    Tìm minimum ship capacity để ship packages trong D days
    Input: weights - package weights, D - số days
    Output: minimum capacity
    """
    # TODO: Implement using binary search on capacity
    pass

def smallest_divisor_given_threshold(nums, threshold):
    """
    Tìm smallest divisor sao cho sum of division results <= threshold
    Input: nums - array, threshold - upper bound
    Output: smallest divisor
    """
    # TODO: Implement using binary search on divisor
    pass

# Helper classes
class ArrayReader:
    """Mock infinite array reader"""
    def __init__(self, arr):
        self.arr = arr
    
    def get(self, index):
        if index >= len(self.arr):
            return float('inf')
        return self.arr[index]

class TreeNode:
    """Binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Test cases
if __name__ == "__main__":
    # Test split_array_largest_sum
    print("=== SPLIT ARRAY LARGEST SUM ===")
    
    test_cases = [
        ([7, 2, 5, 10, 8], 2),  # Expected: 18
        ([1, 2, 3, 4, 5], 2),   # Expected: 9
        ([1, 4, 4], 3)          # Expected: 4
    ]
    
    for nums, m in test_cases:
        result = split_array_largest_sum(nums, m)
        print(f"Split {nums} into {m} parts: {result}")
    
    # Test find_minimum_in_rotated_sorted_array_ii
    print(f"\n=== MINIMUM IN ROTATED ARRAY WITH DUPLICATES ===")
    
    rotated_arrays = [
        [1, 3, 5],
        [2, 2, 2, 0, 1],
        [1, 1, 1, 1, 1],
        [3, 1, 3, 3, 3]
    ]
    
    for arr in rotated_arrays:
        minimum = find_minimum_in_rotated_sorted_array_ii(arr)
        print(f"Minimum trong {arr}: {minimum}")
    
    # Test search_for_range_in_infinite_array
    print(f"\n=== RANGE IN INFINITE ARRAY ===")
    
    infinite_arr = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9]
    reader = ArrayReader(infinite_arr)
    target = 3
    
    range_result = search_for_range_in_infinite_array(reader, target)
    print(f"Range của {target} trong infinite array: {range_result}")
    
    # Test find_k_closest_elements
    print(f"\n=== K CLOSEST ELEMENTS ===")
    
    closest_test_cases = [
        ([1, 2, 3, 4, 5], 4, 3),     # Expected: [1,2,3,4]
        ([1, 2, 3, 4, 5], 4, -1),    # Expected: [1,2,3,4]
        ([1, 2, 3, 4, 5], 4, 6)      # Expected: [2,3,4,5]
    ]
    
    for arr, k, x in closest_test_cases:
        closest = find_k_closest_elements(arr, k, x)
        print(f"{k} closest to {x} trong {arr}: {closest}")
    
    # Test count_complete_tree_nodes
    print(f"\n=== COUNT COMPLETE TREE NODES ===")
    
    # Create complete binary tree: [1,2,3,4,5,6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    
    node_count = count_complete_tree_nodes(root)
    print(f"Complete tree node count: {node_count}")  # Expected: 6
    
    # Test find_duplicate_number_binary_search
    print(f"\n=== FIND DUPLICATE NUMBER ===")
    
    duplicate_arrays = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [1, 1],
        [1, 1, 2]
    ]
    
    for nums in duplicate_arrays:
        duplicate = find_duplicate_number_binary_search(nums)
        print(f"Duplicate trong {nums}: {duplicate}")
    
    # Test median_of_two_sorted_arrays
    print(f"\n=== MEDIAN OF TWO SORTED ARRAYS ===")
    
    median_test_cases = [
        ([1, 3], [2]),           # Expected: 2.0
        ([1, 2], [3, 4]),        # Expected: 2.5
        ([0, 0], [0, 0]),        # Expected: 0.0
        ([], [1]),               # Expected: 1.0
        ([2], [])                # Expected: 2.0
    ]
    
    for nums1, nums2 in median_test_cases:
        median = median_of_two_sorted_arrays(nums1, nums2)
        print(f"Median của {nums1} và {nums2}: {median}")
    
    # Test find_peak_element_ii
    print(f"\n=== 2D PEAK ELEMENT ===")
    
    matrix_2d = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    
    peak_2d = find_peak_element_ii(matrix_2d)
    if peak_2d:
        row, col = peak_2d
        print(f"2D Peak tại ({row}, {col}) = {matrix_2d[row][col]}")
    
    # Test capacity_to_ship_packages
    print(f"\n=== SHIP CAPACITY ===")
    
    ship_test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),  # Expected: 15
        ([3, 2, 2, 4, 1, 4], 3),                # Expected: 6
        ([1, 2, 3, 1, 1], 4)                    # Expected: 3
    ]
    
    for weights, D in ship_test_cases:
        capacity = capacity_to_ship_packages(weights, D)
        print(f"Ship {weights} trong {D} days: capacity = {capacity}")
    
    # Test smallest_divisor_given_threshold
    print(f"\n=== SMALLEST DIVISOR ===")
    
    divisor_test_cases = [
        ([1, 2, 5, 9], 6),      # Expected: 5
        ([2, 3, 5, 7, 11], 11), # Expected: 3
        ([19], 5)               # Expected: 4
    ]
    
    for nums, threshold in divisor_test_cases:
        divisor = smallest_divisor_given_threshold(nums, threshold)
        print(f"Smallest divisor cho {nums} với threshold {threshold}: {divisor}")
    
    # Performance analysis
    print(f"\n=== PERFORMANCE ANALYSIS ===")
    
    import time
    
    # Test performance với large arrays
    large_arr1 = list(range(0, 100000, 2))      # Even numbers
    large_arr2 = list(range(1, 100000, 2))      # Odd numbers
    
    start = time.time()
    median_large = median_of_two_sorted_arrays(large_arr1[:1000], large_arr2[:1000])
    end = time.time()
    
    print(f"Median của 2 arrays (1000 elements each): {end-start:.6f}s")
    
    print(f"\n=== COMPLEXITY SUMMARY ===")
    print("Advanced Binary Search Problems:")
    print("  - Split Array: O(n log(sum)) where sum is array sum")
    print("  - Rotated Min (duplicates): O(log n) avg, O(n) worst")
    print("  - K Closest Elements: O(log n + k)")
    print("  - Complete Tree Nodes: O(log²n)")
    print("  - Duplicate Number: O(n log n)")
    print("  - Median Two Arrays: O(log(min(m,n)))")
    print("  - 2D Peak: O(m log n)")
    print("  - Ship Capacity: O(n log(sum))")
    print("  - Smallest Divisor: O(n log(max))")
    
    print("\\nKey Techniques:")
    print("  - Binary search on answer space")
    print("  - Handling duplicates in rotated arrays")
    print("  - Two pointers với binary search")
    print("  - Divide and conquer trong 2D")
    print("  - Optimization problems as decision problems")