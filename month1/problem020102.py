# Problem 02.01.02: Thao tác với chữ số
print("=== THAO TÁC VỚI CHỮ SỐ ===")

n = int(input("Nhập một số nguyên: "))

# Phân tích số
print(f"\nPhân tích số {n}:")
print(f"Chữ số cuối: {n % 10}")
print(f"Bỏ chữ số cuối: {n // 10}")
print(f"Số chẵn hay lẻ: {'Chẵn' if n % 2 == 0 else 'Lẻ'}")

# Đếm chữ số
temp = abs(n)  # Lấy giá trị tuyệt đối
count = 0
if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10
print(f"Số chữ số: {count}")