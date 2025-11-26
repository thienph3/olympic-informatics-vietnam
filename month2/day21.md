# Day 21: Phân tích hiệu suất, Space Complexity

## Mục tiêu học tập

Sau buổi học này, học sinh sẽ:
- Đo lường hiệu suất thực tế của thuật toán
- Phân tích chi tiết space complexity
- Hiểu memory management trong Python
- Tối ưu hóa memory usage cho Olympic
- Profiling và debugging performance issues

## Phần 1: Performance Measurement (45 phút)

### 1.1 Đo lường thời gian thực thi

```python
import time
import timeit
from functools import wraps

def measure_time(func):
    """Decorator để đo thời gian thực thi"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {end - start:.6f} seconds")
        return result
    return wrapper

def benchmark_function(func, *args, number=1000):
    """Benchmark function với timeit"""
    time_taken = timeit.timeit(lambda: func(*args), number=number)
    return time_taken / number

def compare_algorithms(algorithms, test_data, iterations=100):
    """So sánh hiệu suất nhiều thuật toán"""
    results = {}
    for name, algorithm in algorithms.items():
        time_taken = benchmark_function(algorithm, test_data, iterations)
        results[name] = time_taken
    return results
```

### 1.2 Profiling với cProfile

```python
import cProfile
import pstats
from io import StringIO

def profile_function(func, *args):
    """Profile function và hiển thị kết quả"""
    pr = cProfile.Profile()
    pr.enable()
    
    result = func(*args)
    
    pr.disable()
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    
    print(s.getvalue())
    return result

def line_profiler_example():
    """Ví dụ về line-by-line profiling"""
    # Cần cài kernprof: pip install line_profiler
    # Sử dụng @profile decorator và chạy: kernprof -l -v script.py
    pass
```

### 1.3 Memory Profiling

```python
import sys
import tracemalloc
from memory_profiler import profile  # pip install memory-profiler

def get_size(obj):
    """Tính kích thước object"""
    size = sys.getsizeof(obj)
    if isinstance(obj, dict):
        size += sum([get_size(v) for v in obj.values()])
        size += sum([get_size(k) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i) for i in obj])
    return size

def memory_usage_tracker():
    """Track memory usage during execution"""
    tracemalloc.start()
    
    # Your code here
    data = [i**2 for i in range(100000)]
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.1f} MB")
    
    tracemalloc.stop()
```

## Phần 2: Space Complexity Analysis (45 phút)

### 2.1 Auxiliary Space vs Total Space

```python
def analyze_space_types():
    """Phân biệt auxiliary space và total space"""
    
    # Auxiliary Space: O(1) - chỉ dùng biến phụ
    def sum_array_constant_aux(arr):
        total = 0  # O(1) auxiliary space
        for num in arr:  # arr không tính vào auxiliary space
            total += num
        return total
    
    # Auxiliary Space: O(n) - tạo thêm structure
    def reverse_array_linear_aux(arr):
        return arr[::-1]  # O(n) auxiliary space
    
    # Total Space: bao gồm cả input space
    def recursive_factorial(n):
        # Total space: O(n) do call stack
        # Auxiliary space: O(n) do recursion
        if n <= 1:
            return 1
        return n * recursive_factorial(n - 1)
    
    def iterative_factorial(n):
        # Total space: O(1)
        # Auxiliary space: O(1)
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
```

### 2.2 Python Memory Model

```python
def python_memory_analysis():
    """Phân tích memory model của Python"""
    
    # Integer caching (-5 to 256)
    a = 100
    b = 100
    print(f"a is b: {a is b}")  # True - same object
    
    c = 300
    d = 300
    print(f"c is d: {c is d}")  # False - different objects
    
    # List memory allocation
    list1 = []
    print(f"Empty list size: {sys.getsizeof(list1)} bytes")
    
    for i in range(10):
        list1.append(i)
        print(f"Size after {i+1} elements: {sys.getsizeof(list1)} bytes")
    
    # String interning
    s1 = "hello"
    s2 = "hello"
    print(f"s1 is s2: {s1 is s2}")  # True - interned
    
    # Dictionary memory
    dict1 = {}
    print(f"Empty dict size: {sys.getsizeof(dict1)} bytes")
    
    for i in range(10):
        dict1[i] = i**2
        print(f"Dict size with {i+1} items: {sys.getsizeof(dict1)} bytes")
```

### 2.3 Memory-Efficient Data Structures

```python
def memory_efficient_alternatives():
    """So sánh memory efficiency của các data structures"""
    
    # Array vs List
    import array
    
    # List of integers
    int_list = list(range(1000))
    print(f"List size: {sys.getsizeof(int_list)} bytes")
    
    # Array of integers
    int_array = array.array('i', range(1000))
    print(f"Array size: {sys.getsizeof(int_array)} bytes")
    
    # Generator vs List
    def number_generator(n):
        for i in range(n):
            yield i**2
    
    def number_list(n):
        return [i**2 for i in range(n)]
    
    gen = number_generator(1000)
    lst = number_list(1000)
    
    print(f"Generator size: {sys.getsizeof(gen)} bytes")
    print(f"List size: {sys.getsizeof(lst)} bytes")
    
    # Slots vs Dict
    class RegularClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class SlottedClass:
        __slots__ = ['x', 'y']
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    regular = RegularClass(1, 2)
    slotted = SlottedClass(1, 2)
    
    print(f"Regular class size: {sys.getsizeof(regular) + sys.getsizeof(regular.__dict__)} bytes")
    print(f"Slotted class size: {sys.getsizeof(slotted)} bytes")
```

## Phần 3: Memory Optimization Techniques (45 phút)

### 3.1 In-place Algorithms

```python
def in_place_optimizations():
    """Thuật toán in-place để tiết kiệm memory"""
    
    def reverse_array_in_place(arr):
        # O(1) space instead of O(n)
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
    
    def rotate_array_in_place(arr, k):
        # O(1) space rotation
        n = len(arr)
        k = k % n
        
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return arr
    
    def remove_duplicates_in_place(arr):
        # O(1) space for sorted array
        if not arr:
            return 0
        
        write_index = 1
        for read_index in range(1, len(arr)):
            if arr[read_index] != arr[read_index - 1]:
                arr[write_index] = arr[read_index]
                write_index += 1
        
        return write_index
```

### 3.2 Memory Pool và Object Reuse

```python
class ObjectPool:
    """Simple object pool để tái sử dụng objects"""
    def __init__(self, create_func, reset_func=None):
        self.create_func = create_func
        self.reset_func = reset_func
        self.pool = []
    
    def get(self):
        if self.pool:
            obj = self.pool.pop()
            if self.reset_func:
                self.reset_func(obj)
            return obj
        return self.create_func()
    
    def release(self, obj):
        self.pool.append(obj)

def memory_pool_example():
    """Ví dụ sử dụng object pool"""
    
    # Pool for lists
    def create_list():
        return []
    
    def reset_list(lst):
        lst.clear()
    
    list_pool = ObjectPool(create_list, reset_list)
    
    # Sử dụng
    temp_list = list_pool.get()
    temp_list.extend([1, 2, 3, 4, 5])
    # Process temp_list
    list_pool.release(temp_list)
```

### 3.3 Lazy Evaluation và Generators

```python
def lazy_evaluation_examples():
    """Lazy evaluation để tiết kiệm memory"""
    
    def fibonacci_generator():
        """Generator cho Fibonacci sequence"""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    def prime_sieve_generator(limit):
        """Sieve of Eratosthenes với generator"""
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, limit + 1, i):
                    is_prime[j] = False
        
        for i in range(2, limit + 1):
            if is_prime[i]:
                yield i
    
    def lazy_file_processing(filename):
        """Xử lý file lớn với generator"""
        def process_lines():
            with open(filename, 'r') as f:
                for line in f:
                    # Process line
                    yield line.strip().upper()
        
        return process_lines()
    
    # Itertools cho lazy operations
    import itertools
    
    def lazy_combinations():
        """Lazy combinations thay vì tạo tất cả"""
        data = range(100)
        # Thay vì: list(itertools.combinations(data, 3))
        # Dùng: itertools.combinations(data, 3)
        return itertools.combinations(data, 3)
```

## Phần 4: Performance Optimization Strategies (45 phút)

### 4.1 Algorithmic Optimizations

```python
def algorithmic_optimizations():
    """Tối ưu hóa thuật toán"""
    
    # Memoization
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fibonacci_memoized(n):
        if n <= 1:
            return n
        return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    
    # Early termination
    def find_first_duplicate_optimized(arr):
        seen = set()
        for num in arr:
            if num in seen:
                return num  # Early return
            seen.add(num)
        return None
    
    # Preprocessing
    class PrefixSum:
        def __init__(self, arr):
            self.prefix = [0]
            for num in arr:
                self.prefix.append(self.prefix[-1] + num)
        
        def range_sum(self, left, right):
            # O(1) query after O(n) preprocessing
            return self.prefix[right + 1] - self.prefix[left]
    
    # Binary search optimization
    def binary_search_leftmost(arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
```

### 4.2 Data Structure Optimizations

```python
def data_structure_optimizations():
    """Tối ưu hóa data structures"""
    
    # Use appropriate data structures
    def count_characters_optimized(text):
        # Counter thay vì dict thủ công
        from collections import Counter
        return Counter(text)
    
    def unique_elements_optimized(arr):
        # Set thay vì list
        return list(set(arr))
    
    def fast_membership_test():
        # Set cho membership test O(1) thay vì list O(n)
        large_list = list(range(10000))
        large_set = set(large_list)
        
        # Slow: 5000 in large_list
        # Fast: 5000 in large_set
        return large_set
    
    # Deque for queue operations
    from collections import deque
    
    def queue_operations_optimized():
        # deque thay vì list cho queue
        queue = deque()
        queue.append(1)      # O(1)
        queue.appendleft(0)  # O(1)
        queue.popleft()      # O(1)
        return queue
```

### 4.3 Python-specific Optimizations

```python
def python_specific_optimizations():
    """Tối ưu hóa đặc thù Python"""
    
    # List comprehension vs loops
    def squares_loop(n):
        result = []
        for i in range(n):
            result.append(i**2)
        return result
    
    def squares_comprehension(n):
        return [i**2 for i in range(n)]
    
    # String operations
    def join_strings_optimized(strings):
        # join() thay vì += trong loop
        return ''.join(strings)
    
    def join_strings_slow(strings):
        result = ""
        for s in strings:
            result += s  # Creates new string each time
        return result
    
    # Multiple assignment
    def swap_optimized(a, b):
        return b, a  # Pythonic way
    
    def swap_traditional(a, b):
        temp = a
        a = b
        b = temp
        return a, b
    
    # Use built-in functions
    def sum_optimized(arr):
        return sum(arr)  # Built-in C implementation
    
    def sum_manual(arr):
        total = 0
        for num in arr:
            total += num
        return total
```

### 4.4 Olympic-specific Optimizations

```python
def olympic_optimizations():
    """Tối ưu hóa cho Olympic programming"""
    
    # Fast I/O
    import sys
    
    def fast_input():
        # sys.stdin.readline() nhanh hơn input()
        return sys.stdin.readline().strip()
    
    def fast_int_input():
        return int(sys.stdin.readline())
    
    def fast_multiple_ints():
        return map(int, sys.stdin.readline().split())
    
    # Avoid function calls in tight loops
    def optimize_tight_loops(arr):
        # Cache function references
        append = arr.append
        for i in range(1000):
            append(i)  # Faster than arr.append(i)
        return arr
    
    # Use local variables
    def optimize_global_access():
        # Cache global references as local
        local_len = len
        local_range = range
        
        result = []
        for i in local_range(1000):
            if local_len(result) < 500:
                result.append(i)
        return result
    
    # Bit operations
    def bit_optimizations():
        # Bit shifts for multiplication/division by powers of 2
        def multiply_by_8(x):
            return x << 3  # Faster than x * 8
        
        def divide_by_4(x):
            return x >> 2  # Faster than x // 4
        
        def is_even(x):
            return (x & 1) == 0  # Faster than x % 2 == 0
        
        return multiply_by_8, divide_by_4, is_even
```

## Bài tập thực hành

1. **[problem210101.py]** - Performance measurement tools
2. **[problem210102.py]** - Profiling và benchmarking
3. **[problem210201.py]** - Space complexity analysis
4. **[problem210202.py]** - Memory usage optimization
5. **[problem210301.py]** - In-place algorithms
6. **[problem210302.py]** - Memory-efficient data structures
7. **[problem210401.py]** - Performance optimization techniques
8. **[problem210402.py]** - Olympic-specific optimizations

## Tổng kết

- Performance measurement cần tools phù hợp (timeit, cProfile, memory_profiler)
- Space complexity bao gồm auxiliary space và total space
- Python có memory overhead, cần hiểu để tối ưu
- In-place algorithms tiết kiệm memory đáng kể
- Generators và lazy evaluation cho memory efficiency
- Olympic programming cần tối ưu I/O và tight loops
- Profiling giúp identify bottlenecks thực tế