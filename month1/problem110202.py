"""
Problem 110202: Functional programming patterns
Áp dụng functional programming: partial functions, composition, currying

Bài 1: Partial Functions và Currying
- Partial application
- Currying techniques
- Function specialization

Bài 2: Function Composition và Pipelines
- Compose functions
- Data processing pipelines
- Monadic patterns
"""

from functools import partial, reduce

# Partial Functions
def create_partial_examples():
    """Examples of partial function application"""
    
    # Basic partial application
    def multiply(x, y, z):
        return x * y * z
    
    # Create specialized functions
    double = partial(multiply, 2, 1)  # Fix x=2, y=1
    triple = partial(multiply, 3, 1)  # Fix x=3, y=1
    
    print(f"Double 5: {double(5)}")  # 2 * 1 * 5 = 10
    print(f"Triple 4: {triple(4)}")  # 3 * 1 * 4 = 12
    
    # Partial with keyword arguments
    def greet(greeting, name, punctuation="!"):
        return f"{greeting}, {name}{punctuation}"
    
    say_hello = partial(greet, "Hello")
    say_hi = partial(greet, "Hi", punctuation=".")
    
    print(f"Say hello: {say_hello('Alice')}")
    print(f"Say hi: {say_hi('Bob')}")
    
    # Partial for data processing
    def filter_and_transform(data, predicate, transformer):
        return [transformer(x) for x in data if predicate(x)]
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Create specialized processors
    process_evens = partial(filter_and_transform, 
                           predicate=lambda x: x % 2 == 0,
                           transformer=lambda x: x ** 2)
    
    process_odds = partial(filter_and_transform,
                          predicate=lambda x: x % 2 == 1,
                          transformer=lambda x: x * 3)
    
    even_squares = process_evens(numbers)
    odd_triples = process_odds(numbers)
    
    print(f"Even squares: {even_squares}")
    print(f"Odd triples: {odd_triples}")

def currying_examples():
    """Examples of currying techniques"""
    
    # Manual currying
    def curry_add(x):
        def add_x(y):
            def add_xy(z):
                return x + y + z
            return add_xy
        return add_x
    
    # Usage: curry_add(1)(2)(3) = 6
    result = curry_add(1)(2)(3)
    print(f"Curried add: {result}")
    
    # Partial currying
    add_1 = curry_add(1)
    add_1_2 = add_1(2)
    
    print(f"Partial curry: {add_1_2(5)}")  # 1 + 2 + 5 = 8
    
    # Generic currying function
    def curry(func, arity=None):
        if arity is None:
            arity = func.__code__.co_argcount
        
        def curried(*args):
            if len(args) >= arity:
                return func(*args[:arity])
            else:
                return lambda *more_args: curried(*(args + more_args))
        
        return curried
    
    # Test generic currying
    def multiply_three(x, y, z):
        return x * y * z
    
    curried_multiply = curry(multiply_three)
    
    # Different ways to call
    result1 = curried_multiply(2)(3)(4)  # 24
    result2 = curried_multiply(2, 3)(4)  # 24
    result3 = curried_multiply(2)(3, 4)  # 24
    
    print(f"Curried multiply: {result1}, {result2}, {result3}")
    
    # Practical currying example
    def create_validator(field_name, validation_func, error_message):
        def validate(value):
            if validation_func(value):
                return True, None
            else:
                return False, f"{field_name}: {error_message}"
        return validate
    
    # Create curried validator factory
    curried_validator = curry(create_validator)
    
    # Create specific validators
    name_validator = curried_validator("name")(lambda x: len(x) > 0)("Name cannot be empty")
    age_validator = curried_validator("age")(lambda x: 0 <= x <= 120)("Age must be 0-120")
    email_validator = curried_validator("email")(lambda x: "@" in x)("Invalid email format")
    
    # Test validators
    print(f"Name validation: {name_validator('Alice')}")
    print(f"Age validation: {age_validator(25)}")
    print(f"Email validation: {email_validator('invalid-email')}")

def function_composition():
    """Function composition patterns"""
    
    # Simple composition
    def compose2(f, g):
        return lambda x: f(g(x))
    
    # Multiple function composition
    def compose(*functions):
        return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)
    
    # Test functions
    add_one = lambda x: x + 1
    multiply_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    # Compose functions
    transform1 = compose2(square, add_one)  # square(add_one(x))
    transform2 = compose(square, multiply_two, add_one)  # square(multiply_two(add_one(x)))
    
    print(f"Transform1(3): {transform1(3)}")  # (3+1)^2 = 16
    print(f"Transform2(3): {transform2(3)}")  # ((3+1)*2)^2 = 64
    
    # Pipe operator simulation
    def pipe(value, *functions):
        return reduce(lambda acc, func: func(acc), functions, value)
    
    # Usage: pipe(value, func1, func2, func3)
    result = pipe(3, add_one, multiply_two, square)
    print(f"Pipe result: {result}")  # ((3+1)*2)^2 = 64
    
    # Composable data transformations
    def map_compose(func):
        return lambda data: list(map(func, data))
    
    def filter_compose(predicate):
        return lambda data: list(filter(predicate, data))
    
    def reduce_compose(func, initial=None):
        return lambda data: reduce(func, data, initial) if initial is not None else reduce(func, data)
    
    # Create data processing pipeline
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Pipeline: filter evens -> square -> sum
    process_data = compose(
        reduce_compose(lambda x, y: x + y),
        map_compose(lambda x: x ** 2),
        filter_compose(lambda x: x % 2 == 0)
    )
    
    result = process_data(numbers)
    print(f"Pipeline result: {result}")  # 2^2 + 4^2 + 6^2 + 8^2 + 10^2 = 220

def monadic_patterns():
    """Simple monadic patterns for error handling"""
    
    class Maybe:
        def __init__(self, value):
            self.value = value
        
        def bind(self, func):
            if self.value is None:
                return Maybe(None)
            try:
                return Maybe(func(self.value))
            except:
                return Maybe(None)
        
        def map(self, func):
            return self.bind(func)
        
        def get(self, default=None):
            return self.value if self.value is not None else default
        
        def __str__(self):
            return f"Maybe({self.value})"
    
    # Chain operations safely
    def safe_divide(x, y):
        return x / y if y != 0 else None
    
    def safe_sqrt(x):
        import math
        return math.sqrt(x) if x >= 0 else None
    
    # Test monadic chaining
    result1 = Maybe(16).bind(lambda x: safe_sqrt(x)).bind(lambda x: safe_divide(x, 2))
    result2 = Maybe(-4).bind(lambda x: safe_sqrt(x)).bind(lambda x: safe_divide(x, 2))
    result3 = Maybe(16).bind(lambda x: safe_sqrt(x)).bind(lambda x: safe_divide(x, 0))
    
    print(f"Safe computation 1: {result1.get()}")  # 2.0
    print(f"Safe computation 2: {result2.get()}")  # None (negative sqrt)
    print(f"Safe computation 3: {result3.get()}")  # None (divide by zero)

def advanced_pipelines():
    """Advanced data processing pipelines"""
    
    # Pipeline builder
    class Pipeline:
        def __init__(self, data=None):
            self.data = data
            self.operations = []
        
        def map(self, func):
            new_pipeline = Pipeline()
            new_pipeline.operations = self.operations + [('map', func)]
            return new_pipeline
        
        def filter(self, predicate):
            new_pipeline = Pipeline()
            new_pipeline.operations = self.operations + [('filter', predicate)]
            return new_pipeline
        
        def reduce(self, func, initial=None):
            new_pipeline = Pipeline()
            new_pipeline.operations = self.operations + [('reduce', func, initial)]
            return new_pipeline
        
        def execute(self, data):
            result = data
            for operation in self.operations:
                if operation[0] == 'map':
                    result = list(map(operation[1], result))
                elif operation[0] == 'filter':
                    result = list(filter(operation[1], result))
                elif operation[0] == 'reduce':
                    if len(operation) > 2 and operation[2] is not None:
                        result = reduce(operation[1], result, operation[2])
                    else:
                        result = reduce(operation[1], result)
            return result
    
    # Create and use pipeline
    numbers = list(range(1, 11))
    
    pipeline = (Pipeline()
                .filter(lambda x: x % 2 == 0)  # Keep evens
                .map(lambda x: x ** 2)         # Square them
                .reduce(lambda x, y: x + y))   # Sum them
    
    result = pipeline.execute(numbers)
    print(f"Pipeline result: {result}")  # 2^2 + 4^2 + 6^2 + 8^2 + 10^2 = 220
    
    # Reusable pipeline
    even_squares_sum = pipeline
    
    # Test with different data
    test_data = [1, 2, 3, 4, 5, 6, 7, 8]
    result2 = even_squares_sum.execute(test_data)
    print(f"Pipeline with different data: {result2}")

def functional_utilities():
    """Utility functions for functional programming"""
    
    # Flip function arguments
    def flip(func):
        return lambda x, y: func(y, x)
    
    # Test flip
    divide = lambda x, y: x / y
    flipped_divide = flip(divide)
    
    print(f"Normal divide: {divide(10, 2)}")    # 5.0
    print(f"Flipped divide: {flipped_divide(10, 2)}")  # 0.2
    
    # Constant function
    def constant(value):
        return lambda *args, **kwargs: value
    
    always_42 = constant(42)
    print(f"Always 42: {always_42(1, 2, 3)}")  # 42
    
    # Identity function
    def identity(x):
        return x
    
    # Apply function n times
    def apply_n_times(func, n):
        def applied(x):
            result = x
            for _ in range(n):
                result = func(result)
            return result
        return applied
    
    # Test apply_n_times
    increment = lambda x: x + 1
    add_5 = apply_n_times(increment, 5)
    
    print(f"Add 5: {add_5(10)}")  # 15
    
    # Until function
    def until(predicate, func):
        def until_func(x):
            result = x
            while not predicate(result):
                result = func(result)
            return result
        return until_func
    
    # Find next power of 2
    next_power_of_2 = until(
        lambda x: x & (x - 1) == 0,  # Check if power of 2
        lambda x: x + 1
    )
    
    print(f"Next power of 2 after 10: {next_power_of_2(10)}")  # 16

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Partial Functions và Currying ===")
    
    print("Partial functions:")
    create_partial_examples()
    
    print("\nCurrying examples:")
    currying_examples()
    
    print("\n=== Bài 2: Function Composition và Pipelines ===")
    
    print("Function composition:")
    function_composition()
    
    print("\nMonadic patterns:")
    monadic_patterns()
    
    print("\nAdvanced pipelines:")
    advanced_pipelines()
    
    print("\nFunctional utilities:")
    functional_utilities()

    print("\n=== Bài tập thực hành ===")
    print("1. Build reactive programming system với function composition")
    print("2. Create domain-specific language với curried functions")
    print("3. Implement async pipeline với error handling")
    print("4. Build functional validation library")