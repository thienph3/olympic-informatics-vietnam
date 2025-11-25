# Problem 04.02.02: Xử lý danh sách số

print("=== XỬ LÝ DANH SÁCH SỐ ===")

# Nhập danh sách số
numbers = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    num = int(input(f"Nhập số thứ {i+1}: "))
    numbers.append(num)

print(f"Danh sách: {numbers}")

# Tính các thống kê
total = 0
positive_count = 0
negative_count = 0
zero_count = 0
even_count = 0
odd_count = 0

for num in numbers:
    total += num
    
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / len(numbers) if numbers else 0

print(f"\nThống kê:")
print(f"Tổng: {total}")
print(f"Trung bình: {average:.2f}")
print(f"Số dương: {positive_count}")
print(f"Số âm: {negative_count}")
print(f"Số 0: {zero_count}")
print(f"Số chẵn: {even_count}")
print(f"Số lẻ: {odd_count}")

# Tìm min, max và vị trí
if numbers:
    min_val = max_val = numbers[0]
    min_positions = [0]
    max_positions = [0]
    
    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]
            min_positions = [i]
        elif numbers[i] == min_val:
            min_positions.append(i)
        
        if numbers[i] > max_val:
            max_val = numbers[i]
            max_positions = [i]
        elif numbers[i] == max_val:
            max_positions.append(i)
    
    print(f"Giá trị nhỏ nhất: {min_val} tại vị trí {min_positions}")
    print(f"Giá trị lớn nhất: {max_val} tại vị trí {max_positions}")