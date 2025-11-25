# Problem 05.01.02: Xử lý số học với while

print("=== XỬ LÝ SỐ HỌC VỚI WHILE ===")

# Bài 1: Đảo ngược số
def reverse_number(n):
    reversed_num = 0
    n = abs(n)  # Lấy giá trị tuyệt đối
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

number = int(input("Nhập một số: "))
reversed_num = reverse_number(number)
print(f"Số đảo ngược của {number}: {reversed_num}")

# Bài 2: Kiểm tra số palindrome
def is_palindrome_number(n):
    return n == reverse_number(n)

if is_palindrome_number(abs(number)):
    print(f"{number} là số palindrome")
else:
    print(f"{number} không là số palindrome")

# Bài 3: Tính tổng các chữ số
def sum_of_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total

digit_sum = sum_of_digits(number)
print(f"Tổng các chữ số của {number}: {digit_sum}")

# Bài 4: Tìm ước chung lớn nhất (GCD)
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhập số thứ nhất cho GCD: "))
b = int(input("Nhập số thứ hai cho GCD: "))
result = gcd(a, b)
print(f"GCD({a}, {b}) = {result}")

# Bài 5: Dãy Fibonacci
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    return fib

n = int(input("Nhập số lượng số Fibonacci cần tạo: "))
fib_sequence = fibonacci_sequence(n)
print(f"{n} số Fibonacci đầu tiên: {fib_sequence}")