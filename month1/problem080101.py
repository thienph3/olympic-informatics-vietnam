# Problem 08.01.01: List comprehension cơ bản

print("=== LIST COMPREHENSION CƠ BẢN ===")

# Bài 1: Tạo list với comprehension
print("1. Tạo list với comprehension:")

# Bình phương từ 0 đến 9
squares = [x**2 for x in range(10)]
print(f"Bình phương 0-9: {squares}")

# Số chẵn từ 0 đến 20
evens = [x for x in range(21) if x % 2 == 0]
print(f"Số chẵn 0-20: {evens}")

# Số lẻ từ 1 đến 15
odds = [x for x in range(1, 16) if x % 2 == 1]
print(f"Số lẻ 1-15: {odds}")

# Bài 2: Xử lý chuỗi
print("\n2. Xử lý chuỗi:")
words = ["python", "java", "javascript", "go", "rust"]
print(f"Từ gốc: {words}")

# Viết hoa chữ cái đầu
capitalized = [word.capitalize() for word in words]
print(f"Viết hoa: {capitalized}")

# Lọc từ có độ dài > 4
long_words = [word for word in words if len(word) > 4]
print(f"Từ dài > 4: {long_words}")

# Độ dài của từng từ
lengths = [len(word) for word in words]
print(f"Độ dài: {lengths}")

# Bài 3: Biến đổi số học
print("\n3. Biến đổi số học:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Số gốc: {numbers}")

# Nhân đôi
doubled = [x * 2 for x in numbers]
print(f"Nhân đôi: {doubled}")

# Lập phương số lẻ
odd_cubes = [x**3 for x in numbers if x % 2 == 1]
print(f"Lập phương số lẻ: {odd_cubes}")

# Chia hết cho 3
div_by_3 = [x for x in numbers if x % 3 == 0]
print(f"Chia hết cho 3: {div_by_3}")

# Bài 4: Chuyển đổi kiểu dữ liệu
print("\n4. Chuyển đổi kiểu dữ liệu:")

# String sang int
str_numbers = ["10", "20", "30", "40", "50"]
int_numbers = [int(x) for x in str_numbers]
print(f"String: {str_numbers}")
print(f"Integer: {int_numbers}")

# Float sang int (làm tròn)
float_numbers = [1.7, 2.3, 3.8, 4.1, 5.9]
rounded = [round(x) for x in float_numbers]
print(f"Float: {float_numbers}")
print(f"Rounded: {rounded}")

# Bài 5: Lọc và biến đổi kết hợp
print("\n5. Lọc và biến đổi kết hợp:")
grades = [85, 92, 78, 96, 88, 76, 94, 82, 90, 87]
print(f"Điểm gốc: {grades}")

# Điểm >= 85, cộng thêm 5 điểm thưởng
bonus_grades = [grade + 5 for grade in grades if grade >= 85]
print(f"Điểm >= 85 + 5 thưởng: {bonus_grades}")

# Phân loại điểm
classifications = ["Giỏi" if grade >= 85 else "Khá" if grade >= 70 else "Trung bình" 
                  for grade in grades]
print(f"Phân loại: {classifications}")

# Bài 6: Xử lý với range
print("\n6. Xử lý với range:")

# Bảng cửu chương 5
table_5 = [5 * i for i in range(1, 11)]
print(f"Bảng cửu chương 5: {table_5}")

# Số Fibonacci đầu tiên (dùng comprehension đơn giản)
fib_simple = [1, 1] + [0 for _ in range(8)]  # Khởi tạo
for i in range(2, 10):
    fib_simple[i] = fib_simple[i-1] + fib_simple[i-2]
print(f"Fibonacci 10 số đầu: {fib_simple}")

# Số nguyên tố đơn giản (kiểm tra từ 2 đến 30)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 31) if is_prime(x)]
print(f"Số nguyên tố 2-30: {primes}")

# Bài 7: Nested range
print("\n7. Nested range:")

# Tọa độ trong lưới 3x3
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"Tọa độ 3x3: {coordinates}")

# Tích Cartesian của 2 list
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
products = [f"{color}-{size}" for color in colors for size in sizes]
print(f"Sản phẩm: {products}")