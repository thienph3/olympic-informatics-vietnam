# Problem 06.02.01: Pattern số học nâng cao

print("=== PATTERN SỐ HỌC NÂNG CAO ===")

n = int(input("Nhập kích thước: "))

print("\n1. Tam giác Pascal:")
for i in range(n):
    # In khoảng trắng
    for j in range(n - i - 1):
        print("  ", end="")
    
    # Tính và in số Pascal
    num = 1
    for j in range(i + 1):
        print(f"{num:4d}", end="")
        if j < i:
            num = num * (i - j) // (j + 1)
    print()

print(f"\n2. Dãy Fibonacci trong tam giác:")
# Tạo dãy Fibonacci đủ dài
fib = [0, 1]
total_numbers = n * (n + 1) // 2
while len(fib) < total_numbers:
    fib.append(fib[-1] + fib[-2])

index = 0
for i in range(1, n + 1):
    for j in range(i):
        print(f"{fib[index]:4d}", end=" ")
        index += 1
    print()

print(f"\n3. Tam giác số nguyên tố:")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Tạo danh sách số nguyên tố
primes = []
num = 2
while len(primes) < total_numbers:
    if is_prime(num):
        primes.append(num)
    num += 1

index = 0
for i in range(1, n + 1):
    for j in range(i):
        print(f"{primes[index]:4d}", end=" ")
        index += 1
    print()

print(f"\n4. Pattern số chính phương:")
squares = [i*i for i in range(1, total_numbers + 1)]
index = 0
for i in range(1, n + 1):
    for j in range(i):
        print(f"{squares[index]:4d}", end=" ")
        index += 1
    print()

print(f"\n5. Pattern tổng hàng:")
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, i + 1):
        print(f"{j:3d}", end=" ")
        row_sum += j
    print(f" | Tổng: {row_sum}")