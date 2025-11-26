"""
Day 13 - Problem 7: Olympic search problems
Thời gian: 30 phút
"""

def two_sum_sorted(arr, target):
    """
    Tìm cặp số trong mảng sắp xếp có tổng = target
    Input: arr - sorted array, target - tổng cần tìm
    Output: [index1, index2] hoặc [-1, -1] nếu không có
    """
    # TODO: Implement two sum using two pointers
    pass

def three_sum_closest(arr, target):
    """
    Tìm 3 số có tổng gần target nhất
    Input: arr - list số nguyên, target - target sum
    Output: tổng gần nhất
    """
    # TODO: Implement three sum closest
    pass

def search_range_in_sorted(arr, target):
    """
    Tìm range của target trong sorted array
    Input: arr - sorted array, target - số cần tìm
    Output: [start_index, end_index] hoặc [-1, -1]
    """
    # TODO: Implement search range
    pass

def find_duplicate_number(arr):
    """
    Tìm số duplicate trong array [1,n+1] có n+1 phần tử
    Input: arr - array chứa số từ 1 đến n, có 1 số duplicate
    Output: số bị duplicate
    """
    # TODO: Implement using binary search (Floyd's algorithm cũng được)
    pass

def search_in_infinite_array(arr, target):
    """
    Tìm kiếm trong mảng vô hạn (không biết kích thước)
    Input: arr - infinite sorted array, target - số cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement search in infinite array
    # Hint: Tìm bound trước, sau đó binary search
    pass

def find_kth_missing_positive(arr, k):
    """
    Tìm số dương thứ k bị thiếu trong sorted array
    Input: arr - sorted array số dương, k - thứ tự số thiếu
    Output: số dương thứ k bị thiếu
    """
    # TODO: Implement using binary search
    pass

def median_of_two_sorted_arrays(arr1, arr2):
    """
    Tìm median của 2 sorted arrays
    Input: arr1, arr2 - sorted arrays
    Output: median value
    """
    # TODO: Implement using binary search
    pass

def find_minimum_in_rotated_sorted_array_with_duplicates(arr):
    """
    Tìm minimum trong rotated sorted array có duplicates
    Input: arr - rotated sorted array với duplicates
    Output: giá trị minimum
    """
    # TODO: Implement với xử lý duplicates
    pass

# Test cases
if __name__ == "__main__":
    print("=== OLYMPIC SEARCH PROBLEMS ===\n")
    
    # Test two_sum_sorted
    arr1 = [2, 7, 11, 15]
    target1 = 9
    result = two_sum_sorted(arr1, target1)
    print(f"Two sum trong {arr1} với target {target1}: {result}")  # Expected: [0, 1]
    
    # Test three_sum_closest
    arr2 = [-1, 2, 1, -4]
    target2 = 1
    result = three_sum_closest(arr2, target2)
    print(f"Three sum closest trong {arr2} với target {target2}: {result}")  # Expected: 2
    
    # Test search_range_in_sorted
    arr3 = [5, 7, 7, 8, 8, 8, 10]
    target3 = 8
    result = search_range_in_sorted(arr3, target3)
    print(f"Range của {target3} trong {arr3}: {result}")  # Expected: [3, 5]
    
    # Test find_duplicate_number
    arr4 = [1, 3, 4, 2, 2]
    result = find_duplicate_number(arr4)
    print(f"Duplicate number trong {arr4}: {result}")  # Expected: 2
    
    # Test search_in_infinite_array (simulate với large array)
    arr5 = list(range(1, 1000000, 2))  # [1, 3, 5, 7, ...]
    target5 = 999
    result = search_in_infinite_array(arr5, target5)
    print(f"Tìm {target5} trong infinite array: {result}")  # Expected: 499
    
    # Test find_kth_missing_positive
    arr6 = [2, 3, 4, 7, 11]
    k = 5
    result = find_kth_missing_positive(arr6, k)
    print(f"Số dương thứ {k} bị thiếu trong {arr6}: {result}")  # Expected: 9
    
    # Test median_of_two_sorted_arrays
    arr7 = [1, 3]
    arr8 = [2]
    result = median_of_two_sorted_arrays(arr7, arr8)
    print(f"Median của {arr7} và {arr8}: {result}")  # Expected: 2.0
    
    arr9 = [1, 2]
    arr10 = [3, 4]
    result = median_of_two_sorted_arrays(arr9, arr10)
    print(f"Median của {arr9} và {arr10}: {result}")  # Expected: 2.5
    
    # Test find_minimum_in_rotated_sorted_array_with_duplicates
    arr11 = [2, 2, 2, 0, 1]
    result = find_minimum_in_rotated_sorted_array_with_duplicates(arr11)
    print(f"Minimum trong rotated array với duplicates {arr11}: {result}")  # Expected: 0
    
    print("\n=== PERFORMANCE NOTES ===")
    print("Two Sum: O(n) với two pointers")
    print("Three Sum Closest: O(n²) với sorting + two pointers")
    print("Search Range: O(log n) với binary search")
    print("Find Duplicate: O(log n) với binary search hoặc O(n) với Floyd's")
    print("Infinite Array: O(log n) với exponential search + binary search")
    print("Kth Missing: O(log n) với binary search")
    print("Median Two Arrays: O(log(min(m,n))) với binary search")
    print("Min Rotated Duplicates: O(n) worst case, O(log n) average")