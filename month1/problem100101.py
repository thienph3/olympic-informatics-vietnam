"""
Problem 100101: Function cơ bản và parameters
Tạo functions đơn giản với parameters và return values

Bài 1: Basic Functions
- Tạo function chào hỏi
- Function tính toán đơn giản
- Function với nhiều parameters

Bài 2: Return Values
- Function trả về một giá trị
- Function trả về nhiều giá trị
- Function với conditional return
"""

def greet():
    """Function đơn giản không có parameter"""
    return "Hello, World!"

def greet_person(name):
    """Function với một parameter"""
    return f"Hello, {name}!"

def greet_full(first_name, last_name):
    """Function với nhiều parameters"""
    return f"Hello, {first_name} {last_name}!"

def add_two_numbers(a, b):
    """Function tính tổng hai số"""
    return a + b

def calculate_basic(a, b, operation):
    """Function tính toán với operation"""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

def get_student_info():
    """Function trả về nhiều giá trị"""
    name = "Alice"
    age = 20
    grade = "A"
    return name, age, grade

def check_even_odd(number):
    """Function với conditional return"""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def get_max_min(a, b, c):
    """Function tìm max và min của 3 số"""
    maximum = max(a, b, c)
    minimum = min(a, b, c)
    return maximum, minimum

def is_positive(number):
    """Function kiểm tra số dương"""
    return number > 0

def calculate_grade(score):
    """Function tính grade từ điểm số"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Basic Functions ===")
    
    # Test basic functions
    print(greet())
    print(greet_person("Alice"))
    print(greet_full("John", "Doe"))
    
    # Test calculation functions
    print(f"5 + 3 = {add_two_numbers(5, 3)}")
    print(f"10 - 4 = {calculate_basic(10, 4, '-')}")
    print(f"6 * 7 = {calculate_basic(6, 7, '*')}")
    print(f"15 / 3 = {calculate_basic(15, 3, '/')}")
    print(f"10 / 0 = {calculate_basic(10, 0, '/')}")
    
    print("\n=== Bài 2: Return Values ===")
    
    # Test multiple return values
    name, age, grade = get_student_info()
    print(f"Student: {name}, Age: {age}, Grade: {grade}")
    
    # Test conditional return
    print(f"5 is {check_even_odd(5)}")
    print(f"8 is {check_even_odd(8)}")
    
    # Test max/min function
    max_val, min_val = get_max_min(10, 5, 15)
    print(f"Max: {max_val}, Min: {min_val}")
    
    # Test boolean return
    print(f"Is 5 positive? {is_positive(5)}")
    print(f"Is -3 positive? {is_positive(-3)}")
    
    # Test grade calculation
    scores = [95, 87, 73, 65, 45]
    for score in scores:
        print(f"Score {score}: Grade {calculate_grade(score)}")

    print("\n=== Bài tập thực hành ===")
    print("1. Viết function tính chu vi và diện tích hình chữ nhật")
    print("2. Tạo function kiểm tra năm nhuận")
    print("3. Function tìm ước chung lớn nhất của 2 số")
    print("4. Function chuyển đổi nhiệt độ C sang F và ngược lại")