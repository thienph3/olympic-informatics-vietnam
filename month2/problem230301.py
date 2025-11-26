"""
Problem 230301: Search Algorithms và Variants
Thuật toán tìm kiếm sử dụng divide and conquer

Topics: Binary search variants, search in special arrays, optimization problems
"""

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary search đệ quy
    Time: O(log n), Space: O(log n)
    """
    # TODO: Implement recursive binary search
    pass

def binary_search_leftmost(arr, target):
    """
    Tìm vị trí leftmost của target (first occurrence)
    """
    # TODO: Find leftmost position of target
    pass

def binary_search_rightmost(arr, target):
    """
    Tìm vị trí rightmost của target (last occurrence)
    """
    # TODO: Find rightmost position of target
    pass

def search_rotated_array(arr, target):
    """
    Tìm kiếm trong mảng đã rotate
    Time: O(log n), Space: O(log n)
    """
    # TODO: Search in rotated sorted array
    pass

def find_peak_element(arr):
    """
    Tìm peak element (lớn hơn neighbors)
    Time: O(log n), Space: O(log n)
    """
    # TODO: Find peak element using binary search
    pass

def find_minimum_rotated_array(arr):
    """
    Tìm minimum trong rotated sorted array
    Time: O(log n), Space: O(log n)
    """
    # TODO: Find minimum in rotated sorted array
    pass

def search_2d_matrix(matrix, target):
    """
    Tìm kiếm trong ma trận 2D đã sắp xếp
    Time: O(log(m*n)), Space: O(log(m*n))
    """
    # TODO: Search in 2D sorted matrix
    pass

def find_missing_number(arr):
    """
    Tìm số bị thiếu trong dãy liên tiếp
    Time: O(log n), Space: O(log n)
    """
    # TODO: Find missing number in consecutive sequence
    pass

def sqrt_binary_search(x):
    """
    Tính căn bậc hai bằng binary search
    Time: O(log x), Space: O(log x)
    """
    # TODO: Calculate square root using binary search
    pass

def find_kth_smallest_two_arrays(arr1, arr2, k):
    """
    Tìm k-th smallest element trong hai mảng đã sắp xếp
    Time: O(log(min(m,n))), Space: O(log(min(m,n)))
    """
    # TODO: Find k-th smallest in two sorted arrays
    pass

# Test cases
def test_search_algorithms():
    print("Search Algorithms and Variants")
    print("=" * 35)
    
    # Test recursive binary search
    print("1. Recursive Binary Search:")
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    search_targets = [7, 4, 1, 15, 20]
    for target in search_targets:
        result = binary_search_recursive(sorted_arr, target)
        print(f"search {target} in {sorted_arr}: index {result}")
    
    # Test leftmost binary search
    print("\n2. Binary Search Leftmost:")
    duplicate_arr = [1, 2, 2, 2, 3, 4, 4, 5]
    leftmost_targets = [2, 4, 1, 6]
    for target in leftmost_targets:
        result = binary_search_leftmost(duplicate_arr, target)
        print(f"leftmost {target} in {duplicate_arr}: index {result}")
    
    # Test rightmost binary search
    print("\n3. Binary Search Rightmost:")
    for target in leftmost_targets:
        result = binary_search_rightmost(duplicate_arr, target)
        print(f"rightmost {target} in {duplicate_arr}: index {result}")
    
    # Test search in rotated array
    print("\n4. Search in Rotated Array:")
    rotated_arrays = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
        ([1, 3], 3)
    ]
    for arr, target in rotated_arrays:
        result = search_rotated_array(arr, target)
        print(f"search {target} in rotated {arr}: index {result}")
    
    # Test find peak element
    print("\n5. Find Peak Element:")
    peak_arrays = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1],
        [1, 2]
    ]
    for arr in peak_arrays:
        peak_idx = find_peak_element(arr)
        print(f"peak in {arr}: index {peak_idx} (value: {arr[peak_idx] if peak_idx != -1 else 'None'})")
    
    # Test find minimum in rotated array
    print("\n6. Find Minimum in Rotated Array:")
    min_rotated_tests = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
        [2, 1]
    ]
    for arr in min_rotated_tests:
        min_val = find_minimum_rotated_array(arr)
        print(f"minimum in rotated {arr}: {min_val}")
    
    # Test search in 2D matrix
    print("\n7. Search in 2D Matrix:")
    matrix_tests = [
        ([[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], 5),
        ([[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], 13),
        ([[1]], 1),
        ([[1]], 2)
    ]
    for matrix, target in matrix_tests:
        found = search_2d_matrix(matrix, target)
        print(f"search {target} in 2D matrix: {found}")
    
    # Test find missing number
    print("\n8. Find Missing Number:")
    missing_tests = [
        [0, 1, 3, 4, 5],  # Missing 2
        [1, 2, 3, 4, 5],  # Missing 0
        [0, 1, 2, 3, 4, 5, 6, 8],  # Missing 7
        [1]  # Missing 0
    ]
    for arr in missing_tests:
        missing = find_missing_number(arr)
        print(f"missing number in {arr}: {missing}")
    
    # Test square root
    print("\n9. Square Root using Binary Search:")
    sqrt_tests = [4, 8, 16, 25, 10, 1, 0]
    for x in sqrt_tests:
        sqrt_val = sqrt_binary_search(x)
        print(f"sqrt({x}) = {sqrt_val}")
    
    # Test k-th smallest in two arrays
    print("\n10. K-th Smallest in Two Arrays:")
    two_array_tests = [
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 1),
        ([0, 0], [0, 0], 1),
        ([1, 3, 5], [2, 4, 6], 4)
    ]
    for arr1, arr2, k in two_array_tests:
        result = find_kth_smallest_two_arrays(arr1, arr2, k)
        print(f"{k}th smallest in {arr1} and {arr2}: {result}")

if __name__ == "__main__":
    test_search_algorithms()