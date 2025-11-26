"""
Problem 240302: Đề thi Olympic 2021 - Bài dễ
Thực hành với đề thi Olympic thực tế năm 2021

Bài 1: Số hoàn hảo và ước số
Bài 2: Sắp xếp theo tần suất
Bài 3: Tìm kiếm nhị phân biến thể
"""

def problem_1_perfect_numbers(n):
    """
    Bài 1: Đếm số hoàn hảo từ 1 đến n
    Số hoàn hảo là số bằng tổng các ước số thực sự của nó
    
    Input: Số nguyên n (1 ≤ n ≤ 10^6)
    Output: Số lượng số hoàn hảo từ 1 đến n
    
    Ví dụ: 6 = 1 + 2 + 3 (ước số thực sự: 1, 2, 3)
    """
    # TODO: Implement đếm số hoàn hảo
    pass

def problem_2_frequency_sort(arr):
    """
    Bài 2: Sắp xếp theo tần suất xuất hiện
    Sắp xếp mảng theo tần suất tăng dần, nếu bằng thì theo giá trị tăng dần
    
    Input: Mảng n số nguyên
    Output: Mảng đã sắp xếp theo tần suất
    
    Ví dụ: [4,6,2,2,3,4,6,8] → [8,3,2,2,4,4,6,6]
    """
    # TODO: Implement sắp xếp theo tần suất
    pass

def problem_3_binary_search_variant(arr, x):
    """
    Bài 3: Tìm số lớn nhất ≤ x trong mảng đã sắp xếp
    
    Input: Mảng đã sắp xếp và số x
    Output: Số lớn nhất trong mảng mà ≤ x, -1 nếu không có
    
    Ví dụ: [1,3,5,7,9], x=6 → 5
    """
    # TODO: Implement binary search variant
    pass

def is_perfect_number(num):
    """Kiểm tra số hoàn hảo"""
    # TODO: Implement kiểm tra số hoàn hảo
    pass

def count_perfect_numbers_optimized(n):
    """Đếm số hoàn hảo tối ưu"""
    # TODO: Implement với tối ưu hóa
    pass

def frequency_sort_stable(arr):
    """Sắp xếp theo tần suất ổn định"""
    # TODO: Implement stable frequency sort
    pass

def binary_search_floor(arr, x):
    """Binary search tìm floor value"""
    # TODO: Implement binary search floor
    pass

def olympic_2021_contest():
    """Mô phỏng đề thi Olympic 2021"""
    print("=== ĐỀ THI OLYMPIC TIN HỌC 2021 ===")
    print("Thời gian: 180 phút")
    print("Số bài: 3 bài")
    
    # Bài 1
    print("\nBài 1: Số hoàn hảo")
    print("Input: n = 30")
    print("Số hoàn hảo ≤ 30: 6, 28")
    print("Expected: 2")
    # TODO: Test số hoàn hảo
    
    # Bài 2
    print("\nBài 2: Sắp xếp tần suất")
    arr = [4, 6, 2, 2, 3, 4, 6, 8]
    print(f"Input: {arr}")
    print("Tần suất: 8(1), 3(1), 2(2), 4(2), 6(2)")
    print("Expected: [8, 3, 2, 2, 4, 4, 6, 6]")
    # TODO: Test sắp xếp tần suất
    
    # Bài 3
    print("\nBài 3: Binary search floor")
    arr = [1, 3, 5, 7, 9]
    x = 6
    print(f"Input: {arr}, x = {x}")
    print("Expected: 5")
    # TODO: Test binary search floor

def advanced_number_theory():
    """Lý thuyết số nâng cao"""
    
    def sum_of_divisors(n):
        """Tính tổng ước số hiệu quả"""
        # TODO: Implement sum of divisors O(√n)
        pass
    
    def sieve_sum_divisors(n):
        """Sàng tính tổng ước số cho nhiều số"""
        # TODO: Implement sieve for sum of divisors
        pass
    
    def euler_totient(n):
        """Hàm Euler totient φ(n)"""
        # TODO: Implement Euler's totient function
        pass

def advanced_sorting_techniques():
    """Kỹ thuật sắp xếp nâng cao"""
    
    def counting_sort_frequency(arr):
        """Counting sort cho frequency sorting"""
        # TODO: Implement counting sort variant
        pass
    
    def bucket_sort_frequency(arr):
        """Bucket sort cho frequency sorting"""
        # TODO: Implement bucket sort variant
        pass
    
    def radix_sort_frequency(arr):
        """Radix sort cho frequency sorting"""
        # TODO: Implement radix sort variant
        pass

def binary_search_variants():
    """Các biến thể binary search"""
    
    def lower_bound(arr, x):
        """Tìm vị trí đầu tiên ≥ x"""
        # TODO: Implement lower bound
        pass
    
    def upper_bound(arr, x):
        """Tìm vị trí đầu tiên > x"""
        # TODO: Implement upper bound
        pass
    
    def equal_range(arr, x):
        """Tìm range của x trong mảng"""
        # TODO: Implement equal range
        pass

# Test cases
def test_olympic_2021():
    """Test đề Olympic 2021"""
    
    # Test số hoàn hảo
    perfect_tests = [30, 100, 1000, 10000]
    expected_perfect = [2, 2, 3, 3]  # 6, 28, 496, 8128
    for n, expected in zip(perfect_tests, expected_perfect):
        # TODO: Test perfect numbers
        pass
    
    # Test sắp xếp tần suất
    frequency_tests = [
        [4, 6, 2, 2, 3, 4, 6, 8],
        [1, 1, 1, 2, 2, 3],
        [5, 5, 4, 6, 4],
        [1, 2, 3, 4, 5]
    ]
    for arr in frequency_tests:
        # TODO: Test frequency sort
        pass
    
    # Test binary search floor
    search_tests = [
        ([1, 3, 5, 7, 9], 6, 5),
        ([1, 3, 5, 7, 9], 1, 1),
        ([1, 3, 5, 7, 9], 0, -1),
        ([1, 3, 5, 7, 9], 10, 9)
    ]
    for arr, x, expected in search_tests:
        # TODO: Test binary search floor
        pass
    
    print("Olympic 2021 tests completed!")

def performance_analysis():
    """Phân tích hiệu suất các thuật toán"""
    
    def time_complexity_analysis():
        """Phân tích độ phức tạp thời gian"""
        print("Perfect numbers: O(n√n) naive, O(n log log n) optimized")
        print("Frequency sort: O(n log n)")
        print("Binary search floor: O(log n)")
    
    def space_complexity_analysis():
        """Phân tích độ phức tạp không gian"""
        print("Perfect numbers: O(1)")
        print("Frequency sort: O(n)")
        print("Binary search floor: O(1)")
    
    def optimization_tips():
        """Mẹo tối ưu hóa"""
        print("1. Sử dụng sàng cho nhiều truy vấn")
        print("2. Cache kết quả tính toán")
        print("3. Tối ưu constant factors")

if __name__ == "__main__":
    olympic_2021_contest()
    test_olympic_2021()
    performance_analysis()