# Problem 04.04.02: Xử lý dãy số và pattern

print("=== PHÂN TÍCH DÃY SỐ ===")

# Nhập dãy số
sequence = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    num = int(input(f"Nhập số thứ {i+1}: "))
    sequence.append(num)

print(f"Dãy số: {sequence}")

# Phân tích dãy số
print("\n=== PHÂN TÍCH ===")

# 1. Kiểm tra dãy tăng/giảm
is_increasing = True
is_decreasing = True
is_non_decreasing = True
is_non_increasing = True

for i in range(1, len(sequence)):
    if sequence[i] <= sequence[i-1]:
        is_increasing = False
    if sequence[i] >= sequence[i-1]:
        is_decreasing = False
    if sequence[i] < sequence[i-1]:
        is_non_decreasing = False
    if sequence[i] > sequence[i-1]:
        is_non_increasing = False

print(f"Dãy tăng nghiêm ngặt: {'Có' if is_increasing else 'Không'}")
print(f"Dãy giảm nghiêm ngặt: {'Có' if is_decreasing else 'Không'}")
print(f"Dãy không giảm: {'Có' if is_non_decreasing else 'Không'}")
print(f"Dãy không tăng: {'Có' if is_non_increasing else 'Không'}")

# 2. Tìm dãy con tăng dài nhất
max_length = 1
current_length = 1
max_start = 0
current_start = 0

for i in range(1, len(sequence)):
    if sequence[i] > sequence[i-1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            max_start = current_start
        current_length = 1
        current_start = i

# Kiểm tra lần cuối
if current_length > max_length:
    max_length = current_length
    max_start = current_start

longest_increasing = sequence[max_start:max_start + max_length]
print(f"Dãy con tăng dài nhất: {longest_increasing} (độ dài: {max_length})")

# 3. Tìm peak và valley
peaks = []  # Đỉnh (lớn hơn cả 2 bên)
valleys = []  # Thung lũng (nhỏ hơn cả 2 bên)

for i in range(1, len(sequence) - 1):
    if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1]:
        peaks.append((i, sequence[i]))
    elif sequence[i] < sequence[i-1] and sequence[i] < sequence[i+1]:
        valleys.append((i, sequence[i]))

print(f"Các đỉnh (peaks): {peaks}")
print(f"Các thung lũng (valleys): {valleys}")

# 4. Tìm chu kỳ lặp
def find_period(seq):
    n = len(seq)
    for period in range(1, n // 2 + 1):
        is_periodic = True
        for i in range(period, n):
            if seq[i] != seq[i % period]:
                is_periodic = False
                break
        if is_periodic:
            return period
    return 0

period = find_period(sequence)
if period > 0:
    print(f"Dãy có chu kỳ: {period}")
    print(f"Mẫu lặp: {sequence[:period]}")
else:
    print("Dãy không có chu kỳ")

# 5. Thống kê tần suất
frequency = {}
for num in sequence:
    frequency[num] = frequency.get(num, 0) + 1

print(f"\nThống kê tần suất:")
for num, count in sorted(frequency.items()):
    print(f"Số {num}: xuất hiện {count} lần")

# Tìm mode (số xuất hiện nhiều nhất)
max_freq = max(frequency.values())
modes = [num for num, freq in frequency.items() if freq == max_freq]
print(f"Mode (số xuất hiện nhiều nhất): {modes} ({max_freq} lần)")