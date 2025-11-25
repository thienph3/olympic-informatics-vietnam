# Problem 02.04.03: Kiểm tra số nguyên tố
import math

def is_prime(n):
    """Kiểm tra số nguyên tố"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Chỉ cần kiểm tra đến √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Tìm tất cả số nguyên tố trong khoảng"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print("=== KIỂM TRA SỐ NGUYÊN TỐ ===")

# Kiểm tra một số
n = int(input("Nhập số cần kiểm tra: "))
if is_prime(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không là số nguyên tố")

# Tìm số nguyên tố trong khoảng
start = int(input("Nhập số bắt đầu: "))
end = int(input("Nhập số kết thúc: "))

primes = find_primes_in_range(start, end)
print(f"Các số nguyên tố từ {start} đến {end}: {primes}")
print(f"Tổng cộng: {len(primes)} số nguyên tố")