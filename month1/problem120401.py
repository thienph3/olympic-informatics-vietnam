"""
Problem 120401: Debugging và logging
Implement debugging techniques, logging, và simple testing

Bài 1: Debugging Techniques
- Print debugging
- Assert statements
- Logging framework

Bài 2: Testing và Profiling
- Unit testing patterns
- Performance profiling
- Memory usage tracking
"""

import logging
import time
import sys
import traceback
import cProfile
import pstats
import io
from functools import wraps
from typing import Any, Callable, Dict, List

# Debugging Techniques
def print_debugging_demo():
    """Demonstrate print debugging techniques"""
    print("=== Print Debugging Demo ===")
    
    def calculate_factorial(n):
        """Calculate factorial with debug prints"""
        print(f"DEBUG: calculate_factorial called with n={n}")
        
        if n < 0:
            print(f"DEBUG: Invalid input n={n}, returning None")
            return None
        
        result = 1
        print(f"DEBUG: Starting calculation, initial result={result}")
        
        for i in range(1, n + 1):
            old_result = result
            result *= i
            print(f"DEBUG: Step {i}: {old_result} * {i} = {result}")
        
        print(f"DEBUG: Final result for {n}! = {result}")
        return result
    
    # Test with debug output
    test_values = [0, 1, 5, -1]
    for val in test_values:
        print(f"\nTesting factorial({val}):")
        result = calculate_factorial(val)
        print(f"Result: {result}")

def debug_decorator_demo():
    """Demonstrate debug decorator"""
    print("\n=== Debug Decorator Demo ===")
    
    def debug_calls(func):
        """Decorator to debug function calls"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log function entry
            args_str = ', '.join([repr(arg) for arg in args])
            kwargs_str = ', '.join([f"{k}={repr(v)}" for k, v in kwargs.items()])
            all_args = ', '.join(filter(None, [args_str, kwargs_str]))
            
            print(f"DEBUG: Calling {func.__name__}({all_args})")
            
            # Call function and measure time
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                
                print(f"DEBUG: {func.__name__} returned {repr(result)} in {end_time - start_time:.4f}s")
                return result
                
            except Exception as e:
                end_time = time.time()
                print(f"DEBUG: {func.__name__} raised {type(e).__name__}: {e} in {end_time - start_time:.4f}s")
                raise
        
        return wrapper
    
    @debug_calls
    def fibonacci(n):
        """Calculate fibonacci number"""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    @debug_calls
    def divide(a, b):
        """Divide two numbers"""
        return a / b
    
    # Test debug decorator
    print("Testing fibonacci(5):")
    result = fibonacci(5)
    
    print("\nTesting division:")
    result = divide(10, 2)
    
    try:
        result = divide(10, 0)
    except ZeroDivisionError:
        print("Caught expected division by zero error")

def assert_debugging_demo():
    """Demonstrate assert statements for debugging"""
    print("\n=== Assert Debugging Demo ===")
    
    def validate_input(data):
        """Validate input data with assertions"""
        # Type assertions
        assert isinstance(data, dict), f"Expected dict, got {type(data)}"
        
        # Required fields
        required_fields = ['name', 'age', 'email']
        for field in required_fields:
            assert field in data, f"Missing required field: {field}"
        
        # Value assertions
        assert isinstance(data['name'], str), "Name must be string"
        assert len(data['name']) > 0, "Name cannot be empty"
        
        assert isinstance(data['age'], int), "Age must be integer"
        assert 0 <= data['age'] <= 150, f"Invalid age: {data['age']}"
        
        assert isinstance(data['email'], str), "Email must be string"
        assert '@' in data['email'], "Invalid email format"
        
        return True
    
    def process_user_data(users):
        """Process user data with assertions"""
        assert isinstance(users, list), "Users must be a list"
        assert len(users) > 0, "User list cannot be empty"
        
        processed = []
        for i, user in enumerate(users):
            print(f"Processing user {i + 1}: {user.get('name', 'Unknown')}")
            
            # Validate each user
            validate_input(user)
            
            # Process user
            processed_user = {
                'name': user['name'].strip().title(),
                'age': user['age'],
                'email': user['email'].lower(),
                'adult': user['age'] >= 18
            }
            
            processed.append(processed_user)
        
        assert len(processed) == len(users), "Processing count mismatch"
        return processed
    
    # Test with valid data
    valid_users = [
        {'name': 'alice', 'age': 25, 'email': 'Alice@Email.com'},
        {'name': 'bob', 'age': 17, 'email': 'bob@email.com'}
    ]
    
    try:
        result = process_user_data(valid_users)
        print(f"✓ Processed {len(result)} users successfully")
        for user in result:
            print(f"  {user['name']}: {user['age']} years, adult: {user['adult']}")
    except AssertionError as e:
        print(f"✗ Assertion failed: {e}")
    
    # Test with invalid data
    invalid_users = [
        {'name': '', 'age': 25, 'email': 'test@email.com'},  # Empty name
        {'name': 'Charlie', 'age': -5, 'email': 'charlie@email.com'}  # Invalid age
    ]
    
    for i, invalid_user in enumerate(invalid_users):
        try:
            process_user_data([invalid_user])
        except AssertionError as e:
            print(f"✓ Caught expected assertion error for invalid user {i + 1}: {e}")

# Logging Framework
def logging_setup_demo():
    """Demonstrate logging setup and usage"""
    print("\n=== Logging Setup Demo ===")
    
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('debug.log', mode='w')
        ]
    )
    
    # Create logger
    logger = logging.getLogger('demo_logger')
    
    def process_data(data):
        """Process data with comprehensive logging"""
        logger.info(f"Starting data processing for {len(data)} items")
        
        results = []
        errors = 0
        
        for i, item in enumerate(data):
            logger.debug(f"Processing item {i}: {item}")
            
            try:
                if not isinstance(item, (int, float)):
                    raise TypeError(f"Expected number, got {type(item)}")
                
                if item < 0:
                    logger.warning(f"Negative value encountered: {item}")
                
                # Simulate processing
                result = item ** 2
                results.append(result)
                
                logger.debug(f"Item {i} processed: {item} -> {result}")
                
            except Exception as e:
                logger.error(f"Error processing item {i} ({item}): {e}")
                errors += 1
        
        logger.info(f"Processing complete: {len(results)} successful, {errors} errors")
        
        if errors > 0:
            logger.warning(f"Processing completed with {errors} errors")
        
        return results
    
    # Test logging
    test_data = [1, 2, 3, -4, 5, "invalid", 6.5, None, 7]
    results = process_data(test_data)
    
    print(f"✓ Processing complete. Results: {results}")
    print("✓ Check 'debug.log' file for detailed logs")

def custom_logger_demo():
    """Demonstrate custom logger configuration"""
    print("\n=== Custom Logger Demo ===")
    
    class ColoredFormatter(logging.Formatter):
        """Custom formatter with colors"""
        
        COLORS = {
            'DEBUG': '\033[36m',    # Cyan
            'INFO': '\033[32m',     # Green
            'WARNING': '\033[33m',  # Yellow
            'ERROR': '\033[31m',    # Red
            'CRITICAL': '\033[35m', # Magenta
        }
        RESET = '\033[0m'
        
        def format(self, record):
            log_color = self.COLORS.get(record.levelname, '')
            record.levelname = f"{log_color}{record.levelname}{self.RESET}"
            return super().format(record)
    
    # Create custom logger
    custom_logger = logging.getLogger('custom_logger')
    custom_logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers
    custom_logger.handlers.clear()
    
    # Create console handler with custom formatter
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    
    formatter = ColoredFormatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    custom_logger.addHandler(console_handler)
    
    # Test custom logger
    custom_logger.debug("This is a debug message")
    custom_logger.info("This is an info message")
    custom_logger.warning("This is a warning message")
    custom_logger.error("This is an error message")
    custom_logger.critical("This is a critical message")

# Testing Patterns
def simple_testing_demo():
    """Demonstrate simple testing patterns"""
    print("\n=== Simple Testing Demo ===")
    
    # Functions to test
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def is_even(n):
        """Check if number is even"""
        return n % 2 == 0
    
    # Test framework
    class SimpleTestRunner:
        def __init__(self):
            self.tests_run = 0
            self.tests_passed = 0
            self.tests_failed = 0
            self.failures = []
        
        def assert_equal(self, actual, expected, message=""):
            """Assert that two values are equal"""
            self.tests_run += 1
            if actual == expected:
                self.tests_passed += 1
                print(f"✓ Test passed: {message}")
            else:
                self.tests_failed += 1
                failure_msg = f"✗ Test failed: {message}\n  Expected: {expected}\n  Actual: {actual}"
                print(failure_msg)
                self.failures.append(failure_msg)
        
        def assert_raises(self, func, exception_type, *args, **kwargs):
            """Assert that function raises specific exception"""
            self.tests_run += 1
            try:
                result = func(*args, **kwargs)
                self.tests_failed += 1
                failure_msg = f"✗ Expected {exception_type.__name__} but got result: {result}"
                print(failure_msg)
                self.failures.append(failure_msg)
            except exception_type:
                self.tests_passed += 1
                print(f"✓ Correctly raised {exception_type.__name__}")
            except Exception as e:
                self.tests_failed += 1
                failure_msg = f"✗ Expected {exception_type.__name__} but got {type(e).__name__}: {e}"
                print(failure_msg)
                self.failures.append(failure_msg)
        
        def run_summary(self):
            """Print test summary"""
            print(f"\n=== Test Summary ===")
            print(f"Tests run: {self.tests_run}")
            print(f"Passed: {self.tests_passed}")
            print(f"Failed: {self.tests_failed}")
            print(f"Success rate: {self.tests_passed/self.tests_run*100:.1f}%")
            
            if self.failures:
                print("\nFailures:")
                for failure in self.failures:
                    print(failure)
    
    # Run tests
    runner = SimpleTestRunner()
    
    # Test add function
    runner.assert_equal(add(2, 3), 5, "add(2, 3) == 5")
    runner.assert_equal(add(-1, 1), 0, "add(-1, 1) == 0")
    runner.assert_equal(add(0, 0), 0, "add(0, 0) == 0")
    
    # Test multiply function
    runner.assert_equal(multiply(3, 4), 12, "multiply(3, 4) == 12")
    runner.assert_equal(multiply(-2, 5), -10, "multiply(-2, 5) == -10")
    runner.assert_equal(multiply(0, 100), 0, "multiply(0, 100) == 0")
    
    # Test divide function
    runner.assert_equal(divide(10, 2), 5, "divide(10, 2) == 5")
    runner.assert_equal(divide(7, 2), 3.5, "divide(7, 2) == 3.5")
    runner.assert_raises(divide, ValueError, 10, 0)
    
    # Test is_even function
    runner.assert_equal(is_even(4), True, "is_even(4) == True")
    runner.assert_equal(is_even(5), False, "is_even(5) == False")
    runner.assert_equal(is_even(0), True, "is_even(0) == True")
    
    # Intentional failure for demo
    runner.assert_equal(add(2, 2), 5, "Intentional failure: add(2, 2) == 5")
    
    runner.run_summary()

# Performance Profiling
def profiling_demo():
    """Demonstrate performance profiling"""
    print("\n=== Performance Profiling Demo ===")
    
    def slow_function():
        """Intentionally slow function for profiling"""
        total = 0
        for i in range(100000):
            total += i * i
        return total
    
    def medium_function():
        """Medium speed function"""
        return sum(i * i for i in range(10000))
    
    def fast_function():
        """Fast function"""
        return sum(range(1000))
    
    def profile_function(func, *args, **kwargs):
        """Profile a single function"""
        profiler = cProfile.Profile()
        
        # Profile the function
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        
        # Get stats
        stats_stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stats_stream)
        stats.sort_stats('cumulative')
        stats.print_stats(10)  # Top 10 functions
        
        print(f"Function {func.__name__} result: {result}")
        print("Profiling stats:")
        print(stats_stream.getvalue())
        
        return result
    
    # Profile individual functions
    print("Profiling slow_function:")
    profile_function(slow_function)
    
    print("\nProfiling medium_function:")
    profile_function(medium_function)
    
    # Time comparison
    def time_functions():
        """Compare function execution times"""
        functions = [fast_function, medium_function, slow_function]
        
        print("\nExecution time comparison:")
        for func in functions:
            start_time = time.time()
            result = func()
            end_time = time.time()
            
            print(f"{func.__name__}: {end_time - start_time:.4f}s (result: {result})")
    
    time_functions()

def memory_tracking_demo():
    """Demonstrate simple memory usage tracking"""
    print("\n=== Memory Tracking Demo ===")
    
    def get_object_size(obj):
        """Get approximate size of object"""
        return sys.getsizeof(obj)
    
    def memory_usage_test():
        """Test memory usage of different data structures"""
        # Test different data structures
        small_list = list(range(100))
        large_list = list(range(100000))
        
        small_dict = {i: i*2 for i in range(100)}
        large_dict = {i: i*2 for i in range(100000)}
        
        small_string = "Hello World" * 10
        large_string = "Hello World" * 10000
        
        objects = [
            ("small_list", small_list),
            ("large_list", large_list),
            ("small_dict", small_dict),
            ("large_dict", large_dict),
            ("small_string", small_string),
            ("large_string", large_string)
        ]
        
        print("Memory usage comparison:")
        for name, obj in objects:
            size = get_object_size(obj)
            print(f"{name}: {size:,} bytes ({size/1024:.1f} KB)")
    
    memory_usage_test()

# Test all functions
if __name__ == "__main__":
    print_debugging_demo()
    debug_decorator_demo()
    assert_debugging_demo()
    logging_setup_demo()
    custom_logger_demo()
    simple_testing_demo()
    profiling_demo()
    memory_tracking_demo()
    
    print("\n=== Bài tập thực hành ===")
    print("1. Build comprehensive test suite cho Olympic algorithms")
    print("2. Create performance benchmarking tool")
    print("3. Implement debugging dashboard với real-time monitoring")
    print("4. Build automated testing framework với coverage reporting")