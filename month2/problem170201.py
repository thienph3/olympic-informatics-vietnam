"""
Problem 170201: Radix Sort Implementations
Các implementation khác nhau của radix sort

Topics: LSD radix sort, MSD radix sort, string sorting
"""

def radix_sort_lsd(arr):
    """
    LSD (Least Significant Digit) Radix Sort
    Time: O(d * (n + k)), Space: O(n + k)
    """
    # TODO: Implement LSD radix sort
    pass

def radix_sort_msd(arr):
    """
    MSD (Most Significant Digit) Radix Sort
    Time: O(d * (n + k)), Space: O(n + k)
    """
    # TODO: Implement MSD radix sort
    pass

def radix_sort_negative(arr):
    """
    Radix sort cho số âm và dương
    Time: O(d * (n + k)), Space: O(n + k)
    """
    # TODO: Handle negative numbers
    pass

def radix_sort_strings(arr):
    """
    Radix sort cho chuỗi ký tự
    Time: O(d * (n + k)), Space: O(n + k)
    """
    # TODO: Sort strings using radix sort
    pass

def radix_sort_base(arr, base=10):
    """
    Radix sort với base tùy chỉnh
    Time: O(d * (n + base)), Space: O(n + base)
    """
    # TODO: Use custom base
    pass

def counting_sort_digit(arr, exp, base=10):
    """
    Counting sort theo chữ số cụ thể
    Helper function cho radix sort
    """
    # TODO: Sort by specific digit position
    pass

def get_max_digits(arr):
    """
    Tìm số chữ số tối đa trong mảng
    Time: O(n), Space: O(1)
    """
    # TODO: Find maximum number of digits
    pass

def radix_sort_inplace(arr):
    """
    Radix sort in-place (modify original array)
    Time: O(d * (n + k)), Space: O(k)
    """
    # TODO: Implement in-place version
    pass

# Test cases
def test_radix_sort():
    # Test LSD
    arr1 = [170, 45, 75, 90, 2, 802, 24, 66]
    print("LSD:", radix_sort_lsd(arr1.copy()))
    
    # Test MSD
    arr2 = [170, 45, 75, 90, 2, 802, 24, 66]
    print("MSD:", radix_sort_msd(arr2.copy()))
    
    # Test negative
    arr3 = [-170, 45, -75, 90, -2, 802]
    print("Negative:", radix_sort_negative(arr3.copy()))
    
    # Test strings
    strings = ["abc", "def", "aaa", "xyz", "bcd"]
    print("Strings:", radix_sort_strings(strings.copy()))
    
    # Test custom base
    arr4 = [15, 8, 23, 42, 7]  # Base 16
    print("Base 16:", radix_sort_base(arr4.copy(), 16))
    
    # Test max digits
    arr5 = [1, 12, 123, 1234]
    print("Max digits:", get_max_digits(arr5))
    
    # Test in-place
    arr6 = [64, 34, 25, 12, 22, 11, 90]
    radix_sort_inplace(arr6)
    print("In-place:", arr6)

if __name__ == "__main__":
    test_radix_sort()