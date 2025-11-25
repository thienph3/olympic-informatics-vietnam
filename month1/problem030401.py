# Problem 03.04.01: Hệ thống login

print("=== HỆ THỐNG ĐĂNG NHẬP ===")

# Database giả lập
users = {
    "admin": {"password": "admin123", "role": "administrator"},
    "user1": {"password": "pass123", "role": "user"},
    "guest": {"password": "guest", "role": "guest"}
}

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Tên đăng nhập: ").strip()
    password = input("Mật khẩu: ").strip()
    
    # Kiểm tra username tồn tại
    if username not in users:
        print("❌ Tên đăng nhập không tồn tại!")
        attempts += 1
        remaining = max_attempts - attempts
        
        if remaining > 0:
            print(f"Còn lại {remaining} lần thử")
        continue
    
    # Kiểm tra password
    if users[username]["password"] != password:
        print("❌ Mật khẩu không đúng!")
        attempts += 1
        remaining = max_attempts - attempts
        
        if remaining > 0:
            print(f"Còn lại {remaining} lần thử")
        continue
    
    # Đăng nhập thành công
    role = users[username]["role"]
    print(f"✅ Đăng nhập thành công!")
    print(f"Chào mừng {username} ({role})")
    
    # Hiển thị menu theo role
    if role == "administrator":
        print("\n🔧 Menu Admin:")
        print("1. Quản lý người dùng")
        print("2. Xem báo cáo hệ thống")
        print("3. Cấu hình hệ thống")
    elif role == "user":
        print("\n👤 Menu User:")
        print("1. Xem thông tin cá nhân")
        print("2. Thay đổi mật khẩu")
        print("3. Xem lịch sử")
    else:  # guest
        print("\n👥 Menu Guest:")
        print("1. Xem thông tin công khai")
        print("2. Liên hệ hỗ trợ")
    
    break
else:
    print("🚫 Đã hết số lần thử. Tài khoản bị khóa!")