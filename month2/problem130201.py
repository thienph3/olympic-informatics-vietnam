"""
Day 13 - Problem 3: Binary Search implementations
Thời gian: 25 phút
"""

def binary_search_iterative(arr, target):
    """
    Binary search iterative implementation
    Input: arr - sorted list, target - số cần tìm
    Output: index của target, -1 nếu không tìm thấy
    """
    # TODO: Implement binary search iterative
    pass

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary search recursive implementation
    Input: arr - sorted list, target - số cần tìm, left/right - boundaries
    Output: index của target, -1 nếu không tìm thấy
    """
    # TODO: Implement binary search recursive
    pass

def search_insert_position(arr, target):
    """
    Tìm vị trí để chèn target vào mảng sắp xếp
    Input: arr - sorted list, target - số cần chèn
    Output: index để chèn target
    """
    # TODO: Implement search insert position
    pass

def find_first_occurrence(arr, target):
    """
    Tìm vị trí đầu tiên của target trong sorted array
    Input: arr - sorted list (có thể có duplicate), target - số cần tìm
    Output: index đầu tiên của target, -1 nếu không có
    """
    # TODO: Implement find first occurrence
    pass

def find_last_occurrence(arr, target):
    """
    Tìm vị trí cuối cùng của target trong sorted array
    Input: arr - sorted list (có thể có duplicate), target - số cần tìm
    Output: index cuối cùng của target, -1 nếu không có
    """
    # TODO: Implement find last occurrence
    pass

def find_range(arr, target):
    """
    Tìm range [first, last] của target
    Input: arr - sorted list, target - số cần tìm
    Output: [first_index, last_index], [-1, -1] nếu không có
    """
    # TODO: Implement find range using first and last occurrence
    pass

def count_occurrences(arr, target):
    """
    Đếm số lần xuất hiện của target trong sorted array
    Input: arr - sorted list, target - số cần đếm
    Output: số lần xuất hiện
    """
    # TODO: Implement count occurrences using range
    pass

# Test cases
if __name__ == "__main__":
    # Test binary_search_iterative
    arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Test binary_search_iterative:")
    print(f"Tìm 7 trong {arr1}: {binary_search_iterative(arr1, 7)}")  # Expected: 3
    print(f"Tìm 20 trong {arr1}: {binary_search_iterative(arr1, 20)}")  # Expected: -1
    
    # Test binary_search_recursive
    print(f"\nTìm 7 (recursive): {binary_search_recursive(arr1, 7)}")  # Expected: 3
    
    # Test search_insert_position
    arr2 = [1, 3, 5, 6]
    print(f"\nVị trí chèn 5 trong {arr2}: {search_insert_position(arr2, 5)}")  # Expected: 2
    print(f"Vị trí chèn 2 trong {arr2}: {search_insert_position(arr2, 2)}")  # Expected: 1
    print(f"Vị trí chèn 7 trong {arr2}: {search_insert_position(arr2, 7)}")  # Expected: 4
    
    # Test find_first_occurrence và find_last_occurrence
    arr3 = [5, 7, 7, 8, 8, 8, 10]
    target = 8
    print(f"\nFirst occurrence của {target} trong {arr3}: {find_first_occurrence(arr3, target)}")  # Expected: 3
    print(f"Last occurrence của {target} trong {arr3}: {find_last_occurrence(arr3, target)}")  # Expected: 5
    
    # Test find_range
    print(f"Range của {target} trong {arr3}: {find_range(arr3, target)}")  # Expected: [3, 5]
    
    # Test count_occurrences
    print(f"Số lần xuất hiện của {target}: {count_occurrences(arr3, target)}")  # Expected: 3