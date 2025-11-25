# Problem 08.01.02: Biến đổi và lọc dữ liệu

print("=== BIẾN ĐỔI VÀ LỌC DỮ LIỆU ===")

# Bài 1: Xử lý danh sách học sinh
print("1. Xử lý danh sách học sinh:")
students = [
    {"name": "An", "age": 16, "grade": 85},
    {"name": "Bình", "age": 17, "grade": 92},
    {"name": "Cường", "age": 16, "grade": 78},
    {"name": "Dung", "age": 17, "grade": 96},
    {"name": "Em", "age": 16, "grade": 88}
]

# Lấy tên học sinh
names = [student["name"] for student in students]
print(f"Tên học sinh: {names}")

# Học sinh điểm >= 85
good_students = [student["name"] for student in students if student["grade"] >= 85]
print(f"Học sinh giỏi (>=85): {good_students}")

# Tuổi trung bình
ages = [student["age"] for student in students]
avg_age = sum(ages) / len(ages)
print(f"Tuổi trung bình: {avg_age:.1f}")

# Thông tin tóm tắt
summary = [f"{s['name']}: {s['grade']} điểm" for s in students]
print(f"Tóm tắt: {summary}")

# Bài 2: Xử lý dữ liệu sản phẩm
print("\n2. Xử lý dữ liệu sản phẩm:")
products = [
    {"name": "Laptop", "price": 1000, "category": "Electronics"},
    {"name": "Phone", "price": 500, "category": "Electronics"},
    {"name": "Book", "price": 20, "category": "Education"},
    {"name": "Headphones", "price": 100, "category": "Electronics"},
    {"name": "Notebook", "price": 5, "category": "Education"}
]

# Sản phẩm Electronics
electronics = [p["name"] for p in products if p["category"] == "Electronics"]
print(f"Sản phẩm Electronics: {electronics}")

# Giá sau thuế (10%)
prices_with_tax = [p["price"] * 1.1 for p in products]
print(f"Giá sau thuế: {prices_with_tax}")

# Sản phẩm đắt (>= 100)
expensive = [f"{p['name']}: ${p['price']}" for p in products if p["price"] >= 100]
print(f"Sản phẩm đắt: {expensive}")

# Bài 3: Xử lý chuỗi văn bản
print("\n3. Xử lý chuỗi văn bản:")
text = "Python is a powerful programming language for data science"
words = text.split()
print(f"Câu gốc: {text}")
print(f"Từ: {words}")

# Từ có độ dài >= 5
long_words = [word for word in words if len(word) >= 5]
print(f"Từ dài >= 5: {long_words}")

# Từ chứa chữ 'a'
words_with_a = [word for word in words if 'a' in word.lower()]
print(f"Từ chứa 'a': {words_with_a}")

# Viết hoa từ đầu tiên của mỗi từ
capitalized_words = [word.capitalize() for word in words]
print(f"Viết hoa: {' '.join(capitalized_words)}")

# Độ dài từng từ
word_lengths = [f"{word}({len(word)})" for word in words]
print(f"Độ dài từ: {word_lengths}")

# Bài 4: Xử lý số liệu thống kê
print("\n4. Xử lý số liệu thống kê:")
temperatures = [22.5, 25.1, 19.8, 30.2, 18.7, 26.9, 23.4, 28.1, 21.3, 24.6]
print(f"Nhiệt độ (°C): {temperatures}")

# Chuyển sang Fahrenheit
fahrenheit = [temp * 9/5 + 32 for temp in temperatures]
print(f"Fahrenheit: {[f'{f:.1f}' for f in fahrenheit]}")

# Nhiệt độ trong khoảng 20-25°C
comfortable = [temp for temp in temperatures if 20 <= temp <= 25]
print(f"Nhiệt độ dễ chịu (20-25°C): {comfortable}")

# Phân loại nhiệt độ
categories = ["Lạnh" if t < 20 else "Dễ chịu" if t <= 25 else "Nóng" 
             for t in temperatures]
print(f"Phân loại: {categories}")

# Bài 5: Xử lý dữ liệu bán hàng
print("\n5. Xử lý dữ liệu bán hàng:")
sales_data = [120, 150, 180, 200, 170, 190, 220, 240, 210, 180, 160, 140]
months = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12"]

# Tháng có doanh thu > 180
good_months = [months[i] for i in range(len(sales_data)) if sales_data[i] > 180]
print(f"Tháng doanh thu > 180: {good_months}")

# Tăng trưởng so với tháng trước
growth = [sales_data[i] - sales_data[i-1] for i in range(1, len(sales_data))]
print(f"Tăng trưởng hàng tháng: {growth}")

# Tháng tăng trưởng dương
positive_growth_months = [months[i+1] for i in range(len(growth)) if growth[i] > 0]
print(f"Tháng tăng trưởng dương: {positive_growth_months}")

# Bài 6: Ma trận đơn giản
print("\n6. Ma trận đơn giản:")

# Tạo ma trận 3x3 với giá trị i*j
matrix = [[i*j for j in range(3)] for i in range(3)]
print("Ma trận 3x3 (i*j):")
for row in matrix:
    print(row)

# Lấy đường chéo chính
diagonal = [matrix[i][i] for i in range(3)]
print(f"Đường chéo chính: {diagonal}")

# Flatten ma trận
flattened = [element for row in matrix for element in row]
print(f"Ma trận flatten: {flattened}")

# Bài 7: Xử lý email
print("\n7. Xử lý email:")
emails = [
    "user1@gmail.com",
    "admin@company.org", 
    "test@yahoo.com",
    "info@company.org",
    "user2@hotmail.com"
]

# Lấy tên domain
domains = [email.split('@')[1] for email in emails]
print(f"Domains: {domains}")

# Email từ company.org
company_emails = [email for email in emails if email.endswith('@company.org')]
print(f"Email công ty: {company_emails}")

# Tên người dùng
usernames = [email.split('@')[0] for email in emails]
print(f"Usernames: {usernames}")

# Email có username dài > 4
long_username_emails = [email for email in emails if len(email.split('@')[0]) > 4]
print(f"Email username dài > 4: {long_username_emails}")