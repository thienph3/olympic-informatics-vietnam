# Problem 07.02.01: Slicing cơ bản và nâng cao

print("=== SLICING CƠ BẢN VÀ NÂNG CAO ===")

# Tạo list mẫu
numbers = list(range(0, 20))  # [0, 1, 2, ..., 19]
print(f"List gốc: {numbers}")

# Bài 1: Slicing cơ bản
print("\n1. Slicing cơ bản:")
print(f"numbers[5:10] = {numbers[5:10]}")
print(f"numbers[:8] = {numbers[:8]}")
print(f"numbers[12:] = {numbers[12:]}")
print(f"numbers[:] = {numbers[:]}")

# Bài 2: Slicing với step
print("\n2. Slicing với step:")
print(f"numbers[::2] = {numbers[::2]}")  # Số chẵn index
print(f"numbers[1::2] = {numbers[1::2]}")  # Số lẻ index
print(f"numbers[::3] = {numbers[::3]}")  # Bước nhảy 3
print(f"numbers[2::4] = {numbers[2::4]}")  # Từ index 2, bước 4

# Bài 3: Slicing với index âm
print("\n3. Slicing với index âm:")
print(f"numbers[-5:] = {numbers[-5:]}")  # 5 phần tử cuối
print(f"numbers[:-5] = {numbers[:-5]}")  # Bỏ 5 phần tử cuối
print(f"numbers[-10:-3] = {numbers[-10:-3]}")  # Từ -10 đến -4
print(f"numbers[-1::-1] = {numbers[-1::-1]}")  # Đảo ngược từ cuối

# Bài 4: Đảo ngược và pattern
print("\n4. Đảo ngược và pattern:")
print(f"Đảo ngược toàn bộ: {numbers[::-1]}")
print(f"Đảo ngược từ 15 về 5: {numbers[15:5:-1]}")
print(f"Lấy ngược mỗi 2 phần tử: {numbers[::-2]}")
print(f"Từ giữa ra 2 bên: {numbers[10:5:-1] + numbers[10:15]}")

# Bài 5: Ứng dụng slicing
print("\n5. Ứng dụng slicing:")

# Chia đôi list
mid = len(numbers) // 2
left_half = numbers[:mid]
right_half = numbers[mid:]
print(f"Nửa trái: {left_half}")
print(f"Nửa phải: {right_half}")

# Lấy phần tử ở vị trí chẵn và lẻ
even_positions = numbers[::2]
odd_positions = numbers[1::2]
print(f"Vị trí chẵn: {even_positions}")
print(f"Vị trí lẻ: {odd_positions}")

# Lấy 3 đầu, 3 cuối, phần giữa
first_3 = numbers[:3]
last_3 = numbers[-3:]
middle = numbers[3:-3]
print(f"3 đầu: {first_3}")
print(f"3 cuối: {last_3}")
print(f"Phần giữa: {middle}")

# Bài 6: Kiểm tra palindrome bằng slicing
print("\n6. Kiểm tra palindrome:")
test_lists = [
    [1, 2, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [7, 8, 9, 8, 7],
    [1, 2, 2, 1]
]

for test_list in test_lists:
    is_palindrome = test_list == test_list[::-1]
    print(f"{test_list}: {'Palindrome' if is_palindrome else 'Không phải palindrome'}")

# Bài 7: Tạo pattern với slicing
print("\n7. Tạo pattern với slicing:")
pattern_list = list(range(1, 11))  # [1, 2, 3, ..., 10]
print(f"Gốc: {pattern_list}")
print(f"Xen kẽ từ đầu: {pattern_list[::2] + pattern_list[1::2]}")
print(f"Đảo từng cặp: {pattern_list[1::2] + pattern_list[::2]}")
print(f"Zigzag: {pattern_list[:5] + pattern_list[9:4:-1]}")