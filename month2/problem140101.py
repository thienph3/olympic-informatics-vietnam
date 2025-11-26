"""
Day 14 - Problem 1: Lower/Upper bound implementations
Thời gian: 30 phút
"""

def lower_bound(arr, target):
    """
    Tìm vị trí đầu tiên >= target (leftmost insertion point)
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index đầu tiên có arr[i] >= target
    """
    # TODO: Implement lower_bound
    pass

def upper_bound(arr, target):
    """
    Tìm vị trí đầu tiên > target (rightmost insertion point)
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index đầu tiên có arr[i] > target
    """
    # TODO: Implement upper_bound
    pass

def equal_range(arr, target):
    """
    Tìm range [first, last) của target
    Input: arr - sorted array, target - giá trị cần tìm
    Output: tuple (first_pos, last_pos) where arr[first:last] chứa tất cả target
    """
    # TODO: Implement equal_range using lower_bound và upper_bound
    pass

def count_occurrences_bounds(arr, target):
    """
    Đếm số lần xuất hiện của target sử dụng bounds
    Input: arr - sorted array, target - giá trị cần đếm
    Output: số lần xuất hiện
    """
    # TODO: Implement count using bounds
    pass

def find_closest_elements(arr, target, k):
    """
    Tìm k phần tử gần target nhất trong sorted array
    Input: arr - sorted array, target - giá trị tham chiếu, k - số phần tử
    Output: list k phần tử gần target nhất
    """
    # TODO: Implement using bounds để tìm starting position
    pass

def range_sum_query(arr, queries):
    """
    Trả lời multiple range sum queries trên sorted array
    Input: arr - sorted array, queries - list of (left_val, right_val)
    Output: list tổng các phần tử trong mỗi range [left_val, right_val]
    """
    # TODO: Implement using prefix sum và bounds
    pass

def insert_and_get_rank(arr, value):
    """
    Insert value vào sorted array và trả về rank (0-indexed)
    Input: arr - sorted array (sẽ được modify), value - giá trị insert
    Output: rank của value sau khi insert
    """
    # TODO: Implement using lower_bound
    pass

# Test cases
if __name__ == "__main__":
    # Test lower_bound và upper_bound
    arr1 = [1, 2, 2, 2, 3, 4, 4, 5]
    target = 2
    print("Test lower_bound và upper_bound:")
    print(f"Array: {arr1}")
    print(f"Lower bound của {target}: {lower_bound(arr1, target)}")  # Expected: 1
    print(f"Upper bound của {target}: {upper_bound(arr1, target)}")  # Expected: 4
    
    target2 = 0
    print(f"Lower bound của {target2}: {lower_bound(arr1, target2)}")  # Expected: 0
    print(f"Upper bound của {target2}: {upper_bound(arr1, target2)}")  # Expected: 0
    
    target3 = 6
    print(f"Lower bound của {target3}: {lower_bound(arr1, target3)}")  # Expected: 8
    print(f"Upper bound của {target3}: {upper_bound(arr1, target3)}")  # Expected: 8
    
    # Test equal_range
    print(f"\nEqual range của {target}: {equal_range(arr1, target)}")  # Expected: (1, 4)
    
    # Test count_occurrences_bounds
    print(f"Count của {target}: {count_occurrences_bounds(arr1, target)}")  # Expected: 3
    
    # Test find_closest_elements
    arr2 = [1, 2, 3, 4, 5]
    target = 3.6
    k = 3
    closest = find_closest_elements(arr2, target, k)
    print(f"\n{k} phần tử gần {target} nhất trong {arr2}: {closest}")  # Expected: [3, 4, 2] hoặc similar
    
    # Test range_sum_query
    arr3 = [1, 3, 5, 7, 9, 11]
    queries = [(3, 7), (1, 5), (8, 12)]
    results = range_sum_query(arr3, queries)
    print(f"\nRange sum queries trên {arr3}:")
    for i, (left, right) in enumerate(queries):
        print(f"  Sum in range [{left}, {right}]: {results[i]}")
    
    # Test insert_and_get_rank
    arr4 = [1, 3, 5, 7, 9]
    value = 4
    print(f"\nBefore insert: {arr4}")
    rank = insert_and_get_rank(arr4, value)
    print(f"After inserting {value}: {arr4}")
    print(f"Rank của {value}: {rank}")  # Expected: 2
    
    # Edge cases
    print(f"\n=== EDGE CASES ===")
    empty_arr = []
    print(f"Lower bound trong empty array: {lower_bound(empty_arr, 5)}")  # Expected: 0
    
    single_arr = [5]
    print(f"Lower bound của 3 trong [5]: {lower_bound(single_arr, 3)}")  # Expected: 0
    print(f"Lower bound của 5 trong [5]: {lower_bound(single_arr, 5)}")  # Expected: 0
    print(f"Lower bound của 7 trong [5]: {lower_bound(single_arr, 7)}")  # Expected: 1