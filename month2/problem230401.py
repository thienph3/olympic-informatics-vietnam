"""
Problem 230401: Geometric Algorithms (Closest Pair, Convex Hull)
Thuật toán hình học sử dụng divide and conquer

Topics: Closest pair of points, convex hull, geometric divide and conquer
"""

import math

def distance(p1, p2):
    """
    Tính khoảng cách Euclidean giữa hai điểm
    """
    # TODO: Calculate Euclidean distance between two points
    pass

def closest_pair_brute_force(points):
    """
    Tìm cặp điểm gần nhất bằng brute force
    Time: O(n²), Space: O(1)
    """
    # TODO: Find closest pair using brute force
    pass

def closest_pair_divide_conquer(points):
    """
    Tìm cặp điểm gần nhất bằng divide and conquer
    Time: O(n log n), Space: O(n)
    """
    # TODO: Find closest pair using divide and conquer
    pass

def closest_pair_in_strip(strip, d):
    """
    Tìm cặp điểm gần nhất trong strip
    """
    # TODO: Find closest pair in vertical strip
    pass

def convex_hull_graham_scan(points):
    """
    Tìm convex hull bằng Graham scan
    Time: O(n log n), Space: O(n)
    """
    # TODO: Find convex hull using Graham scan
    pass

def convex_hull_divide_conquer(points):
    """
    Tìm convex hull bằng divide and conquer
    Time: O(n log n), Space: O(n)
    """
    # TODO: Find convex hull using divide and conquer
    pass

def cross_product(o, a, b):
    """
    Tính cross product của vectors OA và OB
    """
    # TODO: Calculate cross product for orientation test
    pass

def merge_hulls(left_hull, right_hull):
    """
    Merge hai convex hulls
    """
    # TODO: Merge two convex hulls
    pass

def point_in_polygon(point, polygon):
    """
    Kiểm tra điểm có nằm trong polygon không
    """
    # TODO: Check if point is inside polygon
    pass

def line_intersection(line1, line2):
    """
    Tìm giao điểm của hai đường thẳng
    """
    # TODO: Find intersection of two lines
    pass

# Test cases
def test_geometric_algorithms():
    print("Geometric Algorithms (Divide and Conquer)")
    print("=" * 45)
    
    # Test distance calculation
    print("1. Distance Calculation:")
    distance_tests = [
        ((0, 0), (3, 4)),
        ((1, 1), (4, 5)),
        ((0, 0), (0, 0)),
        ((-1, -1), (1, 1))
    ]
    for p1, p2 in distance_tests:
        dist = distance(p1, p2)
        print(f"distance({p1}, {p2}) = {dist:.2f}")
    
    # Test closest pair brute force
    print("\n2. Closest Pair (Brute Force):")
    point_sets = [
        [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(1, 1), (1, 2), (2, 1), (2, 2)],
        [(0, 0), (10, 10)]
    ]
    
    for points in point_sets:
        if len(points) >= 2:
            min_dist, pair = closest_pair_brute_force(points)
            print(f"closest pair in {points}: {pair} with distance {min_dist:.2f}")
    
    # Test closest pair divide and conquer
    print("\n3. Closest Pair (Divide and Conquer):")
    for points in point_sets:
        if len(points) >= 2:
            min_dist, pair = closest_pair_divide_conquer(points)
            print(f"closest pair in {points}: {pair} with distance {min_dist:.2f}")
    
    # Test strip search
    print("\n4. Closest Pair in Strip:")
    strip_points = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]
    strip_distance = 2.0
    min_dist = closest_pair_in_strip(strip_points, strip_distance)
    print(f"closest in strip {strip_points} with d={strip_distance}: {min_dist:.2f}")
    
    # Test Graham scan
    print("\n5. Convex Hull (Graham Scan):")
    hull_point_sets = [
        [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)],
        [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)],
        [(1, 1), (2, 2), (3, 3), (4, 4)],  # Collinear points
        [(0, 0), (1, 1), (0, 1), (1, 0)]   # Square
    ]
    
    for points in hull_point_sets:
        hull = convex_hull_graham_scan(points)
        print(f"convex hull of {points}: {hull}")
    
    # Test divide and conquer convex hull
    print("\n6. Convex Hull (Divide and Conquer):")
    for points in hull_point_sets:
        hull = convex_hull_divide_conquer(points)
        print(f"convex hull (D&C) of {points}: {hull}")
    
    # Test cross product
    print("\n7. Cross Product (Orientation Test):")
    cross_tests = [
        ((0, 0), (1, 0), (0, 1)),  # Counter-clockwise
        ((0, 0), (0, 1), (1, 0)),  # Clockwise
        ((0, 0), (1, 1), (2, 2))   # Collinear
    ]
    for o, a, b in cross_tests:
        cross = cross_product(o, a, b)
        orientation = "CCW" if cross > 0 else "CW" if cross < 0 else "Collinear"
        print(f"cross_product({o}, {a}, {b}) = {cross} ({orientation})")
    
    # Test hull merging
    print("\n8. Merge Convex Hulls:")
    left_hull = [(0, 0), (0, 2), (1, 3), (2, 2), (2, 0)]
    right_hull = [(3, 0), (3, 2), (4, 3), (5, 2), (5, 0)]
    merged_hull = merge_hulls(left_hull, right_hull)
    print(f"merge hulls {left_hull} and {right_hull}: {merged_hull}")
    
    # Test point in polygon
    print("\n9. Point in Polygon:")
    polygon = [(0, 0), (4, 0), (4, 4), (0, 4)]  # Square
    test_points = [(2, 2), (5, 5), (0, 0), (2, 0)]
    for point in test_points:
        inside = point_in_polygon(point, polygon)
        print(f"point {point} in polygon {polygon}: {inside}")
    
    # Test line intersection
    print("\n10. Line Intersection:")
    line_tests = [
        (((0, 0), (2, 2)), ((0, 2), (2, 0))),  # Intersecting
        (((0, 0), (1, 1)), ((2, 2), (3, 3))),  # Parallel
        (((0, 0), (2, 0)), ((1, -1), (1, 1)))  # Perpendicular
    ]
    for line1, line2 in line_tests:
        intersection = line_intersection(line1, line2)
        print(f"intersection of {line1} and {line2}: {intersection}")
    
    # Performance comparison
    print("\n11. Performance Comparison:")
    import time
    import random
    
    # Generate random points
    large_point_set = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(100)]
    
    # Time brute force
    start = time.time()
    bf_result = closest_pair_brute_force(large_point_set)
    bf_time = time.time() - start
    
    # Time divide and conquer
    start = time.time()
    dc_result = closest_pair_divide_conquer(large_point_set)
    dc_time = time.time() - start
    
    print(f"Closest pair on 100 points:")
    print(f"Brute force: {bf_time:.4f}s")
    print(f"Divide & Conquer: {dc_time:.4f}s")
    print(f"Results match: {abs(bf_result[0] - dc_result[0]) < 1e-9}")

if __name__ == "__main__":
    test_geometric_algorithms()