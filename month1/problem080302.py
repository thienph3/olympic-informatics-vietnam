# Problem 08.03.02: Xử lý dữ liệu 2D

print("=== XỬ LÝ DỮ LIỆU 2D ===")

# Bài 1: Bảng điểm học sinh
print("1. Bảng điểm học sinh:")

# Dữ liệu: [Toán, Lý, Hóa, Sinh, Văn]
students_scores = [
    [8.5, 7.0, 8.0, 7.5, 9.0],  # An
    [9.0, 8.5, 7.5, 8.0, 8.5],  # Bình  
    [7.0, 6.5, 7.5, 7.0, 8.0],  # Cường
    [9.5, 9.0, 9.0, 8.5, 9.5],  # Dung
    [8.0, 7.5, 8.5, 8.0, 8.5]   # Em
]

subjects = ["Toán", "Lý", "Hóa", "Sinh", "Văn"]
student_names = ["An", "Bình", "Cường", "Dung", "Em"]

print("Bảng điểm:")
print(f"{'Tên':8}", end="")
for subject in subjects:
    print(f"{subject:6}", end="")
print(f"{'TB':6}")

for i, scores in enumerate(students_scores):
    avg = sum(scores) / len(scores)
    print(f"{student_names[i]:8}", end="")
    for score in scores:
        print(f"{score:6.1f}", end="")
    print(f"{avg:6.1f}")

# Điểm trung bình từng môn
subject_averages = [sum(students_scores[i][j] for i in range(len(students_scores))) / len(students_scores) 
                   for j in range(len(subjects))]
print(f"\nĐiểm TB từng môn:")
for i, subject in enumerate(subjects):
    print(f"{subject}: {subject_averages[i]:.2f}")

# Học sinh có điểm TB cao nhất
student_averages = [sum(scores) / len(scores) for scores in students_scores]
best_student_idx = student_averages.index(max(student_averages))
print(f"Học sinh giỏi nhất: {student_names[best_student_idx]} ({student_averages[best_student_idx]:.2f})")

# Bài 2: Ma trận ảnh (grayscale)
print("\n2. Xử lý ảnh grayscale:")

# Tạo ảnh mẫu 5x5 (giá trị 0-255)
image = [
    [100, 120, 140, 120, 100],
    [120, 200, 220, 200, 120],
    [140, 220, 255, 220, 140],
    [120, 200, 220, 200, 120],
    [100, 120, 140, 120, 100]
]

def print_image(img, title="Ảnh"):
    print(f"{title}:")
    for row in img:
        for pixel in row:
            print(f"{pixel:3d}", end=" ")
        print()

print_image(image, "Ảnh gốc")

# Tính histogram
def calculate_histogram(img):
    histogram = {}
    for row in img:
        for pixel in row:
            histogram[pixel] = histogram.get(pixel, 0) + 1
    return histogram

hist = calculate_histogram(image)
print(f"Histogram: {dict(sorted(hist.items()))}")

# Áp dụng threshold
def apply_threshold(img, threshold):
    return [[255 if pixel >= threshold else 0 for pixel in row] for row in img]

binary_image = apply_threshold(image, 150)
print_image(binary_image, "Ảnh nhị phân (threshold=150)")

# Tìm pixel sáng nhất và tối nhất
def find_extremes(img):
    flat = [pixel for row in img for pixel in row]
    return min(flat), max(flat)

min_pixel, max_pixel = find_extremes(image)
print(f"Pixel tối nhất: {min_pixel}, sáng nhất: {max_pixel}")

# Bài 3: Dữ liệu bán hàng theo tháng
print("\n3. Dữ liệu bán hàng:")

# Dữ liệu bán hàng 4 sản phẩm x 12 tháng
sales_data = [
    [120, 130, 125, 140, 135, 150, 160, 155, 145, 140, 135, 130],  # Sản phẩm A
    [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],     # Sản phẩm B  
    [200, 195, 210, 205, 220, 215, 230, 225, 240, 235, 250, 245], # Sản phẩm C
    [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]         # Sản phẩm D
]

products = ["Sản phẩm A", "Sản phẩm B", "Sản phẩm C", "Sản phẩm D"]
months = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12"]

# In bảng dữ liệu
print("Doanh số bán hàng:")
print(f"{'Sản phẩm':12}", end="")
for month in months:
    print(f"{month:6}", end="")
print(f"{'Tổng':8}")

for i, product in enumerate(products):
    total = sum(sales_data[i])
    print(f"{product:12}", end="")
    for sales in sales_data[i]:
        print(f"{sales:6}", end="")
    print(f"{total:8}")

# Doanh số theo tháng
monthly_totals = [sum(sales_data[i][j] for i in range(len(products))) 
                 for j in range(len(months))]
print(f"\nDoanh số theo tháng:")
for i, month in enumerate(months):
    print(f"{month}: {monthly_totals[i]}")

# Sản phẩm bán chạy nhất
product_totals = [sum(sales) for sales in sales_data]
best_product_idx = product_totals.index(max(product_totals))
print(f"Sản phẩm bán chạy nhất: {products[best_product_idx]} ({product_totals[best_product_idx]})")

# Tháng có doanh số cao nhất
best_month_idx = monthly_totals.index(max(monthly_totals))
print(f"Tháng bán chạy nhất: {months[best_month_idx]} ({monthly_totals[best_month_idx]})")

# Bài 4: Lưới tọa độ và khoảng cách
print("\n4. Lưới tọa độ:")

# Tạo lưới 5x5 với khoảng cách từ tâm
size = 5
center = size // 2
distance_grid = [[abs(i - center) + abs(j - center) for j in range(size)] 
                for i in range(size)]

print("Khoảng cách Manhattan từ tâm:")
for row in distance_grid:
    print(row)

# Tìm các điểm có khoảng cách = 2
points_distance_2 = [(i, j) for i in range(size) for j in range(size) 
                    if distance_grid[i][j] == 2]
print(f"Điểm có khoảng cách = 2 từ tâm: {points_distance_2}")

# Tạo pattern hình tròn
circle_grid = [["*" if distance_grid[i][j] <= 2 else " " for j in range(size)] 
              for i in range(size)]
print("Pattern hình tròn (khoảng cách <= 2):")
for row in circle_grid:
    print(" ".join(row))

# Bài 5: Xử lý nhiệt độ theo vùng
print("\n5. Nhiệt độ theo vùng:")

# Nhiệt độ 4 vùng x 7 ngày
temperature_data = [
    [22, 24, 26, 28, 27, 25, 23],  # Vùng Bắc
    [28, 30, 32, 34, 33, 31, 29],  # Vùng Trung
    [26, 28, 30, 32, 31, 29, 27],  # Vùng Nam
    [24, 26, 28, 30, 29, 27, 25]   # Vùng Tây Nguyên
]

regions = ["Bắc", "Trung", "Nam", "Tây Nguyên"]
days = ["T2", "T3", "T4", "T5", "T6", "T7", "CN"]

print("Nhiệt độ theo vùng và ngày:")
print(f"{'Vùng':12}", end="")
for day in days:
    print(f"{day:4}", end="")
print(f"{'TB':6}")

for i, region in enumerate(regions):
    avg_temp = sum(temperature_data[i]) / len(temperature_data[i])
    print(f"{region:12}", end="")
    for temp in temperature_data[i]:
        print(f"{temp:4}", end="")
    print(f"{avg_temp:6.1f}")

# Ngày nóng nhất và lạnh nhất
daily_averages = [sum(temperature_data[i][j] for i in range(len(regions))) / len(regions) 
                 for j in range(len(days))]
hottest_day_idx = daily_averages.index(max(daily_averages))
coldest_day_idx = daily_averages.index(min(daily_averages))

print(f"\nNgày nóng nhất: {days[hottest_day_idx]} ({daily_averages[hottest_day_idx]:.1f}°C)")
print(f"Ngày lạnh nhất: {days[coldest_day_idx]} ({daily_averages[coldest_day_idx]:.1f}°C)")

# Vùng có nhiệt độ trung bình cao nhất
region_averages = [sum(temps) / len(temps) for temps in temperature_data]
hottest_region_idx = region_averages.index(max(region_averages))
print(f"Vùng nóng nhất: {regions[hottest_region_idx]} ({region_averages[hottest_region_idx]:.1f}°C)")