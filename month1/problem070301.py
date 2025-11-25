# Problem 07.03.01: List methods cơ bản

print("=== LIST METHODS CƠ BẢN ===")

# Bài 1: Thêm phần tử
print("1. Thêm phần tử:")
fruits = ["apple", "banana"]
print(f"List ban đầu: {fruits}")

# append()
fruits.append("orange")
print(f"Sau append('orange'): {fruits}")

# insert()
fruits.insert(1, "grape")
print(f"Sau insert(1, 'grape'): {fruits}")

# extend()
fruits.extend(["mango", "kiwi"])
print(f"Sau extend(['mango', 'kiwi']): {fruits}")

# Toán tử +
new_fruits = fruits + ["pineapple", "strawberry"]
print(f"Dùng toán tử +: {new_fruits}")

# Bài 2: Xóa phần tử
print("\n2. Xóa phần tử:")
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"List ban đầu: {numbers}")

# remove() - xóa phần tử đầu tiên
numbers_copy = numbers.copy()
numbers_copy.remove(2)
print(f"Sau remove(2): {numbers_copy}")

# pop() - xóa và trả về
numbers_copy = numbers.copy()
last_item = numbers_copy.pop()
print(f"pop() trả về: {last_item}, list còn lại: {numbers_copy}")

second_item = numbers_copy.pop(1)
print(f"pop(1) trả về: {second_item}, list còn lại: {numbers_copy}")

# del - xóa theo index
numbers_copy = numbers.copy()
del numbers_copy[0]
print(f"Sau del numbers_copy[0]: {numbers_copy}")

# Xóa tất cả số 2
numbers_copy = numbers.copy()
while 2 in numbers_copy:
    numbers_copy.remove(2)
print(f"Sau khi xóa tất cả số 2: {numbers_copy}")

# Bài 3: Sắp xếp
print("\n3. Sắp xếp:")
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Dữ liệu gốc: {data}")

# sort() - sắp xếp tại chỗ
data_copy = data.copy()
data_copy.sort()
print(f"Sau sort(): {data_copy}")

# sort() với reverse
data_copy = data.copy()
data_copy.sort(reverse=True)
print(f"Sau sort(reverse=True): {data_copy}")

# sorted() - tạo list mới
sorted_data = sorted(data)
print(f"sorted() tạo list mới: {sorted_data}")
print(f"Dữ liệu gốc không đổi: {data}")

# Bài 4: Đảo ngược
print("\n4. Đảo ngược:")
letters = ['a', 'b', 'c', 'd', 'e']
print(f"List gốc: {letters}")

# reverse() - đảo ngược tại chỗ
letters_copy = letters.copy()
letters_copy.reverse()
print(f"Sau reverse(): {letters_copy}")

# Slicing để đảo ngược
reversed_letters = letters[::-1]
print(f"Dùng slicing [::-1]: {reversed_letters}")
print(f"List gốc không đổi: {letters}")

# Bài 5: Kết hợp các methods
print("\n5. Kết hợp các methods:")
shopping_list = []
print(f"Danh sách mua sắm ban đầu: {shopping_list}")

# Thêm các món
items_to_add = ["bread", "milk", "eggs", "butter", "cheese"]
for item in items_to_add:
    shopping_list.append(item)
    print(f"Thêm {item}: {shopping_list}")

# Chèn món khẩn cấp vào đầu
shopping_list.insert(0, "medicine")
print(f"Chèn medicine vào đầu: {shopping_list}")

# Xóa món không cần
if "butter" in shopping_list:
    shopping_list.remove("butter")
    print(f"Xóa butter: {shopping_list}")

# Sắp xếp theo alphabet
shopping_list.sort()
print(f"Sắp xếp theo alphabet: {shopping_list}")

# Thêm nhiều món cùng lúc
shopping_list.extend(["apple", "banana"])
print(f"Thêm trái cây: {shopping_list}")

# Đảo ngược danh sách
shopping_list.reverse()
print(f"Đảo ngược danh sách: {shopping_list}")

print(f"Danh sách cuối cùng có {len(shopping_list)} món")