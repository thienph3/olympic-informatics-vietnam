"""
Problem 100201: Default parameters và keyword arguments
Thực hành default parameters, keyword arguments và *args/**kwargs

Bài 1: Default Parameters
- Functions với giá trị mặc định
- Multiple default parameters

Bài 2: Keyword Arguments và Variable Arguments
- Keyword arguments
- *args và **kwargs
"""

# Default Parameters
def greet_with_default(name, greeting="Hello", punctuation="!"):
    """Function với default parameters"""
    return f"{greeting}, {name}{punctuation}"

def create_user_profile(name, age=18, city="Unknown", country="Vietnam"):
    """Tạo profile user với default values"""
    return {
        "name": name,
        "age": age,
        "city": city,
        "country": country
    }

def calculate_discount(price, discount_percent=10, tax_rate=0.1):
    """Tính giá sau giảm giá và thuế"""
    discounted_price = price * (1 - discount_percent / 100)
    final_price = discounted_price * (1 + tax_rate)
    return round(final_price, 2)

def format_text(text, uppercase=False, add_prefix="", add_suffix=""):
    """Format text với các options"""
    result = text
    if uppercase:
        result = result.upper()
    result = add_prefix + result + add_suffix
    return result

# Variable Arguments (*args)
def sum_all(*numbers):
    """Tính tổng tất cả các số"""
    return sum(numbers)

def find_maximum(*numbers):
    """Tìm số lớn nhất"""
    if not numbers:
        return None
    return max(numbers)

def calculate_average(*scores):
    """Tính điểm trung bình"""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def concatenate_strings(*strings, separator=" "):
    """Nối các chuỗi với separator"""
    return separator.join(strings)

# Keyword Arguments (**kwargs)
def print_student_info(**info):
    """In thông tin học sinh"""
    result = []
    for key, value in info.items():
        result.append(f"{key.capitalize()}: {value}")
    return "\n".join(result)

def create_database_record(**fields):
    """Tạo record database"""
    record = {}
    for key, value in fields.items():
        record[key] = value
    return record

def build_query(**conditions):
    """Tạo SQL query từ conditions"""
    if not conditions:
        return "SELECT * FROM table"
    
    where_clauses = []
    for key, value in conditions.items():
        if isinstance(value, str):
            where_clauses.append(f"{key} = '{value}'")
        else:
            where_clauses.append(f"{key} = {value}")
    
    return f"SELECT * FROM table WHERE {' AND '.join(where_clauses)}"

# Mixed Arguments
def process_order(customer_name, *items, discount=0, **customer_info):
    """Xử lý đơn hàng với mixed arguments"""
    order = {
        "customer": customer_name,
        "items": list(items),
        "discount": discount,
        "customer_info": customer_info,
        "total_items": len(items)
    }
    return order

def log_message(message, *args, level="INFO", timestamp=True, **kwargs):
    """Log message với flexible parameters"""
    log_entry = f"[{level}] {message}"
    
    if args:
        log_entry += f" Args: {args}"
    
    if timestamp:
        import datetime
        log_entry = f"{datetime.datetime.now()} - {log_entry}"
    
    if kwargs:
        log_entry += f" Extra: {kwargs}"
    
    return log_entry

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Default Parameters ===")
    
    # Test greeting with defaults
    print(greet_with_default("Alice"))
    print(greet_with_default("Bob", "Hi"))
    print(greet_with_default("Charlie", "Hey", "."))
    print(greet_with_default("David", punctuation="!!!"))
    
    # Test user profile
    print("\nUser Profiles:")
    print(create_user_profile("Alice"))
    print(create_user_profile("Bob", 25))
    print(create_user_profile("Charlie", 30, "Hanoi"))
    print(create_user_profile("David", city="HCMC", age=28))
    
    # Test discount calculation
    print(f"\nPrice calculations:")
    print(f"$100 with defaults: ${calculate_discount(100)}")
    print(f"$100 with 20% discount: ${calculate_discount(100, 20)}")
    print(f"$100 with 15% discount, 5% tax: ${calculate_discount(100, 15, 0.05)}")
    
    # Test text formatting
    print(f"\nText formatting:")
    print(f"'{format_text('hello world')}'")
    print(f"'{format_text('hello world', uppercase=True)}'")
    print(f"'{format_text('hello world', add_prefix='>>> ', add_suffix=' <<<')}'")
    
    print("\n=== Bài 2: Variable Arguments ===")
    
    # Test *args
    print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")
    print(f"Max: {find_maximum(10, 5, 8, 3, 12)}")
    print(f"Average: {calculate_average(85, 90, 78, 92, 88):.2f}")
    print(f"Concatenate: '{concatenate_strings('Hello', 'World', 'Python')}'")
    print(f"With separator: '{concatenate_strings('A', 'B', 'C', separator='-')}'")
    
    # Test **kwargs
    print(f"\nStudent info:")
    print(print_student_info(name="Alice", age=20, grade="A", subject="Math"))
    
    print(f"\nDatabase record:")
    record = create_database_record(id=1, name="John", email="john@email.com", active=True)
    print(record)
    
    print(f"\nSQL queries:")
    print(build_query())
    print(build_query(name="Alice", age=25))
    print(build_query(city="Hanoi", active=True))
    
    # Test mixed arguments
    print(f"\nOrder processing:")
    order1 = process_order("Alice", "laptop", "mouse", "keyboard", discount=10)
    print(order1)
    
    order2 = process_order("Bob", "phone", "case", discount=5, 
                          email="bob@email.com", phone="123456789")
    print(order2)
    
    # Test logging
    print(f"\nLog messages:")
    print(log_message("System started"))
    print(log_message("User login", "alice", level="DEBUG"))
    print(log_message("Error occurred", level="ERROR", 
                     error_code=500, module="auth"))

    print("\n=== Bài tập thực hành ===")
    print("1. Viết function tạo email template với default subject")
    print("2. Function tính lương với overtime và bonus")
    print("3. Function tạo HTML tag với attributes")
    print("4. Function xử lý config với default settings")