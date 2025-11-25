# Problem 03.01.01: Kiểm tra điều kiện đơn giản

print("=== KIỂM TRA ĐIỀU KIỆN ĐƠN GIẢN ===")

# Kiểm tra tuổi
age = int(input("Nhập tuổi của bạn: "))

if age >= 18:
    print("Bạn đã trưởng thành")

if age >= 60:
    print("Bạn đã về hưu")

if age < 13:
    print("Bạn còn nhỏ")

# Kiểm tra điểm số
score = float(input("Nhập điểm của bạn (0-10): "))

if score >= 8.0:
    print("Điểm xuất sắc!")

if score >= 6.5:
    print("Điểm khá tốt")

if score < 5.0:
    print("Cần cố gắng hơn")

# Kiểm tra số chẵn lẻ
number = int(input("Nhập một số: "))

if number % 2 == 0:
    print(f"{number} là số chẵn")

if number % 2 == 1:
    print(f"{number} là số lẻ")

if number > 0:
    print(f"{number} là số dương")

if number < 0:
    print(f"{number} là số âm")

if number == 0:
    print("Đây là số 0")