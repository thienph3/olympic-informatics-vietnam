"""
Problem 200102: Time Complexity Measurement
Đo lường thời gian thực thi và xác minh độ phức tạp lý thuyết

Topics: Empirical analysis, performance measurement, complexity verification
"""

import time
import random

def measure_execution_time(func, *args):
    """
    Đo thời gian thực thi của function
    """
    # TODO: Measure execution time accurately
    pass

def generate_test_data(size, data_type='random'):
    """
    Tạo test data với kích thước khác nhau
    """
    # TODO: Generate different types of test data
    pass

def linear_algorithm(arr):
    """
    Thuật toán O(n) - tìm max
    """
    # TODO: Implement O(n) algorithm
    pass

def quadratic_algorithm(arr):
    """
    Thuật toán O(n²) - bubble sort
    """
    # TODO: Implement O(n²) algorithm
    pass

def logarithmic_algorithm(arr, target):
    """
    Thuật toán O(log n) - binary search
    """
    # TODO: Implement O(log n) algorithm
    pass

def nlogn_algorithm(arr):
    """
    Thuật toán O(n log n) - merge sort
    """
    # TODO: Implement O(n log n) algorithm
    pass

def exponential_algorithm(n):
    """
    Thuật toán O(2ⁿ) - fibonacci naive
    """
    # TODO: Implement O(2ⁿ) algorithm (careful with large n!)
    pass

def complexity_growth_analysis():
    """
    Phân tích growth rate của các thuật toán
    """
    # TODO: Test algorithms with increasing input sizes
    pass

def verify_theoretical_complexity():
    """
    Xác minh độ phức tạp lý thuyết bằng thực nghiệm
    """
    # TODO: Compare theoretical vs empirical complexity
    pass

def best_worst_average_case_analysis():
    """
    Phân tích best, worst, average case
    """
    # TODO: Test with different input patterns
    pass

# Test cases
def test_time_measurement():
    print("Time Complexity Measurement Analysis")
    print("=" * 50)
    
    # Test different input sizes
    sizes = [100, 500, 1000, 2000, 5000]
    
    print("1. Linear Algorithm O(n) - Find Maximum:")
    for size in sizes:
        data = generate_test_data(size)
        time_taken = measure_execution_time(linear_algorithm, data)
        print(f"Size: {size:5d}, Time: {time_taken:.6f}s")
    
    print("\n2. Quadratic Algorithm O(n²) - Bubble Sort:")
    small_sizes = [100, 200, 400, 800]  # Smaller sizes for O(n²)
    for size in small_sizes:
        data = generate_test_data(size)
        time_taken = measure_execution_time(quadratic_algorithm, data)
        print(f"Size: {size:5d}, Time: {time_taken:.6f}s")
    
    print("\n3. Logarithmic Algorithm O(log n) - Binary Search:")
    for size in sizes:
        data = generate_test_data(size, 'sorted')
        target = data[size // 2]  # Target in middle
        time_taken = measure_execution_time(logarithmic_algorithm, data, target)
        print(f"Size: {size:5d}, Time: {time_taken:.6f}s")
    
    print("\n4. N Log N Algorithm O(n log n) - Merge Sort:")
    for size in sizes:
        data = generate_test_data(size)
        time_taken = measure_execution_time(nlogn_algorithm, data)
        print(f"Size: {size:5d}, Time: {time_taken:.6f}s")
    
    print("\n5. Exponential Algorithm O(2ⁿ) - Fibonacci:")
    exp_sizes = [10, 15, 20, 25]  # Very small sizes for exponential!
    for size in exp_sizes:
        time_taken = measure_execution_time(exponential_algorithm, size)
        print(f"n: {size:2d}, Time: {time_taken:.6f}s")
    
    print("\n6. Growth Rate Analysis:")
    complexity_growth_analysis()
    
    print("\n7. Theoretical vs Empirical Verification:")
    verify_theoretical_complexity()
    
    print("\n8. Best/Worst/Average Case Analysis:")
    best_worst_average_case_analysis()

if __name__ == "__main__":
    test_time_measurement()