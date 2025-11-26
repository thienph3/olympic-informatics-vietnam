# Day 21: Speed Training

## Fast I/O Techniques

### Optimized Input/Output Operations
```python
# Standard fast I/O template
import sys
input = sys.stdin.readline

def fast_io_setup():
    """
    Setup cho fast I/O trong Python
    """
    
    # Method 1: sys.stdin.readline
    import sys
    input = sys.stdin.readline
    
    # Đọc single integer
    n = int(input())
    
    # Đọc multiple integers
    a, b, c = map(int, input().split())
    
    # Đọc array
    arr = list(map(int, input().split()))
    
    # Đọc string (remove newline)
    s = input().strip()

def advanced_io_techniques():
    """
    Advanced I/O techniques cho performance
    """
    
    techniques = {
        "Bulk Reading": """
# Đọc tất cả input một lần
import sys
data = sys.stdin.read().split()
idx = 0

def next_int():
    global idx
    val = int(data[idx])
    idx += 1
    return val

n = next_int()
arr = [next_int() for _ in range(n)]
        """,
        
        "Output Buffering": """
# Buffer output để giảm system calls
output_buffer = []

def fast_print(value):
    output_buffer.append(str(value))

def flush_output():
    print('\\n'.join(output_buffer))
    output_buffer.clear()

# Sử dụng
for i in range(n):
    fast_print(result[i])
flush_output()
        """,
        
        "Memory Efficient Reading": """
# Cho input rất lớn
def read_large_input(filename):
    with open(filename, 'r') as f:
        for line in f:
            # Process line by line thay vì load all
            yield line.strip()

# Hoặc sử dụng mmap cho file rất lớn
import mmap

def read_with_mmap(filename):
    with open(filename, 'r') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            return mm.read().decode('utf-8')
        """
    }
    
    return techniques
```

### Template Code Preparation

#### Essential Templates
```python
class ContestTemplates:
    """
    Essential templates cho contest speed
    """
    
    @staticmethod
    def binary_search_template():
        """
        Binary search template với variants
        """
        
        templates = {
            "Standard Binary Search": """
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
            """,
            
            "Lower Bound": """
def lower_bound(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
            """,
            
            "Upper Bound": """
def upper_bound(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left
            """,
            
            "Binary Search on Answer": """
def binary_search_answer(check_func, low, high):
    while low < high:
        mid = (low + high) // 2
        if check_func(mid):
            high = mid
        else:
            low = mid + 1
    return low
            """
        }
        
        return templates
    
    @staticmethod
    def graph_templates():
        """
        Graph algorithm templates
        """
        
        templates = {
            "DFS Template": """
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result
            """,
            
            "BFS Template": """
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
            """,
            
            "Dijkstra Template": """
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
            """
        }
        
        return templates
    
    @staticmethod
    def dp_templates():
        """
        DP templates cho common patterns
        """
        
        templates = {
            "1D DP": """
def dp_1d(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    
    for i in range(1, n):
        dp[i] = max(dp[i-1], arr[i])  # Example: max subarray ending here
    
    return dp[n-1]
            """,
            
            "2D DP": """
def dp_2d(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    
    # Initialize first row and column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill the rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]
            """,
            
            "Knapsack Template": """
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
            """
        }
        
        return templates
```

### Time Management Strategies

#### Speed Optimization Techniques
```python
def speed_optimization_framework():
    """
    Framework tối ưu tốc độ coding
    """
    
    optimization_areas = {
        "Reading Speed": {
            "techniques": [
                "Skim problem for key information first",
                "Identify input/output format quickly", 
                "Look for constraint patterns",
                "Recognize problem type from keywords"
            ],
            "time_target": "2-3 minutes for simple problems, 5-8 for complex",
            "practice_methods": [
                "Speed reading exercises",
                "Pattern recognition drills",
                "Constraint analysis practice"
            ]
        },
        
        "Algorithm Selection Speed": {
            "techniques": [
                "Memorize complexity requirements for common constraints",
                "Build mental library of algorithm patterns",
                "Practice quick complexity estimation",
                "Use decision trees for algorithm choice"
            ],
            "time_target": "1-3 minutes for algorithm selection",
            "practice_methods": [
                "Algorithm flashcards",
                "Complexity estimation drills",
                "Pattern matching exercises"
            ]
        },
        
        "Implementation Speed": {
            "techniques": [
                "Use templates for common patterns",
                "Practice typing common constructs",
                "Minimize debugging through careful coding",
                "Use IDE shortcuts effectively"
            ],
            "time_target": "15-30 minutes depending on complexity",
            "practice_methods": [
                "Template memorization",
                "Typing speed practice",
                "IDE proficiency training"
            ]
        }
    }
    
    return optimization_areas

def time_allocation_strategies():
    """
    Strategies phân bổ thời gian optimal
    """
    
    strategies = {
        "15-Minute Problems": {
            "target_problems": "Implementation, basic math, simple greedy",
            "time_breakdown": {
                "Reading": "2-3 minutes",
                "Algorithm": "1-2 minutes", 
                "Coding": "8-10 minutes",
                "Testing": "2-3 minutes"
            },
            "optimization_focus": "Minimize reading and testing time"
        },
        
        "25-Minute Problems": {
            "target_problems": "Basic DP, graph traversal, binary search",
            "time_breakdown": {
                "Reading": "3-5 minutes",
                "Algorithm": "3-5 minutes",
                "Coding": "12-15 minutes", 
                "Testing": "3-5 minutes"
            },
            "optimization_focus": "Efficient algorithm selection"
        },
        
        "35-Minute Problems": {
            "target_problems": "Complex DP, advanced graph, data structures",
            "time_breakdown": {
                "Reading": "5-8 minutes",
                "Algorithm": "5-10 minutes",
                "Coding": "15-20 minutes",
                "Testing": "5-8 minutes"
            },
            "optimization_focus": "Careful implementation to minimize debugging"
        }
    }
    
    return strategies
```

### Quick Debugging Methods

#### Systematic Debugging for Speed
```python
def speed_debugging_techniques():
    """
    Debugging techniques tối ưu cho speed
    """
    
    techniques = {
        "Prevention-First Approach": {
            "coding_practices": [
                "Use meaningful variable names",
                "Add bounds checking for arrays",
                "Initialize variables explicitly",
                "Use consistent coding style"
            ],
            "common_checks": [
                "Array bounds (0 to n-1)",
                "Integer overflow possibilities",
                "Edge cases (n=1, empty input)",
                "Output format requirements"
            ]
        },
        
        "Rapid Bug Location": {
            "systematic_approach": [
                "Test with sample input first",
                "Add print statements at key points",
                "Binary search for bug location",
                "Check one component at a time"
            ],
            "debugging_prints": """
# Strategic print placement
def debug_function(arr, target):
    print(f"Input: arr={arr}, target={target}")  # Input verification
    
    result = process_array(arr)
    print(f"After processing: {result}")  # Intermediate result
    
    final = compute_final(result, target)
    print(f"Final result: {final}")  # Final verification
    
    return final
            """
        },
        
        "Quick Fix Strategies": {
            "common_fixes": [
                "Off-by-one: Check loop bounds and array indices",
                "Wrong algorithm: Verify complexity matches constraints", 
                "Logic error: Trace through small example manually",
                "Output format: Check spacing, newlines, precision"
            ],
            "when_to_rewrite": [
                "Bug location unclear after 10 minutes",
                "Multiple interrelated bugs found",
                "Code structure makes debugging difficult"
            ]
        }
    }
    
    return techniques

def debugging_tools_and_tricks():
    """
    Tools và tricks cho debugging nhanh
    """
    
    tools = {
        "Assert Statements": """
# Use asserts for debugging
def binary_search(arr, target):
    assert len(arr) > 0, "Array cannot be empty"
    assert all(arr[i] <= arr[i+1] for i in range(len(arr)-1)), "Array must be sorted"
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        assert 0 <= mid < len(arr), f"Invalid mid index: {mid}"
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
        """,
        
        "Trace Functions": """
def trace_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@trace_execution
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
        """,
        
        "Visual Debugging": """
def visualize_array_state(arr, highlight_indices=None):
    if highlight_indices is None:
        highlight_indices = []
    
    print("Array state:")
    for i, val in enumerate(arr):
        marker = " -> " if i in highlight_indices else "    "
        print(f"{marker}[{i}]: {val}")
    print()

# Usage during debugging
def debug_sorting(arr):
    print("Initial state:")
    visualize_array_state(arr)
    
    # ... sorting algorithm with visualization at key points
        """
    }
    
    return tools
```

### Speed Training Exercises

#### Progressive Speed Building
```python
def speed_training_program():
    """
    Program training tốc độ systematic
    """
    
    training_levels = {
        "Level 1: Basic Speed (Week 1-2)": {
            "focus": "Template memorization and typing speed",
            "exercises": [
                "Type common templates from memory",
                "Implement basic algorithms under time pressure",
                "Practice reading problems quickly"
            ],
            "targets": {
                "Template recall": "< 30 seconds",
                "Basic implementation": "< 15 minutes",
                "Problem reading": "< 3 minutes"
            }
        },
        
        "Level 2: Pattern Recognition (Week 3-4)": {
            "focus": "Quick algorithm identification",
            "exercises": [
                "Classify 50 problems by type in 30 minutes",
                "Estimate complexity requirements quickly",
                "Practice algorithm selection decisions"
            ],
            "targets": {
                "Problem classification": "< 1 minute per problem",
                "Algorithm selection": "< 2 minutes",
                "Complexity estimation": "< 30 seconds"
            }
        },
        
        "Level 3: Implementation Speed (Week 5-6)": {
            "focus": "Fast, bug-free coding",
            "exercises": [
                "Implement solutions without debugging",
                "Code review for common bug patterns",
                "Practice clean coding under pressure"
            ],
            "targets": {
                "Bug-free implementation": "> 80% success rate",
                "Coding speed": "< 20 minutes for medium problems",
                "First submission AC": "> 70% success rate"
            }
        },
        
        "Level 4: Contest Simulation (Week 7-8)": {
            "focus": "Full contest performance",
            "exercises": [
                "Complete contests under time pressure",
                "Practice time management strategies",
                "Simulate contest stress conditions"
            ],
            "targets": {
                "Contest completion": "> 4 problems in 3 hours",
                "Time management": "Optimal allocation across problems",
                "Stress performance": "Maintain speed under pressure"
            }
        }
    }
    
    return training_levels

def speed_measurement_metrics():
    """
    Metrics đo lường tốc độ improvement
    """
    
    metrics = {
        "Reading Speed Metrics": {
            "Words per minute": "Target: > 300 WPM for technical text",
            "Comprehension accuracy": "Target: > 95% key information retention",
            "Pattern recognition time": "Target: < 30 seconds for common patterns"
        },
        
        "Coding Speed Metrics": {
            "Lines of code per minute": "Target: > 5 LOC/min for contest code",
            "Template recall time": "Target: < 30 seconds for any template",
            "Bug introduction rate": "Target: < 1 bug per 50 lines"
        },
        
        "Problem Solving Speed": {
            "Time to first approach": "Target: < 5 minutes for familiar problems",
            "Implementation time": "Target: < 2x theoretical minimum",
            "Debug time ratio": "Target: < 20% of total solving time"
        },
        
        "Contest Performance": {
            "Problems solved per hour": "Target: > 1.5 problems/hour average",
            "First submission accuracy": "Target: > 70% AC rate",
            "Time allocation efficiency": "Target: < 10% time waste"
        }
    }
    
    return metrics
```

## Speed Training Targets for Day 21

### Specific Time Targets
- **SORTSTRING**: 15 minutes (String manipulation)
- **ICPC**: 20 minutes (Simulation problem)  
- **TRICKLES**: 25 minutes (Graph problem)
- **GAME**: 30 minutes (Game theory)
- **OTT**: 35 minutes (Mathematical problem)

### Key Speed Skills to Master
1. **Instant Template Recall**: < 30 seconds for any common pattern
2. **Rapid Problem Classification**: < 1 minute to identify problem type
3. **Efficient Implementation**: Minimal debugging required
4. **Quick Testing**: Systematic verification in < 5 minutes
5. **Time Awareness**: Constant monitoring of time allocation
6. **Stress Management**: Maintain speed under pressure
7. **Strategic Skipping**: Quick decisions on problem difficulty