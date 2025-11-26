"""
Problem 220101: Basic Recursion Patterns
Các pattern đệ quy cơ bản

Topics: Base cases, recursive cases, linear recursion
"""

def factorial_recursive(n):
    """
    Tính giai thừa bằng đệ quy
    Time: O(n), Space: O(n)
    """
    # TODO: Implement recursive factorial
    pass

def sum_recursive(n):
    """
    Tính tổng từ 1 đến n bằng đệ quy
    Time: O(n), Space: O(n)
    """
    # TODO: Implement recursive sum
    pass

def power_recursive(base, exp):
    """
    Tính lũy thừa bằng đệ quy
    Time: O(exp), Space: O(exp)
    """
    # TODO: Implement recursive power
    pass

def countdown_recursive(n):
    """
    Đếm ngược từ n về 0
    """
    # TODO: Print countdown using recursion
    pass

def print_digits_recursive(n):
    """
    In từng chữ số của n (từ trái sang phải)
    """
    # TODO: Print each digit using recursion
    pass

def gcd_recursive(a, b):
    """
    Tìm ước chung lớn nhất bằng thuật toán Euclid
    Time: O(log(min(a,b))), Space: O(log(min(a,b)))
    """
    # TODO: Implement Euclidean algorithm recursively
    pass

def fibonacci_basic(n):
    """
    Fibonacci cơ bản (chưa tối ưu)
    Time: O(2^n), Space: O(n)
    """
    # TODO: Implement basic fibonacci
    pass

def count_digits_recursive(n):
    """
    Đếm số chữ số của n
    Time: O(log n), Space: O(log n)
    """
    # TODO: Count digits recursively
    pass

# Test cases
def test_basic_recursion():
    print("Basic Recursion Patterns")
    print("=" * 30)
    
    # Test factorial
    print("1. Factorial:")
    for i in range(6):
        result = factorial_recursive(i)
        print(f"factorial({i}) = {result}")
    
    # Test sum
    print("\n2. Sum 1 to n:")
    for i in range(1, 6):
        result = sum_recursive(i)
        print(f"sum(1 to {i}) = {result}")
    
    # Test power
    print("\n3. Power:")
    test_cases = [(2, 3), (3, 4), (5, 0), (2, 10)]
    for base, exp in test_cases:
        result = power_recursive(base, exp)
        print(f"{base}^{exp} = {result}")
    
    # Test countdown
    print("\n4. Countdown:")
    countdown_recursive(5)
    
    # Test print digits
    print("\n5. Print Digits:")
    numbers = [123, 4567, 89]
    for num in numbers:
        print(f"Digits of {num}:", end=" ")
        print_digits_recursive(num)
        print()
    
    # Test GCD
    print("\n6. GCD:")
    gcd_cases = [(48, 18), (100, 25), (17, 13)]
    for a, b in gcd_cases:
        result = gcd_recursive(a, b)
        print(f"gcd({a}, {b}) = {result}")
    
    # Test fibonacci
    print("\n7. Fibonacci:")
    for i in range(8):
        result = fibonacci_basic(i)
        print(f"fib({i}) = {result}")
    
    # Test count digits
    print("\n8. Count Digits:")
    digit_numbers = [123, 4567, 89, 1, 0]
    for num in digit_numbers:
        result = count_digits_recursive(num)
        print(f"digits in {num}: {result}")

if __name__ == "__main__":
    test_basic_recursion()