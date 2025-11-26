"""
Day 15 - Problem 2: Ternary search applications
Thời gian: 30 phút
"""

def minimize_max_distance_gas_stations(stations, k):
    """
    Minimize maximum distance between consecutive gas stations
    by adding k new stations optimally using ternary search
    Input: stations - sorted positions, k - số stations thêm vào
    Output: minimum possible maximum distance
    """
    # TODO: Implement using ternary search on answer
    def can_achieve_max_distance(max_dist):
        # TODO: Check if có thể achieve max_dist với k stations
        pass
    
    # TODO: Ternary search on distance range
    pass

def find_minimum_speed_to_arrive_on_time(dist, hour):
    """
    Tìm tốc độ tối thiểu để đi hết quãng đường trong thời gian cho phép
    Input: dist - list distances, hour - total time allowed
    Output: minimum speed, -1 nếu không thể
    """
    # TODO: Implement using ternary search on speed
    def time_needed(speed):
        # TODO: Calculate time needed với given speed
        pass
    
    # TODO: Ternary search on speed range
    pass

def optimal_cow_placement(stalls, cows):
    """
    Đặt cows vào stalls sao cho khoảng cách minimum giữa các cows là lớn nhất
    Input: stalls - sorted positions, cows - số con bò
    Output: maximum minimum distance
    """
    # TODO: Implement using ternary search on distance
    def can_place_cows(min_distance):
        # TODO: Check if có thể place all cows với min_distance
        pass
    
    # TODO: Ternary search on distance range
    pass

def find_rotation_count_ternary(arr):
    """
    Tìm số lần rotate của sorted array bằng ternary search
    Input: arr - rotated sorted array
    Output: số lần rotate
    """
    # TODO: Implement using ternary search to find minimum element
    pass

def search_in_mountain_array_ternary(mountain_arr, target):
    """
    Tìm kiếm trong mountain array bằng ternary search
    Input: mountain_arr - mountain array, target - giá trị cần tìm
    Output: index của target hoặc -1
    """
    # TODO: Implement bằng cách tìm peak với ternary search
    def find_peak_ternary():
        # TODO: Find peak using ternary search
        pass
    
    def binary_search_ascending(left, right):
        # TODO: Binary search trong ascending part
        pass
    
    def binary_search_descending(left, right):
        # TODO: Binary search trong descending part
        pass
    
    # TODO: Combine peak finding với binary searches
    pass

def minimize_maximum_subarray_sum_ternary(arr, k):
    """
    Minimize maximum subarray sum khi split array thành k parts
    Input: arr - array, k - số parts
    Output: minimum possible maximum sum
    """
    # TODO: Implement using ternary search on sum range
    def can_split_with_max_sum(max_sum):
        # TODO: Check if có thể split với max_sum
        pass
    
    # TODO: Ternary search on sum range
    pass

def find_optimal_meeting_point(points):
    """
    Tìm điểm meeting optimal để minimize total distance
    Input: points - list of (x, y) coordinates
    Output: (x, y) của optimal meeting point
    """
    # TODO: Implement using ternary search on x và y coordinates
    def total_distance(x, y):
        # TODO: Calculate total distance to all points
        pass
    
    # TODO: Ternary search on x coordinate
    def find_optimal_x():
        pass
    
    # TODO: Ternary search on y coordinate  
    def find_optimal_y(x):
        pass
    
    # TODO: Combine searches
    pass

# Test cases
if __name__ == "__main__":
    # Test minimize_max_distance_gas_stations
    print("=== GAS STATIONS OPTIMIZATION ===")
    
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k_values = [1, 2, 3, 5]
    
    for k in k_values:
        min_max_dist = minimize_max_distance_gas_stations(stations, k)
        print(f"Với {k} stations thêm, min max distance: {min_max_dist:.6f}")
    
    # Test find_minimum_speed_to_arrive_on_time
    print(f"\n=== MINIMUM SPEED CALCULATION ===")
    
    test_cases = [
        ([1, 3, 2], 6),      # distances, time
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
        ([1, 2, 4, 8, 9], 3),    # stalls, cows
        ([1, 2, 3, 4, 5], 3),
        ([0, 3, 4, 7, 10, 9], 4)
    ]
    
    for stalls, cows in stall_configs:
        stalls_sorted = sorted(stalls)
        max_min_dist = optimal_cow_placement(stalls_sorted, cows)
        print(f"Stalls {stalls_sorted}, {cows} cows: max min distance = {max_min_dist}")
    
    # Test find_rotation_count_ternary
    print(f"\n=== ROTATION COUNT ===")
    
    rotated_arrays = [
        [4, 5, 6, 7, 0, 1, 2],
        [0, 1, 2, 4, 5, 6, 7],
        [1, 2, 3],
        [2, 1],
        [1]
    ]
    
    for arr in rotated_arrays:
        rotation_count = find_rotation_count_ternary(arr)
        print(f"Array {arr}: rotated {rotation_count} times")
    
    # Test search_in_mountain_array_ternary
    print(f"\n=== SEARCH IN MOUNTAIN ARRAY ===")
    
    mountain_arr = [1, 2, 3, 4, 5, 3, 1]
    targets = [3, 5, 2, 0]
    
    for target in targets:
        result = search_in_mountain_array_ternary(mountain_arr, target)
        print(f"Tìm {target} trong mountain array: {result}")
    
    # Test minimize_maximum_subarray_sum_ternary
    print(f"\n=== MINIMIZE MAXIMUM SUBARRAY SUM ===")
    
    subarray_test_cases = [
        ([7, 2, 5, 10, 8], 2),   # Expected: 18
        ([1, 2, 3, 4, 5], 2),    # Expected: 9
        ([1, 4, 4], 3)           # Expected: 4
    ]
    
    for arr, k in subarray_test_cases:
        result = minimize_maximum_subarray_sum_ternary(arr, k)
        print(f"Split {arr} into {k} parts: min max sum = {result}")
    
    # Test find_optimal_meeting_point
    print(f"\n=== OPTIMAL MEETING POINT ===")
    
    point_sets = [
        [(1, 1), (3, 3), (2, 2)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(1, 4), (0, 2), (3, 1)]
    ]
    
    for points in point_sets:
        optimal_point = find_optimal_meeting_point(points)
        print(f"Points {points}: optimal meeting point = {optimal_point}")
    
    # Performance analysis
    print(f"\n=== PERFORMANCE ANALYSIS ===")
    
    import time
    
    # Test performance với large dataset
    large_stations = list(range(0, 10000, 10))
    k_large = 100
    
    start = time.time()
    result = minimize_max_distance_gas_stations(large_stations, k_large)
    end = time.time()
    
    print(f"Large dataset ({len(large_stations)} stations, k={k_large}):")
    print(f"  Result: {result:.6f}")
    print(f"  Time: {end-start:.6f}s")
    
    print(f"\n=== TERNARY SEARCH APPLICATIONS SUMMARY ===")
    print("Optimization Problems:")
    print("  - Gas stations: Minimize maximum distance")
    print("  - Speed calculation: Find minimum feasible speed")
    print("  - Cow placement: Maximize minimum distance")
    print("  - Array splitting: Minimize maximum sum")
    print("  - Meeting point: Minimize total distance")
    
    print("\\nSearch Problems:")
    print("  - Rotation count: Find minimum in rotated array")
    print("  - Mountain array: Peak finding + binary search")
    
    print("\\nKey Advantages:")
    print("  - Good for unimodal optimization functions")
    print("  - Fewer iterations than binary search")
    print("  - Natural for continuous optimization")
    
    print("\\nLimitations:")
    print("  - More comparisons per iteration")
    print("  - Only works for unimodal functions")
    print("  - May not be faster in practice due to overhead")