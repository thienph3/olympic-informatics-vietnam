"""
Problem 180301: Interval Sorting và Merging
Sắp xếp và gộp các khoảng thời gian

Topics: Interval problems, merging overlapping intervals, scheduling
"""

def sort_intervals(intervals):
    """
    Sắp xếp intervals theo start time, sau đó end time
    intervals: list of (start, end) tuples
    """
    # TODO: Sort intervals by start then end
    pass

def merge_overlapping_intervals(intervals):
    """
    Gộp các intervals chồng lấp
    """
    # TODO: Merge overlapping intervals
    pass

def find_free_time_slots(busy_intervals, total_duration):
    """
    Tìm các khoảng thời gian rảnh
    """
    # TODO: Find free time slots between busy intervals
    pass

def schedule_meetings(meetings, room_capacity):
    """
    Sắp xếp lịch họp tối ưu
    meetings: list of (start, end, attendees)
    """
    # TODO: Schedule meetings optimally
    pass

def interval_intersection(intervals1, intervals2):
    """
    Tìm giao của hai tập intervals
    """
    # TODO: Find intersection of two interval sets
    pass

def remove_covered_intervals(intervals):
    """
    Loại bỏ intervals bị bao phủ hoàn toàn
    """
    # TODO: Remove intervals that are completely covered
    pass

def sort_by_interval_length(intervals):
    """
    Sắp xếp intervals theo độ dài
    """
    # TODO: Sort by interval length
    pass

def find_maximum_overlapping_point(intervals):
    """
    Tìm điểm có nhiều intervals chồng lấp nhất
    """
    # TODO: Find point with maximum overlap
    pass

# Test cases
def test_interval_sorting():
    # Test basic sorting
    intervals = [(3, 6), (1, 4), (2, 8), (5, 7)]
    print("Sorted intervals:", sort_intervals(intervals))
    
    # Test merging
    overlapping = [(1, 3), (2, 6), (8, 10), (15, 18)]
    print("Merged intervals:", merge_overlapping_intervals(overlapping))
    
    # Test free time
    busy = [(9, 10), (12, 13), (16, 18)]
    total = (8, 20)  # 8 AM to 8 PM
    print("Free time slots:", find_free_time_slots(busy, total))
    
    # Test meeting scheduling
    meetings = [
        (9, 10, 5),   # 9-10 AM, 5 people
        (9, 11, 3),   # 9-11 AM, 3 people
        (10, 12, 4),  # 10-12 PM, 4 people
        (11, 13, 2)   # 11-1 PM, 2 people
    ]
    print("Scheduled meetings:", schedule_meetings(meetings, 10))
    
    # Test intersection
    set1 = [(1, 3), (5, 8), (10, 12)]
    set2 = [(2, 4), (6, 7), (11, 15)]
    print("Intersection:", interval_intersection(set1, set2))
    
    # Test remove covered
    covered = [(1, 4), (2, 3), (5, 8), (6, 7), (9, 12)]
    print("After removing covered:", remove_covered_intervals(covered))
    
    # Test sort by length
    by_length = [(1, 5), (2, 3), (4, 10), (7, 8)]
    print("Sorted by length:", sort_by_interval_length(by_length))
    
    # Test maximum overlap
    overlap_test = [(1, 4), (2, 6), (3, 5), (7, 9)]
    print("Max overlapping point:", find_maximum_overlapping_point(overlap_test))

if __name__ == "__main__":
    test_interval_sorting()