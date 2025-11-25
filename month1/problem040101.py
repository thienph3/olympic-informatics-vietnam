# Problem 04.01.01: Tính toán cơ bản với for

print("=== TÍNH TOÁN CƠ BẢN VỚI FOR ===")

# Bài 1: Tính tổng các số chẵn từ 1 đến n
n = int(input("Nhập n: "))
even_sum = 0
for i in range(2, n + 1, 2):  # Chỉ lấy số chẵn
    even_sum += i
print(f"Tổng các số chẵn từ 1 đến {n}: {even_sum}")

# Bài 2: Tính tổng bình phương
square_sum = 0
for i in range(1, n + 1):
    square_sum += i ** 2
print(f"Tổng bình phương từ 1 đến {n}: {square_sum}")

# Bài 3: Đếm số chia hết cho 3
count_div3 = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count_div3 += 1
print(f"Số lượng số chia hết cho 3 từ 1 đến {n}: {count_div3}")

# Bài 4: Tìm số lớn nhất chia hết cho 7
largest_div7 = 0
for i in range(n, 0, -1):  # Duyệt ngược từ n về 1
    if i % 7 == 0:
        largest_div7 = i
        break
print(f"Số lớn nhất ≤ {n} chia hết cho 7: {largest_div7}")