"""
Problem 110401: Memoization và optimization
Implement memoization, compare performance, optimize recursive solutions

Bài 1: Memoization Techniques
- Manual memoization
- functools.lru_cache
- Custom cache implementations

Bài 2: Performance Optimization
- Tail recursion simulation
- Dynamic programming conversion
- Space-time tradeoffs
"""

import time
import functools
from typing import Dict, Any, Callable

# Manual Memoization
def fibonacci_memo_manual(n, memo=None):
    """Fibonacci với manual memoization"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci_memo_manual(n-1, memo) + fibonacci_memo_manual(n-2, memo)
    
    memo[n] = result
    return result

def factorial_memo_manual(n, memo=None):
    """Factorial với manual memoization"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        result = 1
    else:
        result = n * factorial_memo_manual(n-1, memo)
    
    memo[n] = result
    return result

# Using functools.lru_cache
@functools.lru_cache(maxsize=None)
def fibonacci_lru_cache(n):
    """Fibonacci với lru_cache decorator"""
    if n <= 1:
        return n
    return fibonacci_lru_cache(n-1) + fibonacci_lru_cache(n-2)

@functools.lru_cache(maxsize=128)
def expensive_computation(x, y):
    """Simulate expensive computation với cache"""
    time.sleep(0.01)  # Simulate work
    return x ** y + y ** x

@functools.lru_cache(maxsize=None)
def catalan_cached(n):
    """Catalan numbers với cache"""
    if n <= 1:
        return 1
    
    result = 0
    for i in range(n):
        result += catalan_cached(i) * catalan_cached(n - 1 - i)
    return result

# Custom Cache Implementation
class MemoCache:
    """Custom memoization cache"""
    
    def __init__(self, maxsize=128):
        self.cache = {}
        self.maxsize = maxsize
        self.access_order = []
    
    def get(self, key):
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def set(self, key, value):
        if key in self.cache:
            # Update existing
            self.cache[key] = value
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            # Add new
            if len(self.cache) >= self.maxsize:
                # Remove least recently used
                oldest = self.access_order.pop(0)
                del self.cache[oldest]
            
            self.cache[key] = value
            self.access_order.append(key)
    
    def clear(self):
        self.cache.clear()
        self.access_order.clear()
    
    def info(self):
        return {
            'size': len(self.cache),
            'maxsize': self.maxsize,
            'keys': list(self.cache.keys())
        }

def memoize_with_custom_cache(cache):
    """Decorator sử dụng custom cache"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Create cache key
            key = str(args) + str(sorted(kwargs.items()))
            
            # Check cache
            result = cache.get(key)
            if result is not None:
                return result
            
            # Compute and cache
            result = func(*args, **kwargs)
            cache.set(key, result)
            return result
        
        wrapper.cache = cache
        return wrapper
    return decorator

# Example with custom cache
custom_cache = MemoCache(maxsize=50)

@memoize_with_custom_cache(custom_cache)
def fibonacci_custom_cache(n):
    """Fibonacci với custom cache"""
    if n <= 1:
        return n
    return fibonacci_custom_cache(n-1) + fibonacci_custom_cache(n-2)

# Advanced Memoization Patterns
class SmartMemo:
    """Smart memoization với different strategies"""
    
    def __init__(self, strategy='lru', maxsize=128):
        self.strategy = strategy
        self.maxsize = maxsize
        self.cache = {}
        self.access_count = {}
        self.access_order = []
    
    def memoize(self, func):
        def wrapper(*args, **kwargs):
            key = str(args) + str(sorted(kwargs.items()))
            
            if key in self.cache:
                self._update_access(key)
                return self.cache[key]
            
            result = func(*args, **kwargs)
            self._store(key, result)
            return result
        
        wrapper.cache_info = lambda: {
            'size': len(self.cache),
            'maxsize': self.maxsize,
            'strategy': self.strategy
        }
        wrapper.cache_clear = lambda: self._clear()
        
        return wrapper
    
    def _update_access(self, key):
        self.access_count[key] = self.access_count.get(key, 0) + 1
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)
    
    def _store(self, key, value):
        if len(self.cache) >= self.maxsize:
            self._evict()
        
        self.cache[key] = value
        self.access_count[key] = 1
        self.access_order.append(key)
    
    def _evict(self):
        if self.strategy == 'lru':
            # Least Recently Used
            key_to_remove = self.access_order.pop(0)
        elif self.strategy == 'lfu':
            # Least Frequently Used
            key_to_remove = min(self.access_count.keys(), 
                               key=lambda k: self.access_count[k])
            self.access_order.remove(key_to_remove)
        
        del self.cache[key_to_remove]
        del self.access_count[key_to_remove]
    
    def _clear(self):
        self.cache.clear()
        self.access_count.clear()
        self.access_order.clear()

# Tail Recursion Simulation
def factorial_tail_recursive(n, accumulator=1):
    """Factorial với tail recursion"""
    if n <= 1:
        return accumulator
    return factorial_tail_recursive(n - 1, n * accumulator)

def fibonacci_tail_recursive(n, a=0, b=1):
    """Fibonacci với tail recursion"""
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tail_recursive(n - 1, b, a + b)

def sum_tail_recursive(numbers, accumulator=0):
    """Sum list với tail recursion"""
    if not numbers:
        return accumulator
    return sum_tail_recursive(numbers[1:], accumulator + numbers[0])

# Trampoline Pattern (simulate tail call optimization)
class TailCall:
    """Represent a tail call"""
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

def trampoline(func):
    """Execute function với trampoline pattern"""
    result = func
    while isinstance(result, TailCall):
        result = result.func(*result.args, **result.kwargs)
    return result

def factorial_trampoline(n, acc=1):
    """Factorial với trampoline pattern"""
    if n <= 1:
        return acc
    return TailCall(factorial_trampoline, n - 1, n * acc)

# Dynamic Programming Conversion
def fibonacci_dp_bottom_up(n):
    """Fibonacci với bottom-up DP"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def fibonacci_dp_space_optimized(n):
    """Fibonacci với space-optimized DP"""
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

def longest_common_subsequence_memo(text1, text2):
    """LCS với memoization"""
    memo = {}
    
    def lcs_helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(text1) or j == len(text2):
            result = 0
        elif text1[i] == text2[j]:
            result = 1 + lcs_helper(i + 1, j + 1)
        else:
            result = max(lcs_helper(i + 1, j), lcs_helper(i, j + 1))
        
        memo[(i, j)] = result
        return result
    
    return lcs_helper(0, 0)

# Performance Testing
def performance_comparison():
    """Compare performance của different approaches"""
    
    def time_function(func, *args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start
    
    n = 35
    
    print(f"Computing Fibonacci({n}):")
    
    # Naive recursive (too slow for large n)
    if n <= 30:
        def fibonacci_naive(n):
            if n <= 1:
                return n
            return fibonacci_naive(n-1) + fibonacci_naive(n-2)
        
        result, time_taken = time_function(fibonacci_naive, n)
        print(f"  Naive recursive: {result} ({time_taken:.4f}s)")
    
    # Memoized versions
    result, time_taken = time_function(fibonacci_memo_manual, n)
    print(f"  Manual memo: {result} ({time_taken:.6f}s)")
    
    result, time_taken = time_function(fibonacci_lru_cache, n)
    print(f"  LRU cache: {result} ({time_taken:.6f}s)")
    
    result, time_taken = time_function(fibonacci_custom_cache, n)
    print(f"  Custom cache: {result} ({time_taken:.6f}s)")
    
    # DP versions
    result, time_taken = time_function(fibonacci_dp_bottom_up, n)
    print(f"  Bottom-up DP: {result} ({time_taken:.6f}s)")
    
    result, time_taken = time_function(fibonacci_dp_space_optimized, n)
    print(f"  Space-optimized DP: {result} ({time_taken:.6f}s)")
    
    # Tail recursive
    result, time_taken = time_function(fibonacci_tail_recursive, n)
    print(f"  Tail recursive: {result} ({time_taken:.6f}s)")

def cache_analysis():
    """Analyze cache behavior"""
    
    # Test LRU cache
    fibonacci_lru_cache.cache_clear()
    
    # Compute some values
    for i in range(10):
        fibonacci_lru_cache(i)
    
    print("LRU Cache info:", fibonacci_lru_cache.cache_info())
    
    # Test custom cache
    custom_cache.clear()
    for i in range(10):
        fibonacci_custom_cache(i)
    
    print("Custom cache info:", custom_cache.info())
    
    # Test smart memo with different strategies
    lru_memo = SmartMemo('lru', maxsize=5)
    lfu_memo = SmartMemo('lfu', maxsize=5)
    
    @lru_memo.memoize
    def test_func_lru(x):
        return x ** 2
    
    @lfu_memo.memoize
    def test_func_lfu(x):
        return x ** 2
    
    # Test access patterns
    for i in [1, 2, 3, 4, 5, 6, 1, 2, 7]:
        test_func_lru(i)
        test_func_lfu(i)
    
    print("LRU strategy:", test_func_lru.cache_info())
    print("LFU strategy:", test_func_lfu.cache_info())

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Memoization Techniques ===")
    
    # Test manual memoization
    print("Manual memoization:")
    result = fibonacci_memo_manual(30)
    print(f"Fibonacci(30) = {result}")
    
    # Test LRU cache
    print(f"\nLRU cache:")
    result = fibonacci_lru_cache(30)
    print(f"Fibonacci(30) = {result}")
    print("Cache info:", fibonacci_lru_cache.cache_info())
    
    # Test expensive computation caching
    print(f"\nExpensive computation:")
    start = time.time()
    result1 = expensive_computation(2, 10)
    time1 = time.time() - start
    
    start = time.time()
    result2 = expensive_computation(2, 10)  # Should be cached
    time2 = time.time() - start
    
    print(f"First call: {result1} ({time1:.4f}s)")
    print(f"Second call: {result2} ({time2:.6f}s)")
    
    # Test custom cache
    print(f"\nCustom cache:")
    result = fibonacci_custom_cache(25)
    print(f"Fibonacci(25) = {result}")
    print("Cache info:", custom_cache.info())
    
    print("\n=== Bài 2: Performance Optimization ===")
    
    # Performance comparison
    performance_comparison()
    
    # Cache analysis
    print(f"\n=== Cache Analysis ===")
    cache_analysis()
    
    # Test trampoline
    print(f"\n=== Trampoline Pattern ===")
    result = trampoline(factorial_trampoline(10))
    print(f"Factorial(10) with trampoline: {result}")
    
    # Test LCS memoization
    print(f"\n=== LCS Memoization ===")
    text1 = "ABCDGH"
    text2 = "AEDFHR"
    result = longest_common_subsequence_memo(text1, text2)
    print(f"LCS of '{text1}' and '{text2}': {result}")

    print("\n=== Bài tập thực hành ===")
    print("1. Implement memoized edit distance")
    print("2. Create adaptive cache với different eviction policies")
    print("3. Build memoized graph algorithms")
    print("4. Optimize recursive parsing với memoization")