# Problem 08.02.02: Set và Dictionary comprehension

print("=== SET VÀ DICTIONARY COMPREHENSION ===")

# Bài 1: Set comprehension cơ bản
print("1. Set comprehension cơ bản:")

# Loại bỏ trùng lặp và tính bình phương
numbers = [1, 2, 2, 3, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers}
print(f"Số gốc: {numbers}")
print(f"Bình phương không trùng: {unique_squares}")

# Ký tự duy nhất trong chuỗi
text = "hello world"
unique_chars = {char for char in text if char != ' '}
print(f"Chuỗi: '{text}'")
print(f"Ký tự duy nhất: {unique_chars}")

# Số chia hết cho 3 hoặc 5
divisible = {x for x in range(1, 31) if x % 3 == 0 or x % 5 == 0}
print(f"Số chia hết cho 3 hoặc 5 (1-30): {divisible}")

# Bài 2: Dictionary comprehension cơ bản
print("\n2. Dictionary comprehension cơ bản:")

# Từ và độ dài
words = ["python", "java", "javascript", "go", "rust"]
word_lengths = {word: len(word) for word in words}
print(f"Từ và độ dài: {word_lengths}")

# Số và bình phương
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Số và bình phương: {squares_dict}")

# Bảng cửu chương 7
table_7 = {i: 7 * i for i in range(1, 11)}
print(f"Bảng cửu chương 7: {table_7}")

# Bài 3: Lọc với set/dict comprehension
print("\n3. Lọc với set/dict comprehension:")

# Từ dài hơn 4 ký tự
long_words_dict = {word: len(word) for word in words if len(word) > 4}
print(f"Từ dài > 4: {long_words_dict}")

# Số chẵn và lập phương
even_cubes = {x: x**3 for x in range(1, 11) if x % 2 == 0}
print(f"Số chẵn và lập phương: {even_cubes}")

# Ký tự nguyên âm
vowels_in_words = {word: {char for char in word if char in 'aeiou'} 
                   for word in words}
print(f"Nguyên âm trong từ: {vowels_in_words}")

# Bài 4: Xử lý dữ liệu học sinh
print("\n4. Xử lý dữ liệu học sinh:")
students = [
    {"name": "An", "math": 85, "english": 78},
    {"name": "Bình", "math": 92, "english": 88},
    {"name": "Cường", "math": 76, "english": 82},
    {"name": "Dung", "math": 88, "english": 90}
]

# Tên và điểm trung bình
avg_scores = {s["name"]: (s["math"] + s["english"]) / 2 for s in students}
print(f"Điểm trung bình: {avg_scores}")

# Học sinh giỏi toán (>= 85)
good_math = {s["name"]: s["math"] for s in students if s["math"] >= 85}
print(f"Giỏi toán (>=85): {good_math}")

# Tất cả điểm số duy nhất
all_scores = {score for s in students for score in [s["math"], s["english"]]}
print(f"Tất cả điểm số: {sorted(all_scores)}")

# Bài 5: Đảo ngược dictionary
print("\n5. Đảo ngược dictionary:")

# Dictionary gốc
original_dict = {"a": 1, "b": 2, "c": 3, "d": 2}
print(f"Dictionary gốc: {original_dict}")

# Đảo ngược (value -> key)
reversed_dict = {v: k for k, v in original_dict.items()}
print(f"Đảo ngược: {reversed_dict}")

# Nhóm key theo value
grouped = {}
for k, v in original_dict.items():
    if v not in grouped:
        grouped[v] = []
    grouped[v].append(k)
print(f"Nhóm theo value: {grouped}")

# Bài 6: Xử lý văn bản
print("\n6. Xử lý văn bản:")
text = "the quick brown fox jumps over the lazy dog"
words_list = text.split()
print(f"Câu: {text}")

# Đếm tần suất từ
word_count = {word: words_list.count(word) for word in set(words_list)}
print(f"Tần suất từ: {word_count}")

# Từ và ký tự đầu
first_chars = {word: word[0] for word in words_list}
print(f"Ký tự đầu: {first_chars}")

# Độ dài từ duy nhất
unique_lengths = {len(word) for word in words_list}
print(f"Độ dài từ duy nhất: {sorted(unique_lengths)}")

# Bài 7: Ma trận thành dictionary
print("\n7. Ma trận thành dictionary:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Ma trận:")
for row in matrix:
    print(row)

# Tọa độ và giá trị
coord_values = {(i, j): matrix[i][j] 
               for i in range(len(matrix)) 
               for j in range(len(matrix[0]))}
print(f"Tọa độ -> giá trị: {coord_values}")

# Chỉ lấy phần tử lẻ
odd_coords = {(i, j): matrix[i][j] 
             for i in range(len(matrix)) 
             for j in range(len(matrix[0])) 
             if matrix[i][j] % 2 == 1}
print(f"Tọa độ phần tử lẻ: {odd_coords}")

# Bài 8: Xử lý email domains
print("\n8. Xử lý email domains:")
emails = [
    "user1@gmail.com", "admin@company.org", "test@yahoo.com",
    "user2@gmail.com", "info@company.org", "support@yahoo.com"
]

# Đếm email theo domain
domain_count = {}
for email in emails:
    domain = email.split('@')[1]
    domain_count[domain] = domain_count.get(domain, 0) + 1
print(f"Email theo domain: {domain_count}")

# Sử dụng comprehension
domains = [email.split('@')[1] for email in emails]
domain_count_comp = {domain: domains.count(domain) for domain in set(domains)}
print(f"Dùng comprehension: {domain_count_comp}")

# Username theo domain
users_by_domain = {}
for email in emails:
    username, domain = email.split('@')
    if domain not in users_by_domain:
        users_by_domain[domain] = set()
    users_by_domain[domain].add(username)

print(f"Users theo domain: {users_by_domain}")

# Bài 9: Conditional comprehension
print("\n9. Conditional comprehension:")

# Phân loại số
numbers = range(1, 21)
number_types = {n: "even" if n % 2 == 0 else "odd" for n in numbers}
print(f"Phân loại số 1-20: {number_types}")

# Điểm và xếp loại
scores = [85, 92, 78, 96, 88, 76, 94, 82]
grades = {f"Student_{i+1}": "A" if score >= 90 else "B" if score >= 80 else "C" 
         for i, score in enumerate(scores)}
print(f"Xếp loại: {grades}")

# Set các ước số
divisors_sets = {n: {i for i in range(1, n+1) if n % i == 0} for n in range(1, 11)}
print(f"Ước số 1-10: {divisors_sets}")