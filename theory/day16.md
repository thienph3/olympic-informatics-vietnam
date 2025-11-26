# Day 16: Mixed Algorithm Problems

## Combination of All Algorithms

### Problem Classification Framework
```python
def classify_problem(problem_description):
    """
    Framework để classify loại problem và chọn algorithm phù hợp
    """
    
    problem_types = {
        "Dynamic Programming": {
            "keywords": ["optimal", "maximum", "minimum", "count ways", "subsequence"],
            "patterns": ["overlapping subproblems", "optimal substructure"],
            "examples": ["knapsack", "LIS", "LCS", "coin change"]
        },
        
        "Greedy": {
            "keywords": ["activity selection", "scheduling", "minimum spanning tree"],
            "patterns": ["greedy choice property", "local optimum"],
            "examples": ["fractional knapsack", "Huffman coding", "Dijkstra"]
        },
        
        "Graph Algorithms": {
            "keywords": ["path", "connectivity", "cycle", "tree", "network"],
            "patterns": ["vertices and edges", "traversal", "shortest path"],
            "examples": ["BFS", "DFS", "topological sort", "MST"]
        },
        
        "Backtracking": {
            "keywords": ["all solutions", "permutations", "combinations", "N-Queens"],
            "patterns": ["try all possibilities", "constraint satisfaction"],
            "examples": ["sudoku", "word search", "subset generation"]
        },
        
        "Divide and Conquer": {
            "keywords": ["merge", "split", "recursive"],
            "patterns": ["divide problem", "conquer subproblems", "combine results"],
            "examples": ["merge sort", "quick sort", "binary search"]
        }
    }
    
    return problem_types

def algorithm_selection_guide():
    """
    Hướng dẫn chọn algorithm dựa trên đặc điểm bài toán
    """
    
    decision_tree = {
        "Is it an optimization problem?": {
            "Yes": {
                "Does it have optimal substructure?": {
                    "Yes": {
                        "Are there overlapping subproblems?": {
                            "Yes": "Dynamic Programming",
                            "No": "Divide and Conquer or Greedy"
                        }
                    },
                    "No": "Greedy (if greedy choice property holds)"
                }
            },
            "No": {
                "Do you need all solutions?": {
                    "Yes": "Backtracking",
                    "No": {
                        "Is it a graph problem?": {
                            "Yes": "Graph Algorithms (BFS/DFS/etc)",
                            "No": "Depends on specific requirements"
                        }
                    }
                }
            }
        }
    }
    
    return decision_tree
```

### Multi-Algorithm Problem Examples

#### Problem 1: Robot Path with Obstacles
```python
def robot_path_multi_approach(grid, start, end):
    """
    Robot path problem - có thể giải bằng nhiều cách
    """
    
    # Approach 1: BFS (shortest path in unweighted grid)
    def bfs_approach():
        from collections import deque
        
        rows, cols = len(grid), len(grid[0])
        queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
        visited = {start}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col, dist = queue.popleft()
            
            if (row, col) == end:
                return dist
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < rows and 0 <= new_col < cols and
                    (new_row, new_col) not in visited and
                    grid[new_row][new_col] == 0):  # 0 = free, 1 = obstacle
                    
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, dist + 1))
        
        return -1  # No path
    
    # Approach 2: Dynamic Programming (count all paths)
    def dp_approach():
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        
        # Base case
        if grid[start[0]][start[1]] == 0:
            dp[start[0]][start[1]] = 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # Obstacle
                    continue
                
                # Can come from top
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                
                # Can come from left
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[end[0]][end[1]]
    
    # Approach 3: A* (heuristic search)
    def a_star_approach():
        import heapq
        
        def heuristic(pos):
            return abs(pos[0] - end[0]) + abs(pos[1] - end[1])
        
        rows, cols = len(grid), len(grid[0])
        open_set = [(heuristic(start), 0, start)]  # (f_score, g_score, position)
        g_score = {start: 0}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while open_set:
            f, g, (row, col) = heapq.heappop(open_set)
            
            if (row, col) == end:
                return g
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                new_pos = (new_row, new_col)
                
                if (0 <= new_row < rows and 0 <= new_col < cols and
                    grid[new_row][new_col] == 0):
                    
                    tentative_g = g + 1
                    
                    if new_pos not in g_score or tentative_g < g_score[new_pos]:
                        g_score[new_pos] = tentative_g
                        f_score = tentative_g + heuristic(new_pos)
                        heapq.heappush(open_set, (f_score, tentative_g, new_pos))
        
        return -1
    
    return {
        "BFS (shortest path)": bfs_approach(),
        "DP (count paths)": dp_approach(),
        "A* (heuristic)": a_star_approach()
    }

# Test robot path
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

results = robot_path_multi_approach(grid, (0, 0), (3, 3))
print("Robot path results:", results)
```

#### Problem 2: Stock Trading with Multiple Constraints
```python
def stock_trading_multi_constraint(prices, max_transactions=None, cooldown=False, fee=0):
    """
    Stock trading problem với multiple constraints
    Có thể giải bằng DP với different states
    """
    
    if not prices:
        return 0
    
    n = len(prices)
    
    # Approach 1: Unlimited transactions, no cooldown, no fee
    def unlimited_simple():
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
    # Approach 2: With cooldown
    def with_cooldown():
        if n <= 1:
            return 0
        
        # States: held, sold, rest
        held = [0] * n
        sold = [0] * n
        rest = [0] * n
        
        held[0] = -prices[0]
        
        for i in range(1, n):
            held[i] = max(held[i-1], rest[i-1] - prices[i])
            sold[i] = held[i-1] + prices[i]
            rest[i] = max(rest[i-1], sold[i-1])
        
        return max(sold[n-1], rest[n-1])
    
    # Approach 3: With transaction fee
    def with_fee():
        if n <= 1:
            return 0
        
        buy = -prices[0]
        sell = 0
        
        for i in range(1, n):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        
        return sell
    
    # Approach 4: Limited transactions
    def limited_transactions(k):
        if k >= n // 2:
            return unlimited_simple()
        
        # DP with k transactions
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        
        for price in prices:
            for j in range(k, 0, -1):
                sell[j] = max(sell[j], buy[j] + price)
                buy[j] = max(buy[j], sell[j-1] - price)
        
        return sell[k]
    
    # Choose appropriate approach based on constraints
    if max_transactions is None and not cooldown and fee == 0:
        return unlimited_simple()
    elif cooldown and max_transactions is None:
        return with_cooldown()
    elif fee > 0 and max_transactions is None:
        return with_fee()
    elif max_transactions is not None:
        return limited_transactions(max_transactions)
    else:
        # Complex case - combine multiple constraints
        # This would require more sophisticated DP state design
        return 0

# Test stock trading
prices = [7, 1, 5, 3, 6, 4]
print(f"Unlimited transactions: {stock_trading_multi_constraint(prices)}")
print(f"With cooldown: {stock_trading_multi_constraint(prices, cooldown=True)}")
print(f"With fee: {stock_trading_multi_constraint(prices, fee=2)}")
print(f"Max 2 transactions: {stock_trading_multi_constraint(prices, max_transactions=2)}")
```

#### Problem 3: Network Flow with Multiple Objectives
```python
def network_flow_multi_objective(graph, source, sink, objectives):
    """
    Network flow với multiple objectives: max flow, min cost, min latency
    """
    
    # Approach 1: Maximum Flow (Ford-Fulkerson with BFS)
    def max_flow():
        from collections import deque
        
        def bfs_find_path():
            visited = set([source])
            queue = deque([(source, [source])])
            
            while queue:
                node, path = queue.popleft()
                
                for neighbor, capacity in graph[node].items():
                    if neighbor not in visited and capacity > 0:
                        new_path = path + [neighbor]
                        if neighbor == sink:
                            return new_path
                        
                        visited.add(neighbor)
                        queue.append((neighbor, new_path))
            
            return None
        
        max_flow_value = 0
        
        while True:
            path = bfs_find_path()
            if not path:
                break
            
            # Find bottleneck capacity
            flow = float('inf')
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                flow = min(flow, graph[u][v])
            
            # Update residual capacities
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                graph[u][v] -= flow
                if v not in graph:
                    graph[v] = {}
                graph[v][u] = graph[v].get(u, 0) + flow
            
            max_flow_value += flow
        
        return max_flow_value
    
    # Approach 2: Minimum Cost Flow
    def min_cost_flow(demand):
        # Simplified min cost flow using successive shortest paths
        import heapq
        
        def dijkstra_with_potentials():
            dist = {node: float('inf') for node in graph}
            dist[source] = 0
            pq = [(0, source)]
            parent = {}
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > dist[u]:
                    continue
                
                for v, (capacity, cost) in graph[u].items():
                    if capacity > 0:
                        new_dist = dist[u] + cost
                        if new_dist < dist[v]:
                            dist[v] = new_dist
                            parent[v] = u
                            heapq.heappush(pq, (new_dist, v))
            
            return dist, parent
        
        total_cost = 0
        remaining_demand = demand
        
        while remaining_demand > 0:
            dist, parent = dijkstra_with_potentials()
            
            if dist[sink] == float('inf'):
                break  # No more augmenting paths
            
            # Reconstruct path
            path = []
            current = sink
            while current != source:
                path.append(current)
                current = parent[current]
            path.append(source)
            path.reverse()
            
            # Find bottleneck
            flow = remaining_demand
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                flow = min(flow, graph[u][v][0])  # capacity
            
            # Update graph and cost
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                capacity, cost = graph[u][v]
                graph[u][v] = (capacity - flow, cost)
                
                if v not in graph:
                    graph[v] = {}
                if u not in graph[v]:
                    graph[v][u] = (0, -cost)
                
                old_capacity, old_cost = graph[v][u]
                graph[v][u] = (old_capacity + flow, old_cost)
            
            total_cost += flow * dist[sink]
            remaining_demand -= flow
        
        return total_cost
    
    # Choose approach based on objectives
    results = {}
    
    if 'max_flow' in objectives:
        # Make a copy of graph for max flow
        graph_copy = {u: dict(neighbors) for u, neighbors in graph.items()}
        results['max_flow'] = max_flow()
    
    if 'min_cost' in objectives:
        # Assuming graph has (capacity, cost) tuples
        results['min_cost'] = min_cost_flow(objectives.get('demand', 1))
    
    return results

# Test network flow (simplified example)
flow_graph = {
    'S': {'A': 10, 'B': 8},
    'A': {'B': 5, 'T': 10},
    'B': {'T': 10},
    'T': {}
}

# flow_results = network_flow_multi_objective(flow_graph, 'S', 'T', ['max_flow'])
# print("Network flow results:", flow_results)
```

### Algorithm Combination Strategies

#### Strategy 1: Preprocessing + Main Algorithm
```python
def two_phase_solution(data, query_type):
    """
    Two-phase approach: preprocessing + query answering
    """
    
    # Phase 1: Preprocessing
    def preprocess_for_range_queries(arr):
        """Preprocess array for range sum queries"""
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        
        return prefix_sum
    
    def preprocess_for_lca(tree, root):
        """Preprocess tree for LCA queries using binary lifting"""
        n = len(tree)
        LOG = 20  # log2(max_n)
        
        # Binary lifting table
        up = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        
        def dfs(v, p, d):
            up[v][0] = p
            depth[v] = d
            
            for i in range(1, LOG):
                if up[v][i-1] != -1:
                    up[v][i] = up[up[v][i-1]][i-1]
            
            for u in tree[v]:
                if u != p:
                    dfs(u, v, d + 1)
        
        dfs(root, -1, 0)
        return up, depth
    
    # Phase 2: Query answering
    def answer_range_query(prefix_sum, left, right):
        """Answer range sum query in O(1)"""
        return prefix_sum[right + 1] - prefix_sum[left]
    
    def answer_lca_query(up, depth, u, v):
        """Answer LCA query in O(log n)"""
        if depth[u] < depth[v]:
            u, v = v, u
        
        # Bring u to same level as v
        diff = depth[u] - depth[v]
        for i in range(20):
            if (diff >> i) & 1:
                u = up[u][i]
        
        if u == v:
            return u
        
        # Binary search for LCA
        for i in range(19, -1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        
        return up[u][0]
    
    if query_type == "range_sum":
        preprocessed = preprocess_for_range_queries(data)
        return lambda l, r: answer_range_query(preprocessed, l, r)
    elif query_type == "lca":
        tree, root = data
        up, depth = preprocess_for_lca(tree, root)
        return lambda u, v: answer_lca_query(up, depth, u, v)

# Test two-phase solution
arr = [1, 3, 5, 7, 9, 11]
range_query_func = two_phase_solution(arr, "range_sum")
print(f"Range sum [1, 3]: {range_query_func(1, 3)}")  # 3 + 5 + 7 = 15
```

#### Strategy 2: Hybrid Algorithms
```python
def hybrid_sorting_algorithm(arr, threshold=10):
    """
    Hybrid sorting: Quick sort + Insertion sort
    """
    
    def insertion_sort(arr, left, right):
        """Insertion sort for small subarrays"""
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
    
    def partition(arr, left, right):
        """Partition for quicksort"""
        pivot = arr[right]
        i = left - 1
        
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
    
    def hybrid_quick_sort(arr, left, right):
        """Hybrid quicksort with insertion sort for small subarrays"""
        if left < right:
            if right - left + 1 <= threshold:
                insertion_sort(arr, left, right)
            else:
                pi = partition(arr, left, right)
                hybrid_quick_sort(arr, left, pi - 1)
                hybrid_quick_sort(arr, pi + 1, right)
    
    hybrid_quick_sort(arr, 0, len(arr) - 1)
    return arr

def adaptive_algorithm_selection(problem_size, problem_type):
    """
    Adaptively choose algorithm based on problem characteristics
    """
    
    if problem_type == "sorting":
        if problem_size < 50:
            return "insertion_sort"
        elif problem_size < 1000:
            return "quick_sort"
        else:
            return "merge_sort"
    
    elif problem_type == "shortest_path":
        if problem_size < 100:
            return "floyd_warshall"
        else:
            return "dijkstra"
    
    elif problem_type == "string_matching":
        if problem_size < 1000:
            return "naive"
        else:
            return "kmp"
    
    return "default"

# Test hybrid sorting
test_arr = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_arr = hybrid_sorting_algorithm(test_arr.copy())
print(f"Hybrid sorted: {sorted_arr}")
```

### Performance Analysis Framework

```python
import time
import random

class AlgorithmBenchmark:
    """
    Framework để benchmark và compare algorithms
    """
    
    def __init__(self):
        self.results = {}
    
    def benchmark_algorithm(self, algorithm, data_generator, sizes, iterations=5):
        """
        Benchmark algorithm với different input sizes
        """
        results = []
        
        for size in sizes:
            times = []
            
            for _ in range(iterations):
                data = data_generator(size)
                
                start_time = time.time()
                algorithm(data)
                end_time = time.time()
                
                times.append(end_time - start_time)
            
            avg_time = sum(times) / len(times)
            results.append((size, avg_time))
        
        return results
    
    def compare_algorithms(self, algorithms, data_generator, sizes):
        """
        Compare multiple algorithms
        """
        comparison = {}
        
        for name, algorithm in algorithms.items():
            comparison[name] = self.benchmark_algorithm(algorithm, data_generator, sizes)
        
        return comparison
    
    def analyze_complexity(self, results):
        """
        Analyze time complexity from benchmark results
        """
        analysis = {}
        
        for name, data in results.items():
            if len(data) >= 2:
                # Simple complexity analysis
                size1, time1 = data[0]
                size2, time2 = data[-1]
                
                if time1 > 0:
                    ratio = (time2 / time1) / (size2 / size1)
                    
                    if ratio < 1.5:
                        complexity = "O(n)"
                    elif ratio < 3:
                        complexity = "O(n log n)"
                    elif ratio < 10:
                        complexity = "O(n²)"
                    else:
                        complexity = "O(n³) or worse"
                    
                    analysis[name] = complexity
        
        return analysis

# Test benchmark framework
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def random_array_generator(size):
    return [random.randint(1, 1000) for _ in range(size)]

# benchmark = AlgorithmBenchmark()
# algorithms = {
#     "bubble_sort": bubble_sort,
#     "quick_sort": quick_sort
# }
# 
# results = benchmark.compare_algorithms(algorithms, random_array_generator, [10, 50, 100])
# complexity_analysis = benchmark.analyze_complexity(results)
# print("Complexity analysis:", complexity_analysis)
```

### Real-World Problem Integration

```python
def solve_complex_optimization_problem(constraints, objectives, data):
    """
    Solve complex real-world problem using multiple algorithms
    """
    
    # Step 1: Problem decomposition
    def decompose_problem(constraints):
        subproblems = []
        
        if "graph" in constraints:
            subproblems.append("graph_optimization")
        
        if "scheduling" in constraints:
            subproblems.append("scheduling_optimization")
        
        if "resource_allocation" in constraints:
            subproblems.append("allocation_optimization")
        
        return subproblems
    
    # Step 2: Algorithm selection for each subproblem
    def select_algorithms(subproblems):
        algorithm_map = {
            "graph_optimization": ["dijkstra", "mst", "max_flow"],
            "scheduling_optimization": ["topological_sort", "greedy"],
            "allocation_optimization": ["dp", "linear_programming"]
        }
        
        selected = {}
        for subproblem in subproblems:
            selected[subproblem] = algorithm_map.get(subproblem, ["heuristic"])
        
        return selected
    
    # Step 3: Solve subproblems
    def solve_subproblems(selected_algorithms, data):
        solutions = {}
        
        for subproblem, algorithms in selected_algorithms.items():
            # Try multiple algorithms and pick best result
            best_solution = None
            best_score = float('-inf')
            
            for algorithm in algorithms:
                try:
                    solution = apply_algorithm(algorithm, data[subproblem])
                    score = evaluate_solution(solution, objectives)
                    
                    if score > best_score:
                        best_score = score
                        best_solution = solution
                
                except Exception as e:
                    print(f"Algorithm {algorithm} failed: {e}")
                    continue
            
            solutions[subproblem] = best_solution
        
        return solutions
    
    # Step 4: Combine solutions
    def combine_solutions(solutions):
        # This would depend on specific problem structure
        combined_score = 0
        combined_solution = {}
        
        for subproblem, solution in solutions.items():
            if solution:
                combined_solution[subproblem] = solution
                combined_score += evaluate_solution(solution, objectives)
        
        return combined_solution, combined_score
    
    def apply_algorithm(algorithm, data):
        # Placeholder for actual algorithm implementations
        return f"Solution using {algorithm}"
    
    def evaluate_solution(solution, objectives):
        # Placeholder for solution evaluation
        return random.random()
    
    # Execute the pipeline
    subproblems = decompose_problem(constraints)
    selected_algorithms = select_algorithms(subproblems)
    solutions = solve_subproblems(selected_algorithms, data)
    final_solution, score = combine_solutions(solutions)
    
    return {
        "solution": final_solution,
        "score": score,
        "subproblems": subproblems,
        "algorithms_used": selected_algorithms
    }

# Test complex problem solving
constraints = ["graph", "scheduling", "resource_allocation"]
objectives = ["minimize_cost", "maximize_efficiency"]
data = {
    "graph_optimization": {"nodes": 100, "edges": 500},
    "scheduling_optimization": {"tasks": 50, "dependencies": 20},
    "allocation_optimization": {"resources": 10, "demands": 30}
}

result = solve_complex_optimization_problem(constraints, objectives, data)
print("Complex problem result:", result)
```

## Best Practices for Mixed Problems

1. **Problem Analysis**: Thoroughly understand problem requirements
2. **Algorithm Selection**: Choose appropriate algorithms for each component
3. **Modular Design**: Break complex problems into manageable pieces
4. **Performance Monitoring**: Benchmark different approaches
5. **Error Handling**: Gracefully handle algorithm failures
6. **Scalability**: Consider how solution scales with input size
7. **Maintainability**: Write clean, documented code for complex solutions