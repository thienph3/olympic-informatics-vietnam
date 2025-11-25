# Problem 02.03.02: Thao tác bit
print("=== THAO TÁC BIT ===")

# Nhập số
n = int(input("Nhập một số nguyên dương: "))

print(f"\nSố {n} trong hệ nhị phân: {bin(n)}")

# Các thao tác bit
print(f"\nCác thao tác bit:")
print(f"Dịch trái 1 bit: {n} << 1 = {n << 1}")
print(f"Dịch phải 1 bit: {n} >> 1 = {n >> 1}")
print(f"AND với 15: {n} & 15 = {n & 15}")
print(f"OR với 15: {n} | 15 = {n | 15}")
print(f"XOR với 15: {n} ^ 15 = {n ^ 15}")

# Đếm bit 1
def count_ones(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

print(f"Số bit 1 trong {n}: {count_ones(n)}")

# Kiểm tra bit tại vị trí
pos = int(input("Nhập vị trí bit cần kiểm tra (0-indexed): "))
bit_value = (n >> pos) & 1
print(f"Bit tại vị trí {pos}: {bit_value}")