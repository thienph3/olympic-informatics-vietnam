# Problem 05.04.01: Thuật toán số học Olympic

print("=== THUẬT TOÁN SỐ HỌC OLYMPIC ===")

# Bài 1: Thuật toán Euclidean mở rộng
def extended_gcd(a, b):
    """Tìm GCD và các hệ số x, y sao cho ax + by = gcd(a, b)"""
    if b == 0:
        return a, 1, 0
    
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    return old_r, old_s, old_t  # gcd, x, y

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

gcd, x, y = extended_gcd(a, b)
print(f"GCD({a}, {b}) = {gcd}")
print(f"Phương trình: {a} × {x} + {b} × {y} = {gcd}")

# Verification
result = a * x + b * y
print(f"Kiểm tra: {a} × {x} + {b} × {y} = {result}")

# Bài 2: Tìm số Armstrong trong khoảng
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def is_armstrong_number(n):
    original = n
    num_digits = count_digits(n)
    sum_powers = 0
    
    while n > 0:
        digit = n % 10
        sum_powers += digit ** num_digits
        n //= 10
    
    return sum_powers == original

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    current = start
    
    while current <= end:
        if is_armstrong_number(current):
            armstrong_numbers.append(current)
        current += 1
    
    return armstrong_numbers

start = int(input("Nhập số bắt đầu: "))
end = int(input("Nhập số kết thúc: "))

armstrong_nums = find_armstrong_numbers(start, end)
print(f"Các số Armstrong từ {start} đến {end}: {armstrong_nums}")

# In chi tiết
for num in armstrong_nums:
    digits = []
    temp = num
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    digits.reverse()
    
    num_digits = len(digits)
    calculation = " + ".join([f"{d}^{num_digits}" for d in digits])
    print(f"{num} = {calculation} = {sum(d**num_digits for d in digits)}")