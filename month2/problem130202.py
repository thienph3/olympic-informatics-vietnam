"""
Day 13 - Problem 4: Binary Search applications
Thời gian: 25 phút
"""

def sqrt_binary_search(x):
    """
    Tìm căn bậc hai nguyên của x bằng binary search
    Input: x - số nguyên không âm
    Output: căn bậc hai nguyên lớn nhất của x
    """
    # TODO: Implement sqrt using binary search
    pass

def search_in_rotated_array(arr, target):
    """
    Tìm kiếm trong mảng sắp xếp bị xoay
    Input: arr - rotated sorted array, target - số cần tìm
    Output: index của target, -1 nếu không tìm thấy
    """
    # TODO: Implement search in rotated sorted array
    pass

def find_minimum_in_rotated_array(arr):
    """
    Tìm phần tử nhỏ nhất trong mảng sắp xếp bị xoay
    Input: arr - rotated sorted array
    Output: giá trị nhỏ nhất
    """
    # TODO: Implement find minimum in rotated array
    pass

def search_2d_matrix(matrix, target):
    """
    Tìm kiếm trong ma trận 2D được sắp xếp
    Input: matrix - 2D list sorted row-wise và column-wise, target - số cần tìm
    Output: True nếu tìm thấy, False nếu không
    """
    # TODO: Implement search in 2D matrix
    pass

def find_peak_element_binary(arr):
    """
    Tìm peak element bằng binary search
    Input: arr - list số nguyên
    Output: index của một peak element
    """
    # TODO: Implement find peak using binary search
    pass

def find_kth_smallest(arr1, arr2, k):
    """
    Tìm phần tử thứ k nhỏ nhất trong 2 mảng sắp xếp
    Input: arr1, arr2 - sorted arrays, k - vị trí cần tìm (1-indexed)
    Output: phần tử thứ k nhỏ nhất
    """
    # TODO: Implement find kth smallest using binary search
    pass

def capacity_to_ship_packages(weights, D):
    """
    Tìm capacity tối thiểu để ship tất cả packages trong D ngày
    Input: weights - list trọng lượng packages, D - số ngày
    Output: capacity tối thiểu
    """
    # TODO: Implement using binary search on answer
    pass

# Test cases
if __name__ == "__main__":
    # Test sqrt_binary_search
    print("Test sqrt_binary_search:")
    print(f"sqrt(4) = {sqrt_binary_search(4)}")  # Expected: 2
    print(f"sqrt(8) = {sqrt_binary_search(8)}")  # Expected: 2
    print(f"sqrt(16) = {sqrt_binary_search(16)}")  # Expected: 4
    
    # Test search_in_rotated_array
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    print(f"\nTìm 0 trong rotated array {arr1}: {search_in_rotated_array(arr1, 0)}")  # Expected: 4
    print(f"Tìm 3 trong rotated array {arr1}: {search_in_rotated_array(arr1, 3)}")  # Expected: -1
    
    # Test find_minimum_in_rotated_array
    arr2 = [3, 4, 5, 1, 2]
    print(f"\nMinimum trong rotated array {arr2}: {find_minimum_in_rotated_array(arr2)}")  # Expected: 1
    
    # Test search_2d_matrix
    matrix = [
        [1,  4,  7,  11],
        [2,  5,  8,  12],
        [3,  6,  9,  16]
    ]
    print(f"\nTìm 5 trong matrix: {search_2d_matrix(matrix, 5)}")  # Expected: True
    print(f"Tìm 13 trong matrix: {search_2d_matrix(matrix, 13)}")  # Expected: False
    
    # Test find_peak_element_binary
    arr3 = [1, 2, 3, 1]
    print(f"\nPeak element trong {arr3}: {find_peak_element_binary(arr3)}")  # Expected: 2
    
    # Test find_kth_smallest
    arr4 = [1, 3, 5]
    arr5 = [2, 4, 6]
    k = 4
    print(f"\nPhần tử thứ {k} nhỏ nhất trong {arr4} và {arr5}: {find_kth_smallest(arr4, arr5, k)}")  # Expected: 4
    
    # Test capacity_to_ship_packages
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D = 5
    print(f"\nCapacity tối thiểu để ship {weights} trong {D} ngày: {capacity_to_ship_packages(weights, D)}")  # Expected: 15