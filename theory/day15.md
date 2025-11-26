# Day 15: Advanced Graph Problems

## Topological Sorting

### Khái niệm
Topological sorting là sắp xếp tuyến tính các đỉnh của DAG (Directed Acyclic Graph) sao cho với mọi cạnh u→v, u xuất hiện trước v trong thứ tự.

### DFS-based Topological Sort
```python
def topological_sort_dfs(graph):
    """
    Topological sort sử dụng DFS
    Time: O(V + E), Space: O(V)
    """
    visited = set()
    stack = []
    
    def dfs(vertex):
        visited.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(vertex)  # Add to stack after visiting all descendants
    
    # Visit all vertices
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    
    return stack[::-1]  # Reverse to get topological order

def topological_sort_with_cycle_detection(graph):
    """
    Topological sort với cycle detection
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {vertex: WHITE for vertex in graph}
    result = []
    
    def dfs(vertex):
        if color[vertex] == GRAY:
            return False  # Back edge found - cycle detected
        
        if color[vertex] == BLACK:
            return True  # Already processed
        
        color[vertex] = GRAY
        
        for neighbor in graph.get(vertex, []):
            if not dfs(neighbor):
                return False
        
        color[vertex] = BLACK
        result.append(vertex)
        return True
    
    # Process all vertices
    for vertex in graph:
        if color[vertex] == WHITE:
            if not dfs(vertex):
                return None  # Cycle detected
    
    return result[::-1]

# Test topological sort
graph_dag = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

topo_order = topological_sort_dfs(graph_dag)
print(f"Topological order: {topo_order}")

# Test with cycle detection
graph_with_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']  # Creates cycle
}

topo_cycle = topological_sort_with_cycle_detection(graph_with_cycle)
print(f"Topological order (with cycle): {topo_cycle}")
```

### BFS-based Topological Sort (Kahn's Algorithm)
```python
from collections import deque, defaultdict

def topological_sort_bfs(graph):
    """
    Kahn's algorithm - BFS-based topological sort
    """
    # Calculate in-degrees
    in_degree = defaultdict(int)
    vertices = set()
    
    for vertex in graph:
        vertices.add(vertex)
        for neighbor in graph[vertex]:
            vertices.add(neighbor)
            in_degree[neighbor] += 1
    
    # Initialize queue with vertices having in-degree 0
    queue = deque([v for v in vertices if in_degree[v] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Remove this vertex and update in-degrees
        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all vertices are processed (no cycle)
    if len(result) != len(vertices):
        return None  # Cycle detected
    
    return result

def all_topological_sorts(graph):
    """
    Tìm tất cả topological sorts có thể
    """
    # Calculate in-degrees
    in_degree = defaultdict(int)
    vertices = set()
    
    for vertex in graph:
        vertices.add(vertex)
        for neighbor in graph[vertex]:
            vertices.add(neighbor)
            in_degree[neighbor] += 1
    
    def backtrack(current_order, remaining_in_degree):
        if len(current_order) == len(vertices):
            all_orders.append(current_order[:])
            return
        
        # Find all vertices with in-degree 0
        candidates = [v for v in vertices 
                     if v not in current_order and remaining_in_degree[v] == 0]
        
        for candidate in candidates:
            # Choose candidate
            current_order.append(candidate)
            
            # Update in-degrees
            temp_changes = []
            for neighbor in graph.get(candidate, []):
                remaining_in_degree[neighbor] -= 1
                temp_changes.append(neighbor)
            
            # Recurse
            backtrack(current_order, remaining_in_degree)
            
            # Backtrack
            current_order.pop()
            for neighbor in temp_changes:
                remaining_in_degree[neighbor] += 1
    
    all_orders = []
    backtrack([], in_degree.copy())
    return all_orders

# Test Kahn's algorithm
topo_bfs = topological_sort_bfs(graph_dag)
print(f"Topological order (BFS): {topo_bfs}")

# Test all topological sorts
all_sorts = all_topological_sorts(graph_dag)
print(f"All topological sorts: {all_sorts}")
```

## Strongly Connected Components (SCC)

### Kosaraju's Algorithm
```python
def kosaraju_scc(graph):
    """
    Kosaraju's algorithm để tìm Strongly Connected Components
    Time: O(V + E), Space: O(V)
    """
    def dfs1(vertex, visited, stack):
        """First DFS to fill stack by finish time"""
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs1(neighbor, visited, stack)
        stack.append(vertex)
    
    def dfs2(vertex, visited, component, transpose_graph):
        """Second DFS on transpose graph"""
        visited.add(vertex)
        component.append(vertex)
        for neighbor in transpose_graph.get(vertex, []):
            if neighbor not in visited:
                dfs2(neighbor, visited, component, transpose_graph)
    
    # Step 1: Fill stack according to finish times
    visited = set()
    stack = []
    
    for vertex in graph:
        if vertex not in visited:
            dfs1(vertex, visited, stack)
    
    # Step 2: Create transpose graph
    transpose_graph = defaultdict(list)
    for vertex in graph:
        for neighbor in graph[vertex]:
            transpose_graph[neighbor].append(vertex)
    
    # Step 3: Process vertices in reverse finish time order
    visited = set()
    sccs = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component = []
            dfs2(vertex, visited, component, transpose_graph)
            sccs.append(component)
    
    return sccs

# Test Kosaraju
directed_graph = {
    'A': ['B'],
    'B': ['C', 'E', 'F'],
    'C': ['D', 'G'],
    'D': ['C', 'H'],
    'E': ['A', 'F'],
    'F': ['G'],
    'G': ['F'],
    'H': ['D', 'G']
}

sccs = kosaraju_scc(directed_graph)
print(f"Strongly Connected Components: {sccs}")
```

### Tarjan's Algorithm
```python
def tarjan_scc(graph):
    """
    Tarjan's algorithm để tìm SCC trong một lần DFS
    Time: O(V + E), Space: O(V)
    """
    index_counter = [0]
    stack = []
    lowlinks = {}
    index = {}
    on_stack = {}
    sccs = []
    
    def strongconnect(vertex):
        # Set depth index for vertex
        index[vertex] = index_counter[0]
        lowlinks[vertex] = index_counter[0]
        index_counter[0] += 1
        stack.append(vertex)
        on_stack[vertex] = True
        
        # Consider successors
        for neighbor in graph.get(vertex, []):
            if neighbor not in index:
                # Successor not yet visited; recurse
                strongconnect(neighbor)
                lowlinks[vertex] = min(lowlinks[vertex], lowlinks[neighbor])
            elif on_stack[neighbor]:
                # Successor is in stack and hence in current SCC
                lowlinks[vertex] = min(lowlinks[vertex], index[neighbor])
        
        # If vertex is root node, pop the stack and create SCC
        if lowlinks[vertex] == index[vertex]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == vertex:
                    break
            sccs.append(component)
    
    # Find SCCs for all vertices
    for vertex in graph:
        if vertex not in index:
            strongconnect(vertex)
    
    return sccs

def tarjan_bridges(graph):
    """
    Tarjan's algorithm để tìm bridges (cut edges)
    """
    time = [0]
    visited = set()
    disc = {}  # Discovery times
    low = {}   # Low values
    parent = {}
    bridges = []
    
    def bridge_dfs(u):
        visited.add(u)
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                bridge_dfs(v)
                
                # Check if subtree rooted at v has back edge
                low[u] = min(low[u], low[v])
                
                # If low value of v is more than discovery value of u,
                # then u-v is a bridge
                if low[v] > disc[u]:
                    bridges.append((u, v))
            
            elif v != parent.get(u):  # Back edge
                low[u] = min(low[u], disc[v])
    
    # Find bridges for all components
    for vertex in graph:
        if vertex not in visited:
            bridge_dfs(vertex)
    
    return bridges

# Test Tarjan's algorithms
sccs_tarjan = tarjan_scc(directed_graph)
print(f"SCCs (Tarjan): {sccs_tarjan}")

# Test bridge finding
undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'E'],
    'E': ['D']
}

bridges = tarjan_bridges(undirected_graph)
print(f"Bridges: {bridges}")
```

## Applications in Real Problems

### Course Scheduling
```python
def course_schedule(num_courses, prerequisites):
    """
    Course scheduling problem sử dụng topological sort
    """
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Kahn's algorithm
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    # Check if all courses can be taken
    if len(order) == num_courses:
        return order
    else:
        return None  # Impossible due to cycle

def find_course_order_all_possible(num_courses, prerequisites):
    """
    Tìm tất cả thứ tự có thể học courses
    """
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    def backtrack(current_order, remaining_in_degree):
        if len(current_order) == num_courses:
            all_orders.append(current_order[:])
            return
        
        # Find courses with no prerequisites
        available = [i for i in range(num_courses) 
                    if i not in current_order and remaining_in_degree[i] == 0]
        
        for course in available:
            current_order.append(course)
            
            # Update in-degrees
            temp_changes = []
            for next_course in graph[course]:
                remaining_in_degree[next_course] -= 1
                temp_changes.append(next_course)
            
            backtrack(current_order, remaining_in_degree)
            
            # Backtrack
            current_order.pop()
            for next_course in temp_changes:
                remaining_in_degree[next_course] += 1
    
    all_orders = []
    backtrack([], in_degree[:])
    return all_orders

# Test course scheduling
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
order = course_schedule(4, prerequisites)
print(f"Course order: {order}")
```

### Social Network Analysis
```python
def find_influential_users(graph):
    """
    Tìm users có ảnh hưởng trong social network
    Sử dụng SCC để tìm groups có ảnh hưởng lẫn nhau
    """
    sccs = tarjan_scc(graph)
    
    # Calculate influence score for each SCC
    scc_influence = []
    
    for i, scc in enumerate(sccs):
        # Influence = size of SCC + outgoing connections
        outgoing = set()
        for user in scc:
            for follower in graph.get(user, []):
                if follower not in scc:
                    outgoing.add(follower)
        
        influence_score = len(scc) * 2 + len(outgoing)
        scc_influence.append((influence_score, scc))
    
    # Sort by influence score
    scc_influence.sort(reverse=True)
    
    return scc_influence

def detect_echo_chambers(graph):
    """
    Phát hiện echo chambers (groups isolated from outside influence)
    """
    sccs = tarjan_scc(graph)
    echo_chambers = []
    
    for scc in sccs:
        if len(scc) > 1:  # Must have multiple users
            # Check if SCC has incoming edges from outside
            has_external_input = False
            
            for user in scc:
                # Check all possible incoming edges
                for other_user in graph:
                    if other_user not in scc and user in graph.get(other_user, []):
                        has_external_input = True
                        break
                
                if has_external_input:
                    break
            
            if not has_external_input:
                echo_chambers.append(scc)
    
    return echo_chambers

# Test social network analysis
social_graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David'],
    'Charlie': ['Alice', 'Eve'],
    'David': ['Bob'],
    'Eve': ['Charlie', 'Frank'],
    'Frank': ['Eve']
}

influential = find_influential_users(social_graph)
print(f"Influential users: {influential}")

echo_chambers = detect_echo_chambers(social_graph)
print(f"Echo chambers: {echo_chambers}")
```

### Dependency Resolution
```python
class DependencyResolver:
    """
    Dependency resolution system sử dụng topological sort
    """
    def __init__(self):
        self.dependencies = defaultdict(list)  # package -> [dependencies]
        self.dependents = defaultdict(list)    # package -> [dependents]
    
    def add_dependency(self, package, dependency):
        """Add dependency: package depends on dependency"""
        self.dependencies[package].append(dependency)
        self.dependents[dependency].append(package)
    
    def resolve_install_order(self, packages):
        """
        Resolve installation order for given packages
        """
        # Build subgraph for required packages and their dependencies
        required = set()
        queue = deque(packages)
        
        while queue:
            pkg = queue.popleft()
            if pkg not in required:
                required.add(pkg)
                queue.extend(self.dependencies[pkg])
        
        # Build dependency graph for required packages
        graph = {}
        for pkg in required:
            graph[pkg] = [dep for dep in self.dependencies[pkg] if dep in required]
        
        # Topological sort
        return topological_sort_bfs(graph)
    
    def find_circular_dependencies(self):
        """
        Tìm circular dependencies
        """
        # Try topological sort on full graph
        result = topological_sort_with_cycle_detection(self.dependencies)
        
        if result is None:
            # Find actual cycles using DFS
            visited = set()
            rec_stack = set()
            cycles = []
            
            def dfs(pkg, path):
                if pkg in rec_stack:
                    # Found cycle
                    cycle_start = path.index(pkg)
                    cycles.append(path[cycle_start:] + [pkg])
                    return
                
                if pkg in visited:
                    return
                
                visited.add(pkg)
                rec_stack.add(pkg)
                path.append(pkg)
                
                for dep in self.dependencies[pkg]:
                    dfs(dep, path)
                
                path.pop()
                rec_stack.remove(pkg)
            
            for pkg in self.dependencies:
                if pkg not in visited:
                    dfs(pkg, [])
            
            return cycles
        
        return []  # No cycles
    
    def impact_analysis(self, package):
        """
        Analyze impact of removing a package
        """
        affected = set()
        queue = deque([package])
        
        while queue:
            pkg = queue.popleft()
            if pkg not in affected:
                affected.add(pkg)
                queue.extend(self.dependents[pkg])
        
        return list(affected)

# Test dependency resolver
resolver = DependencyResolver()
resolver.add_dependency('app', 'framework')
resolver.add_dependency('framework', 'utils')
resolver.add_dependency('framework', 'logging')
resolver.add_dependency('utils', 'math')
resolver.add_dependency('logging', 'utils')

install_order = resolver.resolve_install_order(['app'])
print(f"Install order: {install_order}")

cycles = resolver.find_circular_dependencies()
print(f"Circular dependencies: {cycles}")

impact = resolver.impact_analysis('utils')
print(f"Impact of removing 'utils': {impact}")
```

### Build System Optimization
```python
def optimize_build_order(targets, dependencies, build_times):
    """
    Optimize build order để minimize total build time
    """
    # Create dependency graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for target, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(target)
            in_degree[target] += 1
    
    # Modified topological sort with build time consideration
    import heapq
    
    # Priority queue: (-build_time, target) - build longer tasks first when possible
    available = []
    for target in targets:
        if in_degree[target] == 0:
            heapq.heappush(available, (-build_times.get(target, 0), target))
    
    build_order = []
    total_time = 0
    
    while available:
        neg_time, target = heapq.heappop(available)
        build_order.append(target)
        total_time += -neg_time
        
        # Update dependencies
        for dependent in graph[target]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                heapq.heappush(available, (-build_times.get(dependent, 0), dependent))
    
    return build_order, total_time

def parallel_build_schedule(targets, dependencies, build_times, num_workers=4):
    """
    Schedule builds for parallel execution
    """
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for target, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(target)
            in_degree[target] += 1
    
    # Simulation of parallel build
    time = 0
    workers = [None] * num_workers  # (finish_time, target)
    available = deque([t for t in targets if in_degree[t] == 0])
    completed = set()
    schedule = []
    
    while available or any(w is not None for w in workers):
        # Check for completed builds
        for i in range(num_workers):
            if workers[i] and workers[i][0] <= time:
                finish_time, target = workers[i]
                workers[i] = None
                completed.add(target)
                
                # Update dependencies
                for dependent in graph[target]:
                    in_degree[dependent] -= 1
                    if in_degree[dependent] == 0:
                        available.append(dependent)
        
        # Assign new builds to free workers
        for i in range(num_workers):
            if workers[i] is None and available:
                target = available.popleft()
                build_time = build_times.get(target, 1)
                workers[i] = (time + build_time, target)
                schedule.append((time, target, i))
        
        # Advance time
        if any(w is not None for w in workers):
            time = min(w[0] for w in workers if w is not None)
        else:
            time += 1
    
    return schedule, time

# Test build optimization
targets = ['main', 'lib1', 'lib2', 'utils', 'tests']
dependencies = {
    'main': ['lib1', 'lib2'],
    'lib1': ['utils'],
    'lib2': ['utils'],
    'tests': ['main'],
    'utils': []
}
build_times = {
    'main': 5,
    'lib1': 3,
    'lib2': 4,
    'utils': 2,
    'tests': 1
}

build_order, total_time = optimize_build_order(targets, dependencies, build_times)
print(f"Optimized build order: {build_order}")
print(f"Total build time: {total_time}")

schedule, parallel_time = parallel_build_schedule(targets, dependencies, build_times, 2)
print(f"Parallel schedule: {schedule}")
print(f"Parallel build time: {parallel_time}")
```

## Advanced Techniques

### Condensation Graph
```python
def build_condensation_graph(graph):
    """
    Build condensation graph từ SCCs
    """
    sccs = tarjan_scc(graph)
    
    # Map each vertex to its SCC index
    vertex_to_scc = {}
    for i, scc in enumerate(sccs):
        for vertex in scc:
            vertex_to_scc[vertex] = i
    
    # Build condensation graph
    condensation = defaultdict(set)
    
    for vertex in graph:
        scc_u = vertex_to_scc[vertex]
        for neighbor in graph[vertex]:
            scc_v = vertex_to_scc[neighbor]
            if scc_u != scc_v:
                condensation[scc_u].add(scc_v)
    
    # Convert sets to lists
    condensation_graph = {scc: list(neighbors) for scc, neighbors in condensation.items()}
    
    return condensation_graph, sccs

# Test condensation graph
condensation, sccs = build_condensation_graph(directed_graph)
print(f"SCCs: {sccs}")
print(f"Condensation graph: {condensation}")
```

## Best Practices

1. **Choose Right Algorithm**: DFS vs BFS topological sort
2. **Handle Cycles**: Always check for cycles in DAG algorithms
3. **Optimize for Use Case**: Single vs multiple queries
4. **Memory Management**: Use iterative DFS for large graphs
5. **Preprocessing**: Build auxiliary structures when needed
6. **Error Handling**: Validate input graph properties
7. **Performance Monitoring**: Track algorithm performance on real data