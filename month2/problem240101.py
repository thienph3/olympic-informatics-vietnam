"""
Problem 240101: Giải đề Olympic mẫu - 3 bài cơ bản
Thực hành giải đề Olympic với format chuẩn

Bài 1: Tìm số lớn nhất và vị trí
Bài 2: Đếm số chẵn lẻ  
Bài 3: Sắp xếp theo yêu cầu
"""

def problem1_max_element():
    """
    Bài 1: Tìm số lớn nhất và vị trí của nó
    Input: n, sau đó n số nguyên
    Output: Số lớn nhất và vị trí (bắt đầu từ 1)
    """
    # TODO: Implement tìm số lớn nhất
    pass

def problem2_count_even_odd():
    """
    Bài 2: Đếm số lượng số chẵn và lẻ
    Input: n, sau đó n số nguyên
    Output: Số lượng số chẵn và số lẻ
    """
    # TODO: Implement đếm chẵn lẻ
    pass

def problem3_sort_even_odd():
    """
    Bài 3: Sắp xếp số chẵn trước, số lẻ sau
    Input: n, sau đó n số nguyên
    Output: Dãy đã sắp xếp (chẵn tăng dần, lẻ tăng dần)
    """
    # TODO: Implement sắp xếp theo yêu cầu
    pass

def solve_olympic_basic():
    """Giải bộ đề Olympic cơ bản"""
    print("=== ĐỀ THI OLYMPIC TIN HỌC CƠ BẢN ===")
    
    # Bài 1
    print("\nBài 1: Tìm số lớn nhất")
    print("Input: 5")
    print("       3 7 2 9 1")
    print("Expected: 9 4")
    # TODO: Gọi problem1_max_element()
    
    # Bài 2  
    print("\nBài 2: Đếm số chẵn lẻ")
    print("Input: 6")
    print("       2 3 4 5 6 7")
    print("Expected: 3 3")
    # TODO: Gọi problem2_count_even_odd()
    
    # Bài 3
    print("\nBài 3: Sắp xếp chẵn lẻ")
    print("Input: 6")
    print("       5 2 8 3 1 6")
    print("Expected: 2 6 8 1 3 5")
    # TODO: Gọi problem3_sort_even_odd()

# Test cases
def test_olympic_problems():
    """Test các bài Olympic cơ bản"""
    
    # Test bài 1
    test_data1 = [3, 7, 2, 9, 1]
    # TODO: Test tìm max
    
    # Test bài 2
    test_data2 = [2, 3, 4, 5, 6, 7]
    # TODO: Test đếm chẵn lẻ
    
    # Test bài 3
    test_data3 = [5, 2, 8, 3, 1, 6]
    # TODO: Test sắp xếp
    
    print("All Olympic basic tests completed!")

if __name__ == "__main__":
    solve_olympic_basic()
    test_olympic_problems()