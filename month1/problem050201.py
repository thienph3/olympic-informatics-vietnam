# Problem 05.02.01: Tìm kiếm với break/continue

print("=== TÌM KIẾM VỚI BREAK/CONTINUE ===")

# Bài 1: Tìm số nguyên tố đầu tiên > n
def find_next_prime(n):
    candidate = n + 1
    while True:
        is_prime = True
        if candidate < 2:
            candidate += 1
            continue
        
        # Kiểm tra có phải số nguyên tố
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break
        
        if is_prime:
            return candidate
        candidate += 1

n = int(input("Nhập số n: "))
next_prime = find_next_prime(n)
print(f"Số nguyên tố đầu tiên lớn hơn {n}: {next_prime}")

# Bài 2: Tìm tất cả ước số
def find_all_divisors(n):
    divisors = []
    i = 1
    while i <= n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors

number = int(input("Nhập số cần tìm ước: "))
divisors = find_all_divisors(number)
print(f"Các ước của {number}: {divisors}")

# Bài 3: Tìm phần tử trong danh sách với điều kiện
numbers = [12, 25, 33, 41, 58, 67, 74, 89, 96]
print(f"Danh sách: {numbers}")

# Tìm số chẵn đầu tiên > 50
for num in numbers:
    if num <= 50:
        continue  # Bỏ qua số <= 50
    if num % 2 == 0:  # Số chẵn
        print(f"Số chẵn đầu tiên > 50: {num}")
        break
else:
    print("Không tìm thấy số chẵn > 50")

# Tìm tất cả số lẻ trong khoảng [30, 70]
odd_numbers = []
for num in numbers:
    if num < 30 or num > 70:
        continue  # Bỏ qua số ngoài khoảng
    if num % 2 == 1:  # Số lẻ
        odd_numbers.append(num)

print(f"Số lẻ trong khoảng [30, 70]: {odd_numbers}")