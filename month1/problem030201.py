# Problem 03.02.01: Hệ thống xếp loại

print("=== HỆ THỐNG XẾP LOẠI ===")

# Xếp loại học sinh
math_score = float(input("Điểm Toán: "))
physics_score = float(input("Điểm Lý: "))
chemistry_score = float(input("Điểm Hóa: "))

average = (math_score + physics_score + chemistry_score) / 3

print(f"\nĐiểm trung bình: {average:.2f}")

if average >= 9.0:
    classification = "Xuất sắc"
    scholarship = "Học bổng toàn phần"
elif average >= 8.0:
    classification = "Giỏi"
    scholarship = "Học bổng 50%"
elif average >= 6.5:
    classification = "Khá"
    scholarship = "Không có học bổng"
elif average >= 5.0:
    classification = "Trung bình"
    scholarship = "Không có học bổng"
else:
    classification = "Yếu"
    scholarship = "Cần học lại"

print(f"Xếp loại: {classification}")
print(f"Học bổng: {scholarship}")

# Kiểm tra điều kiện đặc biệt
if math_score < 5.0 or physics_score < 5.0 or chemistry_score < 5.0:
    print("⚠ Cảnh báo: Có môn dưới trung bình!")

if math_score == physics_score == chemistry_score:
    print("🎯 Đặc biệt: Điểm các môn đều bằng nhau!")