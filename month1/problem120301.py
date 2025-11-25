"""
Problem 120301: Exception handling patterns
Handle different types of exceptions, create custom exceptions

Bài 1: Basic Exception Handling
- Try-except patterns
- Multiple exception types
- Exception hierarchy

Bài 2: Advanced Exception Handling
- Custom exceptions
- Exception chaining
- Context managers
"""

import os
import json
import time
import random
from typing import List, Dict, Any, Optional

# Basic Exception Handling
def basic_exception_patterns():
    """Demonstrate basic exception handling patterns"""
    print("=== Basic Exception Patterns ===")
    
    # Pattern 1: Specific exception handling
    def safe_division(a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print(f"✗ Cannot divide {a} by zero")
            return None
        except TypeError as e:
            print(f"✗ Type error in division: {e}")
            return None
    
    # Test safe division
    test_cases = [(10, 2), (10, 0), (10, "invalid"), (None, 5)]
    for a, b in test_cases:
        result = safe_division(a, b)
        if result is not None:
            print(f"✓ {a} / {b} = {result}")
    
    # Pattern 2: Multiple exceptions
    def safe_list_access(lst, index):
        try:
            return lst[index]
        except IndexError:
            print(f"✗ Index {index} out of range for list of length {len(lst)}")
            return None
        except TypeError:
            print(f"✗ Invalid index type: {type(index)}")
            return None
    
    # Test list access
    test_list = [1, 2, 3, 4, 5]
    test_indices = [2, 10, "invalid", -1]
    for idx in test_indices:
        result = safe_list_access(test_list, idx)
        if result is not None:
            print(f"✓ list[{idx}] = {result}")
    
    # Pattern 3: Catch multiple exception types
    def safe_conversion(value, target_type):
        try:
            if target_type == int:
                return int(value)
            elif target_type == float:
                return float(value)
            elif target_type == str:
                return str(value)
            else:
                raise ValueError(f"Unsupported type: {target_type}")
        except (ValueError, TypeError) as e:
            print(f"✗ Conversion error: {e}")
            return None
    
    # Test conversions
    conversions = [
        ("123", int),
        ("12.34", float),
        (456, str),
        ("invalid", int),
        (None, float)
    ]
    
    for value, target in conversions:
        result = safe_conversion(value, target)
        if result is not None:
            print(f"✓ {value} → {target.__name__}: {result}")

def exception_hierarchy_demo():
    """Demonstrate exception hierarchy"""
    print("\n=== Exception Hierarchy Demo ===")
    
    def demonstrate_hierarchy():
        """Show how exception hierarchy works"""
        exceptions_to_test = [
            (ValueError("Invalid value"), "ValueError"),
            (TypeError("Wrong type"), "TypeError"),
            (FileNotFoundError("File not found"), "FileNotFoundError"),
            (KeyError("Missing key"), "KeyError"),
            (IndexError("Index out of range"), "IndexError")
        ]
        
        for exception, name in exceptions_to_test:
            try:
                raise exception
            except LookupError as e:
                print(f"✓ Caught {name} as LookupError: {e}")
            except ValueError as e:
                print(f"✓ Caught {name} as ValueError: {e}")
            except TypeError as e:
                print(f"✓ Caught {name} as TypeError: {e}")
            except OSError as e:
                print(f"✓ Caught {name} as OSError: {e}")
            except Exception as e:
                print(f"✓ Caught {name} as generic Exception: {e}")
    
    demonstrate_hierarchy()
    
    # Demonstrate catch order importance
    def catch_order_demo():
        """Show importance of exception catch order"""
        print("\nException catch order:")
        
        try:
            raise ValueError("Test error")
        except Exception as e:
            print(f"✓ Caught by Exception: {e}")
        except ValueError as e:
            print(f"✗ This will never execute (unreachable)")
        
        # Correct order
        try:
            raise ValueError("Test error")
        except ValueError as e:
            print(f"✓ Caught by ValueError: {e}")
        except Exception as e:
            print(f"✗ This won't execute for ValueError")
    
    catch_order_demo()

def finally_and_else_demo():
    """Demonstrate finally and else clauses"""
    print("\n=== Finally and Else Demo ===")
    
    def file_operation_demo(filename, should_fail=False):
        """Demonstrate finally clause with file operations"""
        file_handle = None
        try:
            print(f"Attempting to open {filename}")
            if should_fail:
                raise FileNotFoundError(f"Simulated error for {filename}")
            
            file_handle = open(filename, 'w')
            file_handle.write("Test content")
            print(f"✓ Successfully wrote to {filename}")
            
        except FileNotFoundError as e:
            print(f"✗ File error: {e}")
            return False
        except IOError as e:
            print(f"✗ IO error: {e}")
            return False
        else:
            print(f"✓ No exceptions occurred for {filename}")
            return True
        finally:
            print(f"Cleanup: Closing file handle for {filename}")
            if file_handle:
                file_handle.close()
            # Clean up test file
            if os.path.exists(filename):
                os.remove(filename)
    
    # Test successful operation
    file_operation_demo("test_success.txt", should_fail=False)
    
    # Test failed operation
    file_operation_demo("test_fail.txt", should_fail=True)
    
    # Demonstrate else clause
    def division_with_else(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print(f"✗ Cannot divide by zero")
            return None
        else:
            print(f"✓ Division successful: {a} / {b} = {result}")
            return result
        finally:
            print(f"Division operation completed for {a} / {b}")
    
    division_with_else(10, 2)
    division_with_else(10, 0)

# Custom Exceptions
class ValidationError(Exception):
    """Custom exception for validation errors"""
    def __init__(self, message, field=None, value=None):
        self.message = message
        self.field = field
        self.value = value
        super().__init__(self.message)
    
    def __str__(self):
        if self.field:
            return f"Validation error in field '{self.field}': {self.message}"
        return f"Validation error: {self.message}"

class DataProcessingError(Exception):
    """Custom exception for data processing errors"""
    def __init__(self, message, data=None, step=None):
        self.message = message
        self.data = data
        self.step = step
        super().__init__(self.message)
    
    def __str__(self):
        base_msg = f"Data processing error: {self.message}"
        if self.step:
            base_msg += f" (at step: {self.step})"
        return base_msg

class ConfigurationError(Exception):
    """Custom exception for configuration errors"""
    pass

def custom_exception_demo():
    """Demonstrate custom exceptions"""
    print("\n=== Custom Exception Demo ===")
    
    def validate_user_data(user_data):
        """Validate user data with custom exceptions"""
        if not isinstance(user_data, dict):
            raise ValidationError("User data must be a dictionary")
        
        # Validate required fields
        required_fields = ['name', 'age', 'email']
        for field in required_fields:
            if field not in user_data:
                raise ValidationError(f"Missing required field", field=field)
        
        # Validate name
        name = user_data['name']
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValidationError("Name must be a non-empty string", field='name', value=name)
        
        # Validate age
        age = user_data['age']
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValidationError("Age must be between 0 and 150", field='age', value=age)
        
        # Validate email
        email = user_data['email']
        if not isinstance(email, str) or '@' not in email:
            raise ValidationError("Invalid email format", field='email', value=email)
        
        return True
    
    # Test validation
    test_users = [
        {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'},  # Valid
        {'name': '', 'age': 25, 'email': 'alice@email.com'},       # Invalid name
        {'name': 'Bob', 'age': -5, 'email': 'bob@email.com'},      # Invalid age
        {'name': 'Charlie', 'age': 30, 'email': 'invalid'},        # Invalid email
        {'name': 'Diana', 'age': 28},                              # Missing email
        "not_a_dict"                                               # Wrong type
    ]
    
    for i, user in enumerate(test_users):
        try:
            validate_user_data(user)
            print(f"✓ User {i+1}: Valid")
        except ValidationError as e:
            print(f"✗ User {i+1}: {e}")
    
    def process_data_with_steps(data):
        """Process data with step tracking"""
        try:
            # Step 1: Validate input
            if not isinstance(data, list):
                raise DataProcessingError("Input must be a list", data=data, step="validation")
            
            # Step 2: Filter data
            filtered_data = []
            for item in data:
                if isinstance(item, (int, float)) and item > 0:
                    filtered_data.append(item)
            
            if not filtered_data:
                raise DataProcessingError("No valid data after filtering", step="filtering")
            
            # Step 3: Calculate statistics
            try:
                mean = sum(filtered_data) / len(filtered_data)
                maximum = max(filtered_data)
                minimum = min(filtered_data)
            except Exception as e:
                raise DataProcessingError(f"Statistics calculation failed: {e}", step="statistics")
            
            return {
                'mean': mean,
                'max': maximum,
                'min': minimum,
                'count': len(filtered_data)
            }
            
        except DataProcessingError:
            raise  # Re-raise custom exceptions
        except Exception as e:
            raise DataProcessingError(f"Unexpected error: {e}", data=data, step="unknown")
    
    # Test data processing
    test_datasets = [
        [1, 2, 3, 4, 5],           # Valid
        [-1, 0, 1, 2],             # Some invalid values
        [],                        # Empty
        "not_a_list",              # Wrong type
        [None, "invalid", {}]      # All invalid values
    ]
    
    for i, dataset in enumerate(test_datasets):
        try:
            result = process_data_with_steps(dataset)
            print(f"✓ Dataset {i+1}: {result}")
        except DataProcessingError as e:
            print(f"✗ Dataset {i+1}: {e}")

def exception_chaining_demo():
    """Demonstrate exception chaining"""
    print("\n=== Exception Chaining Demo ===")
    
    def load_config_file(filename):
        """Load configuration with exception chaining"""
        try:
            with open(filename, 'r') as f:
                config_data = json.load(f)
            return config_data
        except FileNotFoundError as e:
            raise ConfigurationError(f"Configuration file not found: {filename}") from e
        except json.JSONDecodeError as e:
            raise ConfigurationError(f"Invalid JSON in configuration file: {filename}") from e
        except Exception as e:
            raise ConfigurationError(f"Unexpected error loading configuration") from e
    
    def initialize_application(config_file):
        """Initialize application with chained exceptions"""
        try:
            config = load_config_file(config_file)
            
            # Validate required config keys
            required_keys = ['database_url', 'api_key', 'debug']
            for key in required_keys:
                if key not in config:
                    raise ConfigurationError(f"Missing required configuration key: {key}")
            
            return config
            
        except ConfigurationError as e:
            print(f"✗ Application initialization failed: {e}")
            if e.__cause__:
                print(f"  Caused by: {e.__cause__}")
            return None
    
    # Test with non-existent file
    config = initialize_application("nonexistent.json")
    
    # Test with invalid JSON
    invalid_json_file = "invalid.json"
    with open(invalid_json_file, 'w') as f:
        f.write('{"invalid": json,}')  # Invalid JSON
    
    try:
        config = initialize_application(invalid_json_file)
    finally:
        os.remove(invalid_json_file)
    
    # Test with valid but incomplete config
    incomplete_config_file = "incomplete.json"
    with open(incomplete_config_file, 'w') as f:
        json.dump({"database_url": "localhost"}, f)  # Missing keys
    
    try:
        config = initialize_application(incomplete_config_file)
    finally:
        os.remove(incomplete_config_file)

def context_manager_exceptions():
    """Demonstrate exception handling with context managers"""
    print("\n=== Context Manager Exceptions ===")
    
    class DatabaseConnection:
        """Mock database connection context manager"""
        
        def __init__(self, connection_string, should_fail=False):
            self.connection_string = connection_string
            self.should_fail = should_fail
            self.connected = False
        
        def __enter__(self):
            print(f"Connecting to database: {self.connection_string}")
            if self.should_fail:
                raise ConnectionError("Failed to connect to database")
            self.connected = True
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Closing database connection")
            self.connected = False
            
            # Handle specific exceptions
            if exc_type is ValueError:
                print("Handled ValueError in context manager")
                return True  # Suppress the exception
            
            # Let other exceptions propagate
            return False
        
        def execute_query(self, query):
            if not self.connected:
                raise RuntimeError("Not connected to database")
            
            if "DROP" in query.upper():
                raise ValueError("DROP operations not allowed")
            
            return f"Executed: {query}"
    
    # Test successful connection
    try:
        with DatabaseConnection("localhost:5432") as db:
            result = db.execute_query("SELECT * FROM users")
            print(f"✓ Query result: {result}")
    except Exception as e:
        print(f"✗ Database error: {e}")
    
    # Test connection failure
    try:
        with DatabaseConnection("invalid:0000", should_fail=True) as db:
            result = db.execute_query("SELECT * FROM users")
    except ConnectionError as e:
        print(f"✗ Connection failed: {e}")
    
    # Test exception suppression
    try:
        with DatabaseConnection("localhost:5432") as db:
            result = db.execute_query("DROP TABLE users")  # This will raise ValueError
            print(f"This won't be printed")
    except ValueError as e:
        print(f"✗ This won't be printed either (exception suppressed)")
    
    print("✓ Continued execution after suppressed exception")

def retry_pattern_demo():
    """Demonstrate retry pattern with exceptions"""
    print("\n=== Retry Pattern Demo ===")
    
    def retry_operation(func, max_attempts=3, delay=0.1):
        """Retry an operation with exponential backoff"""
        for attempt in range(max_attempts):
            try:
                return func()
            except Exception as e:
                if attempt == max_attempts - 1:
                    print(f"✗ Operation failed after {max_attempts} attempts")
                    raise e
                else:
                    wait_time = delay * (2 ** attempt)
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.1f}s...")
                    time.sleep(wait_time)
    
    def unreliable_operation():
        """Simulate an unreliable operation"""
        if random.random() < 0.7:  # 70% chance of failure
            raise ConnectionError("Network timeout")
        return "Operation successful!"
    
    # Test retry pattern
    random.seed(42)  # For reproducible results
    try:
        result = retry_operation(unreliable_operation, max_attempts=5, delay=0.01)
        print(f"✓ {result}")
    except Exception as e:
        print(f"✗ Final failure: {e}")

# Test all functions
if __name__ == "__main__":
    basic_exception_patterns()
    exception_hierarchy_demo()
    finally_and_else_demo()
    custom_exception_demo()
    exception_chaining_demo()
    context_manager_exceptions()
    retry_pattern_demo()
    
    print("\n=== Bài tập thực hành ===")
    print("1. Build robust file processor với comprehensive error handling")
    print("2. Create validation framework với custom exceptions")
    print("3. Implement retry mechanism cho network operations")
    print("4. Build error reporting system với exception chaining")