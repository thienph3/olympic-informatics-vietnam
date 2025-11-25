# Problem 01.04.01: Chương trình chào hỏi
print("=== CHƯƠNG TRÌNH CHÀO HỎI ===")

# Nhập thông tin
name = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi của bạn: "))
city = input("Bạn sống ở thành phố nào: ")

# In kết quả
print("\n" + "="*40)
print(f"Xin chào {name}!")
print(f"Bạn {age} tuổi và sống ở {city}")
print(f"Năm sau bạn sẽ {age + 1} tuổi")
print("Chúc bạn học tập tốt!")
print("="*40)