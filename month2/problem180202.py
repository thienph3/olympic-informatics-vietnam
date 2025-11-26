"""
Problem 180202: Multi-Criteria Sorting
Sắp xếp theo nhiều tiêu chí

Topics: Multiple keys, complex sorting logic, tuple comparison
"""

def sort_students_multi_criteria(students):
    """
    Sắp xếp sinh viên theo: điểm (giảm dần), tuổi (tăng dần), tên (tăng dần)
    students: list of (name, grade, age)
    """
    # TODO: Sort by multiple criteria
    pass

def sort_employees_complex(employees):
    """
    Sắp xếp nhân viên theo: phòng ban, lương (giảm dần), kinh nghiệm (giảm dần)
    employees: list of (name, department, salary, experience)
    """
    # TODO: Complex multi-criteria sorting
    pass

def sort_products_by_rating_price(products):
    """
    Sắp xếp sản phẩm theo: rating (giảm dần), giá (tăng dần)
    products: list of (name, price, rating)
    """
    # TODO: Sort products by rating then price
    pass

def sort_events_by_date_priority(events):
    """
    Sắp xếp sự kiện theo: ngày, độ ưu tiên
    events: list of (name, date, priority)
    """
    # TODO: Sort events by date and priority
    pass

def sort_files_by_extension_size(files):
    """
    Sắp xếp file theo: extension, size (giảm dần)
    files: list of (filename, size, extension)
    """
    # TODO: Sort files by extension then size
    pass

def sort_coordinates_by_quadrant_distance(points):
    """
    Sắp xếp điểm theo: quadrant, khoảng cách từ gốc
    """
    # TODO: Sort by quadrant then distance
    pass

def sort_with_custom_tie_breaker(items, primary_key, tie_breaker):
    """
    Sắp xếp với tie-breaker tùy chỉnh
    """
    # TODO: Use custom tie-breaking logic
    pass

def stable_multi_criteria_sort(data, criteria):
    """
    Sắp xếp stable theo nhiều tiêu chí
    criteria: list of (key_func, reverse) tuples
    """
    # TODO: Implement stable multi-criteria sorting
    pass

# Test cases
def test_multi_criteria():
    # Test students
    students = [
        ("Alice", 85, 20),
        ("Bob", 90, 19),
        ("Charlie", 85, 21),
        ("David", 90, 20),
        ("Eve", 85, 19)
    ]
    print("Students sorted:", sort_students_multi_criteria(students))
    
    # Test employees
    employees = [
        ("John", "IT", 70000, 5),
        ("Jane", "HR", 60000, 3),
        ("Bob", "IT", 75000, 7),
        ("Alice", "HR", 65000, 4),
        ("Charlie", "IT", 70000, 6)
    ]
    print("Employees sorted:", sort_employees_complex(employees))
    
    # Test products
    products = [
        ("Laptop", 1000, 4.5),
        ("Mouse", 25, 4.2),
        ("Keyboard", 75, 4.5),
        ("Monitor", 300, 4.2),
        ("Tablet", 500, 4.5)
    ]
    print("Products sorted:", sort_products_by_rating_price(products))
    
    # Test events
    from datetime import date
    events = [
        ("Meeting", date(2024, 1, 15), "high"),
        ("Training", date(2024, 1, 15), "medium"),
        ("Review", date(2024, 1, 10), "high"),
        ("Party", date(2024, 1, 20), "low")
    ]
    print("Events sorted:", sort_events_by_date_priority(events))
    
    # Test files
    files = [
        ("doc1.txt", 1024, "txt"),
        ("image.jpg", 2048, "jpg"),
        ("doc2.txt", 512, "txt"),
        ("photo.jpg", 4096, "jpg"),
        ("readme.md", 256, "md")
    ]
    print("Files sorted:", sort_files_by_extension_size(files))
    
    # Test coordinates
    points = [(1, 2), (-1, 3), (2, -1), (-2, -3), (0, 1)]
    print("Points sorted:", sort_coordinates_by_quadrant_distance(points))

if __name__ == "__main__":
    test_multi_criteria()