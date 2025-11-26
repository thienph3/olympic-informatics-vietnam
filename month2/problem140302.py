"""
Day 14 - Problem 6: Ternary search applications
Thời gian: 30 phút
"""

def ternary_search_maximum(func, left, right, epsilon=1e-9):
    """
    Ternary search để tìm maximum của unimodal function
    Input: func - unimodal function, left/right - search range, epsilon - precision
    Output: x tại đó func(x) maximum
    """
    # TODO: Implement ternary search for maximum
    pass

def ternary_search_minimum(func, left, right, epsilon=1e-9):
    """
    Ternary search để tìm minimum của unimodal function
    Input: func - unimodal function, left/right - search range, epsilon - precision
    Output: x tại đó func(x) minimum
    """
    # TODO: Implement ternary search for minimum
    pass

def find_peak_in_mountain_array(arr):
    """
    Tìm peak trong mountain array (tăng rồi giảm)
    Input: arr - mountain array
    Output: index của peak element
    """
    # TODO: Implement using ternary search concept
    pass

def minimize_max_distance_gas_stations(stations, k):
    """
    Minimize maximum distance between consecutive gas stations
    by adding k new stations optimally
    Input: stations - sorted positions, k - số stations thêm vào
    Output: minimum possible maximum distance
    """
    # TODO: Implement using ternary search on answer
    pass

def find_minimum_speed_to_arrive_on_time(dist, hour):
    """
    Tìm tốc độ tối thiểu để đi hết quãng đường trong thời gian cho phép
    Input: dist - list distances, hour - total time allowed
    Output: minimum speed, -1 nếu không thể
    """
    # TODO: Implement using ternary search on speed
    pass

def optimal_cow_placement(stalls, cows):
    """
    Đặt cows vào stalls sao cho khoảng cách minimum giữa các cows là lớn nhất
    Input: stalls - sorted positions, cows - số con bò
    Output: maximum minimum distance
    """
    # TODO: Implement using ternary search on distance
    pass

def find_rotation_count(arr):
    """
    Tìm số lần rotate của sorted array
    Input: arr - rotated sorted array
    Output: số lần rotate
    """
    # TODO: Implement using ternary search concept
    pass

def search_in_mountain_array(mountain_arr, target):
    """
    Tìm kiếm trong mountain array
    Input: mountain_arr - mountain array, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement bằng cách tìm peak trước, sau đó binary search 2 bên
    pass

# Test cases
if __name__ == "__main__":
    import math
    
    # Test ternary_search_maximum
    print("=== TERNARY SEARCH MAXIMUM ===")
    
    # Test với parabola: f(x) = -(x-3)² + 10
    def parabola(x):
        return -(x - 3) ** 2 + 10
    
    max_x = ternary_search_maximum(parabola, 0, 6)
    max_value = parabola(max_x)
    print(f"Maximum của parabola tại x = {max_x:.6f}, f(x) = {max_value:.6f}")
    
    # Test với sin function
    def sin_func(x):
        return math.sin(x)
    
    max_x = ternary_search_maximum(sin_func, 0, math.pi)
    max_value = sin_func(max_x)
    print(f"Maximum của sin(x) trong [0, π] tại x = {max_x:.6f}, sin(x) = {max_value:.6f}")
    
    # Test ternary_search_minimum
    print(f"\n=== TERNARY SEARCH MINIMUM ===")
    
    # Test với parabola: f(x) = (x-2)² + 1
    def parabola_min(x):
        return (x - 2) ** 2 + 1
    
    min_x = ternary_search_minimum(parabola_min, 0, 4)
    min_value = parabola_min(min_x)
    print(f"Minimum của parabola tại x = {min_x:.6f}, f(x) = {min_value:.6f}")
    
    # Test find_peak_in_mountain_array
    print(f"\n=== MOUNTAIN ARRAY PEAK ===")
    
    mountain_arrays = [
        [0, 1, 0],
        [0, 2, 1, 0],
        [0, 10, 5, 2],
        [1, 2, 3, 4, 5, 3, 1]
    ]
    
    for arr in mountain_arrays:
        peak_idx = find_peak_in_mountain_array(arr)
        print(f"Peak trong {arr}: index {peak_idx}, value {arr[peak_idx] if peak_idx != -1 else 'N/A'}")
    
    # Test minimize_max_distance_gas_stations
    print(f"\n=== GAS STATIONS OPTIMIZATION ===")
    
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k_values = [1, 2, 3, 5]
    
    for k in k_values:
        min_max_dist = minimize_max_distance_gas_stations(stations, k)
        print(f"Với {k} stations thêm, min max distance: {min_max_dist:.6f}")
    
    # Test find_minimum_speed_to_arrive_on_time
    print(f"\n=== MINIMUM SPEED CALCULATION ===")
    
    test_cases = [
        ([1, 3, 2], 6),    # distances, time
        ([1, 3, 2], 2.7),
        ([1, 3, 2], 1.9),
        ([1, 1, 100000], 2.01)
    ]
    
    for dist, hour in test_cases:
        min_speed = find_minimum_speed_to_arrive_on_time(dist, hour)
        print(f"Distances {dist}, time {hour}: min speed = {min_speed}")
    
    # Test optimal_cow_placement
    print(f"\n=== AGGRESSIVE COWS ===")
    
    stall_configs = [
        ([1, 2, 4, 8, 9], 3),  # stalls, cows
        ([1, 2, 3, 4, 5], 3),
        ([0, 3, 4, 7, 10, 9], 4)
    ]
    
    for stalls, cows in stall_configs:
        stalls_sorted = sorted(stalls)
        max_min_dist = optimal_cow_placement(stalls_sorted, cows)
        print(f"Stalls {stalls_sorted}, {cows} cows: max min distance = {max_min_dist}")
    
    # Test find_rotation_count
    print(f"\n=== ROTATION COUNT ===")
    
    rotated_arrays = [
        [4, 5, 6, 7, 0, 1, 2],
        [0, 1, 2, 4, 5, 6, 7],
        [1, 2, 3],
        [2, 1],
        [1]
    ]
    
    for arr in rotated_arrays:
        rotation_count = find_rotation_count(arr)
        print(f"Array {arr}: rotated {rotation_count} times")
    
    # Test search_in_mountain_array
    print(f"\n=== SEARCH IN MOUNTAIN ARRAY ===")
    
    mountain_arr = [1, 2, 3, 4, 5, 3, 1]
    targets = [3, 5, 2, 0]
    
    for target in targets:
        result = search_in_mountain_array(mountain_arr, target)
        print(f"Tìm {target} trong mountain array: {result}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE ANALYSIS ===")
    
    # So sánh ternary vs binary search
    def test_function(x):
        return -(x - 50) ** 2 + 2500  # Peak tại x=50
    
    import time
    
    # Ternary search
    start = time.time()
    for _ in range(1000):
        result = ternary_search_maximum(test_function, 0, 100)
    ternary_time = time.time() - start
    
    print(f"1000 ternary searches: {ternary_time:.6f}s")
    print(f"Average per search: {ternary_time/1000:.8f}s")
    
    # Complexity analysis
    print(f"\n=== COMPLEXITY ANALYSIS ===")
    print("Ternary Search:")
    print("  - Time: O(log₃ n) ≈ 0.63 * O(log₂ n)")
    print("  - Space: O(1) iterative, O(log n) recursive")
    print("  - Comparisons per iteration: 2 (vs 1 for binary)")
    
    print("\\nApplications:")
    print("  - Unimodal function optimization")
    print("  - Peak finding in mountain arrays")
    print("  - Binary search on answer space")
    print("  - Optimization problems với convex/concave functions")
    
    print("\\nWhen to use:")
    print("  - Function có single peak/valley")
    print("  - Optimization problems")
    print("  - Alternative to binary search trong special cases")
    
    print("\\nLimitations:")
    print("  - Chỉ work với unimodal functions")
    print("  - More comparisons per iteration than binary search")
    print("  - Floating point precision issues")