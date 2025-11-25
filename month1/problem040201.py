# Problem 04.02.01: Xử lý chuỗi

print("=== XỬ LÝ CHUỖI ===")

text = input("Nhập một chuỗi: ")

# Đếm các loại ký tự
vowels = "aeiouAEIOU"
consonants = 0
vowel_count = 0
digits = 0
spaces = 0
special_chars = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_chars += 1

print(f"\nThống kê chuỗi '{text}':")
print(f"Nguyên âm: {vowel_count}")
print(f"Phụ âm: {consonants}")
print(f"Chữ số: {digits}")
print(f"Khoảng trắng: {spaces}")
print(f"Ký tự đặc biệt: {special_chars}")
print(f"Tổng ký tự: {len(text)}")

# Kiểm tra palindrome
clean_text = ""
for char in text:
    if char.isalnum():
        clean_text += char.lower()

is_palindrome = True
for i in range(len(clean_text) // 2):
    if clean_text[i] != clean_text[len(clean_text) - 1 - i]:
        is_palindrome = False
        break

print(f"Là palindrome: {'Có' if is_palindrome else 'Không'}")

# Đảo ngược chuỗi
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print(f"Chuỗi đảo ngược: '{reversed_text}'")