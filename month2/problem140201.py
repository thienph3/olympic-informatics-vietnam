"""
Day 14 - Problem 3: Bisect module applications
Thời gian: 25 phút
"""

import bisect

def grade_calculator(score, breakpoints, grades):
    """
    Calculate letter grade based on score using bisect
    Input: score - numeric score, breakpoints - sorted thresholds, grades - corresponding grades
    Output: letter grade
    """
    # TODO: Implement grade calculation using bisect
    pass

def find_closest_value(arr, target):
    """
    Tìm giá trị gần target nhất trong sorted array
    Input: arr - sorted array, target - giá trị tham chiếu
    Output: giá trị gần target nhất
    """
    # TODO: Implement using bisect
    pass

def merge_intervals_bisect(intervals, new_interval):
    """
    Merge new interval vào list intervals đã sorted
    Input: intervals - sorted list of [start, end], new_interval - [start, end]
    Output: merged intervals list
    """
    # TODO: Implement using bisect để tìm insertion points
    pass

def range_frequency_queries(arr, queries):
    """
    Trả lời queries về frequency của values trong ranges
    Input: arr - sorted array, queries - list of (value, left, right)
    Output: list frequencies của value trong range [left, right] cho mỗi query
    """
    # TODO: Implement using bisect cho efficient range queries
    pass

def maintain_median_stream():
    """
    Maintain median của stream of numbers using bisect
    Return class MedianFinder với methods addNum(num) và findMedian()
    """
    class MedianFinder:
        def __init__(self):
            # TODO: Initialize data structure
            pass
        
        def addNum(self, num):
            # TODO: Add number và maintain sorted order
            pass
        
        def findMedian(self):
            # TODO: Return median
            pass
    
    return MedianFinder()

def sliding_window_maximum_bisect(arr, k):
    """
    Tìm maximum trong mỗi sliding window size k using bisect
    Input: arr - array, k - window size
    Output: list maximums của mỗi window
    """
    # TODO: Implement using bisect để maintain sorted window
    pass

def count_smaller_after_self(nums):
    """
    Đếm số phần tử nhỏ hơn mỗi phần tử về phía bên phải
    Input: nums - array
    Output: array counts
    """
    # TODO: Implement using bisect, process từ phải sang trái
    pass

# Test cases
if __name__ == "__main__":
    # Test grade_calculator
    print("=== GRADE CALCULATOR ===")
    breakpoints = [60, 70, 80, 90]
    grades = ['F', 'D', 'C', 'B', 'A']
    
    test_scores = [45, 65, 75, 85, 95, 100]
    for score in test_scores:
        grade = grade_calculator(score, breakpoints, grades)
        print(f"Score {score}: Grade {grade}")
    
    # Test find_closest_value
    print(f"\n=== CLOSEST VALUE ===")
    arr = [1, 3, 5, 7, 9, 11]
    test_targets = [0, 2, 4, 6, 8, 12]
    
    for target in test_targets:
        closest = find_closest_value(arr, target)
        print(f"Closest to {target} trong {arr}: {closest}")
    
    # Test merge_intervals_bisect
    print(f"\n=== MERGE INTERVALS ===")
    intervals = [[1, 3], [6, 9]]
    new_intervals = [[2, 5], [15, 18], [0, 0]]
    
    for new_int in new_intervals:
        result = merge_intervals_bisect(intervals.copy(), new_int)
        print(f"Merge {new_int} vào {intervals}: {result}")
    
    # Test range_frequency_queries
    print(f"\n=== RANGE FREQUENCY QUERIES ===")
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    queries = [
        (2, 0, 5),  # Count of 2 in range [0, 5]
        (3, 2, 7),  # Count of 3 in range [2, 7]
        (4, 0, 8),  # Count of 4 in range [0, 8]
        (1, 1, 3)   # Count of 1 in range [1, 3]
    ]
    
    frequencies = range_frequency_queries(arr, queries)
    for i, (value, left, right) in enumerate(queries):
        print(f"Frequency của {value} trong range [{left}, {right}]: {frequencies[i]}")
    
    # Test maintain_median_stream
    print(f"\n=== MEDIAN STREAM ===")
    median_finder = maintain_median_stream()
    
    stream = [1, 2, 3, 4, 5]
    for num in stream:
        median_finder.addNum(num)
        median = median_finder.findMedian()
        print(f"After adding {num}, median: {median}")
    
    # Test sliding_window_maximum_bisect
    print(f"\n=== SLIDING WINDOW MAXIMUM ===")
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    maximums = sliding_window_maximum_bisect(arr, k)
    print(f"Array: {arr}")
    print(f"Window size: {k}")
    print(f"Maximums: {maximums}")  # Expected: [3, 3, 5, 5, 6, 7]
    
    # Test count_smaller_after_self
    print(f"\n=== COUNT SMALLER AFTER SELF ===")
    test_arrays = [
        [5, 2, 6, 1],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [1, 1, 1, 1]
    ]
    
    for nums in test_arrays:
        counts = count_smaller_after_self(nums)
        print(f"Array: {nums}")
        print(f"Counts: {counts}")
    
    # Performance comparison
    print(f"\n=== BISECT PERFORMANCE NOTES ===")
    print("bisect_left vs bisect_right:")
    print("  - bisect_left: leftmost insertion point")
    print("  - bisect_right: rightmost insertion point")
    print("  - Cả hai đều O(log n)")
    
    print("\\ninsort vs manual insert:")
    print("  - insort: O(n) do shifting elements")
    print("  - Tốt cho small arrays hoặc infrequent insertions")
    
    print("\\nBisect applications:")
    print("  - Sorted containers")
    print("  - Range queries")
    print("  - Percentile calculations")
    print("  - Binary search variants")