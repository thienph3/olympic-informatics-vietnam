"""
Day 13 - Problem 1: Linear Search cơ bản và biến thể
Thời gian: 30 phút
"""

def linear_search(arr, target):
    """
    Tìm kiếm tuyến tính cơ bản
    Input: arr - list số nguyên, target - số cần tìm
    Output: index của target, -1 nếu không tìm thấy
    """
    # TODO: Implement linear search
    pass

def linear_search_all(arr, target):
    """
    Tìm tất cả vị trí xuất hiện của target
    Input: arr - list số nguyên, target - số cần tìm
    Output: list các index chứa target
    """
    # TODO: Implement tìm tất cả vị trí
    pass

def linear_search_condition(arr, condition):
    """
    Tìm phần tử đầu tiên thỏa mãn điều kiện
    Input: arr - list số nguyên, condition - function điều kiện
    Output: index của phần tử đầu tiên thỏa mãn, -1 nếu không có
    """
    # TODO: Implement tìm kiếm với điều kiện
    pass

def search_substring(text, pattern):
    """
    Tìm vị trí đầu tiên của pattern trong text
    Input: text - string, pattern - substring cần tìm
    Output: index bắt đầu của pattern, -1 nếu không tìm thấy
    """
    # TODO: Implement tìm kiếm substring
    pass

def sentinel_search(arr, target):
    """
    Tìm kiếm với sentinel để tối ưu hóa
    Input: arr - list số nguyên (có thể modify), target - số cần tìm
    Output: index của target, -1 nếu không tìm thấy
    """
    # TODO: Implement sentinel search
    pass

# Test cases
if __name__ == "__main__":
    # Test linear_search
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Test linear_search:")
    print(f"Tìm 22 trong {arr1}: {linear_search(arr1, 22)}")  # Expected: 4
    print(f"Tìm 100 trong {arr1}: {linear_search(arr1, 100)}")  # Expected: -1
    
    # Test linear_search_all
    arr2 = [1, 3, 5, 3, 7, 3, 9]
    print(f"\nTìm tất cả vị trí của 3 trong {arr2}: {linear_search_all(arr2, 3)}")  # Expected: [1, 3, 5]
    
    # Test linear_search_condition
    arr3 = [1, 3, 5, 8, 9, 12]
    print(f"\nTìm số chẵn đầu tiên trong {arr3}: {linear_search_condition(arr3, lambda x: x % 2 == 0)}")  # Expected: 3
    
    # Test search_substring
    text = "hello world programming"
    pattern = "world"
    print(f"\nTìm '{pattern}' trong '{text}': {search_substring(text, pattern)}")  # Expected: 6
    
    # Test sentinel_search
    arr4 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nSentinel search 22 trong {arr4}: {sentinel_search(arr4.copy(), 22)}")  # Expected: 4