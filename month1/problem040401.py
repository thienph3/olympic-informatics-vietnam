# Problem 04.04.01: Bài toán số học Olympic

print("=== BÀI TOÁN SỐ HỌC OLYMPIC ===")

# Bài 1: Tìm tất cả số nguyên tố từ 1 đến n
n = int(input("Nhập n: "))

def sieve_of_eratosthenes(limit):
    """Sàng Eratosthenes tìm số nguyên tố"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

primes = sieve_of_eratosthenes(n)
print(f"Các số nguyên tố từ 1 đến {n}: {primes}")
print(f"Có {len(primes)} số nguyên tố")

# Bài 2: Tìm số hoàn hảo
def is_perfect_number(num):
    if num < 2:
        return False
    
    divisor_sum = 1  # 1 luôn là ước của mọi số > 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:  # Tránh đếm trùng với số chính phương
                divisor_sum += num // i
    
    return divisor_sum == num

print(f"\nCác số hoàn hảo từ 1 đến {n}:")
perfect_numbers = []
for i in range(1, n + 1):
    if is_perfect_number(i):
        perfect_numbers.append(i)
        print(f"{i} là số hoàn hảo")

if not perfect_numbers:
    print("Không có số hoàn hảo nào trong khoảng này")

# Bài 3: Tìm cặp số có tổng bằng target
target = int(input(f"\nNhập số target để tìm cặp số có tổng bằng target: "))
pairs = []

for i in range(1, target):
    j = target - i
    if i < j and j <= n:  # Tránh trùng lặp và j trong phạm vi
        pairs.append((i, j))

print(f"Các cặp số có tổng bằng {target}:")
for pair in pairs:
    print(f"{pair[0]} + {pair[1]} = {target}")