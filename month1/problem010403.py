# Problem 01.04.03: Thông tin học sinh
print("=== THÔNG TIN HỌC SINH ===")

# Nhập thông tin
full_name = input("Họ và tên: ")
class_name = input("Lớp: ")
math_score = float(input("Điểm Toán: "))
physics_score = float(input("Điểm Lý: "))
chemistry_score = float(input("Điểm Hóa: "))

# Tính điểm trung bình
average = (math_score + physics_score + chemistry_score) / 3

# Xếp loại
if average >= 8.5:
    rank = "Giỏi"
elif average >= 7.0:
    rank = "Khá"
elif average >= 5.0:
    rank = "Trung bình"
else:
    rank = "Yếu"

# In kết quả
print("\n" + "="*50)
print(f"HỌC SINH: {full_name.upper()}")
print(f"Lớp: {class_name}")
print(f"Điểm các môn: Toán={math_score}, Lý={physics_score}, Hóa={chemistry_score}")
print(f"Điểm trung bình: {average:.2f}")
print(f"Xếp loại: {rank}")
print("="*50)