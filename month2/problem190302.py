"""
Problem 190302: Heap Operations và Applications
Ứng dụng heap trong các bài toán thực tế

Topics: Priority queue, heap applications, streaming algorithms
"""

class PriorityQueue:
    """
    Priority Queue implementation using heap
    """
    def __init__(self, max_heap=True):
        # TODO: Initialize priority queue
        pass
    
    def push(self, item, priority):
        # TODO: Add item with priority
        pass
    
    def pop(self):
        # TODO: Remove and return highest priority item
        pass
    
    def peek(self):
        # TODO: Return highest priority item without removing
        pass
    
    def is_empty(self):
        # TODO: Check if queue is empty
        pass

def merge_k_sorted_lists(lists):
    """
    Merge k sorted lists sử dụng heap
    Time: O(n log k), Space: O(k)
    """
    # TODO: Merge k sorted lists using min heap
    pass

def find_median_stream():
    """
    Tìm median trong stream of numbers
    Sử dụng 2 heaps: max heap cho nửa nhỏ, min heap cho nửa lớn
    """
    # TODO: Implement median finder using two heaps
    pass

def top_k_frequent_words(words, k):
    """
    Tìm k từ xuất hiện nhiều nhất
    Time: O(n log k), Space: O(n)
    """
    # TODO: Find top k frequent words using heap
    pass

def sliding_window_median(arr, k):
    """
    Tìm median trong sliding window
    Time: O(n log k), Space: O(k)
    """
    # TODO: Find median in sliding window using heaps
    pass

def heap_based_dijkstra_simulation(graph, start):
    """
    Mô phỏng Dijkstra algorithm sử dụng heap
    """
    # TODO: Simulate shortest path using priority queue
    pass

def kth_largest_in_stream():
    """
    Tìm k-th largest element trong stream
    """
    # TODO: Maintain k-th largest using min heap
    pass

def meeting_rooms_scheduler(meetings):
    """
    Sắp xếp phòng họp tối ưu sử dụng heap
    meetings: list of (start, end) tuples
    """
    # TODO: Schedule meetings optimally using heap
    pass

# Test cases
def test_heap_applications():
    # Test priority queue
    pq = PriorityQueue()
    tasks = [("task1", 3), ("task2", 1), ("task3", 2)]
    for task, priority in tasks:
        pq.push(task, priority)
    
    print("Priority queue:")
    while not pq.is_empty():
        print(pq.pop())
    
    # Test merge k sorted lists
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Merged lists:", merge_k_sorted_lists(lists))
    
    # Test median stream
    median_finder = find_median_stream()
    numbers = [1, 2, 3, 4, 5]
    medians = []
    for num in numbers:
        median_finder.add_number(num)
        medians.append(median_finder.find_median())
    print("Stream medians:", medians)
    
    # Test top k frequent words
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print("Top 2 frequent words:", top_k_frequent_words(words, 2))
    
    # Test sliding window median
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    print("Sliding window medians:", sliding_window_median(arr, 3))
    
    # Test Dijkstra simulation
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    print("Shortest paths from A:", heap_based_dijkstra_simulation(graph, 'A'))
    
    # Test kth largest stream
    kth_finder = kth_largest_in_stream()
    stream = [4, 5, 8, 2, 3, 9, 1]
    k = 3
    results = []
    for num in stream:
        kth_finder.add(num)
        results.append(kth_finder.kth_largest(k))
    print(f"{k}rd largest in stream:", results)
    
    # Test meeting scheduler
    meetings = [(0, 30), (5, 10), (15, 20)]
    print("Meeting rooms needed:", meeting_rooms_scheduler(meetings))

if __name__ == "__main__":
    test_heap_applications()