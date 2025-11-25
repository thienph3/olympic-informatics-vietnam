"""
Problem 120202: Structured data files
Work with CSV, JSON files, data processing và analysis

Bài 1: CSV File Processing
- Read/write CSV files
- Handle different delimiters
- Data validation và cleaning

Bài 2: JSON File Operations
- Parse và generate JSON
- Handle nested structures
- Data transformation
"""

import csv
import json
import os
import tempfile
from datetime import datetime
from typing import List, Dict, Any

# CSV File Processing
def csv_basic_operations():
    """Demonstrate basic CSV operations"""
    print("=== CSV Basic Operations ===")
    
    # Sample data
    students_data = [
        ['Name', 'Age', 'Grade', 'Subject', 'Score'],
        ['Alice', 20, 'A', 'Math', 95],
        ['Bob', 19, 'B', 'Math', 87],
        ['Charlie', 21, 'A', 'Physics', 92],
        ['Diana', 20, 'A', 'Chemistry', 88],
        ['Eve', 19, 'B', 'Math', 91]
    ]
    
    filename = 'students.csv'
    
    # Write CSV
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(students_data)
        print(f"✓ Written {len(students_data)} rows to {filename}")
    except IOError as e:
        print(f"✗ Error writing CSV: {e}")
        return
    
    # Read CSV
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        
        print(f"✓ Read {len(rows)} rows from CSV")
        print("First 3 rows:")
        for i, row in enumerate(rows[:3]):
            print(f"  Row {i}: {row}")
            
    except IOError as e:
        print(f"✗ Error reading CSV: {e}")
    
    # Read with DictReader
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            students = list(reader)
        
        print(f"✓ Read {len(students)} student records")
        print("Sample records:")
        for student in students[:2]:
            print(f"  {student['Name']}: {student['Subject']} = {student['Score']}")
            
    except IOError as e:
        print(f"✗ Error reading CSV with DictReader: {e}")
    
    # Clean up
    os.remove(filename)

def csv_advanced_operations():
    """Demonstrate advanced CSV operations"""
    print("\n=== CSV Advanced Operations ===")
    
    # Create more complex data
    sales_data = [
        {'Date': '2024-01-01', 'Product': 'Laptop', 'Category': 'Electronics', 'Price': 1200.50, 'Quantity': 2},
        {'Date': '2024-01-02', 'Product': 'Mouse', 'Category': 'Electronics', 'Price': 25.99, 'Quantity': 5},
        {'Date': '2024-01-03', 'Product': 'Book', 'Category': 'Education', 'Price': 15.00, 'Quantity': 3},
        {'Date': '2024-01-04', 'Product': 'Pen', 'Category': 'Office', 'Price': 2.50, 'Quantity': 10},
        {'Date': '2024-01-05', 'Product': 'Monitor', 'Category': 'Electronics', 'Price': 300.00, 'Quantity': 1}
    ]
    
    filename = 'sales.csv'
    
    # Write with DictWriter
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Date', 'Product', 'Category', 'Price', 'Quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(sales_data)
        
        print(f"✓ Written sales data with headers")
        
    except IOError as e:
        print(f"✗ Error writing sales CSV: {e}")
        return
    
    # Read and process data
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Calculate statistics
            total_revenue = 0
            category_sales = {}
            product_count = 0
            
            for row in reader:
                product_count += 1
                price = float(row['Price'])
                quantity = int(row['Quantity'])
                revenue = price * quantity
                total_revenue += revenue
                
                category = row['Category']
                if category not in category_sales:
                    category_sales[category] = 0
                category_sales[category] += revenue
        
        print(f"✓ Processed {product_count} products")
        print(f"Total revenue: ${total_revenue:.2f}")
        print("Revenue by category:")
        for category, revenue in category_sales.items():
            print(f"  {category}: ${revenue:.2f}")
            
    except (IOError, ValueError) as e:
        print(f"✗ Error processing sales data: {e}")
    
    # Custom delimiter example
    custom_filename = 'custom_delimiter.csv'
    try:
        # Write with semicolon delimiter
        with open(custom_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['Name', 'Email', 'Phone'])
            writer.writerow(['John Doe', 'john@email.com', '123-456-7890'])
            writer.writerow(['Jane Smith', 'jane@email.com', '098-765-4321'])
        
        # Read with semicolon delimiter
        with open(custom_filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            custom_data = list(reader)
        
        print(f"✓ Custom delimiter CSV: {len(custom_data)} rows")
        for row in custom_data:
            print(f"  {row}")
        
        os.remove(custom_filename)
        
    except IOError as e:
        print(f"✗ Error with custom delimiter: {e}")
    
    # Clean up
    os.remove(filename)

def csv_data_validation():
    """Demonstrate CSV data validation and cleaning"""
    print("\n=== CSV Data Validation ===")
    
    # Create data with errors
    messy_data = [
        ['Name', 'Age', 'Email', 'Salary'],
        ['Alice', '25', 'alice@email.com', '50000'],
        ['Bob', 'invalid_age', 'bob@email.com', '60000'],
        ['Charlie', '30', 'invalid_email', '55000'],
        ['Diana', '28', 'diana@email.com', 'invalid_salary'],
        ['', '35', 'eve@email.com', '70000'],  # Missing name
        ['Frank', '40', 'frank@email.com', '80000']
    ]
    
    filename = 'messy_data.csv'
    
    # Write messy data
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(messy_data)
    
    # Read and validate
    valid_records = []
    errors = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row_num, row in enumerate(reader, start=2):  # Start at 2 (after header)
                row_errors = []
                
                # Validate name
                if not row['Name'].strip():
                    row_errors.append("Missing name")
                
                # Validate age
                try:
                    age = int(row['Age'])
                    if age < 0 or age > 120:
                        row_errors.append("Invalid age range")
                except ValueError:
                    row_errors.append("Invalid age format")
                
                # Validate email
                if '@' not in row['Email'] or '.' not in row['Email']:
                    row_errors.append("Invalid email format")
                
                # Validate salary
                try:
                    salary = float(row['Salary'])
                    if salary < 0:
                        row_errors.append("Negative salary")
                except ValueError:
                    row_errors.append("Invalid salary format")
                
                if row_errors:
                    errors.append({
                        'row': row_num,
                        'data': row,
                        'errors': row_errors
                    })
                else:
                    # Clean and convert data
                    clean_row = {
                        'Name': row['Name'].strip(),
                        'Age': int(row['Age']),
                        'Email': row['Email'].lower().strip(),
                        'Salary': float(row['Salary'])
                    }
                    valid_records.append(clean_row)
        
        print(f"✓ Validation complete:")
        print(f"  Valid records: {len(valid_records)}")
        print(f"  Invalid records: {len(errors)}")
        
        if errors:
            print("Validation errors:")
            for error in errors:
                print(f"  Row {error['row']}: {', '.join(error['errors'])}")
        
        # Write clean data
        if valid_records:
            clean_filename = 'clean_data.csv'
            with open(clean_filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Name', 'Age', 'Email', 'Salary']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(valid_records)
            
            print(f"✓ Written {len(valid_records)} clean records to {clean_filename}")
            os.remove(clean_filename)
        
    except IOError as e:
        print(f"✗ Error in validation: {e}")
    
    # Clean up
    os.remove(filename)

# JSON File Operations
def json_basic_operations():
    """Demonstrate basic JSON operations"""
    print("\n=== JSON Basic Operations ===")
    
    # Sample data
    student_data = {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "A",
        "subjects": ["Math", "Physics", "Chemistry"],
        "scores": {
            "Math": 95,
            "Physics": 92,
            "Chemistry": 88
        },
        "active": True,
        "graduation_year": None
    }
    
    filename = 'student.json'
    
    # Write JSON
    try:
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(student_data, jsonfile, indent=2, ensure_ascii=False)
        print(f"✓ Written JSON data to {filename}")
    except IOError as e:
        print(f"✗ Error writing JSON: {e}")
        return
    
    # Read JSON
    try:
        with open(filename, 'r', encoding='utf-8') as jsonfile:
            loaded_data = json.load(jsonfile)
        
        print(f"✓ Loaded JSON data")
        print(f"Student: {loaded_data['name']}")
        print(f"Subjects: {', '.join(loaded_data['subjects'])}")
        print(f"Average score: {sum(loaded_data['scores'].values()) / len(loaded_data['scores']):.1f}")
        
    except (IOError, json.JSONDecodeError) as e:
        print(f"✗ Error reading JSON: {e}")
    
    # JSON string operations
    json_string = json.dumps(student_data, indent=2)
    print(f"✓ JSON string length: {len(json_string)} characters")
    
    parsed_data = json.loads(json_string)
    print(f"✓ Parsed data matches original: {parsed_data == student_data}")
    
    # Clean up
    os.remove(filename)

def json_complex_operations():
    """Demonstrate complex JSON operations"""
    print("\n=== JSON Complex Operations ===")
    
    # Complex nested data
    school_data = {
        "school": {
            "name": "Olympic High School",
            "address": {
                "street": "123 Education St",
                "city": "Learning City",
                "country": "Vietnam"
            },
            "established": 2000
        },
        "students": [
            {
                "id": 1,
                "name": "Alice",
                "classes": [
                    {"subject": "Math", "teacher": "Mr. Smith", "grade": 95},
                    {"subject": "Physics", "teacher": "Ms. Johnson", "grade": 92}
                ]
            },
            {
                "id": 2,
                "name": "Bob",
                "classes": [
                    {"subject": "Math", "teacher": "Mr. Smith", "grade": 87},
                    {"subject": "Chemistry", "teacher": "Dr. Brown", "grade": 90}
                ]
            }
        ],
        "teachers": {
            "Mr. Smith": {"subject": "Math", "experience": 10},
            "Ms. Johnson": {"subject": "Physics", "experience": 8},
            "Dr. Brown": {"subject": "Chemistry", "experience": 15}
        },
        "metadata": {
            "created": datetime.now().isoformat(),
            "version": "1.0"
        }
    }
    
    filename = 'school.json'
    
    # Write complex JSON
    try:
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(school_data, jsonfile, indent=2, ensure_ascii=False)
        print(f"✓ Written complex JSON structure")
    except IOError as e:
        print(f"✗ Error writing complex JSON: {e}")
        return
    
    # Read and analyze
    try:
        with open(filename, 'r', encoding='utf-8') as jsonfile:
            loaded_school = json.load(jsonfile)
        
        # Extract information
        school_name = loaded_school['school']['name']
        student_count = len(loaded_school['students'])
        teacher_count = len(loaded_school['teachers'])
        
        print(f"✓ School: {school_name}")
        print(f"Students: {student_count}, Teachers: {teacher_count}")
        
        # Calculate statistics
        all_grades = []
        subject_grades = {}
        
        for student in loaded_school['students']:
            for class_info in student['classes']:
                grade = class_info['grade']
                subject = class_info['subject']
                
                all_grades.append(grade)
                
                if subject not in subject_grades:
                    subject_grades[subject] = []
                subject_grades[subject].append(grade)
        
        if all_grades:
            avg_grade = sum(all_grades) / len(all_grades)
            print(f"Overall average grade: {avg_grade:.1f}")
            
            print("Subject averages:")
            for subject, grades in subject_grades.items():
                subject_avg = sum(grades) / len(grades)
                print(f"  {subject}: {subject_avg:.1f}")
        
    except (IOError, json.JSONDecodeError, KeyError) as e:
        print(f"✗ Error processing complex JSON: {e}")
    
    # Clean up
    os.remove(filename)

def json_data_transformation():
    """Demonstrate JSON data transformation"""
    print("\n=== JSON Data Transformation ===")
    
    # Original format
    original_data = [
        {"name": "Alice", "math": 95, "physics": 92, "chemistry": 88},
        {"name": "Bob", "math": 87, "physics": 85, "chemistry": 90},
        {"name": "Charlie", "math": 92, "physics": 88, "chemistry": 85}
    ]
    
    # Transform to different format
    def transform_student_data(students):
        """Transform flat structure to nested structure"""
        transformed = []
        
        for student in students:
            new_student = {
                "name": student["name"],
                "subjects": []
            }
            
            for subject in ["math", "physics", "chemistry"]:
                if subject in student:
                    new_student["subjects"].append({
                        "name": subject.capitalize(),
                        "score": student[subject]
                    })
            
            # Calculate average
            scores = [s["score"] for s in new_student["subjects"]]
            new_student["average"] = sum(scores) / len(scores) if scores else 0
            
            transformed.append(new_student)
        
        return transformed
    
    # Apply transformation
    transformed_data = transform_student_data(original_data)
    
    # Save both formats
    original_file = 'original_format.json'
    transformed_file = 'transformed_format.json'
    
    try:
        # Save original
        with open(original_file, 'w') as f:
            json.dump(original_data, f, indent=2)
        
        # Save transformed
        with open(transformed_file, 'w') as f:
            json.dump(transformed_data, f, indent=2)
        
        print("✓ Saved both data formats")
        
        # Compare file sizes
        original_size = os.path.getsize(original_file)
        transformed_size = os.path.getsize(transformed_file)
        
        print(f"Original format: {original_size} bytes")
        print(f"Transformed format: {transformed_size} bytes")
        
        # Show sample of transformed data
        print("Sample transformed record:")
        sample = transformed_data[0]
        print(f"  Name: {sample['name']}")
        print(f"  Average: {sample['average']:.1f}")
        print(f"  Subjects: {len(sample['subjects'])}")
        
    except IOError as e:
        print(f"✗ Error in transformation: {e}")
    
    finally:
        # Clean up
        for filename in [original_file, transformed_file]:
            if os.path.exists(filename):
                os.remove(filename)

def json_error_handling():
    """Demonstrate JSON error handling"""
    print("\n=== JSON Error Handling ===")
    
    # Create invalid JSON files
    test_cases = [
        ('valid.json', '{"name": "Alice", "age": 25}'),
        ('invalid_syntax.json', '{"name": "Bob", "age": 30,}'),  # Trailing comma
        ('invalid_quotes.json', "{'name': 'Charlie', 'age': 35}"),  # Single quotes
        ('incomplete.json', '{"name": "Diana", "age":'),  # Incomplete
        ('empty.json', ''),  # Empty file
    ]
    
    for filename, content in test_cases:
        # Write test file
        try:
            with open(filename, 'w') as f:
                f.write(content)
        except IOError:
            continue
        
        # Try to read and parse
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            print(f"✓ {filename}: Valid JSON - {data}")
            
        except json.JSONDecodeError as e:
            print(f"✗ {filename}: JSON decode error - {e}")
            
        except IOError as e:
            print(f"✗ {filename}: File error - {e}")
        
        # Clean up
        try:
            os.remove(filename)
        except OSError:
            pass
    
    # Demonstrate safe JSON parsing
    def safe_json_load(filename, default=None):
        """Safely load JSON with fallback"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load {filename}: {e}")
            return default
    
    # Test safe loading
    test_data = {"test": "data"}
    test_file = 'safe_test.json'
    
    with open(test_file, 'w') as f:
        json.dump(test_data, f)
    
    # This should work
    result = safe_json_load(test_file, {})
    print(f"✓ Safe load successful: {result}")
    
    # This should return default
    result = safe_json_load('nonexistent.json', {"default": True})
    print(f"✓ Safe load with default: {result}")
    
    # Clean up
    os.remove(test_file)

# Test all functions
if __name__ == "__main__":
    csv_basic_operations()
    csv_advanced_operations()
    csv_data_validation()
    json_basic_operations()
    json_complex_operations()
    json_data_transformation()
    json_error_handling()
    
    print("\n=== Bài tập thực hành ===")
    print("1. Build data pipeline: CSV → JSON → Database")
    print("2. Create configuration file manager (JSON)")
    print("3. Implement data export system (multiple formats)")
    print("4. Build log file analyzer với structured output")