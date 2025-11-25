# Problem 02.04.02: Bài toán hình học
import math

print("=== TÍNH TOÁN HÌNH HỌC ===")

print("1. Hình tròn")
r = float(input("Nhập bán kính: "))
circle_area = math.pi * r**2
circle_perimeter = 2 * math.pi * r
print(f"Diện tích: {circle_area:.2f}")
print(f"Chu vi: {circle_perimeter:.2f}")

print("\n2. Tam giác vuông")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = math.sqrt(a**2 + b**2)  # Định lý Pythagoras
triangle_area = 0.5 * a * b
print(f"Cạnh huyền c: {c:.2f}")
print(f"Diện tích: {triangle_area:.2f}")

print("\n3. Hình cầu")
r_sphere = float(input("Nhập bán kính hình cầu: "))
sphere_volume = (4/3) * math.pi * r_sphere**3
sphere_surface = 4 * math.pi * r_sphere**2
print(f"Thể tích: {sphere_volume:.2f}")
print(f"Diện tích bề mặt: {sphere_surface:.2f}")