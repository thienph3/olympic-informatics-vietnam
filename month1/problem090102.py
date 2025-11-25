# Problem 09.01.02: Xử lý tọa độ và điểm

print("=== XỬ LÝ TỌA ĐỘ VÀ ĐIỂM ===")

import math

# Bài 1: Tọa độ 2D
print("1. Tọa độ 2D:")

def distance_2d(p1, p2):
    """Tính khoảng cách Euclidean giữa 2 điểm 2D"""
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def manhattan_distance(p1, p2):
    """Tính khoảng cách Manhattan"""
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)

# Test với các điểm
point_a = (0, 0)
point_b = (3, 4)
point_c = (1, 1)

print(f"Điểm A: {point_a}")
print(f"Điểm B: {point_b}")
print(f"Điểm C: {point_c}")

print(f"Khoảng cách Euclidean A-B: {distance_2d(point_a, point_b):.2f}")
print(f"Khoảng cách Manhattan A-B: {manhattan_distance(point_a, point_b)}")
print(f"Khoảng cách Euclidean A-C: {distance_2d(point_a, point_c):.2f}")

# Bài 2: Tọa độ 3D
print("\n2. Tọa độ 3D:")

def distance_3d(p1, p2):
    """Tính khoảng cách Euclidean giữa 2 điểm 3D"""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def midpoint_3d(p1, p2):
    """Tìm điểm giữa của 2 điểm 3D"""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2)

# Test 3D
point_3d_1 = (1, 2, 3)
point_3d_2 = (4, 6, 8)

print(f"Điểm 3D 1: {point_3d_1}")
print(f"Điểm 3D 2: {point_3d_2}")
print(f"Khoảng cách 3D: {distance_3d(point_3d_1, point_3d_2):.2f}")

midpoint = midpoint_3d(point_3d_1, point_3d_2)
print(f"Điểm giữa: {midpoint}")

# Bài 3: Danh sách điểm và xử lý
print("\n3. Danh sách điểm:")

points = [(0, 0), (1, 1), (2, 0), (3, 4), (1, 3), (5, 2)]
print(f"Danh sách điểm: {points}")

# Tìm điểm gần gốc tọa độ nhất
origin = (0, 0)
closest_point = min(points, key=lambda p: distance_2d(origin, p))
closest_distance = distance_2d(origin, closest_point)
print(f"Điểm gần gốc nhất: {closest_point} (khoảng cách: {closest_distance:.2f})")

# Tìm điểm xa gốc tọa độ nhất
farthest_point = max(points, key=lambda p: distance_2d(origin, p))
farthest_distance = distance_2d(origin, farthest_point)
print(f"Điểm xa gốc nhất: {farthest_point} (khoảng cách: {farthest_distance:.2f})")

# Sắp xếp theo khoảng cách từ gốc
sorted_points = sorted(points, key=lambda p: distance_2d(origin, p))
print("Điểm sắp xếp theo khoảng cách từ gốc:")
for i, point in enumerate(sorted_points):
    dist = distance_2d(origin, point)
    print(f"  {i+1}. {point} - khoảng cách: {dist:.2f}")

# Bài 4: Hình học cơ bản
print("\n4. Hình học cơ bản:")

def triangle_area(p1, p2, p3):
    """Tính diện tích tam giác từ 3 điểm"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Công thức Shoelace
    area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)
    return area

def is_collinear(p1, p2, p3):
    """Kiểm tra 3 điểm có thẳng hàng không"""
    return triangle_area(p1, p2, p3) == 0

# Test hình học
triangle_points = [(0, 0), (4, 0), (2, 3)]
print(f"Tam giác: {triangle_points}")
area = triangle_area(*triangle_points)
print(f"Diện tích tam giác: {area}")

# Kiểm tra thẳng hàng
collinear_points = [(0, 0), (1, 1), (2, 2)]
non_collinear_points = [(0, 0), (1, 1), (2, 3)]
print(f"Điểm {collinear_points} thẳng hàng: {is_collinear(*collinear_points)}")
print(f"Điểm {non_collinear_points} thẳng hàng: {is_collinear(*non_collinear_points)}")

# Bài 5: Bounding box
print("\n5. Bounding box:")

def find_bounding_box(points):
    """Tìm hình chữ nhật bao quanh các điểm"""
    if not points:
        return None
    
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    
    return (min_x, min_y), (max_x, max_y)

def bounding_box_area(bbox):
    """Tính diện tích bounding box"""
    if not bbox:
        return 0
    (min_x, min_y), (max_x, max_y) = bbox
    return (max_x - min_x) * (max_y - min_y)

# Test bounding box
test_points = [(1, 2), (5, 1), (3, 6), (0, 3), (4, 4)]
print(f"Các điểm: {test_points}")

bbox = find_bounding_box(test_points)
print(f"Bounding box: {bbox}")

if bbox:
    area = bounding_box_area(bbox)
    print(f"Diện tích bounding box: {area}")

# Bài 6: Vector operations
print("\n6. Vector operations:")

def vector_add(v1, v2):
    """Cộng 2 vector"""
    return tuple(a + b for a, b in zip(v1, v2))

def vector_subtract(v1, v2):
    """Trừ 2 vector"""
    return tuple(a - b for a, b in zip(v1, v2))

def vector_dot_product(v1, v2):
    """Tích vô hướng"""
    return sum(a * b for a, b in zip(v1, v2))

def vector_magnitude(v):
    """Độ lớn vector"""
    return math.sqrt(sum(x**2 for x in v))

# Test vector operations
vec1 = (3, 4)
vec2 = (1, 2)

print(f"Vector 1: {vec1}")
print(f"Vector 2: {vec2}")
print(f"Cộng: {vector_add(vec1, vec2)}")
print(f"Trừ: {vector_subtract(vec1, vec2)}")
print(f"Tích vô hướng: {vector_dot_product(vec1, vec2)}")
print(f"Độ lớn vec1: {vector_magnitude(vec1):.2f}")
print(f"Độ lớn vec2: {vector_magnitude(vec2):.2f}")

# Bài 7: Coordinate transformations
print("\n7. Coordinate transformations:")

def translate_point(point, offset):
    """Tịnh tiến điểm"""
    return tuple(p + o for p, o in zip(point, offset))

def scale_point(point, factor):
    """Phóng to/thu nhỏ điểm"""
    return tuple(p * factor for p in point)

def rotate_point_2d(point, angle_degrees):
    """Xoay điểm 2D quanh gốc tọa độ"""
    x, y = point
    angle_rad = math.radians(angle_degrees)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    
    new_x = x * cos_a - y * sin_a
    new_y = x * sin_a + y * cos_a
    
    return (new_x, new_y)

# Test transformations
original_point = (2, 3)
print(f"Điểm gốc: {original_point}")

# Tịnh tiến
translated = translate_point(original_point, (1, -1))
print(f"Sau tịnh tiến (1, -1): {translated}")

# Phóng to
scaled = scale_point(original_point, 2)
print(f"Sau phóng to x2: {scaled}")

# Xoay 90 độ
rotated = rotate_point_2d(original_point, 90)
print(f"Sau xoay 90°: ({rotated[0]:.2f}, {rotated[1]:.2f})")

# Bài 8: Closest pair of points
print("\n8. Closest pair of points:")

def closest_pair_brute_force(points):
    """Tìm cặp điểm gần nhau nhất (brute force)"""
    if len(points) < 2:
        return None, float('inf')
    
    min_distance = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance_2d(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_distance

# Test closest pair
random_points = [(1, 1), (2, 3), (4, 2), (1.5, 1.2), (3, 4), (5, 1)]
print(f"Các điểm: {random_points}")

pair, min_dist = closest_pair_brute_force(random_points)
if pair:
    print(f"Cặp điểm gần nhau nhất: {pair[0]} và {pair[1]}")
    print(f"Khoảng cách: {min_dist:.3f}")