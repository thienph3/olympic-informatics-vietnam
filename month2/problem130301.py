"""
Day 13 - Problem 5: Performance analysis
Thời gian: 30 phút
"""

import time
import random
import matplotlib.pyplot as plt

def measure_time(func, *args):
    """
    Đo thời gian thực thi của function
    Input: func - function cần đo, *args - arguments
    Output: (result, execution_time)
    """
    # TODO: Implement time measurement
    pass

def linear_search(arr, target):
    """Linear search implementation for comparison"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Binary search implementation for comparison"""
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

def compare_search_algorithms(sizes):
    """
    So sánh hiệu suất Linear vs Binary Search
    Input: sizes - list các kích thước mảng để test
    Output: dictionary chứa kết quả timing
    """
    # TODO: Implement performance comparison
    results = {
        'sizes': sizes,
        'linear_times': [],
        'binary_times': [],
        'speedup_ratios': []
    }
    
    # TODO: Test với các kích thước khác nhau
    # TODO: Tính toán speedup ratio
    
    return results

def analyze_complexity_empirical(algorithm, sizes):
    """
    Phân tích độ phức tạp thực nghiệm
    Input: algorithm - function cần phân tích, sizes - list kích thước test
    Output: list thời gian thực thi
    """
    # TODO: Implement empirical complexity analysis
    pass

def plot_performance_comparison(results):
    """
    Vẽ biểu đồ so sánh hiệu suất
    Input: results - dictionary từ compare_search_algorithms
    """
    # TODO: Implement plotting (optional, có thể skip nếu không có matplotlib)
    pass

def worst_case_analysis():
    """
    Phân tích worst case cho các thuật toán
    """
    print("Phân tích Worst Case:")
    print("Linear Search:")
    print("  - Worst case: Target ở cuối mảng hoặc không có")
    print("  - Time complexity: O(n)")
    print("  - Số phép so sánh: n")
    
    print("\nBinary Search:")
    print("  - Worst case: Target không có trong mảng")
    print("  - Time complexity: O(log n)")
    print("  - Số phép so sánh: ⌊log₂(n)⌋ + 1")
    
    # TODO: Tính toán cụ thể cho các kích thước mảng
    sizes = [100, 1000, 10000, 100000, 1000000]
    print(f"\n{'Size':<10} {'Linear':<10} {'Binary':<10} {'Ratio':<10}")
    print("-" * 40)
    
    for size in sizes:
        linear_ops = size
        binary_ops = int(size.bit_length())  # ≈ log₂(n) + 1
        ratio = linear_ops / binary_ops if binary_ops > 0 else 0
        print(f"{size:<10} {linear_ops:<10} {binary_ops:<10} {ratio:<10.1f}")

def memory_usage_analysis():
    """
    Phân tích memory usage của các thuật toán
    """
    print("\nPhân tích Memory Usage:")
    print("Linear Search (Iterative):")
    print("  - Space complexity: O(1)")
    print("  - Chỉ cần vài biến: index, target")
    
    print("\nBinary Search (Iterative):")
    print("  - Space complexity: O(1)")
    print("  - Cần biến: left, right, mid")
    
    print("\nBinary Search (Recursive):")
    print("  - Space complexity: O(log n)")
    print("  - Call stack depth: log n")

# Test cases và benchmarks
if __name__ == "__main__":
    print("=== PERFORMANCE ANALYSIS ===\n")
    
    # Test measure_time function
    arr = list(range(10000))
    target = 7500
    
    result, exec_time = measure_time(linear_search, arr, target)
    print(f"Linear search result: {result}, time: {exec_time:.6f}s")
    
    result, exec_time = measure_time(binary_search, arr, target)
    print(f"Binary search result: {result}, time: {exec_time:.6f}s")
    
    # Compare algorithms với different sizes
    test_sizes = [1000, 5000, 10000, 50000, 100000]
    print(f"\n=== COMPARISON ACROSS SIZES ===")
    results = compare_search_algorithms(test_sizes)
    
    # Print results
    print(f"{'Size':<10} {'Linear(s)':<12} {'Binary(s)':<12} {'Speedup':<10}")
    print("-" * 50)
    for i, size in enumerate(results['sizes']):
        linear_time = results['linear_times'][i]
        binary_time = results['binary_times'][i]
        speedup = results['speedup_ratios'][i]
        print(f"{size:<10} {linear_time:<12.6f} {binary_time:<12.6f} {speedup:<10.2f}x")
    
    # Theoretical analysis
    print(f"\n=== THEORETICAL ANALYSIS ===")
    worst_case_analysis()
    memory_usage_analysis()
    
    # Empirical complexity analysis
    print(f"\n=== EMPIRICAL COMPLEXITY ===")
    sizes = [100, 200, 400, 800, 1600, 3200]
    linear_times = analyze_complexity_empirical(linear_search, sizes)
    binary_times = analyze_complexity_empirical(binary_search, sizes)
    
    print("Linear Search scaling:")
    for i in range(1, len(sizes)):
        size_ratio = sizes[i] / sizes[i-1]
        time_ratio = linear_times[i] / linear_times[i-1] if linear_times[i-1] > 0 else 0
        print(f"  Size {sizes[i-1]} -> {sizes[i]} (x{size_ratio:.1f}): Time ratio x{time_ratio:.2f}")
    
    print("\nBinary Search scaling:")
    for i in range(1, len(sizes)):
        size_ratio = sizes[i] / sizes[i-1]
        time_ratio = binary_times[i] / binary_times[i-1] if binary_times[i-1] > 0 else 0
        print(f"  Size {sizes[i-1]} -> {sizes[i]} (x{size_ratio:.1f}): Time ratio x{time_ratio:.2f}")