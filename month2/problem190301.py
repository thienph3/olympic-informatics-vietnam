"""
Problem 190301: Heap Sort Implementations
Các implementation của heap sort và heap operations

Topics: Binary heap, heapify, heap sort, priority queue
"""

def heap_sort(arr):
    """
    Heap sort cơ bản
    Time: O(n log n), Space: O(1)
    """
    # TODO: Implement heap sort
    pass

def build_max_heap(arr):
    """
    Xây dựng max heap từ mảng
    Time: O(n), Space: O(1)
    """
    # TODO: Build max heap bottom-up
    pass

def heapify_down(arr, n, i):
    """
    Heapify từ trên xuống dưới
    Time: O(log n), Space: O(1)
    """
    # TODO: Maintain heap property downward
    pass

def heapify_up(arr, i):
    """
    Heapify từ dưới lên trên
    Time: O(log n), Space: O(1)
    """
    # TODO: Maintain heap property upward
    pass

def heap_sort_min(arr):
    """
    Heap sort sử dụng min heap (sắp xếp giảm dần)
    Time: O(n log n), Space: O(1)
    """
    # TODO: Sort in descending order using min heap
    pass

def k_largest_elements(arr, k):
    """
    Tìm k phần tử lớn nhất bằng heap
    Time: O(n log k), Space: O(k)
    """
    # TODO: Find k largest elements using min heap
    pass

def heap_sort_iterative(arr):
    """
    Heap sort iterative (không đệ quy)
    Time: O(n log n), Space: O(1)
    """
    # TODO: Implement iterative heapify
    pass

def verify_heap_property(arr, heap_type='max'):
    """
    Kiểm tra tính chất heap
    """
    # TODO: Verify if array satisfies heap property
    pass

# Test cases
def test_heap_sort():
    # Test basic heap sort
    arr1 = [12, 11, 13, 5, 6, 7]
    print("Heap sort:", heap_sort(arr1.copy()))
    
    # Test build max heap
    arr2 = [4, 10, 3, 5, 1]
    build_max_heap(arr2)
    print("Max heap:", arr2)
    
    # Test heapify operations
    heap = [10, 5, 3, 2, 4]
    heapify_up(heap, 4)  # After inserting at end
    print("After heapify up:", heap)
    
    heap2 = [1, 5, 3, 2, 4]  # Violates heap at root
    heapify_down(heap2, len(heap2), 0)
    print("After heapify down:", heap2)
    
    # Test min heap sort
    arr3 = [12, 11, 13, 5, 6, 7]
    print("Min heap sort (desc):", heap_sort_min(arr3.copy()))
    
    # Test k largest
    arr4 = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"{k} largest:", k_largest_elements(arr4, k))
    
    # Test iterative
    arr5 = [64, 34, 25, 12, 22, 11, 90]
    print("Iterative heap sort:", heap_sort_iterative(arr5.copy()))
    
    # Test heap property verification
    max_heap = [20, 15, 8, 10, 5, 7, 6, 2, 9, 1]
    print("Is max heap?", verify_heap_property(max_heap, 'max'))
    
    min_heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Is min heap?", verify_heap_property(min_heap, 'min'))

if __name__ == "__main__":
    test_heap_sort()