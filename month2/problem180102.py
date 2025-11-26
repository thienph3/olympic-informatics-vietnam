"""
Problem 180102: Stable vs Unstable Comparison
So sánh thuật toán stable và unstable

Topics: Stability analysis, algorithm comparison, practical implications
"""

def demonstrate_stability_difference():
    """
    Minh họa sự khác biệt giữa stable và unstable sorting
    """
    # TODO: Show difference with duplicate values
    pass

def stable_vs_unstable_performance():
    """
    So sánh hiệu suất giữa stable và unstable algorithms
    """
    # TODO: Compare performance metrics
    pass

def when_stability_matters():
    """
    Các trường hợp stability quan trọng
    """
    # TODO: Show practical examples where stability is crucial
    pass

def multi_level_sorting_stable():
    """
    Sắp xếp nhiều cấp với stable sorting
    """
    # TODO: Sort by multiple criteria using stability
    pass

def multi_level_sorting_unstable():
    """
    Sắp xếp nhiều cấp với unstable sorting
    """
    # TODO: Show problems with unstable multi-level sorting
    pass

def preserve_original_order():
    """
    Giữ nguyên thứ tự ban đầu khi có giá trị bằng nhau
    """
    # TODO: Demonstrate order preservation
    pass

def database_like_sorting():
    """
    Sắp xếp giống như database (ORDER BY multiple columns)
    """
    # TODO: Simulate database sorting behavior
    pass

def fix_unstable_algorithm():
    """
    Sửa thuật toán unstable để trở thành stable
    """
    # TODO: Add techniques to make unstable algorithms stable
    pass

# Test cases
def test_stability_comparison():
    # Test data - employees with same salary
    employees = [
        ('Alice', 50000, 'Engineering'),
        ('Bob', 60000, 'Marketing'),
        ('Charlie', 50000, 'Engineering'),
        ('David', 60000, 'Sales'),
        ('Eve', 50000, 'Marketing')
    ]
    
    print("Original order:", employees)
    
    # Demonstrate stability
    print("\nStability demonstration:")
    demonstrate_stability_difference()
    
    # Performance comparison
    print("\nPerformance comparison:")
    stable_vs_unstable_performance()
    
    # When stability matters
    print("\nWhen stability matters:")
    when_stability_matters()
    
    # Multi-level sorting
    print("\nMulti-level sorting (stable):")
    result_stable = multi_level_sorting_stable()
    print(result_stable)
    
    print("\nMulti-level sorting (unstable):")
    result_unstable = multi_level_sorting_unstable()
    print(result_unstable)
    
    # Database-like sorting
    print("\nDatabase-like sorting:")
    db_result = database_like_sorting()
    print(db_result)

if __name__ == "__main__":
    test_stability_comparison()