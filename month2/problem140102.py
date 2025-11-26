"""
Day 14 - Problem 2: Custom binary search variants
Thời gian: 30 phút
"""

def binary_search_custom_comparator(arr, target, key_func=None, reverse=False):
    """
    Binary search với custom key function và reverse order
    Input: arr - sorted array, target, key_func - transform function, reverse - sort order
    Output: index của target hoặc -1
    """
    # TODO: Implement binary search với custom comparator
    pass

def binary_search_float(func, target, left, right, epsilon=1e-9):
    """
    Binary search trên floating point với function
    Input: func - monotonic function, target - target value, left/right - bounds, epsilon - precision
    Output: x sao cho func(x) ≈ target
    """
    # TODO: Implement floating point binary search
    pass

def binary_search_rotated_duplicates(arr, target):
    """
    Binary search trong rotated sorted array có duplicates
    Input: arr - rotated sorted array với duplicates, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement search in rotated array với duplicates
    pass

def find_nth_root_binary(x, n, precision=1e-6):
    """
    Tìm căn bậc n của x bằng binary search
    Input: x - số, n - bậc căn, precision - độ chính xác
    Output: căn bậc n của x
    """
    # TODO: Implement nth root using binary search
    pass

def binary_search_2d_coordinates(points, target_x, target_y):
    """
    Binary search trong array of 2D points sorted by x, then by y
    Input: points - list of (x, y) tuples sorted, target_x, target_y
    Output: index của point (target_x, target_y) hoặc -1
    """
    # TODO: Implement 2D binary search
    pass

def find_transition_point(arr):
    """
    Tìm điểm chuyển từ 0 sang 1 trong binary array
    Input: arr - binary array (0s followed by 1s)
    Output: index của 1 đầu tiên, -1 nếu không có 1
    """
    # TODO: Implement transition point finding
    pass

def search_in_bitonic_array(arr, target):
    """
    Tìm kiếm trong bitonic array (tăng rồi giảm)
    Input: arr - bitonic array, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement bitonic array search
    pass

# Test cases
if __name__ == "__main__":
    # Test binary_search_custom_comparator
    print("=== CUSTOM COMPARATOR TESTS ===")
    
    # Test với tuples sorted by second element
    students = [("Alice", 78), ("Bob", 85), ("Charlie", 90), ("David", 95)]
    target_grade = 85
    result = binary_search_custom_comparator(students, target_grade, key_func=lambda x: x[1])
    print(f"Student với grade {target_grade}: {students[result] if result != -1 else 'Not found'}")
    
    # Test với reverse order
    arr_desc = [10, 8, 6, 4, 2]
    target = 6
    result = binary_search_custom_comparator(arr_desc, target, reverse=True)
    print(f"Tìm {target} trong descending array: {result}")  # Expected: 2
    
    # Test binary_search_float
    print(f"\n=== FLOATING POINT TESTS ===")
    
    # Tìm căn bậc hai của 2
    def square(x):
        return x * x
    
    sqrt_2 = binary_search_float(square, 2, 0, 2)
    print(f"Căn bậc hai của 2: {sqrt_2:.6f}")  # Expected: ~1.414214
    
    # Tìm nghiệm của x^3 - 5 = 0
    def cubic_minus_5(x):
        return x**3 - 5
    
    cube_root_5 = binary_search_float(cubic_minus_5, 0, 0, 3)
    print(f"Căn bậc ba của 5: {cube_root_5:.6f}")  # Expected: ~1.709976
    
    # Test binary_search_rotated_duplicates
    print(f"\n=== ROTATED ARRAY WITH DUPLICATES ===")
    arr_rot_dup = [2, 2, 2, 3, 4, 2]
    target = 3
    result = binary_search_rotated_duplicates(arr_rot_dup, target)
    print(f"Tìm {target} trong rotated array với duplicates: {result}")  # Expected: 3
    
    arr_rot_dup2 = [1, 1, 1, 1, 1, 1, 1, 1]
    target2 = 1
    result = binary_search_rotated_duplicates(arr_rot_dup2, target2)
    print(f"Tìm {target2} trong all duplicates: {result}")  # Expected: any valid index
    
    # Test find_nth_root_binary
    print(f"\n=== NTH ROOT TESTS ===")
    test_cases = [(8, 3), (16, 4), (32, 5), (27, 3)]
    for x, n in test_cases:
        root = find_nth_root_binary(x, n)
        print(f"Căn bậc {n} của {x}: {root:.6f}")
    
    # Test binary_search_2d_coordinates
    print(f"\n=== 2D COORDINATES SEARCH ===")
    points = [(1, 2), (1, 5), (2, 3), (3, 1), (3, 4), (4, 2)]
    target_point = (3, 1)
    result = binary_search_2d_coordinates(points, target_point[0], target_point[1])
    print(f"Tìm point {target_point}: {result}")  # Expected: 3
    
    # Test find_transition_point
    print(f"\n=== TRANSITION POINT TESTS ===")
    binary_arrays = [
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 1],
        [1]
    ]
    
    for arr in binary_arrays:
        transition = find_transition_point(arr)
        print(f"Transition point trong {arr}: {transition}")
    
    # Test search_in_bitonic_array
    print(f"\n=== BITONIC ARRAY SEARCH ===")
    bitonic_arr = [1, 3, 8, 12, 4, 2]
    targets = [12, 3, 2, 5]
    
    for target in targets:
        result = search_in_bitonic_array(bitonic_arr, target)
        print(f"Tìm {target} trong bitonic array: {result}")
    
    print(f"\n=== PERFORMANCE NOTES ===")
    print("Custom comparator: Thêm overhead nhưng flexible")
    print("Floating point: Cần cẩn thận với precision và convergence")
    print("Rotated duplicates: Worst case O(n), average O(log n)")
    print("2D search: O(log n) nếu sorted properly")
    print("Bitonic search: O(log n) với 2 binary searches")