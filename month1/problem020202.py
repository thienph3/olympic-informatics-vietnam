# Problem 02.02.02: Logic game
print("=== GAME LOGIC ===")

# Nhập 3 số
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

# Kiểm tra các điều kiện logic
all_positive = (a > 0) and (b > 0) and (c > 0)
all_even = (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
has_zero = (a == 0) or (b == 0) or (c == 0)
ascending = (a < b) and (b < c)
all_equal = (a == b) and (b == c)

print(f"\nKết quả kiểm tra:")
print(f"Tất cả đều dương: {all_positive}")
print(f"Tất cả đều chẵn: {all_even}")
print(f"Có số 0: {has_zero}")
print(f"Tăng dần: {ascending}")
print(f"Tất cả bằng nhau: {all_equal}")