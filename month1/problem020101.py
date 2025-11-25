# Problem 02.01.01: Máy tính nâng cao
print("=== MÁY TÍNH NÂNG CAO ===")

# Nhập số
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Các phép toán
print(f"\nKết quả các phép toán:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} × {b} = {a * b}")
print(f"{a} ÷ {b} = {a / b if b != 0 else 'Không thể chia cho 0'}")
print(f"{a} ÷ {b} (nguyên) = {a // b if b != 0 else 'Không thể chia cho 0'}")
print(f"{a} % {b} = {a % b if b != 0 else 'Không thể chia cho 0'}")
print(f"{a} ^ {b} = {a ** b}")