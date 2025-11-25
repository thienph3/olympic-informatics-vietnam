# Problem 02.04.01: Máy tính khoa học
import math

print("=== MÁY TÍNH KHOA HỌC ===")

# Nhập số
x = float(input("Nhập số x: "))

print(f"\nCác phép toán với x = {x}:")
print(f"Căn bậc hai: √{x} = {math.sqrt(abs(x))}")
print(f"Bình phương: {x}² = {x**2}")
print(f"Lập phương: {x}³ = {x**3}")
print(f"Giá trị tuyệt đối: |{x}| = {abs(x)}")
print(f"Làm tròn lên: ⌈{x}⌉ = {math.ceil(x)}")
print(f"Làm tròn xuống: ⌊{x}⌋ = {math.floor(x)}")

if x > 0:
    print(f"Logarithm tự nhiên: ln({x}) = {math.log(x)}")
    print(f"Logarithm cơ số 10: log₁₀({x}) = {math.log10(x)}")

# Lượng giác (nếu x trong khoảng hợp lý)
if -10 <= x <= 10:
    print(f"\nHàm lượng giác (x tính bằng radian):")
    print(f"sin({x}) = {math.sin(x):.4f}")
    print(f"cos({x}) = {math.cos(x):.4f}")
    print(f"tan({x}) = {math.tan(x):.4f}")