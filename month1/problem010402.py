# Problem 01.04.02: Máy tính đơn giản
print("=== MÁY TÍNH ĐƠN GIẢN ===")

# Nhập hai số
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

# Tính toán
sum_result = num1 + num2
diff_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "Không thể chia cho 0"

# In kết quả
print(f"\nKết quả:")
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {diff_result}")
print(f"{num1} × {num2} = {mul_result}")
print(f"{num1} ÷ {num2} = {div_result}")