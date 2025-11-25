# Problem 03.01.02: Kiểm tra tính hợp lệ

print("=== KIỂM TRA TÍNH HỢP LỆ ===")

# Kiểm tra mật khẩu
password = input("Nhập mật khẩu: ")

if len(password) >= 8:
    print("✓ Mật khẩu đủ dài")

if password.isupper():
    print("⚠ Mật khẩu toàn chữ hoa")

if password.islower():
    print("⚠ Mật khẩu toàn chữ thường")

if password.isdigit():
    print("⚠ Mật khẩu toàn số")

if password.isalnum():
    print("✓ Mật khẩu chỉ chứa chữ và số")

# Kiểm tra email đơn giản
email = input("Nhập email: ")

if "@" in email:
    print("✓ Email có chứa @")

if "." in email:
    print("✓ Email có chứa dấu chấm")

if email.count("@") == 1:
    print("✓ Email chỉ có một @")

if len(email) >= 5:
    print("✓ Email đủ dài")

# Kiểm tra số điện thoại
phone = input("Nhập số điện thoại: ")

if phone.isdigit():
    print("✓ Số điện thoại chỉ chứa số")

if len(phone) == 10:
    print("✓ Số điện thoại có 10 chữ số")

if phone.startswith("0"):
    print("✓ Số điện thoại bắt đầu bằng 0")