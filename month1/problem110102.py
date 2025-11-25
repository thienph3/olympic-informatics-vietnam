"""
Problem 110102: Lambda trong data processing
Áp dụng lambda cho xử lý dữ liệu phức tạp và functional programming

Bài 1: Data Transformation Pipelines
- Transform nested data structures
- Clean và validate data
- Aggregate operations

Bài 2: Functional Programming Patterns
- Currying với lambda
- Function composition
- Event handling với lambda
"""

# Data Transformation
def transform_student_data():
    """Transform student data using lambda"""
    raw_data = [
        "Alice,20,Math:85,Science:90,English:78",
        "Bob,19,Math:92,Science:88,English:85",
        "Charlie,21,Math:78,Science:82,English:80",
        "Diana,20,Math:95,Science:93,English:97"
    ]
    
    # Parse raw data
    parse_student = lambda line: {
        'name': line.split(',')[0],
        'age': int(line.split(',')[1]),
        'subjects': dict(
            subject.split(':')[0]: int(subject.split(':')[1])
            for subject in line.split(',')[2:]
        )
    }
    
    students = list(map(parse_student, raw_data))
    print("Parsed students:")
    for student in students:
        print(f"  {student}")
    
    # Add calculated fields
    add_stats = lambda s: {
        **s,
        'total_score': sum(s['subjects'].values()),
        'average': sum(s['subjects'].values()) / len(s['subjects']),
        'grade': 'A' if sum(s['subjects'].values()) / len(s['subjects']) >= 90 else
                'B' if sum(s['subjects'].values()) / len(s['subjects']) >= 80 else 'C'
    }
    
    enhanced_students = list(map(add_stats, students))
    
    print("\nEnhanced students:")
    for student in enhanced_students:
        print(f"  {student['name']}: {student['average']:.1f} ({student['grade']})")
    
    return enhanced_students

def data_validation_pipeline():
    """Data validation using lambda functions"""
    data = [
        {"name": "Alice", "email": "alice@email.com", "age": 25, "salary": 50000},
        {"name": "", "email": "bob@email", "age": -5, "salary": 0},
        {"name": "Charlie", "email": "charlie@email.com", "age": 30, "salary": 75000},
        {"name": "Diana", "email": "diana.email.com", "age": 150, "salary": -1000}
    ]
    
    # Validation rules
    validators = {
        'name': lambda x: x and len(x.strip()) > 0,
        'email': lambda x: '@' in x and '.' in x.split('@')[-1],
        'age': lambda x: 0 <= x <= 120,
        'salary': lambda x: x >= 0
    }
    
    # Validate each record
    def validate_record(record):
        errors = []
        for field, validator in validators.items():
            if field in record and not validator(record[field]):
                errors.append(f"Invalid {field}: {record[field]}")
        return {**record, 'valid': len(errors) == 0, 'errors': errors}
    
    validated_data = list(map(validate_record, data))
    
    print("Validation results:")
    for record in validated_data:
        status = "✓" if record['valid'] else "✗"
        print(f"  {status} {record['name']}: {record.get('errors', [])}")
    
    # Filter valid records
    valid_records = list(filter(lambda r: r['valid'], validated_data))
    print(f"\nValid records: {len(valid_records)}/{len(data)}")
    
    return valid_records

def aggregate_operations():
    """Aggregation operations using lambda"""
    sales_data = [
        {"product": "Laptop", "category": "Electronics", "price": 1000, "quantity": 5},
        {"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 20},
        {"product": "Book", "category": "Education", "price": 15, "quantity": 100},
        {"product": "Pen", "category": "Office", "price": 2, "quantity": 500},
        {"product": "Monitor", "category": "Electronics", "price": 300, "quantity": 8}
    ]
    
    # Add revenue field
    add_revenue = lambda item: {**item, 'revenue': item['price'] * item['quantity']}
    sales_with_revenue = list(map(add_revenue, sales_data))
    
    # Group by category
    from itertools import groupby
    
    # Sort by category first
    sorted_sales = sorted(sales_with_revenue, key=lambda x: x['category'])
    
    # Group and aggregate
    category_stats = {}
    for category, items in groupby(sorted_sales, key=lambda x: x['category']):
        items_list = list(items)
        category_stats[category] = {
            'total_revenue': sum(map(lambda x: x['revenue'], items_list)),
            'total_quantity': sum(map(lambda x: x['quantity'], items_list)),
            'avg_price': sum(map(lambda x: x['price'], items_list)) / len(items_list),
            'product_count': len(items_list)
        }
    
    print("Category statistics:")
    for category, stats in category_stats.items():
        print(f"  {category}:")
        print(f"    Revenue: ${stats['total_revenue']:,}")
        print(f"    Quantity: {stats['total_quantity']}")
        print(f"    Avg Price: ${stats['avg_price']:.2f}")
        print(f"    Products: {stats['product_count']}")

def functional_programming_patterns():
    """Functional programming patterns with lambda"""
    
    # Currying simulation
    def curry_add(x):
        return lambda y: x + y
    
    add_5 = curry_add(5)
    add_10 = curry_add(10)
    
    print(f"Curried add: {add_5(3)}, {add_10(7)}")
    
    # Function composition
    def compose(f, g):
        return lambda x: f(g(x))
    
    # Compose functions
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    # Create composed function
    transform = compose(square, compose(multiply_by_two, add_one))
    
    numbers = [1, 2, 3, 4, 5]
    transformed = list(map(transform, numbers))
    print(f"Composed transformation: {transformed}")
    
    # Pipeline pattern
    def pipeline(*functions):
        return lambda x: reduce(lambda acc, f: f(acc), functions, x)
    
    from functools import reduce
    
    # Create pipeline
    process_number = pipeline(
        lambda x: x + 1,      # add 1
        lambda x: x * 2,      # multiply by 2
        lambda x: x ** 2      # square
    )
    
    result = process_number(3)  # ((3 + 1) * 2) ** 2 = 64
    print(f"Pipeline result: {result}")

def event_handling_simulation():
    """Simulate event handling with lambda"""
    
    # Event handlers
    events = []
    
    # Register event handlers
    on_click = lambda event: events.append(f"Clicked: {event['target']}")
    on_hover = lambda event: events.append(f"Hovered: {event['target']}")
    on_focus = lambda event: events.append(f"Focused: {event['target']}")
    
    # Event dispatcher
    handlers = {
        'click': on_click,
        'hover': on_hover,
        'focus': on_focus
    }
    
    def dispatch_event(event_type, target):
        event = {'type': event_type, 'target': target}
        if event_type in handlers:
            handlers[event_type](event)
    
    # Simulate events
    dispatch_event('click', 'button1')
    dispatch_event('hover', 'link1')
    dispatch_event('focus', 'input1')
    dispatch_event('click', 'button2')
    
    print("Event log:")
    for event in events:
        print(f"  {event}")
    
    # Filter events
    click_events = list(filter(lambda e: 'Clicked' in e, events))
    print(f"Click events: {click_events}")

def advanced_data_processing():
    """Advanced data processing with lambda"""
    
    # Complex nested data
    company_data = {
        "departments": [
            {
                "name": "Engineering",
                "employees": [
                    {"name": "Alice", "salary": 80000, "skills": ["Python", "Java"]},
                    {"name": "Bob", "salary": 75000, "skills": ["JavaScript", "React"]}
                ]
            },
            {
                "name": "Marketing", 
                "employees": [
                    {"name": "Charlie", "salary": 60000, "skills": ["SEO", "Analytics"]},
                    {"name": "Diana", "salary": 65000, "skills": ["Design", "Branding"]}
                ]
            }
        ]
    }
    
    # Extract all employees with department info
    extract_employees = lambda dept: [
        {**emp, "department": dept["name"]} 
        for emp in dept["employees"]
    ]
    
    all_employees = []
    for dept in company_data["departments"]:
        all_employees.extend(extract_employees(dept))
    
    # Or using list comprehension with lambda
    all_employees_alt = [
        {**emp, "department": dept["name"]}
        for dept in company_data["departments"]
        for emp in dept["employees"]
    ]
    
    print("All employees:")
    for emp in all_employees:
        print(f"  {emp['name']} ({emp['department']}): ${emp['salary']:,}")
    
    # Calculate statistics
    total_salary = sum(map(lambda e: e['salary'], all_employees))
    avg_salary = total_salary / len(all_employees)
    
    # Find highest paid employee
    highest_paid = max(all_employees, key=lambda e: e['salary'])
    
    print(f"\nCompany statistics:")
    print(f"  Total employees: {len(all_employees)}")
    print(f"  Total salary budget: ${total_salary:,}")
    print(f"  Average salary: ${avg_salary:,.2f}")
    print(f"  Highest paid: {highest_paid['name']} (${highest_paid['salary']:,})")

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Data Transformation Pipelines ===")
    
    print("Student data transformation:")
    transform_student_data()
    
    print("\nData validation pipeline:")
    data_validation_pipeline()
    
    print("\nAggregate operations:")
    aggregate_operations()
    
    print("\n=== Bài 2: Functional Programming Patterns ===")
    
    print("Functional programming patterns:")
    functional_programming_patterns()
    
    print("\nEvent handling simulation:")
    event_handling_simulation()
    
    print("\nAdvanced data processing:")
    advanced_data_processing()

    print("\n=== Bài tập thực hành ===")
    print("1. Build ETL pipeline với lambda functions")
    print("2. Create functional reactive programming system")
    print("3. Implement data streaming processor")
    print("4. Build query engine với lambda expressions")