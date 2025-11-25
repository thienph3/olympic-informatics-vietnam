"""
Problem 110101: Lambda cơ bản với map, filter, sorted
Sử dụng lambda với các built-in functions để xử lý dữ liệu

Bài 1: Lambda với map và filter
- Transform data với map()
- Filter data với điều kiện
- Combine multiple operations

Bài 2: Lambda với sorted và key functions
- Sort với custom criteria
- Multiple sorting keys
- Complex data structures
"""

# Lambda với map()
def test_map_operations():
    """Test lambda với map function"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Square numbers
    squares = list(map(lambda x: x**2, numbers))
    print(f"Squares: {squares}")
    
    # Convert to strings
    str_numbers = list(map(lambda x: str(x), numbers))
    print(f"Strings: {str_numbers}")
    
    # Temperature conversion
    celsius = [0, 20, 30, 40, 100]
    fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
    print(f"Celsius to Fahrenheit: {list(zip(celsius, fahrenheit))}")
    
    # Multiple lists
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    products = list(map(lambda x, y: x * y, list1, list2))
    print(f"Products: {products}")

def test_filter_operations():
    """Test lambda với filter function"""
    numbers = list(range(1, 21))
    
    # Even numbers
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Numbers divisible by 3
    div_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
    print(f"Divisible by 3: {div_by_3}")
    
    # Prime numbers (simple check)
    def is_prime_simple(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = list(filter(lambda x: is_prime_simple(x), numbers))
    print(f"Prime numbers: {primes}")
    
    # Filter strings
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    long_words = list(filter(lambda w: len(w) > 5, words))
    print(f"Long words: {long_words}")
    
    # Filter with multiple conditions
    perfect_squares = list(filter(lambda x: int(x**0.5)**2 == x, numbers))
    print(f"Perfect squares: {perfect_squares}")

def test_sorted_operations():
    """Test lambda với sorted function"""
    # Sort numbers by different criteria
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    # Sort by absolute distance from 5
    sorted_by_distance = sorted(numbers, key=lambda x: abs(x - 5))
    print(f"Sorted by distance from 5: {sorted_by_distance}")
    
    # Sort strings by length
    words = ["python", "java", "c", "javascript", "go", "rust"]
    sorted_by_length = sorted(words, key=lambda w: len(w))
    print(f"Sorted by length: {sorted_by_length}")
    
    # Sort by length, then alphabetically
    sorted_complex = sorted(words, key=lambda w: (len(w), w))
    print(f"Sorted by length then alphabetically: {sorted_complex}")
    
    # Sort tuples
    students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 92)]
    
    # Sort by grade
    by_grade = sorted(students, key=lambda s: s[1])
    print(f"Sorted by grade: {by_grade}")
    
    # Sort by name
    by_name = sorted(students, key=lambda s: s[0])
    print(f"Sorted by name: {by_name}")
    
    # Sort by grade descending
    by_grade_desc = sorted(students, key=lambda s: s[1], reverse=True)
    print(f"Sorted by grade (desc): {by_grade_desc}")

def test_combined_operations():
    """Test combining map, filter, sorted"""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    # Chain operations: filter evens, square them, sort descending
    result = sorted(
        map(lambda x: x**2, 
            filter(lambda x: x % 2 == 0, data)
        ), 
        reverse=True
    )
    print(f"Even squares (desc): {list(result)}")
    
    # Process student data
    students = [
        {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
        {"name": "Bob", "age": 19, "grades": [92, 88, 85]},
        {"name": "Charlie", "age": 21, "grades": [78, 82, 80]},
        {"name": "Diana", "age": 20, "grades": [95, 93, 97]}
    ]
    
    # Calculate average grades
    with_averages = list(map(
        lambda s: {**s, "average": sum(s["grades"]) / len(s["grades"])},
        students
    ))
    
    # Filter high performers (avg >= 85)
    high_performers = list(filter(
        lambda s: s["average"] >= 85,
        with_averages
    ))
    
    # Sort by average descending
    top_students = sorted(high_performers, 
                         key=lambda s: s["average"], 
                         reverse=True)
    
    print("Top students:")
    for student in top_students:
        print(f"  {student['name']}: {student['average']:.1f}")

def test_reduce_operations():
    """Test lambda với reduce function"""
    from functools import reduce
    
    numbers = [1, 2, 3, 4, 5]
    
    # Sum
    total = reduce(lambda x, y: x + y, numbers)
    print(f"Sum: {total}")
    
    # Product
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product: {product}")
    
    # Maximum
    maximum = reduce(lambda x, y: x if x > y else y, numbers)
    print(f"Maximum: {maximum}")
    
    # Concatenate strings
    words = ["Hello", " ", "World", "!"]
    sentence = reduce(lambda x, y: x + y, words)
    print(f"Sentence: '{sentence}'")
    
    # Find longest string
    word_list = ["python", "java", "javascript", "go"]
    longest = reduce(lambda x, y: x if len(x) > len(y) else y, word_list)
    print(f"Longest word: {longest}")

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Lambda với map và filter ===")
    
    print("Map operations:")
    test_map_operations()
    
    print("\nFilter operations:")
    test_filter_operations()
    
    print("\n=== Bài 2: Lambda với sorted ===")
    test_sorted_operations()
    
    print("\n=== Combined Operations ===")
    test_combined_operations()
    
    print("\n=== Reduce Operations ===")
    test_reduce_operations()

    print("\n=== Bài tập thực hành ===")
    print("1. Filter và transform list of dictionaries")
    print("2. Sort complex nested data structures")
    print("3. Chain multiple lambda operations")
    print("4. Create data processing pipeline với lambda")