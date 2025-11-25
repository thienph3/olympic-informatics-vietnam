# Problem 06.04.02: Ứng dụng tổng hợp

print("=== ỨNG DỤNG TỔNG HỢP ===")

# Bài 1: Phân tích dữ liệu bán hàng
def analyze_sales_data(daily_sales):
    """Phân tích dữ liệu bán hàng hàng ngày"""
    n = len(daily_sales)
    if n == 0:
        return {}
    
    # Thống kê cơ bản
    total_sales = sum(daily_sales)
    average_sales = total_sales / n
    max_sales = max(daily_sales)
    min_sales = min(daily_sales)
    
    # Tìm ngày có doanh thu cao nhất và thấp nhất
    max_day = daily_sales.index(max_sales)
    min_day = daily_sales.index(min_sales)
    
    # Tìm streak tăng trưởng dài nhất
    max_growth_streak = 0
    current_streak = 0
    growth_start = 0
    max_growth_start = 0
    
    for i in range(1, n):
        if daily_sales[i] > daily_sales[i-1]:
            if current_streak == 0:
                growth_start = i - 1
            current_streak += 1
        else:
            if current_streak > max_growth_streak:
                max_growth_streak = current_streak
                max_growth_start = growth_start
            current_streak = 0
    
    # Kiểm tra lần cuối
    if current_streak > max_growth_streak:
        max_growth_streak = current_streak
        max_growth_start = growth_start
    
    # Tìm chu kỳ (nếu có)
    def find_weekly_pattern():
        if n < 14:  # Cần ít nhất 2 tuần
            return None
        
        # Kiểm tra pattern 7 ngày
        for start_day in range(7):
            is_pattern = True
            for week in range(1, n // 7):
                for day in range(7):
                    if start_day + week * 7 + day >= n:
                        break
                    if abs(daily_sales[start_day + day] - daily_sales[start_day + week * 7 + day]) > average_sales * 0.1:
                        is_pattern = False
                        break
                if not is_pattern:
                    break
            
            if is_pattern:
                return start_day
        
        return None
    
    weekly_pattern_start = find_weekly_pattern()
    
    return {
        'total_sales': total_sales,
        'average_sales': average_sales,
        'max_sales': max_sales,
        'min_sales': min_sales,
        'max_day': max_day,
        'min_day': min_day,
        'max_growth_streak': max_growth_streak,
        'growth_streak_start': max_growth_start,
        'has_weekly_pattern': weekly_pattern_start is not None,
        'weekly_pattern_start': weekly_pattern_start
    }

# Dữ liệu bán hàng mẫu (30 ngày)
sales_data = [
    120, 135, 142, 158, 165, 180, 95,   # Tuần 1
    125, 140, 145, 160, 170, 185, 100, # Tuần 2
    130, 145, 150, 165, 175, 190, 105, # Tuần 3
    135, 150, 155, 170, 180, 195, 110, # Tuần 4
    140, 155                            # 2 ngày tuần 5
]

analysis = analyze_sales_data(sales_data)

print("PHÂN TÍCH DỮ LIỆU BÁN HÀNG:")
print(f"Tổng doanh thu 30 ngày: ${analysis['total_sales']:,.2f}")
print(f"Doanh thu trung bình/ngày: ${analysis['average_sales']:,.2f}")
print(f"Doanh thu cao nhất: ${analysis['max_sales']:,.2f} (ngày {analysis['max_day'] + 1})")
print(f"Doanh thu thấp nhất: ${analysis['min_sales']:,.2f} (ngày {analysis['min_day'] + 1})")
print(f"Streak tăng trưởng dài nhất: {analysis['max_growth_streak']} ngày")
print(f"Có pattern tuần: {'Có' if analysis['has_weekly_pattern'] else 'Không'}")

# Vẽ biểu đồ đơn giản
print(f"\nBIỂU ĐỒ DOANH THU (mỗi * = $10):")
for i, sales in enumerate(sales_data):
    stars = "*" * (sales // 10)
    print(f"Ngày {i+1:2d}: {stars} (${sales})")

# Bài 2: Trò chơi tìm kho báu
def treasure_hunt_game():
    """Game tìm kho báu với gợi ý"""
    import random
    
    # Tạo bản đồ 10x10
    size = 10
    treasure_row = random.randint(0, size - 1)
    treasure_col = random.randint(0, size - 1)
    
    print(f"\n=== TRÒ CHƠI TÌM KHO BÁU ===")
    print(f"Kho báu được giấu trong bản đồ {size}×{size}")
    print("Nhập tọa độ (hàng cột) để tìm kho báu")
    print("Gợi ý: H (Hot - gần), W (Warm - trung bình), C (Cold - xa)")
    
    attempts = 0
    max_attempts = 15
    
    while attempts < max_attempts:
        try:
            row = int(input(f"Nhập hàng (0-{size-1}): "))
            col = int(input(f"Nhập cột (0-{size-1}): "))
            
            if not (0 <= row < size and 0 <= col < size):
                print("Tọa độ không hợp lệ!")
                continue
            
            attempts += 1
            
            # Tính khoảng cách Manhattan
            distance = abs(row - treasure_row) + abs(col - treasure_col)
            
            if distance == 0:
                print(f"🎉 CHÚC MỪNG! Bạn đã tìm thấy kho báu!")
                print(f"Số lần thử: {attempts}")
                
                # Tính điểm
                score = max(0, 100 - attempts * 5)
                print(f"Điểm số: {score}")
                break
            else:
                # Đưa ra gợi ý
                if distance <= 2:
                    hint = "🔥 HOT - Rất gần rồi!"
                elif distance <= 4:
                    hint = "🌡️ WARM - Khá gần"
                elif distance <= 6:
                    hint = "❄️ COOL - Hơi xa"
                else:
                    hint = "🧊 COLD - Rất xa"
                
                print(f"Lần thử {attempts}: {hint}")
                print(f"Còn lại {max_attempts - attempts} lần thử")
                
                # Gợi ý hướng (sau 5 lần thử)
                if attempts >= 5:
                    if row < treasure_row:
                        row_hint = "xuống dưới"
                    elif row > treasure_row:
                        row_hint = "lên trên"
                    else:
                        row_hint = "đúng hàng"
                    
                    if col < treasure_col:
                        col_hint = "sang phải"
                    elif col > treasure_col:
                        col_hint = "sang trái"
                    else:
                        col_hint = "đúng cột"
                    
                    print(f"Gợi ý hướng: {row_hint}, {col_hint}")
        
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    
    else:
        print(f"💔 Hết lượt thử! Kho báu ở vị trí ({treasure_row}, {treasure_col})")

# Chạy game
play_game = input("Bạn có muốn chơi game tìm kho báu? (y/n): ").lower()
if play_game in ['y', 'yes', 'có']:
    treasure_hunt_game()