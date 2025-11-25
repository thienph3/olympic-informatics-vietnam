# Problem 07.02.02: Ứng dụng slicing trong xử lý dữ liệu

print("=== ỨNG DỤNG SLICING TRONG XỬ LÝ DỮ LIỆU ===")

# Bài 1: Xử lý chuỗi với slicing
print("1. Xử lý chuỗi:")
text = "Python Programming Language"
words = text.split()
print(f"Chuỗi gốc: {text}")
print(f"Danh sách từ: {words}")

# Slicing với words
print(f"Từ đầu tiên: {words[0]}")
print(f"Từ cuối cùng: {words[-1]}")
print(f"2 từ đầu: {words[:2]}")
print(f"Đảo ngược từ: {words[::-1]}")
print(f"Chuỗi đảo ngược: {' '.join(words[::-1])}")

# Bài 2: Phân tích dữ liệu bán hàng
print("\n2. Phân tích dữ liệu bán hàng:")
sales_data = [120, 150, 180, 200, 170, 190, 220, 240, 210, 180, 160, 140]
months = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12"]

print(f"Doanh thu 12 tháng: {sales_data}")

# Phân tích theo quý
q1 = sales_data[:3]    # Quý 1
q2 = sales_data[3:6]   # Quý 2  
q3 = sales_data[6:9]   # Quý 3
q4 = sales_data[9:]    # Quý 4

print(f"Quý 1 (T1-T3): {q1}, Tổng: {sum(q1)}")
print(f"Quý 2 (T4-T6): {q2}, Tổng: {sum(q2)}")
print(f"Quý 3 (T7-T9): {q3}, Tổng: {sum(q3)}")
print(f"Quý 4 (T10-T12): {q4}, Tổng: {sum(q4)}")

# Phân tích nửa năm
first_half = sales_data[:6]
second_half = sales_data[6:]
print(f"Nửa đầu năm: {sum(first_half)}")
print(f"Nửa cuối năm: {sum(second_half)}")

# Bài 3: Xử lý ma trận với slicing
print("\n3. Xử lý ma trận:")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Ma trận gốc:")
for row in matrix:
    print(row)

# Lấy hàng và cột
print(f"Hàng đầu tiên: {matrix[0]}")
print(f"Hàng cuối cùng: {matrix[-1]}")
print(f"Cột đầu tiên: {[row[0] for row in matrix]}")
print(f"Cột cuối cùng: {[row[-1] for row in matrix]}")

# Lấy submatrix
print(f"Submatrix 2x2 góc trái trên: {[row[:2] for row in matrix[:2]]}")
print(f"Submatrix 2x2 góc phải dưới: {[row[2:] for row in matrix[2:]]}")

# Đường chéo
main_diagonal = [matrix[i][i] for i in range(len(matrix))]
anti_diagonal = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]
print(f"Đường chéo chính: {main_diagonal}")
print(f"Đường chéo phụ: {anti_diagonal}")

# Bài 4: Sliding window
print("\n4. Sliding window:")
data = [1, 4, 2, 9, 5, 10, 7, 8, 6, 3]
window_size = 3

print(f"Dữ liệu: {data}")
print(f"Sliding window size {window_size}:")

# Tính trung bình sliding window
for i in range(len(data) - window_size + 1):
    window = data[i:i + window_size]
    avg = sum(window) / len(window)
    print(f"Window {i+1}: {window} -> Trung bình: {avg:.2f}")

# Tìm window có tổng lớn nhất
max_sum = float('-inf')
best_window = []
best_start = 0

for i in range(len(data) - window_size + 1):
    window = data[i:i + window_size]
    window_sum = sum(window)
    if window_sum > max_sum:
        max_sum = window_sum
        best_window = window
        best_start = i

print(f"Window có tổng lớn nhất: {best_window} (tổng: {max_sum}, vị trí: {best_start})")

# Bài 5: Xử lý dãy số với pattern
print("\n5. Xử lý dãy số với pattern:")
sequence = list(range(1, 21))  # 1 đến 20
print(f"Dãy gốc: {sequence}")

# Tách thành các nhóm
group_size = 4
groups = [sequence[i:i+group_size] for i in range(0, len(sequence), group_size)]
print(f"Chia thành nhóm {group_size}: {groups}")

# Xen kẽ 2 nửa
mid = len(sequence) // 2
first_half = sequence[:mid]
second_half = sequence[mid:]
interleaved = []
for i in range(mid):
    interleaved.extend([first_half[i], second_half[i]])
print(f"Xen kẽ 2 nửa: {interleaved}")

# Tạo pattern zigzag
zigzag = sequence[::2] + sequence[1::2][::-1]
print(f"Pattern zigzag: {zigzag}")