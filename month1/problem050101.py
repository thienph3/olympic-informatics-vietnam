# Problem 05.01.01: Validation input với while

print("=== VALIDATION INPUT VỚI WHILE ===")

# Bài 1: Nhập số trong khoảng
print("1. Nhập số trong khoảng [1, 100]")
number = 0
while number < 1 or number > 100:
    try:
        number = int(input("Nhập số (1-100): "))
        if number < 1 or number > 100:
            print("❌ Số phải trong khoảng 1-100!")
    except ValueError:
        print("❌ Vui lòng nhập số nguyên!")
        number = 0

print(f"✅ Số hợp lệ: {number}")

# Bài 2: Nhập mật khẩu mạnh
print("\n2. Nhập mật khẩu mạnh")
password = ""
while True:
    password = input("Nhập mật khẩu: ")
    
    # Kiểm tra độ dài
    if len(password) < 8:
        print("❌ Mật khẩu phải có ít nhất 8 ký tự!")
        continue
    
    # Kiểm tra có chữ hoa
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        print("❌ Mật khẩu phải có ít nhất 1 chữ hoa!")
        continue
    
    # Kiểm tra có chữ thường
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        print("❌ Mật khẩu phải có ít nhất 1 chữ thường!")
        continue
    
    # Kiểm tra có số
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        print("❌ Mật khẩu phải có ít nhất 1 chữ số!")
        continue
    
    # Nếu đến đây thì mật khẩu hợp lệ
    print("✅ Mật khẩu mạnh!")
    break