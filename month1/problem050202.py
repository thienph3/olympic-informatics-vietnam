# Problem 05.02.02: Game đoán số với break/continue

import random

print("=== GAME ĐOÁN SỐ VỚI BREAK/CONTINUE ===")

# Thiết lập game
min_num = 1
max_num = 100
max_attempts = 7
play_again = True

while play_again:
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"\n🎮 Game mới bắt đầu!")
    print(f"Tôi đã nghĩ ra một số từ {min_num} đến {max_num}")
    print(f"Bạn có {max_attempts} lần đoán")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nLần đoán {attempts + 1}: "))
            attempts += 1
            
            # Kiểm tra phạm vi
            if guess < min_num or guess > max_num:
                print(f"❌ Số phải trong khoảng {min_num}-{max_num}!")
                continue  # Không tính vào số lần đoán
            
            # Kiểm tra kết quả
            if guess == secret_number:
                print(f"🎉 Chúc mừng! Bạn đã đoán đúng số {secret_number}")
                
                # Đánh giá hiệu suất
                if attempts == 1:
                    print("🏆 Xuất sắc! Đoán đúng ngay lần đầu!")
                elif attempts <= 3:
                    print("👍 Rất tốt!")
                elif attempts <= 5:
                    print("😊 Khá tốt!")
                else:
                    print("😅 Cuối cùng cũng đoán đúng!")
                break
                
            elif guess < secret_number:
                print("📈 Số cần tìm lớn hơn")
            else:
                print("📉 Số cần tìm nhỏ hơn")
            
            # Gợi ý khi còn ít lần đoán
            remaining = max_attempts - attempts
            if remaining == 1:
                print("⚠️ Đây là cơ hội cuối cùng!")
            elif remaining == 2:
                print("⚠️ Chỉ còn 2 lần đoán!")
                
        except ValueError:
            print("❌ Vui lòng nhập một số nguyên!")
            attempts -= 1  # Không tính lần nhập sai
            continue
    
    else:
        # Chỉ chạy khi vòng while kết thúc bình thường (không break)
        print(f"\n💔 Hết lượt đoán! Số đúng là {secret_number}")
    
    # Hỏi chơi lại
    while True:
        play_choice = input("\nBạn có muốn chơi lại? (y/n): ").lower().strip()
        if play_choice in ['y', 'yes', 'có']:
            play_again = True
            break
        elif play_choice in ['n', 'no', 'không']:
            play_again = False
            break
        else:
            print("Vui lòng nhập 'y' hoặc 'n'")
            continue

print("Cảm ơn bạn đã chơi! 👋")