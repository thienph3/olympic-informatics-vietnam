# Day 22: Debugging & Optimization

## Common Bug Patterns

### Systematic Bug Classification
```python
def common_contest_bugs():
    """
    Phân loại bugs phổ biến trong contest programming
    """
    
    bug_categories = {
        "Logic Errors": {
            "Wrong Algorithm Choice": {
                "symptoms": ["Time limit exceeded", "Wrong answer on complex cases"],
                "examples": [
                    "Using O(n²) when O(n log n) required",
                    "Greedy approach when DP needed",
                    "BFS when Dijkstra required"
                ],
                "detection": "Check algorithm complexity vs constraints",
                "prevention": "Verify algorithm choice before coding"
            },
            
            "Incorrect Base Cases": {
                "symptoms": ["Wrong answer on edge cases", "Runtime errors"],
                "examples": [
                    "DP base case not handled",
                    "Recursion without proper termination",
                    "Empty input not considered"
                ],
                "detection": "Test with minimal inputs (n=0, n=1)",
                "prevention": "Always define base cases explicitly"
            },
            
            "Off-by-One Errors": {
                "symptoms": ["Array index out of bounds", "Wrong answer"],
                "examples": [
                    "for i in range(n+1) instead of range(n)",
                    "Accessing arr[n] when valid range is 0 to n-1",
                    "Loop condition <= vs <"
                ],
                "detection": "Trace through boundary values",
                "prevention": "Use consistent indexing conventions"
            }
        },
        
        "Implementation Errors": {
            "Data Type Issues": {
                "symptoms": ["Integer overflow", "Precision errors"],
                "examples": [
                    "Using int when long long needed",
                    "Float precision loss in calculations",
                    "Modular arithmetic errors"
                ],
                "detection": "Check constraint ranges",
                "prevention": "Use appropriate data types from start"
            },
            
            "Uninitialized Variables": {
                "symptoms": ["Unpredictable behavior", "Wrong answers"],
                "examples": [
                    "Using variables before assignment",
                    "Array not properly initialized",
                    "Global variables with unexpected values"
                ],
                "detection": "Add initialization checks",
                "prevention": "Initialize all variables explicitly"
            },
            
            "Memory Access Errors": {
                "symptoms": ["Segmentation fault", "Runtime error"],
                "examples": [
                    "Array bounds violation",
                    "Null pointer dereference",
                    "Stack overflow from deep recursion"
                ],
                "detection": "Add bounds checking",
                "prevention": "Validate all array accesses"
            }
        },
        
        "Input/Output Errors": {
            "Format Mismatches": {
                "symptoms": ["Wrong answer", "Presentation error"],
                "examples": [
                    "Extra spaces in output",
                    "Missing newlines",
                    "Wrong number format"
                ],
                "detection": "Compare output format exactly",
                "prevention": "Read output requirements carefully"
            },
            
            "Input Parsing Errors": {
                "symptoms": ["Wrong answer", "Runtime error"],
                "examples": [
                    "Reading wrong number of inputs",
                    "Incorrect data type conversion",
                    "Not handling multiple test cases"
                ],
                "detection": "Verify input parsing with samples",
                "prevention": "Test input parsing separately"
            }
        }
    }
    
    return bug_categories

def bug_detection_strategies():
    """
    Strategies để detect bugs efficiently
    """
    
    strategies = {
        "Systematic Testing": {
            "Sample Cases": [
                "Always test provided examples first",
                "Verify exact output format match",
                "Check edge cases mentioned in problem"
            ],
            
            "Edge Case Generation": [
                "Minimum constraints (n=1, empty arrays)",
                "Maximum constraints (n=max_value)",
                "Boundary values (powers of 2, etc.)",
                "Special cases (all same values, sorted arrays)"
            ],
            
            "Stress Testing": [
                "Generate random large inputs",
                "Compare with brute force solution",
                "Test with time limit in mind"
            ]
        },
        
        "Code Review Techniques": {
            "Static Analysis": [
                "Check all array accesses for bounds",
                "Verify loop conditions and increments",
                "Confirm variable initialization",
                "Review data type choices"
            ],
            
            "Logic Verification": [
                "Trace algorithm with small examples",
                "Verify base cases and recursion",
                "Check algorithm complexity",
                "Confirm problem understanding"
            ]
        }
    }
    
    return strategies
```

### Advanced Debugging Techniques

#### Systematic Debugging Process
```python
class AdvancedDebugging:
    """
    Advanced debugging techniques cho contest
    """
    
    @staticmethod
    def binary_search_debugging():
        """
        Binary search approach để locate bugs
        """
        
        technique = """
# Binary search debugging technique
def debug_with_binary_search(input_data, expected_output):
    # Step 1: Identify the range where bug occurs
    def test_partial_algorithm(start_idx, end_idx):
        # Test algorithm with subset of operations
        partial_result = run_partial_algorithm(input_data, start_idx, end_idx)
        return partial_result == expected_partial_output(start_idx, end_idx)
    
    # Step 2: Binary search for bug location
    left, right = 0, total_operations - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if test_partial_algorithm(0, mid):
            left = mid + 1  # Bug is in second half
        else:
            right = mid     # Bug is in first half
    
    return left  # Bug location found
        """
        
        return technique
    
    @staticmethod
    def differential_debugging():
        """
        So sánh với reference implementation
        """
        
        technique = """
def differential_debugging(test_cases):
    def brute_force_solution(input_data):
        # Simple, obviously correct but slow solution
        pass
    
    def optimized_solution(input_data):
        # Fast solution being debugged
        pass
    
    for i, test_case in enumerate(test_cases):
        expected = brute_force_solution(test_case)
        actual = optimized_solution(test_case)
        
        if expected != actual:
            print(f"Bug found in test case {i}")
            print(f"Input: {test_case}")
            print(f"Expected: {expected}")
            print(f"Actual: {actual}")
            
            # Analyze the difference
            analyze_difference(test_case, expected, actual)
            break
        """
        
        return technique
    
    @staticmethod
    def state_tracking_debugging():
        """
        Track algorithm state throughout execution
        """
        
        technique = """
class StateTracker:
    def __init__(self):
        self.states = []
        self.step = 0
    
    def log_state(self, description, variables):
        self.states.append({
            'step': self.step,
            'description': description,
            'variables': variables.copy()
        })
        self.step += 1
    
    def print_trace(self):
        for state in self.states:
            print(f"Step {state['step']}: {state['description']}")
            for var, value in state['variables'].items():
                print(f"  {var} = {value}")
            print()

# Usage in algorithm
def debug_algorithm(input_data):
    tracker = StateTracker()
    
    # Initialize
    dp = [0] * n
    tracker.log_state("Initialization", {'dp': dp, 'n': n})
    
    # Main loop
    for i in range(n):
        dp[i] = compute_value(i)
        tracker.log_state(f"Iteration {i}", {'i': i, 'dp': dp})
    
    tracker.print_trace()
    return dp[n-1]
        """
        
        return technique
```

#### Memory and Performance Debugging
```python
def memory_optimization_techniques():
    """
    Techniques để optimize memory usage
    """
    
    techniques = {
        "Memory Profiling": """
import tracemalloc

def profile_memory_usage(func, *args):
    tracemalloc.start()
    
    result = func(*args)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
    
    return result
        """,
        
        "Space Optimization Patterns": """
# Pattern 1: Rolling arrays for DP
def optimize_dp_space(n, m):
    # Instead of dp[n][m]
    prev = [0] * m
    curr = [0] * m
    
    for i in range(n):
        for j in range(m):
            curr[j] = compute_dp_value(prev, curr, i, j)
        prev, curr = curr, prev
    
    return prev

# Pattern 2: In-place algorithms
def optimize_sorting_space(arr):
    # Modify array in-place instead of creating new one
    def partition(low, high):
        # In-place partitioning
        pass
    
    def quick_sort_inplace(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_inplace(low, pi - 1)
            quick_sort_inplace(pi + 1, high)
    
    quick_sort_inplace(0, len(arr) - 1)
    return arr

# Pattern 3: Generator functions for large datasets
def process_large_dataset(data_source):
    for chunk in read_in_chunks(data_source):
        yield process_chunk(chunk)
        """,
        
        "Memory Leak Detection": """
def detect_memory_leaks():
    import gc
    import sys
    
    def get_memory_usage():
        return sum(sys.getsizeof(obj) for obj in gc.get_objects())
    
    initial_memory = get_memory_usage()
    
    # Run algorithm multiple times
    for i in range(100):
        run_algorithm()
        
        if i % 10 == 0:
            current_memory = get_memory_usage()
            growth = current_memory - initial_memory
            print(f"Iteration {i}: Memory growth = {growth} bytes")
            
            if growth > threshold:
                print("Potential memory leak detected!")
                break
        """
    }
    
    return techniques

def performance_optimization_strategies():
    """
    Strategies để optimize algorithm performance
    """
    
    strategies = {
        "Bottleneck Identification": """
import cProfile
import pstats

def profile_algorithm(func, *args):
    profiler = cProfile.Profile()
    profiler.enable()
    
    result = func(*args)
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 functions
    
    return result
        """,
        
        "Algorithmic Optimizations": """
# Optimization 1: Precomputation
def optimize_with_precomputation(queries):
    # Precompute expensive operations
    precomputed = {}
    for i in range(max_value):
        precomputed[i] = expensive_function(i)
    
    results = []
    for query in queries:
        # O(1) lookup instead of expensive computation
        results.append(precomputed[query])
    
    return results

# Optimization 2: Memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def optimized_recursive_function(n):
    if n <= 1:
        return n
    return optimized_recursive_function(n-1) + optimized_recursive_function(n-2)

# Optimization 3: Early termination
def optimize_with_early_termination(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
        if val > target and is_sorted(arr):
            break  # Early termination for sorted arrays
    return -1
        """,
        
        "Data Structure Optimizations": """
# Use appropriate data structures
from collections import defaultdict, deque, Counter
import heapq
import bisect

def optimize_data_structures():
    # Use Counter for frequency counting
    freq = Counter(arr)  # Instead of manual counting
    
    # Use defaultdict to avoid key checking
    graph = defaultdict(list)  # Instead of checking if key exists
    
    # Use deque for efficient queue operations
    queue = deque()  # Instead of list with pop(0)
    
    # Use heapq for priority queue
    heap = []
    heapq.heappush(heap, item)  # Instead of sorting repeatedly
    
    # Use bisect for binary search
    pos = bisect.bisect_left(sorted_arr, target)  # Instead of manual binary search
        """
    }
    
    return strategies
```

## Code Optimization Techniques

### Performance Optimization Patterns
```python
def advanced_optimization_patterns():
    """
    Advanced patterns cho performance optimization
    """
    
    patterns = {
        "Loop Optimizations": {
            "Loop Unrolling": """
# Manual loop unrolling for small, fixed iterations
def optimized_small_loop(arr):
    n = len(arr)
    result = 0
    
    # Process 4 elements at a time
    for i in range(0, n - 3, 4):
        result += arr[i] + arr[i+1] + arr[i+2] + arr[i+3]
    
    # Handle remaining elements
    for i in range(n - (n % 4), n):
        result += arr[i]
    
    return result
            """,
            
            "Loop Fusion": """
# Combine multiple loops over same data
def fused_loops(arr):
    # Instead of separate loops
    # for i in range(n): sum1 += arr[i]
    # for i in range(n): sum2 += arr[i] * 2
    
    sum1 = sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i]
        sum2 += arr[i] * 2
    
    return sum1, sum2
            """,
            
            "Strength Reduction": """
# Replace expensive operations with cheaper ones
def strength_reduction_example(n):
    # Instead of: result = i * i for i in range(n)
    result = []
    square = 0
    
    for i in range(n):
        result.append(square)
        square += 2 * i + 1  # Next square = current + 2*i + 1
    
    return result
            """
        },
        
        "Cache-Friendly Patterns": {
            "Spatial Locality": """
# Access memory in sequential patterns
def cache_friendly_matrix_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    # Block-wise multiplication for better cache usage
    block_size = 64
    
    for i0 in range(0, n, block_size):
        for j0 in range(0, n, block_size):
            for k0 in range(0, n, block_size):
                # Process block
                for i in range(i0, min(i0 + block_size, n)):
                    for j in range(j0, min(j0 + block_size, n)):
                        for k in range(k0, min(k0 + block_size, n)):
                            C[i][j] += A[i][k] * B[k][j]
    
    return C
            """,
            
            "Temporal Locality": """
# Reuse recently accessed data
def temporal_locality_example(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    # Process row by row to maintain temporal locality
    for i in range(rows):
        row_sum = 0
        row_max = float('-inf')
        
        for j in range(cols):
            val = matrix[i][j]  # Access once, use multiple times
            row_sum += val
            row_max = max(row_max, val)
        
        # Process row results
        process_row_results(i, row_sum, row_max)
            """
        },
        
        "Bit Manipulation Optimizations": """
# Use bit operations for faster arithmetic
def bit_optimization_examples():
    # Fast multiplication/division by powers of 2
    def fast_multiply_by_8(x):
        return x << 3  # Instead of x * 8
    
    def fast_divide_by_4(x):
        return x >> 2  # Instead of x // 4
    
    # Fast modulo for powers of 2
    def fast_modulo_16(x):
        return x & 15  # Instead of x % 16
    
    # Check if number is power of 2
    def is_power_of_2(x):
        return x > 0 and (x & (x - 1)) == 0
    
    # Count set bits
    def count_set_bits(x):
        count = 0
        while x:
            count += 1
            x &= x - 1  # Remove rightmost set bit
        return count
        """
    }
    
    return patterns

def compiler_optimization_hints():
    """
    Hints để help compiler optimize code
    """
    
    hints = {
        "Function Inlining": """
# Small, frequently called functions
def inline_candidate(x, y):
    return x * x + y * y  # Simple operation, good for inlining

# Use local functions for better optimization
def optimized_algorithm(data):
    def helper(x):  # Local function, likely to be inlined
        return x * 2 + 1
    
    return [helper(x) for x in data]
        """,
        
        "Loop Optimization Hints": """
# Help compiler optimize loops
def loop_optimization_hints(arr):
    n = len(arr)
    
    # Hoist invariant computations
    constant_value = compute_constant()  # Outside loop
    
    for i in range(n):
        # Use hoisted value instead of recomputing
        arr[i] = arr[i] * constant_value
    
    return arr
        """,
        
        "Branch Prediction Hints": """
# Organize code to help branch prediction
def branch_prediction_friendly(arr, threshold):
    # Sort by condition to improve branch prediction
    below_threshold = [x for x in arr if x < threshold]
    above_threshold = [x for x in arr if x >= threshold]
    
    # Process each group separately
    process_below(below_threshold)
    process_above(above_threshold)
        """
    }
    
    return hints
```

## Memory and Time Limit Handling

### Resource Management Strategies
```python
def resource_management_framework():
    """
    Framework quản lý resources trong contest
    """
    
    framework = {
        "Memory Limit Strategies": {
            "Estimation": [
                "Calculate theoretical memory usage",
                "Account for overhead (Python objects, etc.)",
                "Leave safety margin (20-30%)",
                "Consider worst-case scenarios"
            ],
            
            "Optimization Techniques": [
                "Use generators instead of lists when possible",
                "Implement rolling arrays for DP",
                "Compress coordinates for sparse data",
                "Use bit manipulation for boolean arrays"
            ],
            
            "Memory Monitoring": """
import psutil
import os

def monitor_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    
    print(f"RSS: {memory_info.rss / 1024 / 1024:.2f} MB")
    print(f"VMS: {memory_info.vms / 1024 / 1024:.2f} MB")
    
    return memory_info.rss

def memory_limited_algorithm(data, memory_limit_mb):
    current_memory = monitor_memory_usage()
    
    if current_memory > memory_limit_mb * 1024 * 1024:
        # Switch to memory-efficient algorithm
        return memory_efficient_version(data)
    else:
        return standard_version(data)
            """
        },
        
        "Time Limit Strategies": {
            "Time Estimation": [
                "Estimate operations per second (~10^8 for Python)",
                "Calculate theoretical runtime",
                "Account for constant factors",
                "Consider input/output time"
            ],
            
            "Optimization Priorities": [
                "Algorithm complexity first",
                "Implementation efficiency second", 
                "Micro-optimizations last",
                "Profile before optimizing"
            ],
            
            "Time Monitoring": """
import time
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Algorithm timed out")

def time_limited_algorithm(data, time_limit_seconds):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(time_limit_seconds)
    
    try:
        start_time = time.time()
        result = algorithm(data)
        end_time = time.time()
        
        print(f"Algorithm completed in {end_time - start_time:.2f} seconds")
        return result
        
    except TimeoutException:
        print("Algorithm timed out, returning partial result")
        return partial_result
        
    finally:
        signal.alarm(0)  # Cancel alarm
            """
        }
    }
    
    return framework

def adaptive_algorithm_selection():
    """
    Adaptive selection dựa trên constraints
    """
    
    selection_strategy = """
def select_algorithm_by_constraints(n, m, time_limit, memory_limit):
    # Estimate resource requirements for different algorithms
    
    algorithms = {
        'brute_force': {
            'time_complexity': n * n,
            'space_complexity': n,
            'implementation_time': 10  # minutes
        },
        'optimized': {
            'time_complexity': n * log(n),
            'space_complexity': n * log(n),
            'implementation_time': 30
        },
        'advanced': {
            'time_complexity': n,
            'space_complexity': n * n,
            'implementation_time': 60
        }
    }
    
    # Select based on constraints and available time
    for name, algo in algorithms.items():
        if (algo['time_complexity'] <= time_limit and 
            algo['space_complexity'] <= memory_limit and
            algo['implementation_time'] <= remaining_contest_time):
            return name
    
    return 'fallback_algorithm'
    """
    
    return selection_strategy
```

## Day 22 Debugging Targets

### Specific Problem Debugging Focus
- **BROKENCLOCK**: Debug time-related calculations and edge cases
- **SOCOLA**: Debug mathematical logic and formula derivation  
- **RAINBOW**: Debug array processing and edge case handling
- **LBIN**: Debug binary search implementation and bounds
- **ONEDIVK**: Debug mathematical optimization and overflow issues

### Key Debugging Skills to Master
1. **Rapid Bug Location**: Find bugs within 5 minutes using systematic approach
2. **Edge Case Identification**: Automatically check common edge cases
3. **Performance Debugging**: Identify and fix performance bottlenecks
4. **Memory Optimization**: Reduce memory usage when approaching limits
5. **Code Quality**: Write debuggable code from the start
6. **Testing Strategy**: Comprehensive testing in minimal time
7. **Optimization Techniques**: Apply optimizations without introducing bugs