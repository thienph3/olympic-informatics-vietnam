"""
Problem 110201: Higher-order functions và closures
Tạo higher-order functions, closures và decorators đơn giản

Bài 1: Higher-order Functions
- Functions nhận functions làm parameters
- Functions trả về functions
- Function factories

Bài 2: Closures và Decorators
- Closures với enclosing scope
- Simple decorators
- Decorator patterns
"""

# Higher-order Functions
def create_operation_applier(operation):
    """Higher-order function nhận operation làm parameter"""
    def apply_to_list(numbers):
        return [operation(x) for x in numbers]
    return apply_to_list

def create_filter_function(condition):
    """Tạo filter function từ condition"""
    def filter_list(items):
        return [item for item in items if condition(item)]
    return filter_list

def create_validator(rules):
    """Tạo validator function từ rules"""
    def validate(data):
        errors = []
        for field, rule in rules.items():
            if field in data:
                if not rule(data[field]):
                    errors.append(f"Invalid {field}")
            else:
                errors.append(f"Missing {field}")
        return len(errors) == 0, errors
    return validate

def compose_functions(*functions):
    """Compose multiple functions"""
    def composed(x):
        result = x
        for func in functions:
            result = func(result)
        return result
    return composed

def create_accumulator(operation, initial=0):
    """Tạo accumulator function"""
    def accumulate(values):
        result = initial
        for value in values:
            result = operation(result, value)
        return result
    return accumulate

# Function Factories
def make_multiplier(factor):
    """Factory tạo multiplier functions"""
    def multiplier(x):
        return x * factor
    return multiplier

def make_range_checker(min_val, max_val):
    """Factory tạo range checker functions"""
    def in_range(x):
        return min_val <= x <= max_val
    return in_range

def make_string_processor(**options):
    """Factory tạo string processor với options"""
    def process(text):
        result = text
        if options.get('strip', False):
            result = result.strip()
        if options.get('lower', False):
            result = result.lower()
        if options.get('replace_spaces', False):
            result = result.replace(' ', '_')
        if 'prefix' in options:
            result = options['prefix'] + result
        if 'suffix' in options:
            result = result + options['suffix']
        return result
    return process

# Closures
def make_counter(start=0, step=1):
    """Closure tạo counter với state"""
    count = start
    
    def counter():
        nonlocal count
        current = count
        count += step
        return current
    
    def reset():
        nonlocal count
        count = start
    
    def get_count():
        return count
    
    # Return multiple functions
    counter.reset = reset
    counter.get_count = get_count
    return counter

def make_bank_account(initial_balance=0):
    """Closure tạo bank account với private state"""
    balance = initial_balance
    transaction_history = []
    
    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposit: +${amount}")
            return balance
        return None
    
    def withdraw(amount):
        nonlocal balance
        if 0 < amount <= balance:
            balance -= amount
            transaction_history.append(f"Withdraw: -${amount}")
            return balance
        return None
    
    def get_balance():
        return balance
    
    def get_history():
        return transaction_history.copy()
    
    # Return account interface
    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': get_balance,
        'history': get_history
    }

def make_cache(max_size=100):
    """Closure tạo cache với size limit"""
    cache = {}
    access_order = []
    
    def get(key):
        if key in cache:
            # Move to end (most recently used)
            access_order.remove(key)
            access_order.append(key)
            return cache[key]
        return None
    
    def set(key, value):
        nonlocal cache, access_order
        
        if key in cache:
            # Update existing
            cache[key] = value
            access_order.remove(key)
            access_order.append(key)
        else:
            # Add new
            if len(cache) >= max_size:
                # Remove least recently used
                oldest = access_order.pop(0)
                del cache[oldest]
            
            cache[key] = value
            access_order.append(key)
    
    def clear():
        nonlocal cache, access_order
        cache.clear()
        access_order.clear()
    
    def size():
        return len(cache)
    
    return {
        'get': get,
        'set': set,
        'clear': clear,
        'size': size
    }

# Simple Decorators
def timer_decorator(func):
    """Decorator đo thời gian execution"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

def retry_decorator(max_attempts=3):
    """Decorator retry function khi fail"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}")
            return None
        return wrapper
    return decorator

def validate_decorator(**validators):
    """Decorator validate function arguments"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validate positional args
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            for param_name, value in bound_args.arguments.items():
                if param_name in validators:
                    validator = validators[param_name]
                    if not validator(value):
                        raise ValueError(f"Invalid {param_name}: {value}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def memoize_decorator(func):
    """Decorator cache function results"""
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Create cache key
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Higher-order Functions ===")
    
    # Test operation applier
    square_applier = create_operation_applier(lambda x: x**2)
    numbers = [1, 2, 3, 4, 5]
    squared = square_applier(numbers)
    print(f"Squared: {squared}")
    
    # Test filter function
    even_filter = create_filter_function(lambda x: x % 2 == 0)
    evens = even_filter(numbers)
    print(f"Evens: {evens}")
    
    # Test validator
    user_validator = create_validator({
        'name': lambda x: len(x) > 0,
        'age': lambda x: 0 <= x <= 120,
        'email': lambda x: '@' in x
    })
    
    valid_user = {'name': 'Alice', 'age': 25, 'email': 'alice@email.com'}
    invalid_user = {'name': '', 'age': -5, 'email': 'invalid'}
    
    print(f"Valid user: {user_validator(valid_user)}")
    print(f"Invalid user: {user_validator(invalid_user)}")
    
    # Test function composition
    add_one = lambda x: x + 1
    multiply_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    composed = compose_functions(add_one, multiply_two, square)
    result = composed(3)  # ((3 + 1) * 2) ** 2 = 64
    print(f"Composed result: {result}")
    
    # Test function factories
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"Double 5: {double(5)}, Triple 5: {triple(5)}")
    
    in_range_0_10 = make_range_checker(0, 10)
    print(f"5 in range 0-10: {in_range_0_10(5)}")
    print(f"15 in range 0-10: {in_range_0_10(15)}")
    
    print("\n=== Bài 2: Closures và Decorators ===")
    
    # Test counter closure
    counter1 = make_counter(0, 1)
    counter2 = make_counter(10, 2)
    
    print(f"Counter1: {counter1()}, {counter1()}, {counter1()}")
    print(f"Counter2: {counter2()}, {counter2()}, {counter2()}")
    print(f"Counter1 current: {counter1.get_count()}")
    
    # Test bank account closure
    account = make_bank_account(1000)
    print(f"Initial balance: ${account['balance']()}")
    
    account['deposit'](500)
    account['withdraw'](200)
    account['withdraw'](2000)  # Should fail
    
    print(f"Final balance: ${account['balance']()}")
    print(f"Transaction history: {account['history']()}")
    
    # Test cache closure
    cache = make_cache(3)
    cache['set']('a', 1)
    cache['set']('b', 2)
    cache['set']('c', 3)
    cache['set']('d', 4)  # Should evict 'a'
    
    print(f"Cache size: {cache['size']()}")
    print(f"Get 'a': {cache['get']('a')}")  # Should be None
    print(f"Get 'b': {cache['get']('b')}")  # Should be 2
    
    # Test decorators
    @timer_decorator
    def slow_function():
        import time
        time.sleep(0.1)
        return "Done"
    
    result = slow_function()
    print(f"Slow function result: {result}")
    
    @memoize_decorator
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"Fibonacci(10) again: {fibonacci(10)}")  # Should be cached

    print("\n=== Bài tập thực hành ===")
    print("1. Tạo event system với closures")
    print("2. Build middleware pattern với higher-order functions")
    print("3. Implement rate limiter decorator")
    print("4. Create function pipeline với error handling")