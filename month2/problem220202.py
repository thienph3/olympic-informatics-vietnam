"""
Problem 220202: Array Recursion
Đệ quy trong xử lý mảng

Topics: Array manipulation, searching, sorting, divide and conquer
"""

def sum_array_recursive(arr):
    """
    Tính tổng mảng bằng đệ quy
    Time: O(n), Space: O(n)
    """
    # TODO: Sum array elements recursively
    pass

def find_max_recursive(arr):
    """
    Tìm phần tử lớn nhất trong mảng
    """
    # TODO: Find maximum element recursively
    pass

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary search đệ quy
    Time: O(log n), Space: O(log n)
    """
    # TODO: Implement binary search recursively
    pass

def merge_sort_recursive(arr):
    """
    Merge sort đệ quy
    Time: O(n log n), Space: O(n)
    """
    # TODO: Implement merge sort recursively
    pass

def quick_sort_recursive(arr):
    """
    Quick sort đệ quy
    Time: O(n log n) average, Space: O(log n)
    """
    # TODO: Implement quick sort recursively
    pass

def reverse_array_recursive(arr):
    """
    Đảo ngược mảng bằng đệ quy
    """
    # TODO: Reverse array recursively
    pass

def count_occurrences_recursive(arr, target):
    """
    Đếm số lần xuất hiện của target trong mảng
    """
    # TODO: Count occurrences recursively
    pass

def is_sorted_recursive(arr):
    """
    Kiểm tra mảng đã sắp xếp chưa
    """
    # TODO: Check if array is sorted recursively
    pass

def array_to_string_recursive(arr):
    """
    Chuyển mảng thành chuỗi (không dùng join)
    """
    # TODO: Convert array to string recursively
    pass

def flatten_array_recursive(nested_arr):
    """
    Làm phẳng mảng lồng nhau
    """
    # TODO: Flatten nested array recursively
    pass

# Test cases
def test_array_recursion():
    print("Array Recursion")
    print("=" * 18)
    
    # Test sum array
    print("1. Sum Array:")
    test_arrays = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [1],
        []
    ]
    for arr in test_arrays:
        result = sum_array_recursive(arr)
        print(f"sum({arr}) = {result}")
    
    # Test find max
    print("\n2. Find Maximum:")
    max_arrays = [
        [1, 5, 3, 9, 2],
        [10, 20, 5, 30],
        [42],
        [-1, -5, -3]
    ]
    for arr in max_arrays:
        if arr:  # Skip empty array
            result = find_max_recursive(arr)
            print(f"max({arr}) = {result}")
    
    # Test binary search
    print("\n3. Binary Search:")
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    search_targets = [7, 4, 1, 15, 20]
    for target in search_targets:
        result = binary_search_recursive(sorted_arr, target)
        print(f"search {target} in {sorted_arr}: index {result}")
    
    # Test merge sort
    print("\n4. Merge Sort:")
    unsorted_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        []
    ]
    for arr in unsorted_arrays:
        sorted_arr = merge_sort_recursive(arr.copy())
        print(f"merge_sort({arr}) = {sorted_arr}")
    
    # Test quick sort
    print("\n5. Quick Sort:")
    for arr in unsorted_arrays:
        sorted_arr = quick_sort_recursive(arr.copy())
        print(f"quick_sort({arr}) = {sorted_arr}")
    
    # Test reverse array
    print("\n6. Reverse Array:")
    reverse_arrays = [[1, 2, 3, 4, 5], [10, 20], [42]]
    for arr in reverse_arrays:
        reversed_arr = reverse_array_recursive(arr.copy())
        print(f"reverse({arr}) = {reversed_arr}")
    
    # Test count occurrences
    print("\n7. Count Occurrences:")
    count_tests = [
        ([1, 2, 3, 2, 2, 4], 2),
        ([5, 5, 5, 5], 5),
        ([1, 2, 3], 4)
    ]
    for arr, target in count_tests:
        count = count_occurrences_recursive(arr, target)
        print(f"count {target} in {arr}: {count}")
    
    # Test is sorted
    print("\n8. Is Sorted Check:")
    sorted_tests = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 2, 4],
        [1, 1, 2, 2, 3]
    ]
    for arr in sorted_tests:
        is_sorted = is_sorted_recursive(arr)
        print(f"{arr} is sorted: {is_sorted}")
    
    # Test array to string
    print("\n9. Array to String:")
    string_arrays = [[1, 2, 3], ['a', 'b', 'c'], []]
    for arr in string_arrays:
        result = array_to_string_recursive(arr)
        print(f"to_string({arr}) = '{result}'")
    
    # Test flatten array
    print("\n10. Flatten Array:")
    nested_arrays = [
        [1, [2, 3], 4],
        [1, [2, [3, 4]], 5],
        [[1, 2], [3, 4]],
        [1, 2, 3]
    ]
    for arr in nested_arrays:
        flattened = flatten_array_recursive(arr)
        print(f"flatten({arr}) = {flattened}")

if __name__ == "__main__":
    test_array_recursion()