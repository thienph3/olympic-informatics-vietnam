# Problem 09.01.01: Tuple cơ bản và unpacking

print("=== TUPLE CƠ BẢN VÀ UNPACKING ===")

# Bài 1: Tạo và truy cập tuple
print("1. Tạo và truy cập tuple:")

# Tạo các loại tuple
empty_tuple = ()
single_tuple = (42,)  # Chú ý dấu phẩy
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True, [1, 2, 3])

print(f"Tuple rỗng: {empty_tuple}, type: {type(empty_tuple)}")
print(f"Tuple 1 phần tử: {single_tuple}, type: {type(single_tuple)}")
print(f"Tuple số: {numbers}")
print(f"Tuple hỗn hợp: {mixed}")

# Truy cập phần tử
print(f"Phần tử đầu tiên: {numbers[0]}")
print(f"Phần tử cuối cùng: {numbers[-1]}")
print(f"Phần tử thứ 3: {numbers[2]}")

# Slicing
print(f"Slice [1:4]: {numbers[1:4]}")
print(f"Slice [:3]: {numbers[:3]}")
print(f"Slice [::2]: {numbers[::2]}")

# Bài 2: Tuple methods
print("\n2. Tuple methods:")
data = (1, 2, 3, 2, 4, 2, 5, 2)
print(f"Tuple: {data}")
print(f"Đếm số 2: {data.count(2)}")
print(f"Vị trí đầu tiên của 3: {data.index(3)}")
print(f"Độ dài tuple: {len(data)}")
print(f"Kiểm tra 4 có trong tuple: {4 in data}")
print(f"Kiểm tra 10 không trong tuple: {10 not in data}")

# Bài 3: Tuple unpacking cơ bản
print("\n3. Tuple unpacking cơ bản:")

# Unpacking đơn giản
point = (10, 20)
x, y = point
print(f"Điểm: {point} -> x = {x}, y = {y}")

# Unpacking với nhiều giá trị
person = ("Alice", 25, "Engineer", "New York")
name, age, job, city = person
print(f"Thông tin: {person}")
print(f"Tên: {name}, Tuổi: {age}, Nghề: {job}, Thành phố: {city}")

# Unpacking với RGB color
color = (255, 128, 0)
red, green, blue = color
print(f"Màu RGB: {color} -> R={red}, G={green}, B={blue}")

# Bài 4: Hoán đổi biến
print("\n4. Hoán đổi biến:")
a, b = 10, 20
print(f"Trước hoán đổi: a = {a}, b = {b}")

# Hoán đổi sử dụng tuple
a, b = b, a
print(f"Sau hoán đổi: a = {a}, b = {b}")

# Hoán đổi nhiều biến
x, y, z = 1, 2, 3
print(f"Trước: x={x}, y={y}, z={z}")
x, y, z = z, x, y  # Xoay vòng
print(f"Sau xoay vòng: x={x}, y={y}, z={z}")

# Bài 5: Unpacking với *
print("\n5. Unpacking với *:")
numbers = (1, 2, 3, 4, 5, 6, 7)
print(f"Tuple: {numbers}")

# Lấy đầu và cuối
first, *middle, last = numbers
print(f"Đầu: {first}, Giữa: {middle}, Cuối: {last}")

# Lấy 2 đầu và phần còn lại
first, second, *rest = numbers
print(f"Hai đầu: {first}, {second}, Còn lại: {rest}")

# Lấy phần đầu và 2 cuối
*beginning, second_last, last = numbers
print(f"Phần đầu: {beginning}, Hai cuối: {second_last}, {last}")

# Bài 6: Tuple operations
print("\n6. Tuple operations:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Nối tuple: {tuple1} + {tuple2} = {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Lặp lại: {tuple1} * 3 = {repeated}")

# Comparison
print(f"So sánh: {tuple1} < {tuple2} = {tuple1 < tuple2}")
print(f"So sánh: {(1, 2)} == (1, 2) = {(1, 2) == (1, 2)}")

# Bài 7: Nested tuple unpacking
print("\n7. Nested tuple unpacking:")
nested_data = (("Alice", 25), ("Bob", 30), ("Charlie", 35))
print(f"Dữ liệu nested: {nested_data}")

# Unpacking từng phần tử
for person_data in nested_data:
    name, age = person_data
    print(f"  {name} - {age} tuổi")

# Unpacking trực tiếp trong loop
print("Unpacking trực tiếp:")
for name, age in nested_data:
    print(f"  {name}: {age} tuổi")

# Bài 8: Tuple làm key trong dictionary
print("\n8. Tuple làm key trong dictionary:")
# Tuple có thể làm key vì immutable
coordinates_data = {
    (0, 0): "Origin",
    (1, 0): "Right",
    (0, 1): "Up",
    (-1, 0): "Left",
    (0, -1): "Down"
}

print("Dữ liệu tọa độ:")
for coord, direction in coordinates_data.items():
    x, y = coord
    print(f"  ({x}, {y}): {direction}")

# Truy cập bằng tuple key
point = (1, 0)
if point in coordinates_data:
    print(f"Điểm {point}: {coordinates_data[point]}")

# Bài 9: Multiple return values
print("\n9. Multiple return values:")
def get_name_age():
    """Hàm trả về nhiều giá trị"""
    return "David", 28

def calculate_stats(numbers):
    """Tính thống kê và trả về tuple"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    minimum = min(numbers) if numbers else 0
    maximum = max(numbers) if numbers else 0
    return total, count, average, minimum, maximum

# Sử dụng multiple return
name, age = get_name_age()
print(f"Từ hàm: {name}, {age}")

# Thống kê
test_numbers = [10, 20, 30, 40, 50]
total, count, avg, min_val, max_val = calculate_stats(test_numbers)
print(f"Số liệu: {test_numbers}")
print(f"Tổng: {total}, Số lượng: {count}, TB: {avg:.1f}")
print(f"Min: {min_val}, Max: {max_val}")