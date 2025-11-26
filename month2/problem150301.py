"""
Day 15 - Problem 5: Interpolation search implementations
Thời gian: 30 phút
"""

def interpolation_search(arr, target):
    """
    Interpolation search - tốt cho uniformly distributed data
    Input: arr - sorted array với uniform distribution, target - giá trị cần tìm
    Output: index của target hoặc -1
    Time complexity: O(log log n) average, O(n) worst case
    """
    # TODO: Implement interpolation search
    pass

def interpolation_search_improved(arr, target):
    """
    Improved interpolation search với better bounds checking
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement improved version với safety checks
    pass

def adaptive_interpolation_search(arr, target, max_interpolation_steps=10):
    """
    Adaptive interpolation search - fallback to binary khi cần
    Input: arr - sorted array, target, max_interpolation_steps - threshold
    Output: index của target hoặc -1
    """
    # TODO: Implement adaptive search
    pass

def interpolation_search_with_distribution_check(arr, target):
    """
    Interpolation search với distribution checking
    Input: arr - sorted array, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    def is_uniformly_distributed(arr, left, right, sample_size=10):
        """Check if data is approximately uniformly distributed"""
        # TODO: Implement distribution checking
        pass
    
    # TODO: Implement search với distribution awareness
    pass

def interpolation_search_first_occurrence(arr, target):
    """
    Tìm first occurrence bằng interpolation search
    Input: arr - sorted array có duplicates, target - giá trị cần tìm
    Output: index đầu tiên của target, -1 nếu không có
    """
    # TODO: Implement first occurrence với interpolation
    pass

def interpolation_search_range(arr, target):
    """
    Tìm range [first, last] bằng interpolation search
    Input: arr - sorted array, target - giá trị cần tìm
    Output: [first_index, last_index], [-1, -1] nếu không có
    """
    # TODO: Implement range finding với interpolation
    pass

def compare_search_algorithms_on_distributions(arr, target):
    """
    So sánh các search algorithms trên different distributions
    Input: arr - sorted array, target - giá trị cần tìm
    Output: dictionary với performance results
    """
    import time
    
    def binary_search(arr, target):
        # TODO: Implement binary search
        pass
    
    def linear_search(arr, target):
        # TODO: Implement linear search
        pass
    
    algorithms = {
        'linear': linear_search,
        'binary': binary_search,
        'interpolation': interpolation_search,
        'interpolation_improved': interpolation_search_improved,
        'adaptive_interpolation': adaptive_interpolation_search
    }
    
    results = {}
    
    for name, func in algorithms.items():
        try:
            start = time.time()
            result = func(arr, target)
            end = time.time()
            
            results[name] = {
                'result': result,
                'time': end - start,
                'found': result != -1
            }
        except Exception as e:
            results[name] = {
                'result': -1,
                'time': float('inf'),
                'found': False,
                'error': str(e)
            }
    
    return results

def analyze_data_distribution(arr):
    """
    Phân tích distribution của data
    Input: arr - sorted array
    Output: dictionary với distribution metrics
    """
    # TODO: Implement distribution analysis
    pass

# Test cases
if __name__ == "__main__":
    # Test với uniform distributed data
    print("=== UNIFORM DISTRIBUTED DATA ===")
    
    uniform_arr = list(range(0, 1000, 10))  # [0, 10, 20, ..., 990]
    targets = [0, 100, 500, 990, 1000]
    
    print(f"Array: uniform steps of 10, size {len(uniform_arr)}")
    
    for target in targets:
        result = interpolation_search(uniform_arr, target)
        print(f"Interpolation search tìm {target}: {result}")
    
    # Test với non-uniform data
    print(f"\n=== NON-UNIFORM DATA ===")
    
    non_uniform_arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    targets = [1, 32, 256, 1024, 500]
    
    print(f"Array: powers of 2, size {len(non_uniform_arr)}")
    
    for target in targets:
        result = interpolation_search(non_uniform_arr, target)
        improved_result = interpolation_search_improved(non_uniform_arr, target)
        adaptive_result = adaptive_interpolation_search(non_uniform_arr, target)
        
        print(f"Target {target}:")
        print(f"  Basic: {result}")
        print(f"  Improved: {improved_result}")
        print(f"  Adaptive: {adaptive_result}")
    
    # Test distribution checking
    print(f"\n=== DISTRIBUTION CHECKING ===")
    
    test_arrays = [
        (list(range(0, 100, 5)), "Uniform"),
        ([i*i for i in range(20)], "Quadratic"),
        ([2**i for i in range(15)], "Exponential"),
        ([1]*10 + list(range(10, 50)) + [50]*10, "Mixed")
    ]
    
    for arr, description in test_arrays:
        distribution_metrics = analyze_data_distribution(arr)
        print(f"{description} array: {distribution_metrics}")
        
        # Test search với distribution awareness
        target = arr[len(arr)//2] if arr else 0
        result = interpolation_search_with_distribution_check(arr, target)
        print(f"  Search result for middle element: {result}")
    
    # Test first occurrence và range
    print(f"\n=== FIRST OCCURRENCE & RANGE ===")
    
    arr_with_dups = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    targets = [2, 4, 5, 7]
    
    for target in targets:
        first_idx = interpolation_search_first_occurrence(arr_with_dups, target)
        range_result = interpolation_search_range(arr_with_dups, target)
        
        print(f"Target {target}:")
        print(f"  First occurrence: {first_idx}")
        print(f"  Range: {range_result}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    # Test với different distributions
    distributions = [
        (list(range(10000)), "Linear uniform"),
        ([i*i for i in range(100)], "Quadratic"),
        ([int(1000 * (i/100)**2) for i in range(100)], "Quadratic scaled"),
        (list(range(0, 10000, 7)), "Linear with step")
    ]
    
    for arr, description in distributions:
        if not arr:
            continue
            
        target = arr[len(arr)//4]  # Target near beginning
        
        print(f"\\n{description} (size: {len(arr)}):")
        results = compare_search_algorithms_on_distributions(arr, target)
        
        print(f"{'Algorithm':<20} {'Time(s)':<12} {'Result':<8} {'Found':<8}")
        print("-" * 50)
        
        for name, data in results.items():
            if 'error' not in data:
                print(f"{name:<20} {data['time']:<12.8f} {data['result']:<8} {data['found']:<8}")
            else:
                print(f"{name:<20} ERROR: {data['error']}")
    
    # Edge cases
    print(f"\n=== EDGE CASES ===")
    
    edge_cases = [
        ([], 5, "Empty array"),
        ([1], 1, "Single element - found"),
        ([1], 2, "Single element - not found"),
        ([1, 1, 1], 1, "All same elements"),
        ([1, 2], 1, "Two elements - first"),
        ([1, 2], 2, "Two elements - second")
    ]
    
    for arr, target, description in edge_cases:
        result = interpolation_search(arr, target)
        improved_result = interpolation_search_improved(arr, target)
        
        print(f"{description}:")
        print(f"  Basic: {result}")
        print(f"  Improved: {improved_result}")
    
    # Large scale performance test
    print(f"\n=== LARGE SCALE PERFORMANCE ===")
    
    import time
    
    # Create large uniform array
    large_uniform = list(range(0, 1000000, 100))
    target = 500000
    
    # Test interpolation search
    start = time.time()
    result = interpolation_search(large_uniform, target)
    interpolation_time = time.time() - start
    
    # Test binary search for comparison
    def binary_search_large(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    start = time.time()
    binary_result = binary_search_large(large_uniform, target)
    binary_time = time.time() - start
    
    print(f"Large uniform array (size: {len(large_uniform)}):")
    print(f"  Interpolation: {interpolation_time:.8f}s, result: {result}")
    print(f"  Binary: {binary_time:.8f}s, result: {binary_result}")
    
    if binary_time > 0:
        speedup = binary_time / interpolation_time
        print(f"  Speedup: {speedup:.2f}x")
    
    print(f"\n=== INTERPOLATION SEARCH SUMMARY ===")
    print("Time Complexity:")
    print("  - Best case: O(1)")
    print("  - Average case (uniform): O(log log n)")
    print("  - Worst case (skewed): O(n)")
    
    print("\\nSpace Complexity:")
    print("  - O(1)")
    
    print("\\nBest Use Cases:")
    print("  - Uniformly distributed data")
    print("  - Large datasets với predictable patterns")
    print("  - Numerical data với linear relationships")
    
    print("\\nWorst Use Cases:")
    print("  - Highly skewed distributions")
    print("  - Small datasets")
    print("  - Data với irregular patterns")
    
    print("\\nKey Insights:")
    print("  - Performance heavily depends on data distribution")
    print("  - Adaptive approaches can mitigate worst-case behavior")
    print("  - Distribution analysis is crucial for algorithm selection")
    print("  - Fallback to binary search provides safety net")