# Problem 09.03.01: String formatting techniques

print("=== STRING FORMATTING TECHNIQUES ===")

# Bài 1: f-strings cơ bản
print("1. f-strings cơ bản:")

name = "Alice"
age = 25
height = 1.68
score = 95.67

print(f"Tên: {name}")
print(f"Tuổi: {age}")
print(f"Chiều cao: {height}m")
print(f"Điểm: {score}")

# f-strings với expressions
print(f"Năm sinh: {2024 - age}")
print(f"Tên viết hoa: {name.upper()}")
print(f"Chiều cao (cm): {height * 100}")
print(f"Điểm làm tròn: {round(score)}")

# Bài 2: f-strings formatting
print("\n2. f-strings formatting:")

pi = 3.14159265359
large_number = 1234567
percentage = 0.856

print(f"Pi với 2 chữ số thập phân: {pi:.2f}")
print(f"Pi với 4 chữ số thập phân: {pi:.4f}")
print(f"Số lớn với dấu phẩy: {large_number:,}")
print(f"Số lớn với padding: {large_number:010d}")
print(f"Phần trăm: {percentage:.1%}")
print(f"Phần trăm chi tiết: {percentage:.2%}")

# Alignment trong f-strings
items = ["Apple", "Banana", "Cherry"]
prices = [1.20, 0.80, 2.50]

print("\nBảng giá (alignment):")
print(f"{'Item':<10} {'Price':>8}")
print("-" * 18)
for item, price in zip(items, prices):
    print(f"{item:<10} ${price:>6.2f}")

# Bài 3: format() method
print("\n3. format() method:")

# Positional arguments
template1 = "Hello, {}! You are {} years old."
print(template1.format("Bob", 30))

# Indexed arguments
template2 = "Hello, {0}! You are {1} years old. Nice to meet you, {0}!"
print(template2.format("Charlie", 35))

# Named arguments
template3 = "Hello, {name}! You are {age} years old and live in {city}."
print(template3.format(name="David", age=40, city="New York"))

# Mixed arguments
template4 = "Product: {0}, Price: ${price:.2f}, Quantity: {1}"
print(template4.format("Laptop", 5, price=999.99))

# Bài 4: format() với specifications
print("\n4. format() với specifications:")

numbers = [42, 3.14159, 0.75, 1234567]

print("Số formatting:")
for num in numbers:
    if isinstance(num, int):
        print(f"Integer {num}:")
        print(f"  Default: '{num}'")
        print(f"  Zero-padded: '{num:05d}'")
        print(f"  With commas: '{num:,}'")
    else:
        print(f"Float {num}:")
        print(f"  Default: '{num}'")
        print(f"  2 decimals: '{num:.2f}'")
        print(f"  Scientific: '{num:.2e}'")
        print(f"  Percentage: '{num:.1%}'")

# Bài 5: % formatting (old style)
print("\n5. % formatting (old style):")

# Basic % formatting
name = "Eve"
age = 28
gpa = 3.85

print("Name: %s" % name)
print("Age: %d" % age)
print("GPA: %.2f" % gpa)

# Multiple values
print("%s is %d years old with GPA %.2f" % (name, age, gpa))

# Dictionary formatting
student = {"name": "Frank", "age": 33, "major": "Computer Science"}
print("Student: %(name)s, Age: %(age)d, Major: %(major)s" % student)

# Bài 6: So sánh các phương pháp
print("\n6. So sánh các phương pháp:")

product = "Laptop"
price = 1299.99
quantity = 3
total = price * quantity

# f-string
f_result = f"Product: {product}, Price: ${price:.2f}, Qty: {quantity}, Total: ${total:.2f}"

# format()
format_result = "Product: {}, Price: ${:.2f}, Qty: {}, Total: ${:.2f}".format(
    product, price, quantity, total)

# % formatting
percent_result = "Product: %s, Price: $%.2f, Qty: %d, Total: $%.2f" % (
    product, price, quantity, total)

print("f-string:", f_result)
print("format():", format_result)
print("% format:", percent_result)

# Bài 7: Advanced f-string features
print("\n7. Advanced f-string features:")

# Nested expressions
data = {"users": [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 87}]}
print(f"Top user: {max(data['users'], key=lambda x: x['score'])['name']}")

# Format specifiers with variables
width = 10
precision = 3
value = 3.14159
print(f"Formatted value: {value:{width}.{precision}f}")

# Debugging (Python 3.8+)
x = 42
y = 24
try:
    print(f"{x=}, {y=}, {x+y=}")  # Debug format
except:
    print(f"x={x}, y={y}, x+y={x+y}")  # Fallback for older Python

# Bài 8: Template strings
print("\n8. Template strings:")
from string import Template

# Template cơ bản
template = Template("Hello $name, your balance is $$$balance")
result = template.substitute(name="John", balance=1500.50)
print("Template result:", result)

# Safe substitute (không lỗi nếu thiếu variable)
incomplete_template = Template("Hello $name, your score is $score, grade: $grade")
safe_result = incomplete_template.safe_substitute(name="Jane", score=95)
print("Safe substitute:", safe_result)

# Bài 9: Formatting tables
print("\n9. Formatting tables:")

students_data = [
    ("Alice Johnson", 95, "A"),
    ("Bob Smith", 87, "B+"),
    ("Charlie Brown", 92, "A-"),
    ("Diana Prince", 98, "A+")
]

# Header
print(f"{'Name':<15} {'Score':>5} {'Grade':>5}")
print("-" * 25)

# Data rows
for name, score, grade in students_data:
    print(f"{name:<15} {score:>5} {grade:>5}")

# Summary
avg_score = sum(score for _, score, _ in students_data) / len(students_data)
print("-" * 25)
print(f"{'Average':<15} {avg_score:>5.1f}")

# Bài 10: Dynamic formatting
print("\n10. Dynamic formatting:")

def format_currency(amount, currency="USD", decimals=2):
    """Format số tiền với currency"""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "VND": "₫"}
    symbol = symbols.get(currency, currency)
    
    if currency == "VND":
        # VND thường không có decimals
        return f"{symbol}{amount:,.0f}"
    else:
        return f"{symbol}{amount:,.{decimals}f}"

amounts = [1234.56, 999999.99, 0.99]
currencies = ["USD", "EUR", "VND"]

print("Currency formatting:")
for amount in amounts:
    for currency in currencies:
        formatted = format_currency(amount, currency)
        print(f"  {amount} -> {formatted}")

# Bài 11: Report generation
print("\n11. Report generation:")

def generate_sales_report(sales_data):
    """Generate formatted sales report"""
    report = []
    report.append("=" * 50)
    report.append("SALES REPORT")
    report.append("=" * 50)
    
    total_sales = 0
    report.append(f"{'Product':<20} {'Quantity':>8} {'Price':>10} {'Total':>10}")
    report.append("-" * 50)
    
    for product, qty, price in sales_data:
        item_total = qty * price
        total_sales += item_total
        report.append(f"{product:<20} {qty:>8} ${price:>8.2f} ${item_total:>8.2f}")
    
    report.append("-" * 50)
    report.append(f"{'TOTAL':<20} {'':<8} {'':<10} ${total_sales:>8.2f}")
    report.append("=" * 50)
    
    return "\n".join(report)

# Sample sales data
sales = [
    ("Laptop", 2, 999.99),
    ("Mouse", 5, 25.50),
    ("Keyboard", 3, 75.00),
    ("Monitor", 1, 299.99)
]

print(generate_sales_report(sales))