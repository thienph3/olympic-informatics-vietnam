"""
Day 13 - Problem 2: Ứng dụng Linear Search trong Olympic
Thời gian: 30 phút
"""

def find_missing_number(arr, n):
    """
    Tìm số bị thiếu trong dãy từ 1 đến n
    Input: arr - list n-1 số từ 1 đến n (thiếu 1 số), n - số lớn nhất
    Output: số bị thiếu
    """
    # TODO: Sử dụng linear search để tìm số thiếu
    pass

def find_peak_element_linear(arr):
    """
    Tìm peak element (phần tử lớn hơn các phần tử kề bên)
    Input: arr - list số nguyên
    Output: index của một peak element
    """
    # TODO: Tìm peak element bằng linear search
    pass

def find_majority_element(arr):
    """
    Tìm phần tử xuất hiện nhiều hơn n/2 lần
    Input: arr - list số nguyên
    Output: phần tử majority, None nếu không có
    """
    # TODO: Tìm majority element
    pass

def find_equilibrium_point(arr):
    """
    Tìm điểm cân bằng (tổng bên trái = tổng bên phải)
    Input: arr - list số nguyên
    Output: index của equilibrium point, -1 nếu không có
    """
    # TODO: Tìm equilibrium point
    pass

def find_leaders(arr):
    """
    Tìm tất cả leaders (phần tử lớn hơn tất cả phần tử bên phải)
    Input: arr - list số nguyên
    Output: list các leaders theo thứ tự xuất hiện
    """
    # TODO: Tìm tất cả leaders
    pass

def count_inversions(arr):
    """
    Đếm số cặp nghịch thế (i < j nhưng arr[i] > arr[j])
    Input: arr - list số nguyên
    Output: số lượng inversions
    """
    # TODO: Đếm inversions bằng nested loops
    pass

# Test cases
if __name__ == "__main__":
    # Test find_missing_number
    arr1 = [1, 2, 4, 5, 6]
    n1 = 6
    print(f"Số thiếu trong {arr1}: {find_missing_number(arr1, n1)}")  # Expected: 3
    
    # Test find_peak_element_linear
    arr2 = [1, 3, 20, 4, 1, 0]
    print(f"Peak element trong {arr2}: {find_peak_element_linear(arr2)}")  # Expected: 2 (index của 20)
    
    # Test find_majority_element
    arr3 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print(f"Majority element trong {arr3}: {find_majority_element(arr3)}")  # Expected: 4
    
    # Test find_equilibrium_point
    arr4 = [1, 3, 5, 2, 2]
    print(f"Equilibrium point trong {arr4}: {find_equilibrium_point(arr4)}")  # Expected: 2 (index của 5)
    
    # Test find_leaders
    arr5 = [16, 17, 4, 3, 5, 2]
    print(f"Leaders trong {arr5}: {find_leaders(arr5)}")  # Expected: [17, 5, 2]
    
    # Test count_inversions
    arr6 = [2, 4, 1, 3, 5]
    print(f"Số inversions trong {arr6}: {count_inversions(arr6)}")  # Expected: 3