# Problem 07.01.02: Xử lý list số và tìm kiếm

print("=== XỬ LÝ LIST SỐ VÀ TÌM KIẾM ===")

# Nhập list số
print("Nhập danh sách số (cách nhau bởi dấu cách):")
numbers = list(map(int, input().split()))
print(f"List đã nhập: {numbers}")

# Bài 1: Thống kê cơ bản
print("\n1. Thống kê cơ bản:")
if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    print(f"Tổng: {total}")
    print(f"Trung bình: {average:.2f}")
    print(f"Giá trị nhỏ nhất: {minimum}")
    print(f"Giá trị lớn nhất: {maximum}")
    print(f"Số phần tử: {len(numbers)}")

# Bài 2: Tìm vị trí min/max
print("\n2. Vị trí min/max:")
min_index = numbers.index(minimum)
max_index = numbers.index(maximum)
print(f"Vị trí số nhỏ nhất ({minimum}): {min_index}")
print(f"Vị trí số lớn nhất ({maximum}): {max_index}")

# Tìm tất cả vị trí min/max
min_positions = [i for i in range(len(numbers)) if numbers[i] == minimum]
max_positions = [i for i in range(len(numbers)) if numbers[i] == maximum]
print(f"Tất cả vị trí min: {min_positions}")
print(f"Tất cả vị trí max: {max_positions}")

# Bài 3: Phân loại số
print("\n3. Phân loại số:")
positive = [x for x in numbers if x > 0]
negative = [x for x in numbers if x < 0]
zero = [x for x in numbers if x == 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

print(f"Số dương: {positive} (có {len(positive)} số)")
print(f"Số âm: {negative} (có {len(negative)} số)")
print(f"Số 0: {zero} (có {len(zero)} số)")
print(f"Số chẵn: {even} (có {len(even)} số)")
print(f"Số lẻ: {odd} (có {len(odd)} số)")

# Bài 4: Tìm kiếm
print("\n4. Tìm kiếm:")
target = int(input("Nhập số cần tìm: "))

if target in numbers:
    first_pos = numbers.index(target)
    count = numbers.count(target)
    all_positions = [i for i in range(len(numbers)) if numbers[i] == target]
    
    print(f"Tìm thấy {target}!")
    print(f"Vị trí đầu tiên: {first_pos}")
    print(f"Số lần xuất hiện: {count}")
    print(f"Tất cả vị trí: {all_positions}")
else:
    print(f"Không tìm thấy {target} trong list")

# Bài 5: Tìm số gần nhất
print("\n5. Tìm số gần nhất với target:")
closest = numbers[0]
min_diff = abs(numbers[0] - target)

for num in numbers:
    diff = abs(num - target)
    if diff < min_diff:
        min_diff = diff
        closest = num

print(f"Số gần nhất với {target}: {closest} (chênh lệch {min_diff})")