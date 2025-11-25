"""
Problem 100301: Scope và variable access
Thực hành local/global scope, LEGB rule và nonlocal

Bài 1: Local vs Global Scope
- Hiểu về local và global variables
- Thực hành global keyword

Bài 2: LEGB Rule và Nonlocal
- Local, Enclosing, Global, Built-in
- Nonlocal keyword trong nested functions
"""

# Global variables
global_counter = 0
global_message = "Hello from global scope"
global_config = {"debug": True, "version": "1.0"}

def demonstrate_local_scope():
    """Minh họa local scope"""
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    
    # Có thể đọc global variable
    print(f"Reading global: {global_message}")
    
    # Không thể modify global variable trực tiếp
    # global_message = "Modified"  # Tạo local variable mới!

def demonstrate_global_keyword():
    """Minh họa global keyword"""
    global global_counter
    global_counter += 1
    print(f"Global counter: {global_counter}")
    
    global global_message
    global_message = "Modified by function"

def read_only_global():
    """Function chỉ đọc global variables"""
    print(f"Config: {global_config}")
    print(f"Debug mode: {global_config['debug']}")

def modify_global_dict():
    """Modify global dictionary (không cần global keyword)"""
    global_config["last_modified"] = "2024-01-15"
    global_config["debug"] = False

# LEGB Rule Examples
x = "global x"

def outer_function():
    """Outer function cho nested scope"""
    x = "enclosing x"
    
    def inner_function():
        x = "local x"
        print(f"Inner function: {x}")  # local x
        
        # Truy cập built-in
        print(f"Length of x: {len(x)}")  # len là built-in
    
    inner_function()
    print(f"Outer function: {x}")  # enclosing x

def demonstrate_legb():
    """Minh họa LEGB rule"""
    print(f"Global: {x}")  # global x
    outer_function()

# Nonlocal Examples
def counter_factory():
    """Factory function tạo counter với nonlocal"""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    return increment, decrement, get_count

def create_accumulator(initial=0):
    """Tạo accumulator function"""
    total = initial
    
    def accumulate(value):
        nonlocal total
        total += value
        return total
    
    def reset():
        nonlocal total
        total = initial
        return total
    
    def get_total():
        return total
    
    return accumulate, reset, get_total

# Scope Challenges
def scope_challenge_1():
    """Challenge về scope"""
    x = 10
    
    def inner():
        print(f"Inner x: {x}")  # Đọc từ enclosing scope
    
    inner()
    print(f"Outer x: {x}")

def scope_challenge_2():
    """Challenge với global và local cùng tên"""
    global_var = "local version"  # Local variable che global
    
    def nested():
        print(f"Nested sees: {global_var}")  # local version
    
    nested()
    print(f"Function sees: {global_var}")  # local version

global_var = "global version"  # Global variable

def scope_challenge_3():
    """Challenge với nonlocal"""
    x = "outer"
    
    def middle():
        x = "middle"
        
        def inner():
            nonlocal x
            x = "inner modified"
            print(f"Inner: {x}")
        
        inner()
        print(f"Middle after inner: {x}")
    
    middle()
    print(f"Outer after middle: {x}")

# Practical Examples
class SimpleBank:
    """Ví dụ thực tế với scope"""
    total_accounts = 0  # Class variable (global-like)
    
    def __init__(self, initial_balance=0):
        SimpleBank.total_accounts += 1
        self.balance = initial_balance  # Instance variable
        self.account_id = SimpleBank.total_accounts
    
    def create_transaction_logger(self):
        """Tạo logger với closure"""
        transactions = []
        
        def log_transaction(amount, transaction_type):
            nonlocal transactions
            transaction = {
                "amount": amount,
                "type": transaction_type,
                "balance_after": self.balance
            }
            transactions.append(transaction)
            return len(transactions)
        
        def get_transactions():
            return transactions.copy()
        
        return log_transaction, get_transactions

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Local vs Global Scope ===")
    
    print(f"Initial global counter: {global_counter}")
    print(f"Initial global message: {global_message}")
    
    # Test local scope
    demonstrate_local_scope()
    
    # Test global keyword
    demonstrate_global_keyword()
    print(f"After modification - counter: {global_counter}")
    print(f"After modification - message: {global_message}")
    
    # Test global dict modification
    print(f"Config before: {global_config}")
    modify_global_dict()
    print(f"Config after: {global_config}")
    
    print("\n=== Bài 2: LEGB Rule và Nonlocal ===")
    
    # Test LEGB rule
    demonstrate_legb()
    
    # Test counter factory
    print(f"\nCounter Factory:")
    inc, dec, get = counter_factory()
    print(f"Initial: {get()}")
    print(f"After increment: {inc()}")
    print(f"After increment: {inc()}")
    print(f"After decrement: {dec()}")
    
    # Test accumulator
    print(f"\nAccumulator:")
    add, reset, total = create_accumulator(100)
    print(f"Initial: {total()}")
    print(f"Add 50: {add(50)}")
    print(f"Add 25: {add(25)}")
    print(f"Reset: {reset()}")
    print(f"Add 10: {add(10)}")
    
    print("\n=== Scope Challenges ===")
    
    print("Challenge 1:")
    scope_challenge_1()
    
    print(f"\nGlobal var before challenge 2: {global_var}")
    print("Challenge 2:")
    scope_challenge_2()
    print(f"Global var after challenge 2: {global_var}")
    
    print("\nChallenge 3:")
    scope_challenge_3()
    
    print("\n=== Practical Example ===")
    
    # Test bank example
    account1 = SimpleBank(1000)
    account2 = SimpleBank(500)
    
    print(f"Total accounts: {SimpleBank.total_accounts}")
    print(f"Account 1 balance: {account1.balance}")
    print(f"Account 2 balance: {account2.balance}")
    
    # Test transaction logger
    log_tx, get_tx = account1.create_transaction_logger()
    
    account1.balance += 200  # Deposit
    log_tx(200, "deposit")
    
    account1.balance -= 50   # Withdrawal
    log_tx(-50, "withdrawal")
    
    print(f"Transactions: {get_tx()}")

    print("\n=== Bài tập thực hành ===")
    print("1. Tạo function factory cho calculator operations")
    print("2. Implement simple state machine với closures")
    print("3. Tạo caching decorator sử dụng nonlocal")
    print("4. Debug scope issues trong nested functions")