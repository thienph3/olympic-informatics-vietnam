# Problem 07.01.01: Thao tác cơ bản với list

print("=== THAO TÁC CƠ BẢN VỚI LIST ===")

# Bài 1: Tạo và truy cập list
print("1. Tạo và truy cập list")
numbers = [10, 20, 30, 40, 50]
print(f"List ban đầu: {numbers}")
print(f"Phần tử đầu tiên: {numbers[0]}")
print(f"Phần tử cuối cùng: {numbers[-1]}")
print(f"Phần tử thứ 3: {numbers[2]}")

# Bài 2: Thay đổi giá trị
print("\n2. Thay đổi giá trị")
numbers[0] = 100
numbers[-1] = 500
print(f"Sau khi thay đổi: {numbers}")

# Bài 3: Kiểm tra tồn tại
print("\n3. Kiểm tra tồn tại")
search_values = [30, 60, 100]
for value in search_values:
    if value in numbers:
        print(f"{value} có trong list tại vị trí {numbers.index(value)}")
    else:
        print(f"{value} không có trong list")

# Bài 4: Đếm và tìm vị trí
print("\n4. Đếm và tìm vị trí")
data = [1, 2, 3, 2, 4, 2, 5]
print(f"List: {data}")
print(f"Số 2 xuất hiện {data.count(2)} lần")
print(f"Vị trí đầu tiên của số 2: {data.index(2)}")

# Tìm tất cả vị trí của số 2
positions = []
for i in range(len(data)):
    if data[i] == 2:
        positions.append(i)
print(f"Tất cả vị trí của số 2: {positions}")

# Bài 5: Thông tin list
print("\n5. Thông tin list")
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"List hỗn hợp: {mixed_list}")
print(f"Độ dài: {len(mixed_list)}")
print(f"Kiểu dữ liệu các phần tử:")
for i, item in enumerate(mixed_list):
    print(f"  Index {i}: {item} ({type(item).__name__})")