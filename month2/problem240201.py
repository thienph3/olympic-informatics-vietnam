"""
Problem 240201: Mock test 2 - Số nguyên tố, palindrome, sắp xếp
Thực hành mock test với các bài toán kinh điển

Bài A: Kiểm tra và đếm số nguyên tố
Bài B: Palindrome và xử lý chuỗi
Bài C: Sắp xếp theo nhiều tiêu chí
"""

def problem_a_prime_operations(n):
    """
    Bài A: Các phép toán với số nguyên tố
    1. Kiểm tra n có phải số nguyên tố không
    2. Đếm số nguyên tố từ 1 đến n
    3. Tìm số nguyên tố lớn nhất ≤ n
    """
    # TODO: Implement kiểm tra nguyên tố
    def is_prime(num):
        pass
    
    # TODO: Implement đếm số nguyên tố
    def count_primes(limit):
        pass
    
    # TODO: Implement tìm nguyên tố lớn nhất
    def largest_prime(limit):
        pass

def problem_b_palindrome_operations(s):
    """
    Bài B: Các phép toán với palindrome
    1. Kiểm tra chuỗi có phải palindrome không
    2. Tìm palindrome con dài nhất
    3. Đếm số palindrome con
    """
    # TODO: Implement kiểm tra palindrome
    def is_palindrome(string):
        pass
    
    # TODO: Implement tìm palindrome con dài nhất
    def longest_palindrome_substring(string):
        pass
    
    # TODO: Implement đếm palindrome con
    def count_palindrome_substrings(string):
        pass

def problem_c_multi_criteria_sort(data):
    """
    Bài C: Sắp xếp theo nhiều tiêu chí
    Input: Danh sách học sinh (tên, điểm toán, điểm lý)
    Sắp xếp theo: điểm tổng giảm dần, nếu bằng thì tên tăng dần
    """
    # TODO: Implement sắp xếp đa tiêu chí
    pass

def sieve_of_eratosthenes(n):
    """Sàng Eratosthenes tìm tất cả số nguyên tố ≤ n"""
    # TODO: Implement sàng Eratosthenes
    pass

def expand_around_center(s, left, right):
    """Mở rộng quanh tâm để tìm palindrome"""
    # TODO: Implement expand around center
    pass

def custom_sort_key(student):
    """Tạo key cho sắp xếp đa tiêu chí"""
    # TODO: Implement custom sort key
    pass

def mock_test_2():
    """Thực hiện Mock test 2"""
    print("=== MOCK TEST 2 - OLYMPIC TIN HỌC ===")
    
    # Bài A
    print("\nBài A: Số nguyên tố")
    print("Input: 20")
    print("Expected: False, 8, 19")
    # TODO: Test các phép toán nguyên tố
    
    # Bài B
    print("\nBài B: Palindrome")
    print("Input: 'racecar'")
    print("Expected: True, 'racecar', 7")
    # TODO: Test các phép toán palindrome
    
    # Bài C
    print("\nBài C: Sắp xếp học sinh")
    students = [
        ("Alice", 8, 9),
        ("Bob", 9, 8), 
        ("Charlie", 7, 10),
        ("Alice", 9, 8)
    ]
    print("Input:", students)
    print("Expected: Sắp xếp theo tổng điểm, tên")
    # TODO: Test sắp xếp đa tiêu chí

def optimization_techniques():
    """Các kỹ thuật tối ưu cho mock test"""
    
    # Tối ưu 1: Sàng nguyên tố
    def optimized_prime_check(n):
        # TODO: Implement kiểm tra nguyên tố tối ưu
        pass
    
    # Tối ưu 2: Palindrome với Manacher's algorithm
    def manacher_algorithm(s):
        # TODO: Implement Manacher's algorithm
        pass
    
    # Tối ưu 3: Sắp xếp ổn định
    def stable_multi_sort(data):
        # TODO: Implement stable sort
        pass

# Test cases
def test_mock_2():
    """Test các bài trong Mock test 2"""
    
    # Test số nguyên tố
    prime_tests = [2, 17, 25, 97, 100]
    for n in prime_tests:
        # TODO: Test prime operations
        pass
    
    # Test palindrome
    palindrome_tests = ["racecar", "hello", "abcba", "a", ""]
    for s in palindrome_tests:
        # TODO: Test palindrome operations
        pass
    
    # Test sắp xếp
    student_data = [
        [("Alice", 8, 9), ("Bob", 9, 8)],
        [("Charlie", 10, 10), ("David", 9, 9), ("Eve", 10, 10)],
        [("X", 5, 5), ("Y", 6, 4), ("Z", 4, 6)]
    ]
    for data in student_data:
        # TODO: Test multi-criteria sort
        pass
    
    print("Mock test 2 completed!")

if __name__ == "__main__":
    mock_test_2()
    test_mock_2()