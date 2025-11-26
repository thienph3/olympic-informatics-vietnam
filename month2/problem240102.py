"""
Problem 240102: Mock test 1 - Tổng ước số, dãy tăng, ma trận xoắn ốc
Thực hành mock test với 3 bài trong 45 phút

Bài A: Tổng ước số
Bài B: Dãy con tăng dần dài nhất
Bài C: Ma trận xoắn ốc
"""

def problem_a_sum_divisors(n):
    """
    Bài A: Tính tổng các ước số của n
    Input: Số nguyên n (1 ≤ n ≤ 10^6)
    Output: Tổng các ước số của n
    
    Ví dụ: n = 12
    Ước số: 1, 2, 3, 4, 6, 12
    Tổng: 28
    """
    # TODO: Implement tính tổng ước số hiệu quả O(√n)
    pass

def problem_b_longest_increasing(arr):
    """
    Bài B: Tìm độ dài dãy con tăng dần dài nhất
    Input: Dãy n số nguyên
    Output: Độ dài dãy con tăng dần liên tiếp dài nhất
    
    Ví dụ: [1, 3, 2, 4, 5, 1, 6]
    Dãy con tăng: [2, 4, 5] hoặc [1, 6]
    Độ dài max: 3
    """
    # TODO: Implement tìm dãy con tăng dần dài nhất
    pass

def problem_c_spiral_matrix(n):
    """
    Bài C: Tạo ma trận xoắn ốc n×n
    Input: Số nguyên n
    Output: Ma trận xoắn ốc từ 1 đến n²
    
    Ví dụ: n = 3
    1 2 3
    8 9 4
    7 6 5
    """
    # TODO: Implement tạo ma trận xoắn ốc
    pass

def mock_test_1():
    """Thực hiện Mock test 1 - 45 phút"""
    print("=== MOCK TEST 1 - OLYMPIC TIN HỌC ===")
    print("Thời gian: 45 phút")
    print("Số bài: 3 bài")
    
    # Bài A
    print("\nBài A: Tổng ước số")
    print("Input: 12")
    print("Expected: 28")
    # TODO: Test bài A
    
    # Bài B
    print("\nBài B: Dãy con tăng dần")
    print("Input: [1, 3, 2, 4, 5, 1, 6]")
    print("Expected: 3")
    # TODO: Test bài B
    
    # Bài C
    print("\nBài C: Ma trận xoắn ốc")
    print("Input: 3")
    print("Expected:")
    print("1 2 3")
    print("8 9 4") 
    print("7 6 5")
    # TODO: Test bài C

def advanced_divisor_sum(n):
    """Tính tổng ước số nâng cao với tối ưu"""
    # TODO: Implement với độ phức tạp O(√n)
    pass

def longest_increasing_optimized(arr):
    """Tìm dãy con tăng dần với thuật toán tối ưu"""
    # TODO: Implement với O(n)
    pass

def spiral_matrix_directions(n):
    """Tạo ma trận xoắn ốc bằng cách sử dụng directions"""
    # TODO: Implement với 4 hướng: right, down, left, up
    pass

# Test cases
def test_mock_1():
    """Test các bài trong Mock test 1"""
    
    # Test bài A - Tổng ước số
    test_cases_a = [1, 6, 12, 28, 100]
    for n in test_cases_a:
        # TODO: Test tổng ước số
        pass
    
    # Test bài B - Dãy con tăng
    test_cases_b = [
        [1, 2, 3, 4, 5],      # Toàn bộ tăng
        [5, 4, 3, 2, 1],      # Toàn bộ giảm
        [1, 3, 2, 4, 5, 1, 6], # Hỗn hợp
        [1, 1, 1, 1]          # Bằng nhau
    ]
    for arr in test_cases_b:
        # TODO: Test dãy con tăng
        pass
    
    # Test bài C - Ma trận xoắn ốc
    test_cases_c = [1, 2, 3, 4, 5]
    for n in test_cases_c:
        # TODO: Test ma trận xoắn ốc
        pass
    
    print("Mock test 1 completed!")

if __name__ == "__main__":
    mock_test_1()
    test_mock_1()