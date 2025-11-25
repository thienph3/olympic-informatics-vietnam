"""
Problem 100401: Mathematical functions cho Olympic
Implement các functions toán học: GCD, LCM, prime check, factorial

Bài 1: Number Theory Functions
- GCD, LCM, prime numbers
- Perfect numbers, Fibonacci

Bài 2: Combinatorics và Advanced Math
- Permutations, combinations
- Modular arithmetic
"""

import math

# Basic Number Theory
def gcd(a, b):
    """Tính ước chung lớn nhất (Euclidean algorithm)"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Tính bội chung nhỏ nhất"""
    return abs(a * b) // gcd(a, b)

def gcd_multiple(*numbers):
    """GCD của nhiều số"""
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

def lcm_multiple(*numbers):
    """LCM của nhiều số"""
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

# Prime Numbers
def is_prime(n):
    """Kiểm tra số nguyên tố"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    """Tìm số nguyên tố tiếp theo"""
    n += 1
    while not is_prime(n):
        n += 1
    return n

def prime_factors(n):
    """Phân tích thừa số nguyên tố"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def sieve_of_eratosthenes(n):
    """Sàng Eratosthenes tìm tất cả số nguyên tố <= n"""
    if n < 2:
        return []
    
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime_arr[i]:
            for j in range(i * i, n + 1, i):
                is_prime_arr[j] = False
    
    return [i for i in range(2, n + 1) if is_prime_arr[i]]

# Factorial and Related
def factorial(n):
    """Tính giai thừa"""
    if n < 0:
        return None
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_mod(n, mod):
    """Tính giai thừa modulo m"""
    if n < 0:
        return None
    
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

def double_factorial(n):
    """Tính giai thừa kép n!! = n * (n-2) * (n-4) * ..."""
    if n <= 0:
        return 1
    
    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result

# Fibonacci and Special Sequences
def fibonacci(n):
    """Tính số Fibonacci thứ n"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(n):
    """Tạo dãy Fibonacci n số đầu"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def is_perfect_number(n):
    """Kiểm tra số hoàn hảo"""
    if n <= 1:
        return False
    
    divisor_sum = 1  # 1 luôn là ước của n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Tránh đếm trùng với số chính phương
                divisor_sum += n // i
    
    return divisor_sum == n

# Combinatorics
def permutation(n, r):
    """Tính hoán vị P(n,r) = n!/(n-r)!"""
    if r > n or r < 0:
        return 0
    
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result

def combination(n, r):
    """Tính tổ hợp C(n,r) = n!/(r!(n-r)!)"""
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    
    # Tối ưu: C(n,r) = C(n,n-r)
    r = min(r, n - r)
    
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result

def catalan_number(n):
    """Tính số Catalan thứ n"""
    if n <= 1:
        return 1
    
    return combination(2 * n, n) // (n + 1)

# Modular Arithmetic
def power_mod(base, exp, mod):
    """Tính (base^exp) % mod hiệu quả"""
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    
    return result

def mod_inverse(a, m):
    """Tìm nghịch đảo modular của a theo modulo m"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        return None  # Không tồn tại nghịch đảo
    return (x % m + m) % m

def chinese_remainder_theorem(remainders, moduli):
    """Giải hệ đồng dư tuyến tính"""
    if len(remainders) != len(moduli):
        return None
    
    total = 0
    prod = 1
    for m in moduli:
        prod *= m
    
    for r, m in zip(remainders, moduli):
        p = prod // m
        total += r * mod_inverse(p, m) * p
    
    return total % prod

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Number Theory Functions ===")
    
    # Test GCD and LCM
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"LCM(48, 18) = {lcm(48, 18)}")
    print(f"GCD(12, 18, 24) = {gcd_multiple(12, 18, 24)}")
    print(f"LCM(4, 6, 8) = {lcm_multiple(4, 6, 8)}")
    
    # Test prime functions
    primes_up_to_30 = sieve_of_eratosthenes(30)
    print(f"Primes up to 30: {primes_up_to_30}")
    
    test_numbers = [17, 25, 29, 100]
    for num in test_numbers:
        print(f"{num} is prime: {is_prime(num)}")
    
    print(f"Next prime after 20: {next_prime(20)}")
    print(f"Prime factors of 60: {prime_factors(60)}")
    
    # Test factorial
    for n in range(6):
        print(f"{n}! = {factorial(n)}")
    
    print(f"10! mod 7 = {factorial_mod(10, 7)}")
    print(f"5!! = {double_factorial(5)}")
    
    # Test Fibonacci
    print(f"Fibonacci(10) = {fibonacci(10)}")
    print(f"First 10 Fibonacci: {fibonacci_sequence(10)}")
    
    # Test perfect numbers
    perfect_candidates = [6, 28, 12, 496]
    for num in perfect_candidates:
        print(f"{num} is perfect: {is_perfect_number(num)}")
    
    print("\n=== Bài 2: Combinatorics và Advanced Math ===")
    
    # Test combinatorics
    print(f"P(5,3) = {permutation(5, 3)}")
    print(f"C(5,3) = {combination(5, 3)}")
    
    # Catalan numbers
    for i in range(6):
        print(f"Catalan({i}) = {catalan_number(i)}")
    
    # Test modular arithmetic
    print(f"2^10 mod 1000 = {power_mod(2, 10, 1000)}")
    print(f"Mod inverse of 3 mod 7 = {mod_inverse(3, 7)}")
    
    # Chinese Remainder Theorem
    remainders = [2, 3, 2]
    moduli = [3, 5, 7]
    result = chinese_remainder_theorem(remainders, moduli)
    print(f"CRT solution: x ≡ {result} (mod {math.prod(moduli)})")

    print("\n=== Bài tập thực hành ===")
    print("1. Implement Miller-Rabin primality test")
    print("2. Tính Euler's totient function φ(n)")
    print("3. Solve linear Diophantine equations")
    print("4. Generate Pascal's triangle using combinations")