"""
Problem 210101: Performance Measurement Tools
Các công cụ đo lường hiệu suất thuật toán

Topics: Timing, benchmarking, performance comparison
"""

import time
import timeit
from functools import wraps

def simple_timer(func):
    """
    Decorator đơn giản để đo thời gian
    """
    # TODO: Implement simple timing decorator
    pass

def precise_timer(func):
    """
    Timer chính xác sử dụng perf_counter
    """
    # TODO: Use time.perf_counter() for precise timing
    pass

def benchmark_function(func, *args, iterations=1000):
    """
    Benchmark function với số lần lặp lại
    """
    # TODO: Use timeit.timeit for accurate benchmarking
    pass

def compare_algorithms(algorithms, test_data):
    """
    So sánh hiệu suất của nhiều thuật toán
    algorithms: dict of {name: function}
    """
    # TODO: Compare multiple algorithms and return results
    pass

def measure_with_different_inputs(func, input_generator, sizes):
    """
    Đo hiệu suất với các kích thước input khác nhau
    """
    # TODO: Measure performance across different input sizes
    pass

def statistical_analysis(measurements):
    """
    Phân tích thống kê các measurements
    """
    # TODO: Calculate mean, median, std deviation, min, max
    pass

def performance_regression_test(func, baseline_time, tolerance=0.1):
    """
    Test regression - kiểm tra performance có bị giảm không
    """
    # TODO: Check if current performance is within tolerance of baseline
    pass

def warmup_and_measure(func, *args, warmup_runs=10, measure_runs=100):
    """
    Warmup trước khi đo để tránh cold start effects
    """
    # TODO: Run warmup iterations then measure performance
    pass

# Test cases
def test_performance_measurement():
    # Sample algorithms to test
    def linear_search(arr, target):
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    def binary_search(arr, target):
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
    
    # Test data
    sorted_data = list(range(10000))
    target = 7500
    
    print("Performance Measurement Tools Test")
    print("=" * 40)
    
    # Test simple timer
    print("1. Simple Timer:")
    timed_linear = simple_timer(linear_search)
    result1 = timed_linear(sorted_data, target)
    
    # Test precise timer
    print("\n2. Precise Timer:")
    timed_binary = precise_timer(binary_search)
    result2 = timed_binary(sorted_data, target)
    
    # Test benchmark function
    print("\n3. Benchmark Function:")
    linear_time = benchmark_function(linear_search, sorted_data, target)
    binary_time = benchmark_function(binary_search, sorted_data, target)
    print(f"Linear search: {linear_time:.6f}s")
    print(f"Binary search: {binary_time:.6f}s")
    
    # Test algorithm comparison
    print("\n4. Algorithm Comparison:")
    algorithms = {
        'linear_search': linear_search,
        'binary_search': binary_search
    }
    comparison_results = compare_algorithms(algorithms, (sorted_data, target))
    print(comparison_results)
    
    # Test different input sizes
    print("\n5. Different Input Sizes:")
    def generate_sorted_array(size):
        return list(range(size)), size // 2
    
    sizes = [1000, 5000, 10000, 20000]
    size_results = measure_with_different_inputs(
        lambda data: binary_search(data[0], data[1]),
        generate_sorted_array,
        sizes
    )
    print(size_results)
    
    # Test statistical analysis
    print("\n6. Statistical Analysis:")
    sample_measurements = [0.001, 0.0012, 0.0009, 0.0011, 0.001, 0.0013, 0.0008]
    stats = statistical_analysis(sample_measurements)
    print(stats)
    
    # Test regression
    print("\n7. Performance Regression Test:")
    baseline = 0.001
    current_time = benchmark_function(binary_search, sorted_data, target, 100)
    regression_result = performance_regression_test(
        lambda: binary_search(sorted_data, target),
        baseline
    )
    print(f"Regression test: {regression_result}")
    
    # Test warmup
    print("\n8. Warmup and Measure:")
    warmed_time = warmup_and_measure(binary_search, sorted_data, target)
    print(f"Warmed up time: {warmed_time}")

if __name__ == "__main__":
    test_performance_measurement()