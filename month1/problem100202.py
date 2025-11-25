"""
Problem 100202: Functions với tham số linh hoạt
Tạo functions xử lý số lượng tham số thay đổi

Bài 1: Flexible Math Functions
- Functions tính toán với số lượng tham số thay đổi
- Statistical functions

Bài 2: Data Processing Functions
- Functions xử lý dữ liệu linh hoạt
- Configuration và settings functions
"""

import statistics

# Flexible Math Functions
def multiply_all(*numbers):
    """Nhân tất cả các số"""
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result

def calculate_statistics(*values):
    """Tính các thống kê cơ bản"""
    if not values:
        return {}
    
    return {
        "count": len(values),
        "sum": sum(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "min": min(values),
        "max": max(values),
        "range": max(values) - min(values)
    }

def find_common_elements(*lists):
    """Tìm phần tử chung trong nhiều list"""
    if not lists:
        return []
    
    common = set(lists[0])
    for lst in lists[1:]:
        common = common.intersection(set(lst))
    
    return list(common)

def weighted_average(*args):
    """Tính trung bình có trọng số: value1, weight1, value2, weight2, ..."""
    if len(args) % 2 != 0:
        return "Error: Must provide pairs of (value, weight)"
    
    total_weighted = 0
    total_weight = 0
    
    for i in range(0, len(args), 2):
        value = args[i]
        weight = args[i + 1]
        total_weighted += value * weight
        total_weight += weight
    
    return total_weighted / total_weight if total_weight != 0 else 0

# Data Processing Functions
def merge_dictionaries(**dicts):
    """Merge nhiều dictionaries"""
    result = {}
    for key, value in dicts.items():
        if isinstance(value, dict):
            result.update(value)
        else:
            result[key] = value
    return result

def filter_data(data, **filters):
    """Lọc dữ liệu theo nhiều điều kiện"""
    if not isinstance(data, list):
        return []
    
    filtered = []
    for item in data:
        match = True
        for key, value in filters.items():
            if key not in item or item[key] != value:
                match = False
                break
        if match:
            filtered.append(item)
    
    return filtered

def create_report(*sections, title="Report", **metadata):
    """Tạo báo cáo với nhiều sections"""
    report = {
        "title": title,
        "metadata": metadata,
        "sections": list(sections),
        "section_count": len(sections)
    }
    return report

def validate_form(**fields):
    """Validate form với các rules"""
    errors = []
    
    # Required fields
    required = ["name", "email"]
    for field in required:
        if field not in fields or not fields[field]:
            errors.append(f"{field} is required")
    
    # Email validation
    if "email" in fields and fields["email"]:
        if "@" not in fields["email"]:
            errors.append("Invalid email format")
    
    # Age validation
    if "age" in fields:
        try:
            age = int(fields["age"])
            if age < 0 or age > 150:
                errors.append("Age must be between 0 and 150")
        except ValueError:
            errors.append("Age must be a number")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "data": fields
    }

# Configuration Functions
def setup_config(config_name, **settings):
    """Setup configuration với default values"""
    defaults = {
        "debug": False,
        "timeout": 30,
        "max_retries": 3,
        "log_level": "INFO"
    }
    
    config = defaults.copy()
    config.update(settings)
    config["name"] = config_name
    
    return config

def build_url(base_url, *path_segments, **query_params):
    """Build URL với path và query parameters"""
    # Join path segments
    if path_segments:
        url = base_url.rstrip("/") + "/" + "/".join(str(seg) for seg in path_segments)
    else:
        url = base_url
    
    # Add query parameters
    if query_params:
        query_string = "&".join(f"{key}={value}" for key, value in query_params.items())
        url += "?" + query_string
    
    return url

def create_menu(*items, **options):
    """Tạo menu với options"""
    menu = {
        "items": list(items),
        "options": options,
        "item_count": len(items)
    }
    
    # Apply formatting options
    if options.get("numbered", False):
        menu["formatted_items"] = [f"{i+1}. {item}" for i, item in enumerate(items)]
    else:
        menu["formatted_items"] = [f"- {item}" for item in items]
    
    return menu

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Flexible Math Functions ===")
    
    # Test multiply_all
    print(f"Multiply: {multiply_all(2, 3, 4, 5)}")
    print(f"Multiply empty: {multiply_all()}")
    
    # Test statistics
    scores = [85, 90, 78, 92, 88, 95, 82]
    stats = calculate_statistics(*scores)
    print(f"\nStatistics for {scores}:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Test common elements
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [4, 5, 6, 7, 8]
    common = find_common_elements(list1, list2, list3)
    print(f"\nCommon elements: {common}")
    
    # Test weighted average
    avg = weighted_average(85, 0.3, 90, 0.4, 78, 0.3)  # score, weight pairs
    print(f"Weighted average: {avg:.2f}")
    
    print("\n=== Bài 2: Data Processing Functions ===")
    
    # Test merge dictionaries
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = merge_dictionaries(first=dict1, second=dict2, extra="value")
    print(f"Merged dict: {merged}")
    
    # Test filter data
    students = [
        {"name": "Alice", "grade": "A", "age": 20},
        {"name": "Bob", "grade": "B", "age": 21},
        {"name": "Charlie", "grade": "A", "age": 19},
        {"name": "David", "grade": "C", "age": 22}
    ]
    
    grade_a_students = filter_data(students, grade="A")
    print(f"\nGrade A students: {[s['name'] for s in grade_a_students]}")
    
    young_students = filter_data(students, age=20)
    print(f"20-year-old students: {[s['name'] for s in young_students]}")
    
    # Test create report
    report = create_report(
        "Introduction", "Data Analysis", "Conclusion",
        title="Monthly Report",
        author="John Doe",
        date="2024-01-15"
    )
    print(f"\nReport: {report}")
    
    # Test form validation
    form1 = validate_form(name="Alice", email="alice@email.com", age="25")
    print(f"\nForm validation 1: {form1}")
    
    form2 = validate_form(name="", email="invalid-email", age="abc")
    print(f"Form validation 2: {form2}")
    
    # Test configuration
    config = setup_config("web_app", debug=True, timeout=60, custom_setting="value")
    print(f"\nConfig: {config}")
    
    # Test URL building
    url1 = build_url("https://api.example.com", "users", 123, "posts")
    print(f"URL 1: {url1}")
    
    url2 = build_url("https://api.example.com", "search", q="python", limit=10, page=2)
    print(f"URL 2: {url2}")
    
    # Test menu creation
    menu = create_menu("Home", "About", "Contact", "Services", numbered=True, style="modern")
    print(f"\nMenu: {menu}")
    print("Formatted items:")
    for item in menu["formatted_items"]:
        print(f"  {item}")

    print("\n=== Bài tập thực hành ===")
    print("1. Function tạo SQL INSERT với flexible columns")
    print("2. Function merge và sort nhiều sorted lists")
    print("3. Function tạo HTML table từ data")
    print("4. Function calculate compound interest với flexible parameters")