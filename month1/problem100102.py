"""
Problem 100102: Functions cho tính toán
Viết functions tính toán: diện tích, chu vi, phép toán cơ bản

Bài 1: Geometry Functions
- Tính diện tích và chu vi các hình
- Functions cho hình học không gian

Bài 2: Mathematical Functions
- Phép toán nâng cao
- Functions xử lý số
"""

import math

# Geometry Functions
def rectangle_area(length, width):
    """Tính diện tích hình chữ nhật"""
    return length * width

def rectangle_perimeter(length, width):
    """Tính chu vi hình chữ nhật"""
    return 2 * (length + width)

def circle_area(radius):
    """Tính diện tích hình tròn"""
    return math.pi * radius ** 2

def circle_circumference(radius):
    """Tính chu vi hình tròn"""
    return 2 * math.pi * radius

def triangle_area(base, height):
    """Tính diện tích tam giác"""
    return 0.5 * base * height

def triangle_area_heron(a, b, c):
    """Tính diện tích tam giác bằng công thức Heron"""
    s = (a + b + c) / 2  # Nửa chu vi
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def sphere_volume(radius):
    """Tính thể tích hình cầu"""
    return (4/3) * math.pi * radius ** 3

def cylinder_volume(radius, height):
    """Tính thể tích hình trụ"""
    return math.pi * radius ** 2 * height

# Mathematical Functions
def power(base, exponent):
    """Tính lũy thừa"""
    return base ** exponent

def square_root(number):
    """Tính căn bậc hai"""
    if number < 0:
        return "Cannot calculate square root of negative number"
    return math.sqrt(number)

def absolute_value(number):
    """Tính giá trị tuyệt đối"""
    return abs(number)

def factorial(n):
    """Tính giai thừa"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a, b):
    """Tính ước chung lớn nhất"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Tính bội chung nhỏ nhất"""
    return abs(a * b) // gcd(a, b)

def is_perfect_square(n):
    """Kiểm tra số chính phương"""
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def sum_of_digits(n):
    """Tính tổng các chữ số"""
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n):
    """Đảo ngược số"""
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

def celsius_to_fahrenheit(celsius):
    """Chuyển độ C sang độ F"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Chuyển độ F sang độ C"""
    return (fahrenheit - 32) * 5/9

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Geometry Functions ===")
    
    # Test rectangle
    length, width = 5, 3
    print(f"Rectangle {length}x{width}:")
    print(f"  Area: {rectangle_area(length, width)}")
    print(f"  Perimeter: {rectangle_perimeter(length, width)}")
    
    # Test circle
    radius = 4
    print(f"\nCircle radius {radius}:")
    print(f"  Area: {circle_area(radius):.2f}")
    print(f"  Circumference: {circle_circumference(radius):.2f}")
    
    # Test triangle
    base, height = 6, 4
    print(f"\nTriangle base={base}, height={height}:")
    print(f"  Area: {triangle_area(base, height)}")
    
    # Test Heron's formula
    a, b, c = 3, 4, 5
    print(f"\nTriangle sides {a}, {b}, {c}:")
    print(f"  Area (Heron): {triangle_area_heron(a, b, c):.2f}")
    
    # Test 3D shapes
    r = 3
    print(f"\nSphere radius {r}:")
    print(f"  Volume: {sphere_volume(r):.2f}")
    
    h = 5
    print(f"\nCylinder radius={r}, height={h}:")
    print(f"  Volume: {cylinder_volume(r, h):.2f}")
    
    print("\n=== Bài 2: Mathematical Functions ===")
    
    # Test basic math
    print(f"2^8 = {power(2, 8)}")
    print(f"√16 = {square_root(16)}")
    print(f"|-5| = {absolute_value(-5)}")
    
    # Test factorial
    for n in [0, 1, 5, 10]:
        print(f"{n}! = {factorial(n)}")
    
    # Test GCD and LCM
    a, b = 12, 18
    print(f"\nGCD({a}, {b}) = {gcd(a, b)}")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
    
    # Test number properties
    numbers = [16, 17, 25, 30]
    for num in numbers:
        print(f"{num} is perfect square: {is_perfect_square(num)}")
    
    # Test digit operations
    number = 12345
    print(f"\nNumber: {number}")
    print(f"Sum of digits: {sum_of_digits(number)}")
    print(f"Reversed: {reverse_number(number)}")
    
    # Test temperature conversion
    celsius = 25
    fahrenheit = 77
    print(f"\n{celsius}°C = {celsius_to_fahrenheit(celsius):.1f}°F")
    print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.1f}°C")

    print("\n=== Bài tập thực hành ===")
    print("1. Viết function tính diện tích hình thang")
    print("2. Function kiểm tra tam giác hợp lệ")
    print("3. Function tính khoảng cách 2 điểm trong mặt phẳng")
    print("4. Function tìm số Fibonacci thứ n")