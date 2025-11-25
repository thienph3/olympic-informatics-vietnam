# Problem 05.04.02: Chuyển đổi hệ số và xử lý bit

print("=== CHUYỂN ĐỔI HỆ SỐ ===")

# Bài 1: Chuyển đổi giữa các hệ số
def decimal_to_base(decimal, base):
    if decimal == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while decimal > 0:
        result = digits[decimal % base] + result
        decimal //= base
    
    return result

def base_to_decimal(number_str, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decimal = 0
    power = 0
    i = len(number_str) - 1
    
    while i >= 0:
        digit_value = digits.index(number_str[i].upper())
        decimal += digit_value * (base ** power)
        power += 1
        i -= 1
    
    return decimal

# Test chuyển đổi
number = int(input("Nhập số thập phân: "))
print(f"Số {number} trong các hệ:")
print(f"Nhị phân (base 2): {decimal_to_base(number, 2)}")
print(f"Bát phân (base 8): {decimal_to_base(number, 8)}")
print(f"Thập lục phân (base 16): {decimal_to_base(number, 16)}")

# Chuyển ngược
binary_str = input("Nhập số nhị phân: ")
decimal_from_binary = base_to_decimal(binary_str, 2)
print(f"Số nhị phân {binary_str} = {decimal_from_binary} (thập phân)")

# Bài 2: Thao tác bit
def count_set_bits(n):
    """Đếm số bit 1"""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def reverse_bits(n, num_bits=8):
    """Đảo ngược bit"""
    result = 0
    i = 0
    while i < num_bits:
        if n & (1 << i):
            result |= (1 << (num_bits - 1 - i))
        i += 1
    return result

def is_power_of_two(n):
    """Kiểm tra có phải lũy thừa của 2"""
    return n > 0 and (n & (n - 1)) == 0

number = int(input("Nhập số để thao tác bit: "))
binary_repr = decimal_to_base(number, 2)
print(f"Số {number} = {binary_repr} (nhị phân)")
print(f"Số bit 1: {count_set_bits(number)}")
print(f"Đảo ngược 8 bit: {reverse_bits(number, 8)} = {decimal_to_base(reverse_bits(number, 8), 2)}")
print(f"Có phải lũy thừa của 2: {'Có' if is_power_of_two(number) else 'Không'}")

# Bài 3: Thuật toán Gray Code
def decimal_to_gray(n):
    """Chuyển đổi sang Gray code"""
    return n ^ (n >> 1)

def gray_to_decimal(gray):
    """Chuyển đổi từ Gray code"""
    decimal = gray
    while gray:
        gray >>= 1
        decimal ^= gray
    return decimal

def generate_gray_sequence(n):
    """Tạo dãy Gray code n bit"""
    sequence = []
    total = 1 << n  # 2^n
    i = 0
    
    while i < total:
        gray = decimal_to_gray(i)
        binary = decimal_to_base(gray, 2).zfill(n)
        sequence.append((i, gray, binary))
        i += 1
    
    return sequence

n_bits = int(input("Nhập số bit cho Gray code: "))
gray_sequence = generate_gray_sequence(n_bits)

print(f"Dãy Gray code {n_bits} bit:")
print("Decimal | Gray | Binary")
print("-" * 25)
for decimal, gray, binary in gray_sequence:
    print(f"{decimal:7d} | {gray:4d} | {binary}")