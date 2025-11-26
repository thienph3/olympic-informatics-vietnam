"""
Problem 170101: Counting Sort Implementations
Các implementation khác nhau của counting sort

Topics: Counting sort, frequency counting, stable sorting
"""

def counting_sort_basic(arr):
    """
    Counting sort cơ bản
    Time: O(n + k), Space: O(k)
    """
    # TODO: Implement basic counting sort
    pass

def counting_sort_stable(arr):
    """
    Counting sort stable (giữ thứ tự tương đối)
    Time: O(n + k), Space: O(n + k)
    """
    # TODO: Implement stable counting sort
    pass

def counting_sort_negative(arr):
    """
    Counting sort cho số âm
    Time: O(n + k), Space: O(k)
    """
    # TODO: Handle negative numbers
    pass

def counting_sort_inplace(arr):
    """
    Counting sort in-place (modify original array)
    Time: O(n + k), Space: O(k)
    """
    # TODO: Implement in-place version
    pass

def counting_sort_range(arr, min_val, max_val):
    """
    Counting sort với phạm vi cho trước
    Time: O(n + k), Space: O(k)
    """
    # TODO: Use given range
    pass

def counting_sort_objects(arr, key_func):
    """
    Counting sort cho objects với key function
    Time: O(n + k), Space: O(n + k)
    """
    # TODO: Sort objects by key
    pass

# Test cases
def test_counting_sort():
    # Test basic
    arr1 = [4, 2, 2, 8, 3, 3, 1]
    print("Basic:", counting_sort_basic(arr1.copy()))
    
    # Test stable
    arr2 = [(4, 'a'), (2, 'b'), (2, 'c'), (1, 'd')]
    print("Stable:", counting_sort_stable(arr2.copy()))
    
    # Test negative
    arr3 = [-5, -1, 0, 3, -2, 1]
    print("Negative:", counting_sort_negative(arr3.copy()))
    
    # Test in-place
    arr4 = [3, 1, 4, 1, 5, 9, 2, 6]
    counting_sort_inplace(arr4)
    print("In-place:", arr4)
    
    # Test range
    arr5 = [15, 12, 18, 11, 19]
    print("Range:", counting_sort_range(arr5, 10, 20))

if __name__ == "__main__":
    test_counting_sort()