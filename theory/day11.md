# Day 11: Greedy Algorithms

## Greedy Choice Property

### Khái niệm Greedy Algorithm
Greedy algorithm đưa ra lựa chọn tối ưu cục bộ tại mỗi bước, hy vọng dẫn đến lời giải tối ưu toàn cục.

### Đặc điểm của Greedy Algorithm
1. **Greedy Choice Property**: Lựa chọn tối ưu cục bộ dẫn đến tối ưu toàn cục
2. **Optimal Substructure**: Lời giải tối ưu chứa lời giải tối ưu của bài toán con
3. **No backtracking**: Không quay lại thay đổi quyết định đã đưa ra

### Template Greedy Algorithm
```python
def greedy_algorithm(items):
    """
    Template cơ bản cho greedy algorithm
    """
    # 1. Sắp xếp items theo tiêu chí greedy
    items.sort(key=lambda x: greedy_criteria(x))
    
    # 2. Khởi tạo solution
    solution = []
    
    # 3. Lặp qua từng item
    for item in items:
        # 4. Kiểm tra feasibility
        if is_feasible(solution, item):
            # 5. Thêm vào solution
            solution.append(item)
    
    return solution

def greedy_criteria(item):
    """Định nghĩa tiêu chí greedy"""
    pass

def is_feasible(solution, item):
    """Kiểm tra có thể thêm item vào solution không"""
    pass
```

## Activity Selection Problem

### Bài toán
Cho n hoạt động với thời gian bắt đầu s[i] và kết thúc f[i]. Chọn tối đa số hoạt động không trùng lặp thời gian.

### Greedy Solution
```python
def activity_selection(activities):
    """
    Activity Selection Problem
    Greedy choice: Chọn activity kết thúc sớm nhất
    Time: O(n log n), Space: O(1)
    """
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_finish = activities[0][1]
    
    for i in range(1, len(activities)):
        start, finish = activities[i]
        if start >= last_finish:  # No overlap
            selected.append(activities[i])
            last_finish = finish
    
    return selected

# Test
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
result = activity_selection(activities)
print(f"Selected activities: {result}")
print(f"Number of activities: {len(result)}")
```

### Proof of Correctness
```python
def activity_selection_with_proof(activities):
    """
    Activity selection với chứng minh tính đúng đắn
    
    Chứng minh:
    1. Greedy choice: Chọn activity kết thúc sớm nhất luôn an toàn
    2. Optimal substructure: Sau khi chọn activity đầu tiên,
       bài toán con vẫn có cấu trúc tối ưu
    """
    if not activities:
        return []
    
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    
    selected = []
    last_finish = -1
    
    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
            print(f"Selected activity ({start}, {finish})")
    
    return selected
```

## Coin Change Greedy Approach

### Khi nào Greedy hoạt động
```python
def coin_change_greedy(coins, amount):
    """
    Coin change với greedy approach
    Chỉ hoạt động với canonical coin systems (VD: 1, 5, 10, 25)
    """
    coins.sort(reverse=True)  # Largest first
    result = []
    
    for coin in coins:
        count = amount // coin
        if count > 0:
            result.extend([coin] * count)
            amount -= coin * count
    
    return result if amount == 0 else None

# Test với canonical system
coins = [25, 10, 5, 1]
amount = 67
result = coin_change_greedy(coins, amount)
print(f"Coins for {amount}: {result}")  # [25, 25, 10, 5, 1, 1]

def coin_change_greedy_counter_example():
    """
    Counter example: Greedy không hoạt động với non-canonical systems
    """
    coins = [4, 3, 1]
    amount = 6
    
    # Greedy solution: [4, 1, 1] = 3 coins
    greedy_result = coin_change_greedy(coins, amount)
    
    # Optimal solution: [3, 3] = 2 coins
    optimal_result = [3, 3]
    
    print(f"Greedy: {greedy_result} ({len(greedy_result)} coins)")
    print(f"Optimal: {optimal_result} ({len(optimal_result)} coins)")
    print("Greedy fails for non-canonical coin systems!")

coin_change_greedy_counter_example()
```

## When Greedy Works vs Fails

### Greedy Works: Fractional Knapsack
```python
def fractional_knapsack(items, capacity):
    """
    Fractional Knapsack - Greedy works
    Có thể lấy một phần của item
    """
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_value = 0
    result = []
    
    for weight, value in items:
        if capacity >= weight:
            # Take whole item
            capacity -= weight
            total_value += value
            result.append((weight, value, 1.0))  # fraction = 1.0
        else:
            # Take fraction of item
            fraction = capacity / weight
            total_value += value * fraction
            result.append((weight, value, fraction))
            break
    
    return total_value, result

# Test
items = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
capacity = 50
max_value, solution = fractional_knapsack(items, capacity)
print(f"Max value: {max_value}")
print(f"Solution: {solution}")
```

### Greedy Fails: 0/1 Knapsack
```python
def knapsack_01_greedy_fails():
    """
    Demonstration: Greedy fails for 0/1 Knapsack
    """
    items = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
    capacity = 50
    
    # Greedy by value/weight ratio
    items_sorted = sorted(items, key=lambda x: x[1]/x[0], reverse=True)
    print("Sorted by value/weight ratio:", items_sorted)
    
    # Greedy solution: Take (10,60) and (20,100) = value 160
    greedy_value = 60 + 100  # = 160
    
    # Optimal solution: Take (20,100) and (30,120) = value 220
    optimal_value = 100 + 120  # = 220
    
    print(f"Greedy solution value: {greedy_value}")
    print(f"Optimal solution value: {optimal_value}")
    print("Greedy fails for 0/1 Knapsack!")

knapsack_01_greedy_fails()
```

### When to Use Greedy
```python
def greedy_applicability_check():
    """
    Kiểm tra khi nào có thể áp dụng greedy
    """
    
    # 1. Greedy Choice Property
    def has_greedy_choice_property(problem):
        """
        Kiểm tra greedy choice property:
        - Lựa chọn tối ưu cục bộ dẫn đến tối ưu toàn cục
        - Có thể chứng minh bằng exchange argument
        """
        pass
    
    # 2. Optimal Substructure
    def has_optimal_substructure(problem):
        """
        Kiểm tra optimal substructure:
        - Lời giải tối ưu chứa lời giải tối ưu của bài toán con
        """
        pass
    
    # 3. Matroid Property (advanced)
    def is_matroid(problem):
        """
        Kiểm tra matroid property:
        - Independence system với exchange property
        """
        pass
    
    problems_greedy_works = [
        "Activity Selection",
        "Fractional Knapsack", 
        "Huffman Coding",
        "Minimum Spanning Tree (Kruskal, Prim)",
        "Shortest Path (Dijkstra)",
        "Job Scheduling"
    ]
    
    problems_greedy_fails = [
        "0/1 Knapsack",
        "Longest Path Problem",
        "Traveling Salesman Problem",
        "Graph Coloring"
    ]
    
    return problems_greedy_works, problems_greedy_fails
```

## More Greedy Examples

### Job Scheduling
```python
def job_scheduling_deadline(jobs):
    """
    Job scheduling với deadline và penalty
    Minimize total penalty
    """
    # Sort by penalty (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    n = len(jobs)
    max_deadline = max(job[1] for job in jobs)
    
    # Schedule array
    schedule = [None] * (max_deadline + 1)
    total_penalty = 0
    
    for job_id, deadline, penalty in jobs:
        # Try to schedule as late as possible
        for t in range(min(deadline, max_deadline), 0, -1):
            if schedule[t] is None:
                schedule[t] = job_id
                break
        else:
            # Cannot schedule - add penalty
            total_penalty += penalty
    
    return schedule, total_penalty

# Test
jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]
# (job_id, deadline, penalty)
schedule, penalty = job_scheduling_deadline(jobs)
print(f"Schedule: {schedule}")
print(f"Total penalty: {penalty}")
```

### Huffman Coding
```python
import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(text):
    """
    Huffman Coding - Greedy algorithm for optimal prefix codes
    """
    # Count frequencies
    freq = Counter(text)
    
    # Create priority queue
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)
    
    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    root = heap[0]
    
    # Generate codes
    codes = {}
    
    def generate_codes(node, code=""):
        if node.char:  # Leaf node
            codes[node.char] = code or "0"  # Handle single character
        else:
            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")
    
    generate_codes(root)
    
    # Encode text
    encoded = "".join(codes[char] for char in text)
    
    return codes, encoded

# Test
text = "ABRACADABRA"
codes, encoded = huffman_coding(text)
print(f"Huffman codes: {codes}")
print(f"Encoded: {encoded}")
print(f"Original length: {len(text) * 8} bits")
print(f"Compressed length: {len(encoded)} bits")
```

### Interval Scheduling Maximization
```python
def interval_scheduling_maximization(intervals):
    """
    Maximize number of non-overlapping intervals
    Same as Activity Selection
    """
    return activity_selection(intervals)

def interval_scheduling_weighted(intervals):
    """
    Weighted interval scheduling - Greedy doesn't work!
    Need DP solution
    """
    # Sort by finish time
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    
    # DP solution (not greedy)
    dp = [0] * n
    dp[0] = intervals[0][2]  # weight
    
    for i in range(1, n):
        # Include current interval
        include = intervals[i][2]
        
        # Find latest non-overlapping interval
        for j in range(i-1, -1, -1):
            if intervals[j][1] <= intervals[i][0]:
                include += dp[j]
                break
        
        # Max of include vs exclude
        dp[i] = max(include, dp[i-1])
    
    return dp[n-1]

# Test weighted intervals
weighted_intervals = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4), (5, 8, 11), (7, 9, 2)]
# (start, finish, weight)
max_weight = interval_scheduling_weighted(weighted_intervals)
print(f"Max weight: {max_weight}")
```

## Greedy vs Dynamic Programming

### Comparison
```python
def greedy_vs_dp_comparison():
    """
    So sánh Greedy vs Dynamic Programming
    """
    
    comparison = {
        "Time Complexity": {
            "Greedy": "Usually O(n log n) due to sorting",
            "DP": "Usually O(n²) or higher"
        },
        "Space Complexity": {
            "Greedy": "O(1) or O(n)",
            "DP": "O(n) to O(n²)"
        },
        "Approach": {
            "Greedy": "Make locally optimal choice",
            "DP": "Consider all possibilities"
        },
        "Guarantee": {
            "Greedy": "Optimal only if greedy choice property holds",
            "DP": "Always optimal if problem has optimal substructure"
        },
        "Implementation": {
            "Greedy": "Usually simpler",
            "DP": "More complex, need to identify states"
        }
    }
    
    return comparison

def when_to_use_greedy():
    """
    Khi nào nên sử dụng Greedy
    """
    use_greedy_when = [
        "Problem has greedy choice property",
        "Can prove correctness with exchange argument",
        "Need fast solution (time constraint)",
        "Problem involves scheduling/selection",
        "Working with matroids"
    ]
    
    use_dp_when = [
        "Greedy doesn't work (counterexample exists)",
        "Problem has overlapping subproblems",
        "Need to consider all possibilities",
        "Optimization problem without greedy property"
    ]
    
    return use_greedy_when, use_dp_when
```

## Common Greedy Patterns

### Pattern 1: Sorting + Selection
```python
def meeting_rooms(intervals):
    """
    Minimum meeting rooms needed
    Pattern: Sort + Greedy selection
    """
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort()
    
    # Min heap for end times
    import heapq
    heap = []
    
    for start, end in intervals:
        # If room available, reuse it
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    return len(heap)
```

### Pattern 2: Two Pointers + Greedy
```python
def assign_cookies(children, cookies):
    """
    Assign cookies to children to maximize satisfaction
    Pattern: Sort + Two pointers
    """
    children.sort()  # Sort by greed factor
    cookies.sort()   # Sort by size
    
    child = cookie = satisfied = 0
    
    while child < len(children) and cookie < len(cookies):
        if cookies[cookie] >= children[child]:
            satisfied += 1
            child += 1
        cookie += 1
    
    return satisfied
```

### Pattern 3: Priority Queue + Greedy
```python
def task_scheduler(tasks, n):
    """
    Task scheduler with cooldown
    Pattern: Priority queue + Greedy
    """
    from collections import Counter
    import heapq
    
    # Count task frequencies
    task_count = Counter(tasks)
    
    # Max heap (use negative values)
    heap = [-count for count in task_count.values()]
    heapq.heapify(heap)
    
    time = 0
    
    while heap:
        temp = []
        
        # Execute tasks in one cycle
        for _ in range(n + 1):
            if heap:
                temp.append(heapq.heappop(heap))
        
        # Add back tasks with remaining count
        for count in temp:
            if count < -1:  # Still has tasks remaining
                heapq.heappush(heap, count + 1)
        
        # Add time for this cycle
        time += (n + 1) if heap else len(temp)
    
    return time
```

## Best Practices

1. **Prove Correctness**: Always prove greedy choice property
2. **Check Counterexamples**: Test with small examples
3. **Consider Edge Cases**: Empty input, single element
4. **Analyze Time Complexity**: Usually dominated by sorting
5. **Compare with DP**: When greedy fails, consider DP
6. **Use Appropriate Data Structures**: Priority queues, sorting