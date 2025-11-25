# Problem 01.03.02: Chuyển đổi kiểu
# Chuyển đổi từ string sang số
str_number = "123"
int_number = int(str_number)
float_number = float(str_number)

print(f"String: {str_number} (type: {type(str_number)})")
print(f"Int: {int_number} (type: {type(int_number)})")
print(f"Float: {float_number} (type: {type(float_number)})")

# Chuyển đổi từ số sang string
age = 18
age_str = str(age)
print(f"\nTuổi dạng số: {age}")
print(f"Tuổi dạng chuỗi: '{age_str}'")

# Thử nghiệm bool
print(f"\nbool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool('Hello'): {bool('Hello')}")