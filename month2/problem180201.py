"""
Problem 180201: Custom Comparators và Key Functions
Sử dụng custom comparators và key functions cho sắp xếp

Topics: Key functions, lambda expressions, custom comparison logic
"""

def sort_by_length(strings):
    """
    Sắp xếp chuỗi theo độ dài
    """
    # TODO: Sort strings by length
    pass

def sort_by_absolute_value(numbers):
    """
    Sắp xếp số theo giá trị tuyệt đối
    """
    # TODO: Sort by absolute value
    pass

def sort_by_last_character(strings):
    """
    Sắp xếp chuỗi theo ký tự cuối
    """
    # TODO: Sort by last character
    pass

def sort_by_digit_sum(numbers):
    """
    Sắp xếp số theo tổng các chữ số
    """
    # TODO: Sort by sum of digits
    pass

def sort_by_word_count(sentences):
    """
    Sắp xếp câu theo số từ
    """
    # TODO: Sort sentences by word count
    pass

def sort_by_distance_from_point(points, target):
    """
    Sắp xếp điểm theo khoảng cách từ điểm target
    """
    # TODO: Sort points by distance from target
    pass

def sort_by_custom_priority(items, priority_dict):
    """
    Sắp xếp theo độ ưu tiên tùy chỉnh
    """
    # TODO: Sort using custom priority mapping
    pass

def sort_case_insensitive(strings):
    """
    Sắp xếp chuỗi không phân biệt hoa thường
    """
    # TODO: Case-insensitive string sorting
    pass

# Test cases
def test_custom_comparators():
    # Test length sorting
    words = ["apple", "pie", "banana", "cat", "elephant"]
    print("By length:", sort_by_length(words))
    
    # Test absolute value
    numbers = [-5, 2, -8, 1, -3, 7]
    print("By absolute:", sort_by_absolute_value(numbers))
    
    # Test last character
    strings = ["hello", "world", "python", "code"]
    print("By last char:", sort_by_last_character(strings))
    
    # Test digit sum
    nums = [123, 45, 789, 12, 999]
    print("By digit sum:", sort_by_digit_sum(nums))
    
    # Test word count
    sentences = [
        "Hello world",
        "This is a test",
        "Python",
        "Programming is fun and exciting"
    ]
    print("By word count:", sort_by_word_count(sentences))
    
    # Test distance
    points = [(1, 2), (3, 4), (0, 0), (5, 1)]
    target = (2, 2)
    print(f"By distance from {target}:", sort_by_distance_from_point(points, target))
    
    # Test custom priority
    tasks = ["urgent", "normal", "low", "critical", "normal"]
    priority = {"critical": 1, "urgent": 2, "normal": 3, "low": 4}
    print("By priority:", sort_by_custom_priority(tasks, priority))
    
    # Test case insensitive
    mixed_case = ["Apple", "banana", "Cherry", "date"]
    print("Case insensitive:", sort_case_insensitive(mixed_case))

if __name__ == "__main__":
    test_custom_comparators()