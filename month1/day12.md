# Day 12: Module, file I/O, exception handling, debugging

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Modules và Packages (45')

### 📚 Lý thuyết (15')

#### Import modules
```python
# Import toàn bộ module
import math
print(math.pi)
print(math.sqrt(16))

# Import specific functions
from math import pi, sqrt, sin, cos
print(pi)
print(sqrt(25))

# Import với alias
import math as m
from math import sqrt as square_root
print(m.pi)
print(square_root(9))

# Import all (không khuyến khích)
from math import *
print(factorial(5))
```

#### Standard library modules
```python
# os module - operating system interface
import os
print(os.getcwd())  # Current directory
print(os.listdir('.'))  # List files

# sys module - system parameters
import sys
print(sys.version)
print(sys.argv)  # Command line arguments

# datetime module
from datetime import datetime, date, timedelta
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# random module
import random
print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c']))

# collections module
from collections import Counter, defaultdict, deque
counter = Counter("hello world")
print(counter)
```

#### Creating custom modules
```python
# File: my_math.py
def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

PI = 3.14159

# File: main.py
import my_math
from my_math import add, PI

result = my_math.multiply(5, 3)
sum_result = add(10, 20)
print(f"Pi = {PI}")
```

#### Module search path
```python
import sys
print("Module search paths:")
for path in sys.path:
    print(f"  {path}")

# Add custom path
sys.path.append('/path/to/custom/modules')
```

### 💻 Thực hành (30')

#### Bài tập 1: Standard library modules

**Yêu cầu:** Sử dụng các standard modules: os, sys, datetime, random, collections.

**File thực hành:** [problem120101.py](problem120101.py)

#### Bài tập 2: Custom modules và packages

**Yêu cầu:** Tạo custom modules, organize code thành packages.

**File thực hành:** [problem120102.py](problem120102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: File I/O (45')

### 📚 Lý thuyết (20')

#### Reading files
```python
# Read entire file
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Read all lines into list
with open('data.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Read specific number of characters
with open('data.txt', 'r') as file:
    chunk = file.read(10)
    print(chunk)
```

#### Writing files
```python
# Write to file (overwrite)
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Python file I/O\n")

# Append to file
with open('output.txt', 'a') as file:
    file.write("Appended line\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)
```

#### File modes và encoding
```python
# Different file modes
# 'r' - read (default)
# 'w' - write (overwrite)
# 'a' - append
# 'x' - exclusive creation
# 'b' - binary mode
# 't' - text mode (default)
# '+' - read and write

# Binary files
with open('image.jpg', 'rb') as file:
    data = file.read()

# Encoding
with open('unicode.txt', 'r', encoding='utf-8') as file:
    content = file.read()

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("Tiếng Việt có dấu")
```

#### Working with CSV
```python
import csv

# Read CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Write CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# CSV with dictionaries
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'])
```

#### JSON files
```python
import json

# Read JSON
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Write JSON
data = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'coding']
}

with open('output.json', 'w') as file:
    json.dump(data, file, indent=2)

# JSON strings
json_string = json.dumps(data, indent=2)
parsed_data = json.loads(json_string)
```

### 💻 Thực hành (25')

#### Bài tập 1: File operations cơ bản

**Yêu cầu:** Read/write text files, handle different encodings, process large files.

**File thực hành:** [problem120201.py](problem120201.py)

#### Bài tập 2: Structured data files

**Yêu cầu:** Work with CSV, JSON files, data processing và analysis.

**File thực hành:** [problem120202.py](problem120202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Exception Handling (45')

### 📚 Lý thuyết (15')

#### Basic exception handling
```python
# Try-except basic
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid number format!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catch multiple exceptions
try:
    # Some risky code
    pass
except (ValueError, TypeError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

# Catch all exceptions
try:
    # Some code
    pass
except Exception as e:
    print(f"Unexpected error: {e}")
```

#### Exception hierarchy
```python
# Common built-in exceptions
try:
    # ValueError - wrong value type
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    # TypeError - wrong type
    "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

try:
    # IndexError - list index out of range
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"IndexError: {e}")

try:
    # KeyError - dictionary key not found
    d = {'a': 1}
    print(d['b'])
except KeyError as e:
    print(f"KeyError: {e}")

try:
    # FileNotFoundError
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
```

#### Finally và else clauses
```python
# Finally - always executes
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    # This always runs
    print("Cleanup code here")
    if 'file' in locals():
        file.close()

# Else - runs if no exception
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Always executed")
```

#### Raising exceptions
```python
# Raise built-in exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

# Custom exceptions
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative")
    if age > 150:
        raise CustomError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except CustomError as e:
    print(f"Validation error: {e}")
```

### 💻 Thực hành (30')

#### Bài tập 1: Exception handling patterns

**Yêu cầu:** Handle different types of exceptions, create custom exceptions.

**File thực hành:** [problem120301.py](problem120301.py)

#### Bài tập 2: Robust file processing

**Yêu cầu:** Build robust file processing với comprehensive error handling.

**File thực hành:** [problem120302.py](problem120302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Debugging và Testing (45')

### 📚 Lý thuyết (15')

#### Debugging techniques
```python
# Print debugging
def calculate_average(numbers):
    print(f"Input: {numbers}")  # Debug print
    total = sum(numbers)
    print(f"Total: {total}")    # Debug print
    count = len(numbers)
    print(f"Count: {count}")    # Debug print
    average = total / count
    print(f"Average: {average}") # Debug print
    return average

# Using assert for debugging
def factorial(n):
    assert n >= 0, "n must be non-negative"
    assert isinstance(n, int), "n must be an integer"
    
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Logging
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(data):
    logging.info(f"Processing {len(data)} items")
    
    for i, item in enumerate(data):
        logging.debug(f"Processing item {i}: {item}")
        
        if item < 0:
            logging.warning(f"Negative value found: {item}")
        
        try:
            result = 1 / item
            logging.debug(f"Result: {result}")
        except ZeroDivisionError:
            logging.error(f"Division by zero for item {i}")
```

#### Simple testing
```python
# Unit testing với assert
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("All add tests passed!")

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    print("All factorial tests passed!")

# Test runner
def run_all_tests():
    try:
        test_add()
        test_factorial()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")

# Doctest
def multiply(a, b):
    """
    Multiply two numbers.
    
    >>> multiply(2, 3)
    6
    >>> multiply(-1, 5)
    -5
    >>> multiply(0, 10)
    0
    """
    return a * b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

#### Performance profiling
```python
import time
import cProfile

# Time measurement
def time_function(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__} took {end - start:.4f} seconds")
    return result

# Profile code
def slow_function():
    total = 0
    for i in range(1000000):
        total += i * i
    return total

# Run profiler
cProfile.run('slow_function()')

# Memory usage (simple tracking)
import sys

def get_size(obj):
    return sys.getsizeof(obj)

# Track object sizes
numbers = list(range(1000))
print(f"List size: {get_size(numbers)} bytes")
```

### 💻 Thực hành (30')

#### Bài tập 1: Debugging và logging

**Yêu cầu:** Implement debugging techniques, logging, và simple testing.

**File thực hành:** [problem120401.py](problem120401.py)

#### Bài tập 2: Olympic problem solver với error handling

**Yêu cầu:** Build complete Olympic problem solver với robust error handling.

**File thực hành:** [problem120402.py](problem120402.py)

---

## Bài tập về nhà

### Bài 1: File Processing System
Tạo hệ thống xử lý file:
- Read/write multiple file formats (txt, csv, json)
- Batch processing với error handling
- Data validation và cleaning
- Progress tracking và logging
- Configuration file support

### Bài 2: Olympic Contest Manager
Build contest management system:
- Problem loading từ files
- Solution testing và validation
- Score calculation và ranking
- Result export (multiple formats)
- Error handling và recovery

### Bài 3: Debug Toolkit
Tạo debugging toolkit:
- Function profiler
- Memory usage tracker
- Test case generator
- Code coverage analyzer
- Performance benchmarking

### Gợi ý làm bài
1. Sử dụng context managers cho file operations
2. Implement comprehensive exception handling
3. Add logging cho debugging và monitoring
4. Create reusable modules và functions

---

## Tổng kết Day 12

**Đã học:**
- Modules và packages: import, standard library, custom modules
- File I/O: text/binary files, CSV, JSON, encoding
- Exception handling: try/except, custom exceptions, error recovery
- Debugging: print debugging, logging, assertions, testing
- Performance: profiling, optimization techniques
- Best practices: code organization, error handling patterns

**Tổng kết Tháng 1:**
- **12 ngày học:** Python fundamentals đến advanced concepts
- **78 file bài tập:** Thực hành từ cơ bản đến Olympic-level
- **Kiến thức nền tảng:** Variables, control flow, functions, data structures
- **Kỹ năng lập trình:** Problem solving, debugging, code organization
- **Chuẩn bị Tháng 2:** Algorithms và data structures cho Olympic

**Chuẩn bị cho Tháng 2:**
- Ôn tập tất cả concepts từ Day 1-12
- Hoàn thành tất cả bài tập về nhà
- Thực hành giải bài toán Olympic cơ bản
- Chuẩn bị học Algorithms và Advanced Data Structures