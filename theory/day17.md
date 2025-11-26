# Day 17: Mock Test 7

## Mock Test Strategy

### Thi thử hoàn toàn như thi thật
Ngày 17 là ngày thi thử đầu tiên trong tháng 3, mục tiêu là simulation hoàn toàn như kỳ thi Olympic thực tế.

### Chuẩn bị trước khi thi
```python
# Checklist chuẩn bị
preparation_checklist = {
    "Environment Setup": [
        "Cài đặt Python 3.10",
        "Chuẩn bị IDE (VS Code)",
        "Kiểm tra internet connection",
        "Chuẩn bị giấy nháp"
    ],
    
    "Mental Preparation": [
        "Ôn lại các pattern algorithms chính",
        "Review template code",
        "Thư giãn và tập trung",
        "Chuẩn bị tâm lý thi 3 tiếng liên tục"
    ],
    
    "Time Management": [
        "Phân bổ thời gian: 5 bài trong 3 tiếng",
        "Đọc đề: 15-20 phút",
        "Coding: 30-40 phút/bài",
        "Debug và test: 10-15 phút/bài"
    ]
}
```

### Contest Format: Free Contest 150

**Thời gian:** 3 tiếng (180 phút)  
**Số bài:** 5 bài  
**Độ khó:** Tăng dần từ dễ đến khó  
**Scoring:** Thường là 100 điểm/bài  

### Template Code cần chuẩn bị

#### Input/Output Template
```python
# Fast I/O template
import sys
input = sys.stdin.readline

def solve():
    # Đọc input
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Xử lý logic
    result = process(arr)
    
    # Output
    print(result)

def process(arr):
    # Main logic here
    return 0

if __name__ == "__main__":
    solve()
```

#### Common Data Structures
```python
# Union-Find template
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

# Segment Tree template
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node, start, mid)
            self.build(arr, 2*node+1, mid+1, end)
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2*node, start, mid, idx, val)
            else:
                self.update(2*node+1, mid+1, end, idx, val)
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(2*node, start, mid, l, r) + 
                self.query(2*node+1, mid+1, end, l, r))
```

#### Algorithm Templates
```python
# Binary Search template
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

# DFS template
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# BFS template
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

# Dijkstra template
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
```

### Contest Strategy

#### Thời gian phân bổ
```python
contest_timeline = {
    "0-20 phút": "Đọc tất cả đề bài, phân loại độ khó",
    "20-60 phút": "Giải bài dễ nhất (thường là bài 1)",
    "60-100 phút": "Giải bài trung bình (bài 2-3)",
    "100-140 phút": "Giải bài khó (bài 4)",
    "140-180 phút": "Giải bài khó nhất (bài 5) hoặc debug"
}

problem_difficulty_estimation = {
    "Easy (100-300 points)": {
        "characteristics": ["Implementation", "Basic math", "Simple greedy"],
        "time_allocation": "20-30 phút",
        "strategy": "Code nhanh, ít bug"
    },
    
    "Medium (400-600 points)": {
        "characteristics": ["DP cơ bản", "Graph traversal", "Binary search"],
        "time_allocation": "30-40 phút", 
        "strategy": "Cẩn thận với edge cases"
    },
    
    "Hard (700-900 points)": {
        "characteristics": ["Advanced DP", "Complex graph", "Data structures"],
        "time_allocation": "40-50 phút",
        "strategy": "Chia nhỏ bài toán, test kỹ"
    }
}
```

#### Problem Reading Strategy
```python
def analyze_problem(problem_statement):
    """
    Framework phân tích đề bài
    """
    
    analysis = {
        "input_constraints": {
            "n_range": "Xác định độ phức tạp cho phép",
            "data_types": "int, float, string?",
            "special_constraints": "Sorted? Unique? Positive?"
        },
        
        "output_format": {
            "single_value": "YES/NO, số nguyên, số thực",
            "multiple_values": "Array, matrix, sequence",
            "special_format": "Modulo, precision requirements"
        },
        
        "algorithm_hints": {
            "keywords": ["maximum", "minimum", "count", "path", "sequence"],
            "constraints": ["n ≤ 10^5 → O(n log n)", "n ≤ 10^3 → O(n²)"],
            "patterns": ["DP", "Graph", "Greedy", "Math"]
        }
    }
    
    return analysis

def estimate_complexity(n_max):
    """
    Ước tính complexity cho phép dựa trên constraints
    """
    
    if n_max <= 20:
        return "O(2^n) - Backtracking, brute force"
    elif n_max <= 100:
        return "O(n³) - Floyd-Warshall, naive DP"
    elif n_max <= 1000:
        return "O(n²) - Nested loops, DP"
    elif n_max <= 10**5:
        return "O(n log n) - Sorting, binary search"
    elif n_max <= 10**6:
        return "O(n) - Linear algorithms"
    else:
        return "O(log n) - Math, binary search on answer"
```

### Debugging Strategy

#### Common Bug Patterns
```python
common_bugs = {
    "Index Errors": [
        "Off-by-one errors",
        "Array bounds checking", 
        "0-indexed vs 1-indexed"
    ],
    
    "Logic Errors": [
        "Wrong base cases",
        "Incorrect loop conditions",
        "Missing edge cases"
    ],
    
    "Input/Output Errors": [
        "Wrong input format",
        "Missing newlines",
        "Integer overflow"
    ],
    
    "Algorithm Errors": [
        "Wrong algorithm choice",
        "Incorrect implementation",
        "Missing optimizations"
    ]
}

def debug_checklist():
    """
    Checklist debug systematic
    """
    
    steps = [
        "1. Kiểm tra sample input/output",
        "2. Test với edge cases (n=1, n=max, empty input)",
        "3. Trace algorithm với small input",
        "4. Kiểm tra data types và overflow",
        "5. Verify algorithm complexity",
        "6. Check input/output format"
    ]
    
    return steps
```

### Sample Problem Analysis

#### Problem Type Recognition
```python
def recognize_problem_type(description):
    """
    Nhận dạng loại bài toán từ mô tả
    """
    
    patterns = {
        "Dynamic Programming": [
            "optimal", "maximum/minimum", "count ways",
            "subsequence", "subarray", "knapsack"
        ],
        
        "Graph Algorithms": [
            "path", "connectivity", "tree", "cycle",
            "shortest", "minimum spanning", "flow"
        ],
        
        "Greedy": [
            "scheduling", "activity selection", "interval",
            "fractional", "local optimum"
        ],
        
        "Math/Number Theory": [
            "gcd", "prime", "modular", "combinatorics",
            "probability", "geometry"
        ],
        
        "Data Structures": [
            "range query", "update", "segment tree",
            "binary indexed tree", "union find"
        ]
    }
    
    return patterns

# Example problem analysis
def analyze_sample_problem():
    """
    Ví dụ phân tích một bài toán mẫu
    """
    
    problem = """
    Given an array of n integers, find the maximum sum of 
    a contiguous subarray with at least k elements.
    
    Constraints: 1 ≤ n ≤ 10^5, 1 ≤ k ≤ n
    """
    
    analysis = {
        "problem_type": "Dynamic Programming / Sliding Window",
        "key_insights": [
            "Contiguous subarray → prefix sums",
            "At least k elements → sliding window",
            "Maximum sum → DP or greedy approach"
        ],
        "algorithm": "Sliding window with prefix sums",
        "complexity": "O(n)",
        "implementation_notes": [
            "Use prefix sums for range queries",
            "Maintain minimum prefix sum in window",
            "Handle edge case k = n"
        ]
    }
    
    return analysis
```

### Post-Contest Review Process

#### Systematic Review
```python
def post_contest_review(problems_attempted, results):
    """
    Process review sau contest
    """
    
    review_framework = {
        "Time Management": {
            "questions": [
                "Có phân bổ thời gian hợp lý không?",
                "Bài nào tốn thời gian quá nhiều?",
                "Có bỏ qua bài dễ để làm bài khó không?"
            ]
        },
        
        "Problem Selection": {
            "questions": [
                "Có chọn đúng thứ tự làm bài không?",
                "Có đánh giá đúng độ khó không?",
                "Có stuck ở bài nào quá lâu không?"
            ]
        },
        
        "Implementation": {
            "questions": [
                "Bug nào xuất hiện nhiều nhất?",
                "Code có clean và readable không?",
                "Có test đủ edge cases không?"
            ]
        },
        
        "Algorithm Knowledge": {
            "questions": [
                "Thuật toán nào cần ôn lại?",
                "Pattern nào chưa nhận ra?",
                "Optimization nào bị miss?"
            ]
        }
    }
    
    return review_framework

def improvement_plan(review_results):
    """
    Lập kế hoạch cải thiện dựa trên review
    """
    
    plan = {
        "Short term (1-2 days)": [
            "Ôn lại algorithms bị sai",
            "Practice similar problems",
            "Improve template code"
        ],
        
        "Medium term (1 week)": [
            "Strengthen weak areas",
            "Speed up implementation",
            "Better time management"
        ],
        
        "Long term (ongoing)": [
            "Expand algorithm knowledge",
            "Improve problem recognition",
            "Build contest experience"
        ]
    }
    
    return plan
```

## Key Takeaways

1. **Simulation thực tế**: Thi đúng 3 tiếng, không nghỉ giữa chừng
2. **Time management**: Phân bổ thời gian hợp lý cho từng bài
3. **Problem selection**: Làm bài dễ trước, khó sau
4. **Code quality**: Viết code clean, dễ debug
5. **Testing**: Test kỹ với sample và edge cases
6. **Stay calm**: Giữ bình tĩnh khi gặp khó khăn
7. **Review thoroughly**: Phân tích kỹ sau khi thi để cải thiện