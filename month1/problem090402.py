"""
Problem 090402: Tuple trong thuật toán Olympic
Sử dụng tuple cho tọa độ, sorting, multiple returns trong bài toán Olympic

Bài 1: Coordinate Processing
- Nhập n điểm tọa độ (x, y)
- Tính khoảng cách Manhattan và Euclidean từ gốc tọa độ
- Sắp xếp theo khoảng cách từ gốc tọa độ
- Tìm cặp điểm gần nhau nhất

Bài 2: Multiple Return Values
- Tìm min/max với indices
- Phân tích thống kê array
- Return multiple results từ function

Bài 3: Tuple Sorting Applications
- Sắp xếp học sinh theo điểm và tên
- Ranking với tie-breaking
- Custom sorting với multiple criteria
"""

import math

def manhattan_distance(p1, p2=(0, 0)):
    """Tính khoảng cách Manhattan giữa 2 điểm"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def euclidean_distance(p1, p2=(0, 0)):
    """Tính khoảng cách Euclidean giữa 2 điểm"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def sort_by_distance_from_origin(points):
    """Sắp xếp điểm theo khoảng cách từ gốc tọa độ"""
    return sorted(points, key=lambda p: p[0]**2 + p[1]**2)

def closest_pair_distance(points):
    """Tìm khoảng cách nhỏ nhất giữa 2 điểm"""
    min_dist = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    
    return min_dist, closest_pair

def min_max_with_indices(arr):
    """Tìm min/max với indices"""
    min_val = min(arr)
    max_val = max(arr)
    min_idx = arr.index(min_val)
    max_idx = arr.index(max_val)
    return (min_val, min_idx), (max_val, max_idx)

def array_statistics(arr):
    """Phân tích thống kê array, return multiple values"""
    n = len(arr)
    total = sum(arr)
    mean = total / n
    
    # Median
    sorted_arr = sorted(arr)
    if n % 2 == 0:
        median = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        median = sorted_arr[n//2]
    
    # Mode (giá trị xuất hiện nhiều nhất)
    from collections import Counter
    counter = Counter(arr)
    mode_count = max(counter.values())
    modes = [k for k, v in counter.items() if v == mode_count]
    
    return mean, median, modes[0] if len(modes) == 1 else modes, min(arr), max(arr)

def sort_students(students):
    """
    Sắp xếp học sinh theo điểm giảm dần, nếu bằng điểm thì theo tên tăng dần
    students: list of tuples (name, score)
    """
    return sorted(students, key=lambda x: (-x[1], x[0]))

def ranking_with_ties(scores):
    """
    Tạo ranking với tie-breaking
    Return list of tuples (score, rank)
    """
    # Sắp xếp điểm giảm dần
    sorted_scores = sorted(enumerate(scores), key=lambda x: -x[1])
    
    rankings = [0] * len(scores)
    current_rank = 1
    
    for i, (original_idx, score) in enumerate(sorted_scores):
        if i > 0 and score < sorted_scores[i-1][1]:
            current_rank = i + 1
        rankings[original_idx] = current_rank
    
    return [(scores[i], rankings[i]) for i in range(len(scores))]

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Coordinate Processing ===")
    
    # Test coordinate processing
    points = [(3, 4), (1, 1), (5, 0), (2, 3), (0, 2)]
    print(f"Điểm gốc: {points}")
    
    # Khoảng cách từ gốc tọa độ
    print("\nKhoảng cách từ gốc tọa độ:")
    for point in points:
        manhattan = manhattan_distance(point)
        euclidean = euclidean_distance(point)
        print(f"{point}: Manhattan = {manhattan}, Euclidean = {euclidean:.2f}")
    
    # Sắp xếp theo khoảng cách
    sorted_points = sort_by_distance_from_origin(points)
    print(f"\nSắp xếp theo khoảng cách: {sorted_points}")
    
    # Cặp điểm gần nhau nhất
    min_dist, closest = closest_pair_distance(points)
    print(f"Cặp điểm gần nhất: {closest}, khoảng cách = {min_dist:.2f}")
    
    print("\n=== Bài 2: Multiple Return Values ===")
    
    # Test multiple return values
    numbers = [3, 7, 2, 9, 1, 8, 5]
    print(f"Array: {numbers}")
    
    (min_val, min_idx), (max_val, max_idx) = min_max_with_indices(numbers)
    print(f"Min: {min_val} tại index {min_idx}")
    print(f"Max: {max_val} tại index {max_idx}")
    
    # Statistics
    mean, median, mode, min_v, max_v = array_statistics(numbers)
    print(f"Mean: {mean:.2f}, Median: {median}, Mode: {mode}, Min: {min_v}, Max: {max_v}")
    
    print("\n=== Bài 3: Tuple Sorting Applications ===")
    
    # Test student sorting
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("David", 78), ("Eve", 92)]
    print(f"Học sinh gốc: {students}")
    
    sorted_students = sort_students(students)
    print(f"Sắp xếp theo điểm: {sorted_students}")
    
    # Test ranking
    scores = [85, 92, 78, 92, 85, 88]
    print(f"\nĐiểm gốc: {scores}")
    
    rankings = ranking_with_ties(scores)
    print("Ranking với tie-breaking:")
    for i, (score, rank) in enumerate(rankings):
        print(f"Học sinh {i+1}: điểm {score}, hạng {rank}")

    print("\n=== Bài tập thực hành ===")
    print("1. Nhập tọa độ các điểm và tìm điểm xa nhất từ gốc")
    print("2. Tạo function trả về top-k điểm gần nhất")
    print("3. Implement convex hull với tuple")
    print("4. Sắp xếp theo nhiều tiêu chí (x, y, distance)")