# Problem 05.03.01: Tìm kiếm với else

print("=== TÌM KIẾM VỚI ELSE ===")

# Bài 1: Tìm kiếm trong danh sách
def linear_search_with_else(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            print(f"Tìm thấy {target} tại vị trí {i}")
            break
    else:
        print(f"Không tìm thấy {target} trong danh sách")
        return -1
    return i

numbers = [10, 25, 33, 47, 52, 68, 74, 89, 96]
print(f"Danh sách: {numbers}")

target = int(input("Nhập số cần tìm: "))
position = linear_search_with_else(numbers, target)

# Bài 2: Kiểm tra số nguyên tố với else
def check_prime_with_else(n):
    if n < 2:
        print(f"{n} không là số nguyên tố (< 2)")
        return False
    
    print(f"Kiểm tra {n} có phải số nguyên tố...")
    for i in range(2, int(n**0.5) + 1):
        print(f"  Kiểm tra chia hết cho {i}: ", end="")
        if n % i == 0:
            print(f"Có! {n} = {i} × {n//i}")
            print(f"➜ {n} không là số nguyên tố")
            return False
        print("Không")
    else:
        print(f"➜ {n} là số nguyên tố!")
        return True

number = int(input("Nhập số cần kiểm tra: "))
is_prime = check_prime_with_else(number)

# Bài 3: Tìm tất cả số nguyên tố trong khoảng
def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    
    return primes

start = int(input("Nhập số bắt đầu: "))
end = int(input("Nhập số kết thúc: "))
primes = find_primes_in_range(start, end)
print(f"Các số nguyên tố từ {start} đến {end}: {primes}")
print(f"Tổng cộng: {len(primes)} số nguyên tố")

# Bài 4: Validation với else
def get_valid_input():
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        try:
            value = int(input(f"Nhập số nguyên (còn {max_attempts - attempts} lần thử): "))
            if value >= 0:
                print(f"✅ Nhập thành công: {value}")
                return value
            else:
                print("❌ Số phải không âm!")
        except ValueError:
            print("❌ Vui lòng nhập số nguyên!")
        
        attempts += 1
    else:
        print("❌ Đã hết số lần thử!")
        return None

result = get_valid_input()
if result is not None:
    print(f"Giá trị cuối cùng: {result}")