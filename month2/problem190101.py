"""
Problem 190101: Merge Sort Implementations
Các implementation khác nhau của merge sort

Topics: Divide and conquer, merge operation, stable sorting
"""

def merge_sort_basic(arr):
    """
    Merge sort cơ bản (tạo mảng mới)
    Time: O(n log n), Space: O(n)
    """
    # TODO: Implement basic merge sort
    pass

def merge_sort_inplace(arr):
    """
    Merge sort in-place (modify original array)
    Time: O(n log n), Space: O(n) for temporary arrays
    """
    # TODO: Implement in-place merge sort
    pass

def merge_arrays(left, right):
    """
    Merge hai mảng đã sắp xếp
    Time: O(n + m), Space: O(n + m)
    """
    # TODO: Merge two sorted arrays
    pass

def merge_sort_iterative(arr):
    """
    Merge sort iterative (bottom-up)
    Time: O(n log n), Space: O(n)
    """
    # TODO: Implement iterative merge sort
    pass

def merge_sort_3way(arr):
    """
    3-way merge sort (chia thành 3 phần)
    Time: O(n log₃ n), Space: O(n)
    """
    # TODO: Implement 3-way merge sort
    pass

def merge_sort_optimized(arr):
    """
    Merge sort với optimizations
    - Insertion sort cho mảng nhỏ
    - Kiểm tra đã sắp xếp
    """
    # TODO: Add optimizations to merge sort
    pass

def external_merge_sort(chunks):
    """
    External merge sort cho dữ liệu lớn
    chunks: list of sorted arrays
    """
    # TODO: Merge multiple sorted chunks
    pass

def merge_k_sorted_arrays(arrays):
    """
    Merge k mảng đã sắp xếp
    Time: O(n log k), Space: O(k)
    """
    # TODO: Merge k sorted arrays using heap
    pass

# Test cases
def test_merge_sort():
    # Test basic
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Basic merge sort:", merge_sort_basic(arr1.copy()))
    
    # Test in-place
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    merge_sort_inplace(arr2)
    print("In-place merge sort:", arr2)
    
    # Test merge arrays
    left = [1, 3, 5, 7]
    right = [2, 4, 6, 8]
    print("Merge arrays:", merge_arrays(left, right))
    
    # Test iterative
    arr3 = [38, 27, 43, 3, 9, 82, 10]
    print("Iterative merge sort:", merge_sort_iterative(arr3.copy()))
    
    # Test 3-way
    arr4 = [45, 23, 11, 89, 77, 98, 4, 28, 65, 43]
    print("3-way merge sort:", merge_sort_3way(arr4.copy()))
    
    # Test optimized
    arr5 = [5, 2, 4, 6, 1, 3]
    print("Optimized merge sort:", merge_sort_optimized(arr5.copy()))
    
    # Test external merge
    chunks = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("External merge:", external_merge_sort(chunks))
    
    # Test k arrays
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Merge k arrays:", merge_k_sorted_arrays(arrays))

if __name__ == "__main__":
    test_merge_sort()