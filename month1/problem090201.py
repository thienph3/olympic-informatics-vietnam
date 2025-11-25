# Problem 09.02.01: String methods cơ bản

print("=== STRING METHODS CƠ BẢN ===")

# Bài 1: Case methods
print("1. Case methods:")
text = "Hello World Python Programming"
print(f"Chuỗi gốc: '{text}'")

print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"title(): '{text.title()}'")
print(f"swapcase(): '{text.swapcase()}'")

# Kiểm tra case
test_strings = ["HELLO", "hello", "Hello World", "hELLO wORLD"]
print("\nKiểm tra case:")
for s in test_strings:
    print(f"'{s}' -> upper: {s.isupper()}, lower: {s.islower()}, title: {s.istitle()}")

# Bài 2: Strip methods
print("\n2. Strip methods:")
messy_text = "   Hello World   "
print(f"Chuỗi gốc: '{messy_text}'")
print(f"strip(): '{messy_text.strip()}'")
print(f"lstrip(): '{messy_text.lstrip()}'")
print(f"rstrip(): '{messy_text.rstrip()}'")

# Strip với ký tự cụ thể
special_text = "***Hello World***"
print(f"Chuỗi đặc biệt: '{special_text}'")
print(f"strip('*'): '{special_text.strip('*')}'")

# Strip nhiều ký tự
mixed_text = " \t\n Hello World \n\t "
print(f"Chuỗi có whitespace: '{repr(mixed_text)}'")
print(f"strip(): '{mixed_text.strip()}'")

# Bài 3: Find và search methods
print("\n3. Find và search methods:")
sentence = "Python is awesome. Python is powerful. Python is easy."
print(f"Câu: '{sentence}'")

# Find methods
print(f"find('Python'): {sentence.find('Python')}")
print(f"rfind('Python'): {sentence.rfind('Python')}")
print(f"find('Java'): {sentence.find('Java')}")

# Count occurrences
print(f"count('Python'): {sentence.count('Python')}")
print(f"count('is'): {sentence.count('is')}")
print(f"count('.'): {sentence.count('.')}")

# Index method (cẩn thận với exception)
try:
    print(f"index('awesome'): {sentence.index('awesome')}")
except ValueError as e:
    print(f"index error: {e}")

# Bài 4: Replace methods
print("\n4. Replace methods:")
original = "I love Java. Java is great. Java programming is fun."
print(f"Gốc: '{original}'")

# Replace tất cả
replaced_all = original.replace("Java", "Python")
print(f"Replace all 'Java' -> 'Python': '{replaced_all}'")

# Replace với limit
replaced_limited = original.replace("Java", "Python", 2)
print(f"Replace first 2 'Java' -> 'Python': '{replaced_limited}'")

# Replace nhiều lần
text_to_clean = "Hello...World...Python"
cleaned = text_to_clean.replace("...", " ")
print(f"Clean '...': '{text_to_clean}' -> '{cleaned}'")

# Bài 5: Validation methods
print("\n5. Validation methods:")
test_cases = [
    "12345",
    "abcdef", 
    "abc123",
    "   ",
    "Hello123",
    "HELLO",
    "hello",
    "Hello World"
]

print("Kiểm tra các chuỗi:")
for test in test_cases:
    print(f"'{test}':")
    print(f"  isdigit(): {test.isdigit()}")
    print(f"  isalpha(): {test.isalpha()}")
    print(f"  isalnum(): {test.isalnum()}")
    print(f"  isspace(): {test.isspace()}")
    print(f"  isupper(): {test.isupper()}")
    print(f"  islower(): {test.islower()}")

# Bài 6: Startswith và endswith
print("\n6. Startswith và endswith:")
filenames = [
    "document.txt",
    "image.jpg", 
    "script.py",
    "data.csv",
    "backup.txt",
    "photo.png"
]

print("Phân loại file:")
for filename in filenames:
    print(f"'{filename}':")
    if filename.endswith('.txt'):
        print("  -> Text file")
    elif filename.endswith(('.jpg', '.png')):
        print("  -> Image file")
    elif filename.endswith('.py'):
        print("  -> Python script")
    elif filename.endswith('.csv'):
        print("  -> CSV data")
    
    if filename.startswith('data'):
        print("  -> Data file")
    elif filename.startswith(('image', 'photo')):
        print("  -> Picture file")

# Bài 7: Split methods
print("\n7. Split methods:")

# Split cơ bản
csv_data = "apple,banana,cherry,date"
fruits = csv_data.split(',')
print(f"CSV: '{csv_data}' -> {fruits}")

# Split với limit
limited_split = csv_data.split(',', 2)
print(f"Split limit 2: {limited_split}")

# Split whitespace
text_with_spaces = "  Python   is    awesome  "
words = text_with_spaces.split()
print(f"Split whitespace: '{text_with_spaces}' -> {words}")

# Splitlines
multiline_text = "Line 1\nLine 2\nLine 3\r\nLine 4"
lines = multiline_text.splitlines()
print(f"Splitlines: {lines}")

# Rsplit (split từ phải)
path = "/home/user/documents/file.txt"
rsplit_result = path.rsplit('/', 1)
print(f"Rsplit path: '{path}' -> {rsplit_result}")

# Bài 8: Join method
print("\n8. Join method:")

# Join cơ bản
word_list = ["Python", "is", "awesome"]
sentence = " ".join(word_list)
print(f"Join words: {word_list} -> '{sentence}'")

# Join với separator khác
numbers = ["1", "2", "3", "4", "5"]
csv_line = ",".join(numbers)
print(f"Join CSV: {numbers} -> '{csv_line}'")

# Join với newline
lines = ["First line", "Second line", "Third line"]
text_block = "\n".join(lines)
print(f"Join lines:\n{text_block}")

# Join empty string
chars = ['H', 'e', 'l', 'l', 'o']
word = "".join(chars)
print(f"Join chars: {chars} -> '{word}'")

# Bài 9: Xử lý email
print("\n9. Xử lý email:")
emails = [
    "user@example.com",
    "admin@company.org",
    "test.email@domain.co.uk",
    "invalid-email",
    "another@test.net"
]

print("Phân tích email:")
for email in emails:
    print(f"Email: '{email}'")
    
    if '@' not in email:
        print("  -> Email không hợp lệ (thiếu @)")
        continue
    
    # Tách username và domain
    parts = email.split('@')
    if len(parts) != 2:
        print("  -> Email không hợp lệ (nhiều @)")
        continue
    
    username, domain = parts
    print(f"  Username: '{username}'")
    print(f"  Domain: '{domain}'")
    
    # Kiểm tra domain
    if '.' not in domain:
        print("  -> Domain không hợp lệ (thiếu .)")
    else:
        domain_parts = domain.split('.')
        print(f"  Domain parts: {domain_parts}")
        
        # Kiểm tra TLD
        tld = domain_parts[-1]
        if tld in ['com', 'org', 'net', 'edu']:
            print(f"  -> TLD phổ biến: {tld}")
        else:
            print(f"  -> TLD khác: {tld}")

# Bài 10: Text cleaning
print("\n10. Text cleaning:")
dirty_text = "  Hello,,,World!!!   Extra   Spaces   "
print(f"Dirty text: '{dirty_text}'")

# Làm sạch từng bước
step1 = dirty_text.strip()
print(f"Step 1 - strip(): '{step1}'")

step2 = step1.replace(",,,", ",")
print(f"Step 2 - replace commas: '{step2}'")

step3 = step2.replace("!!!", "!")
print(f"Step 3 - replace exclamations: '{step3}'")

# Xử lý khoảng trắng thừa
words = step3.split()
step4 = " ".join(words)
print(f"Step 4 - normalize spaces: '{step4}'")

print(f"Final cleaned text: '{step4}'")