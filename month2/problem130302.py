"""
Day 13 - Problem 6: Algorithm selection
Thời gian: 30 phút
"""

def choose_search_algorithm(data_size, is_sorted, search_frequency, memory_constraint=False):
    """
    Chọn thuật toán tìm kiếm phù hợp
    Input: 
        data_size - kích thước dữ liệu
        is_sorted - dữ liệu đã sắp xếp chưa
        search_frequency - tần suất tìm kiếm ('low', 'medium', 'high')
        memory_constraint - có giới hạn memory không
    Output: tuple (algorithm_name, reason)
    """
    # TODO: Implement algorithm selection logic
    pass

def estimate_performance(algorithm, data_size, search_count):
    """
    Ước tính hiệu suất của thuật toán
    Input:
        algorithm - tên thuật toán ('linear', 'binary')
        data_size - kích thước dữ liệu
        search_count - số lần tìm kiếm
    Output: dictionary với estimated operations và time
    """
    # TODO: Implement performance estimation
    pass

def sorting_cost_analysis(data_size, search_count):
    """
    Phân tích chi phí sắp xếp vs lợi ích binary search
    Input: data_size - kích thước dữ liệu, search_count - số lần tìm kiếm
    Output: dictionary với cost analysis
    """
    # TODO: Implement sorting cost analysis
    # Sorting cost: O(n log n)
    # Linear search cost: O(n) per search
    # Binary search cost: O(log n) per search
    pass

def recommend_data_structure(use_case):
    """
    Recommend data structure dựa trên use case
    Input: use_case - dictionary mô tả use case
    Output: recommendation string
    """
    # TODO: Implement data structure recommendation
    # Consider: list, set, dict, sorted list, etc.
    pass

def benchmark_scenario(scenario):
    """
    Benchmark một scenario cụ thể
    Input: scenario - dictionary mô tả scenario
    Output: benchmark results
    """
    # TODO: Implement scenario benchmarking
    pass

# Test scenarios
def create_test_scenarios():
    """Tạo các test scenarios"""
    scenarios = [
        {
            'name': 'Small dataset, infrequent search',
            'data_size': 100,
            'is_sorted': False,
            'search_frequency': 'low',
            'search_count': 5,
            'memory_constraint': False
        },
        {
            'name': 'Large dataset, frequent search',
            'data_size': 1000000,
            'is_sorted': False,
            'search_frequency': 'high',
            'search_count': 10000,
            'memory_constraint': False
        },
        {
            'name': 'Medium dataset, already sorted',
            'data_size': 10000,
            'is_sorted': True,
            'search_frequency': 'medium',
            'search_count': 1000,
            'memory_constraint': False
        },
        {
            'name': 'Large dataset, memory constrained',
            'data_size': 500000,
            'is_sorted': False,
            'search_frequency': 'high',
            'search_count': 5000,
            'memory_constraint': True
        },
        {
            'name': 'Real-time system, low latency required',
            'data_size': 1000,
            'is_sorted': True,
            'search_frequency': 'high',
            'search_count': 100000,
            'memory_constraint': False
        }
    ]
    return scenarios

def analyze_use_cases():
    """Phân tích các use cases thực tế"""
    use_cases = [
        {
            'name': 'Phone book lookup',
            'characteristics': 'Large, sorted, frequent lookups',
            'data_size': 1000000,
            'is_sorted': True,
            'search_frequency': 'high'
        },
        {
            'name': 'Student grade lookup',
            'characteristics': 'Medium, unsorted, occasional lookups',
            'data_size': 1000,
            'is_sorted': False,
            'search_frequency': 'low'
        },
        {
            'name': 'Dictionary word check',
            'characteristics': 'Large, sorted, very frequent',
            'data_size': 500000,
            'is_sorted': True,
            'search_frequency': 'high'
        },
        {
            'name': 'Log file analysis',
            'characteristics': 'Very large, unsorted, batch processing',
            'data_size': 10000000,
            'is_sorted': False,
            'search_frequency': 'medium'
        }
    ]
    
    print("=== USE CASE ANALYSIS ===\n")
    for use_case in use_cases:
        print(f"Use Case: {use_case['name']}")
        print(f"Characteristics: {use_case['characteristics']}")
        
        # Get recommendation
        algorithm, reason = choose_search_algorithm(
            use_case['data_size'],
            use_case['is_sorted'],
            use_case['search_frequency']
        )
        
        print(f"Recommended: {algorithm}")
        print(f"Reason: {reason}")
        print("-" * 50)

# Test cases
if __name__ == "__main__":
    print("=== ALGORITHM SELECTION ANALYSIS ===\n")
    
    # Test choose_search_algorithm
    scenarios = create_test_scenarios()
    
    for scenario in scenarios:
        print(f"Scenario: {scenario['name']}")
        print(f"  Data size: {scenario['data_size']:,}")
        print(f"  Is sorted: {scenario['is_sorted']}")
        print(f"  Search frequency: {scenario['search_frequency']}")
        print(f"  Search count: {scenario['search_count']:,}")
        print(f"  Memory constraint: {scenario['memory_constraint']}")
        
        # Get recommendation
        algorithm, reason = choose_search_algorithm(
            scenario['data_size'],
            scenario['is_sorted'],
            scenario['search_frequency'],
            scenario['memory_constraint']
        )
        
        print(f"  Recommendation: {algorithm}")
        print(f"  Reason: {reason}")
        
        # Estimate performance
        linear_perf = estimate_performance('linear', scenario['data_size'], scenario['search_count'])
        binary_perf = estimate_performance('binary', scenario['data_size'], scenario['search_count'])
        
        print(f"  Linear search estimate: {linear_perf}")
        print(f"  Binary search estimate: {binary_perf}")
        
        # Sorting cost analysis
        if not scenario['is_sorted']:
            cost_analysis = sorting_cost_analysis(scenario['data_size'], scenario['search_count'])
            print(f"  Sorting cost analysis: {cost_analysis}")
        
        print("-" * 60)
    
    # Analyze real-world use cases
    analyze_use_cases()
    
    # Data structure recommendations
    print("\n=== DATA STRUCTURE RECOMMENDATIONS ===\n")
    
    use_case_examples = [
        {
            'name': 'Membership testing',
            'operations': ['search'],
            'data_type': 'unique_values',
            'size': 'large'
        },
        {
            'name': 'Key-value lookup',
            'operations': ['search', 'insert', 'delete'],
            'data_type': 'key_value_pairs',
            'size': 'medium'
        },
        {
            'name': 'Range queries',
            'operations': ['range_search', 'min', 'max'],
            'data_type': 'numeric',
            'size': 'large'
        }
    ]
    
    for use_case in use_case_examples:
        recommendation = recommend_data_structure(use_case)
        print(f"Use case: {use_case['name']}")
        print(f"Recommendation: {recommendation}")
        print("-" * 40)