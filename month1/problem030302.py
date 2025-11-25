# Problem 03.03.02: Game đoán số nâng cao

import random

print("=== GAME ĐOÁN SỐ NÂNG CAO ===")

# Thiết lập game
min_num = 1
max_num = 100
secret_number = random.randint(min_num, max_num)
max_attempts = 7
attempts = 0

print(f"Tôi đã nghĩ ra một số từ {min_num} đến {max_num}")
print(f"Bạn có {max_attempts} lần đoán")

while attempts < max_attempts:
    attempts += 1
    
    try:
        guess = int(input(f"\nLần đoán {attempts}: "))
        
        if guess < min_num or guess > max_num:
            print(f"Số phải trong khoảng {min_num}-{max_num}!")
            continue
            
        if guess == secret_number:
            print(f"🎉 Chúc mừng! Bạn đã đoán đúng số {secret_number}")
            
            # Đánh giá hiệu suất
            if attempts == 1:
                print("🏆 Xuất sắc! Đoán đúng ngay lần đầu!")
            elif attempts <= 3:
                print("👍 Rất tốt! Đoán đúng trong 3 lần đầu!")
            elif attempts <= 5:
                print("😊 Khá tốt!")
            else:
                print("😅 Cuối cùng cũng đoán đúng!")
            break
            
        elif guess < secret_number:
            difference = secret_number - guess
            if difference <= 5:
                print("📈 Gần rồi! Số cần tìm lớn hơn một chút")
            elif difference <= 15:
                print("📈 Số cần tìm lớn hơn")
            else:
                print("📈 Số cần tìm lớn hơn nhiều")
                
        else:  # guess > secret_number
            difference = guess - secret_number
            if difference <= 5:
                print("📉 Gần rồi! Số cần tìm nhỏ hơn một chút")
            elif difference <= 15:
                print("📉 Số cần tìm nhỏ hơn")
            else:
                print("📉 Số cần tìm nhỏ hơn nhiều")
        
        # Gợi ý thêm khi còn ít lần đoán
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Còn lại {remaining} lần đoán")
            
            if remaining == 1:
                print("⚠️ Đây là cơ hội cuối cùng!")
            elif remaining == 2:
                print("⚠️ Chỉ còn 2 lần đoán!")
                
    except ValueError:
        print("❌ Vui lòng nhập một số nguyên!")
        
else:
    print(f"\n💔 Hết lượt đoán! Số đúng là {secret_number}")
    print("Chúc bạn may mắn lần sau!")