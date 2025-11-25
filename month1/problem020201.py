# Problem 02.02.01: Kiểm tra điều kiện
print("=== KIỂM TRA ĐIỀU KIỆN ===")

# Nhập thông tin
age = int(input("Nhập tuổi: "))
height = float(input("Nhập chiều cao (cm): "))
weight = float(input("Nhập cân nặng (kg): "))

# Tính BMI
bmi = weight / ((height / 100) ** 2)

# Kiểm tra các điều kiện
is_adult = age >= 18
is_senior = age >= 60
is_normal_bmi = 18.5 <= bmi <= 24.9
is_tall = height >= 170

print(f"\nKết quả:")
print(f"Tuổi: {age} ({'Người lớn' if is_adult else 'Trẻ em'})")
print(f"BMI: {bmi:.2f} ({'Bình thường' if is_normal_bmi else 'Không bình thường'})")
print(f"Chiều cao: {height}cm ({'Cao' if is_tall else 'Trung bình'})")
print(f"Người cao tuổi: {'Có' if is_senior else 'Không'}")