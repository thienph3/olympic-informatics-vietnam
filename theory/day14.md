# Day 14: Union-Find & MST

## Union-Find Data Structure

### Khái niệm
Union-Find (Disjoint Set Union) là cấu trúc dữ liệu để quản lý các tập hợp rời rạc với hai operations chính: Union (hợp) và Find (tìm).

### Basic Implementation
```python
class UnionFind:
    def __init__(self, n):
        """
        Initialize Union-Find với n elements (0 to n-1)
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        """
        Find root của element x
        Time: O(α(n)) với path compression
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union hai sets chứa x và y
        Time: O(α(n)) với union by rank
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.components -= 1
        return True
    
    def connected(self, x, y):
        """Kiểm tra x và y có trong cùng set không"""
        return self.find(x) == self.find(y)
    
    def get_components(self):
        """Trả về số lượng components"""
        return self.components
    
    def get_component_size(self, x):
        """Lấy size của component chứa x"""
        root = self.find(x)
        return sum(1 for i in range(len(self.parent)) if self.find(i) == root)

# Test Union-Find
uf = UnionFind(6)
print(f"Initial components: {uf.get_components()}")

uf.union(0, 1)
uf.union(2, 3)
uf.union(1, 2)
print(f"After unions: {uf.get_components()}")
print(f"0 and 3 connected: {uf.connected(0, 3)}")
print(f"Component size of 0: {uf.get_component_size(0)}")
```

## Path Compression và Union by Rank

### Path Compression Variants
```python
class UnionFindOptimized:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n  # Size of each component
        self.components = n
    
    def find_iterative(self, x):
        """
        Iterative path compression
        Tránh recursion stack overflow
        """
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        
        # Path compression
        while self.parent[x] != x:
            next_x = self.parent[x]
            self.parent[x] = root
            x = next_x
        
        return root
    
    def find_path_halving(self, x):
        """
        Path halving - lighter version of path compression
        """
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union_by_size(self, x, y):
        """
        Union by size thay vì rank
        """
        root_x = self.find_iterative(x)
        root_y = self.find_iterative(y)
        
        if root_x == root_y:
            return False
        
        # Union by size - attach smaller tree to larger
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        
        self.components -= 1
        return True
    
    def get_all_components(self):
        """Trả về dictionary {root: [members]}"""
        components = {}
        for i in range(len(self.parent)):
            root = self.find_iterative(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        return components

# Performance comparison
import time

def compare_union_find_performance():
    n = 100000
    operations = [(i, (i + 1) % n) for i in range(n // 2)]
    
    # Basic Union-Find
    uf1 = UnionFind(n)
    start = time.time()
    for x, y in operations:
        uf1.union(x, y)
    time1 = time.time() - start
    
    # Optimized Union-Find
    uf2 = UnionFindOptimized(n)
    start = time.time()
    for x, y in operations:
        uf2.union_by_size(x, y)
    time2 = time.time() - start
    
    print(f"Basic UF: {time1:.4f}s")
    print(f"Optimized UF: {time2:.4f}s")

# compare_union_find_performance()
```

### Weighted Union-Find
```python
class WeightedUnionFind:
    """
    Union-Find với weights - useful cho distance queries
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.weight = [0] * n  # Weight from node to its parent
        self.components = n
    
    def find(self, x):
        """Find với weight calculation"""
        if self.parent[x] != x:
            original_parent = self.parent[x]
            self.parent[x] = self.find(original_parent)
            self.weight[x] += self.weight[original_parent]
        return self.parent[x]
    
    def union(self, x, y, w):
        """
        Union với weight w từ x đến y
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Make root_y parent of root_x
        self.parent[root_x] = root_y
        self.weight[root_x] = self.weight[y] - self.weight[x] + w
        self.components -= 1
        return True
    
    def get_distance(self, x, y):
        """Lấy distance từ x đến y nếu connected"""
        if self.find(x) != self.find(y):
            return None  # Not connected
        
        return self.weight[x] - self.weight[y]

# Test weighted Union-Find
wuf = WeightedUnionFind(5)
wuf.union(0, 1, 3)  # Distance from 0 to 1 is 3
wuf.union(1, 2, 2)  # Distance from 1 to 2 is 2
print(f"Distance 0->2: {wuf.get_distance(0, 2)}")  # Should be 5
```

## Kruskal's Algorithm

### Basic Kruskal Implementation
```python
def kruskal_mst(edges, n):
    """
    Kruskal's algorithm để tìm Minimum Spanning Tree
    Time: O(E log E), Space: O(V)
    
    edges: list of (weight, u, v)
    n: number of vertices (0 to n-1)
    """
    # Sort edges by weight
    edges.sort()
    
    uf = UnionFind(n)
    mst_edges = []
    mst_weight = 0
    
    for weight, u, v in edges:
        # If u and v are not connected, add this edge
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            mst_weight += weight
            
            # Early termination: MST has exactly n-1 edges
            if len(mst_edges) == n - 1:
                break
    
    return mst_edges, mst_weight

# Test Kruskal
edges = [
    (1, 0, 1), (2, 0, 2), (3, 1, 2),
    (4, 1, 3), (5, 2, 3), (6, 2, 4),
    (7, 3, 4)
]
n = 5

mst_edges, mst_weight = kruskal_mst(edges, n)
print(f"MST edges: {mst_edges}")
print(f"MST weight: {mst_weight}")
```

### Kruskal with Edge Objects
```python
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __repr__(self):
        return f"Edge({self.u}, {self.v}, {self.weight})"

def kruskal_mst_objects(edges, n):
    """
    Kruskal với Edge objects
    """
    edges.sort()  # Sort by weight using __lt__
    
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for edge in edges:
        if uf.union(edge.u, edge.v):
            mst.append(edge)
            total_weight += edge.weight
            
            if len(mst) == n - 1:
                break
    
    return mst, total_weight

def build_graph_from_edges(edges):
    """Convert edge list to adjacency list"""
    graph = {}
    for edge in edges:
        if edge.u not in graph:
            graph[edge.u] = []
        if edge.v not in graph:
            graph[edge.v] = []
        
        graph[edge.u].append((edge.v, edge.weight))
        graph[edge.v].append((edge.u, edge.weight))
    
    return graph

# Test with Edge objects
edge_objects = [
    Edge(0, 1, 1), Edge(0, 2, 2), Edge(1, 2, 3),
    Edge(1, 3, 4), Edge(2, 3, 5), Edge(2, 4, 6),
    Edge(3, 4, 7)
]

mst, weight = kruskal_mst_objects(edge_objects, 5)
print(f"MST: {mst}")
print(f"Total weight: {weight}")
```

## Prim's Algorithm for MST

### Basic Prim Implementation
```python
import heapq

def prim_mst(graph, start=0):
    """
    Prim's algorithm để tìm MST
    Time: O(E log V), Space: O(V)
    
    graph: adjacency list {u: [(v, weight), ...]}
    """
    if not graph:
        return [], 0
    
    vertices = set(graph.keys())
    visited = {start}
    mst_edges = []
    total_weight = 0
    
    # Priority queue: (weight, u, v)
    pq = []
    for neighbor, weight in graph[start]:
        heapq.heappush(pq, (weight, start, neighbor))
    
    while pq and len(visited) < len(vertices):
        weight, u, v = heapq.heappop(pq)
        
        if v in visited:
            continue
        
        # Add edge to MST
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight
        
        # Add new edges from v
        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, v, neighbor))
    
    return mst_edges, total_weight

def prim_mst_matrix(matrix):
    """
    Prim's algorithm với adjacency matrix
    Time: O(V²), Space: O(V)
    Tốt cho dense graphs
    """
    n = len(matrix)
    visited = [False] * n
    key = [float('inf')] * n  # Minimum weight to connect to MST
    parent = [-1] * n
    
    key[0] = 0  # Start from vertex 0
    mst_weight = 0
    mst_edges = []
    
    for _ in range(n):
        # Find minimum key vertex not yet in MST
        min_key = float('inf')
        min_vertex = -1
        
        for v in range(n):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                min_vertex = v
        
        visited[min_vertex] = True
        mst_weight += key[min_vertex]
        
        if parent[min_vertex] != -1:
            mst_edges.append((parent[min_vertex], min_vertex, key[min_vertex]))
        
        # Update keys of adjacent vertices
        for v in range(n):
            if (not visited[v] and matrix[min_vertex][v] != 0 and
                matrix[min_vertex][v] < key[v]):
                key[v] = matrix[min_vertex][v]
                parent[v] = min_vertex
    
    return mst_edges, mst_weight

# Test Prim
graph_prim = {
    0: [(1, 1), (2, 2)],
    1: [(0, 1), (2, 3), (3, 4)],
    2: [(0, 2), (1, 3), (3, 5), (4, 6)],
    3: [(1, 4), (2, 5), (4, 7)],
    4: [(2, 6), (3, 7)]
}

mst_prim, weight_prim = prim_mst(graph_prim)
print(f"Prim MST: {mst_prim}")
print(f"Prim weight: {weight_prim}")
```

### Prim vs Kruskal Comparison
```python
def compare_mst_algorithms():
    """
    So sánh Prim vs Kruskal
    """
    comparison = {
        "Time Complexity": {
            "Kruskal": "O(E log E) = O(E log V)",
            "Prim (binary heap)": "O(E log V)",
            "Prim (matrix)": "O(V²)"
        },
        "Space Complexity": {
            "Kruskal": "O(V) for Union-Find",
            "Prim": "O(V) for priority queue"
        },
        "Best for": {
            "Kruskal": "Sparse graphs (E << V²)",
            "Prim": "Dense graphs (E ≈ V²)"
        },
        "Data Structure": {
            "Kruskal": "Union-Find + Edge sorting",
            "Prim": "Priority queue + Visited set"
        },
        "Edge Processing": {
            "Kruskal": "Process all edges globally",
            "Prim": "Process edges locally from current MST"
        }
    }
    
    return comparison

def when_to_use_which():
    """
    Hướng dẫn khi nào dùng algorithm nào
    """
    guidelines = {
        "Use Kruskal when": [
            "Graph is sparse (few edges)",
            "Edges are given as list",
            "Need to detect cycles",
            "Working with Union-Find anyway"
        ],
        "Use Prim when": [
            "Graph is dense (many edges)",
            "Graph given as adjacency list/matrix",
            "Need MST starting from specific vertex",
            "Memory is limited"
        ]
    }
    
    return guidelines
```

## Advanced Union-Find Applications

### Dynamic Connectivity
```python
class DynamicConnectivity:
    """
    Dynamic connectivity với Union-Find
    Support add edge, remove edge, query connectivity
    """
    def __init__(self, n):
        self.n = n
        self.uf = UnionFind(n)
        self.edges = set()
    
    def add_edge(self, u, v):
        """Add edge u-v"""
        if (u, v) not in self.edges and (v, u) not in self.edges:
            self.edges.add((u, v))
            self.uf.union(u, v)
    
    def remove_edge(self, u, v):
        """
        Remove edge u-v
        Note: Naive implementation - rebuild UF
        """
        if (u, v) in self.edges:
            self.edges.remove((u, v))
        elif (v, u) in self.edges:
            self.edges.remove((v, u))
        else:
            return  # Edge doesn't exist
        
        # Rebuild Union-Find from remaining edges
        self.uf = UnionFind(self.n)
        for edge_u, edge_v in self.edges:
            self.uf.union(edge_u, edge_v)
    
    def connected(self, u, v):
        """Check if u and v are connected"""
        return self.uf.connected(u, v)
    
    def components_count(self):
        """Get number of connected components"""
        return self.uf.get_components()

# Test dynamic connectivity
dc = DynamicConnectivity(5)
dc.add_edge(0, 1)
dc.add_edge(2, 3)
print(f"Components: {dc.components_count()}")  # 3
print(f"0-3 connected: {dc.connected(0, 3)}")  # False

dc.add_edge(1, 2)
print(f"0-3 connected: {dc.connected(0, 3)}")  # True

dc.remove_edge(1, 2)
print(f"0-3 connected: {dc.connected(0, 3)}")  # False
```

### Cycle Detection
```python
def has_cycle_undirected(edges, n):
    """
    Detect cycle trong undirected graph bằng Union-Find
    """
    uf = UnionFind(n)
    
    for u, v in edges:
        if uf.connected(u, v):
            return True  # Cycle found
        uf.union(u, v)
    
    return False

def find_cycle_edges(edges, n):
    """
    Tìm tất cả edges tạo thành cycle
    """
    uf = UnionFind(n)
    cycle_edges = []
    
    for u, v in edges:
        if uf.connected(u, v):
            cycle_edges.append((u, v))
        else:
            uf.union(u, v)
    
    return cycle_edges

# Test cycle detection
test_edges = [(0, 1), (1, 2), (2, 0), (3, 4)]
print(f"Has cycle: {has_cycle_undirected(test_edges, 5)}")  # True
print(f"Cycle edges: {find_cycle_edges(test_edges, 5)}")   # [(2, 0)]
```

### Percolation Problem
```python
class Percolation:
    """
    Percolation problem sử dụng Union-Find
    """
    def __init__(self, n):
        self.n = n
        self.grid = [[False] * n for _ in range(n)]
        # n*n sites + 2 virtual sites (top and bottom)
        self.uf = UnionFind(n * n + 2)
        self.top_virtual = n * n
        self.bottom_virtual = n * n + 1
        self.open_sites = 0
    
    def _get_index(self, row, col):
        """Convert 2D coordinates to 1D index"""
        return row * self.n + col
    
    def open(self, row, col):
        """Open site at (row, col)"""
        if self.is_open(row, col):
            return
        
        self.grid[row][col] = True
        self.open_sites += 1
        site_index = self._get_index(row, col)
        
        # Connect to virtual top if in first row
        if row == 0:
            self.uf.union(site_index, self.top_virtual)
        
        # Connect to virtual bottom if in last row
        if row == self.n - 1:
            self.uf.union(site_index, self.bottom_virtual)
        
        # Connect to open neighbors
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < self.n and 0 <= new_col < self.n and
                self.is_open(new_row, new_col)):
                neighbor_index = self._get_index(new_row, new_col)
                self.uf.union(site_index, neighbor_index)
    
    def is_open(self, row, col):
        """Check if site is open"""
        return self.grid[row][col]
    
    def is_full(self, row, col):
        """Check if site is full (connected to top)"""
        if not self.is_open(row, col):
            return False
        
        site_index = self._get_index(row, col)
        return self.uf.connected(site_index, self.top_virtual)
    
    def percolates(self):
        """Check if system percolates"""
        return self.uf.connected(self.top_virtual, self.bottom_virtual)
    
    def number_of_open_sites(self):
        """Return number of open sites"""
        return self.open_sites

# Test percolation
perc = Percolation(3)
print(f"Percolates: {perc.percolates()}")  # False

# Open some sites
perc.open(0, 0)
perc.open(1, 0)
perc.open(2, 0)
print(f"Percolates: {perc.percolates()}")  # True
```

## MST Applications

### Network Design
```python
def minimum_cost_network(cities, connections):
    """
    Design minimum cost network to connect all cities
    cities: list of city names
    connections: list of (city1, city2, cost)
    """
    # Map city names to indices
    city_to_index = {city: i for i, city in enumerate(cities)}
    
    # Convert to edge format
    edges = []
    for city1, city2, cost in connections:
        u = city_to_index[city1]
        v = city_to_index[city2]
        edges.append((cost, u, v))
    
    # Find MST
    mst_edges, total_cost = kruskal_mst(edges, len(cities))
    
    # Convert back to city names
    network = []
    for u, v, cost in mst_edges:
        city1 = cities[u]
        city2 = cities[v]
        network.append((city1, city2, cost))
    
    return network, total_cost

# Test network design
cities = ['A', 'B', 'C', 'D']
connections = [
    ('A', 'B', 10), ('A', 'C', 6), ('A', 'D', 5),
    ('B', 'C', 4), ('B', 'D', 15), ('C', 'D', 8)
]

network, cost = minimum_cost_network(cities, connections)
print(f"Minimum cost network: {network}")
print(f"Total cost: {cost}")
```

### Clustering with MST
```python
def mst_clustering(points, k):
    """
    K-clustering sử dụng MST
    Remove k-1 heaviest edges from MST to get k clusters
    """
    n = len(points)
    
    # Calculate all pairwise distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = ((points[i][0] - points[j][0]) ** 2 + 
                   (points[i][1] - points[j][1]) ** 2) ** 0.5
            edges.append((dist, i, j))
    
    # Find MST
    mst_edges, _ = kruskal_mst(edges, n)
    
    # Sort MST edges by weight (descending)
    mst_edges.sort(key=lambda x: x[2], reverse=True)
    
    # Remove k-1 heaviest edges
    cluster_edges = mst_edges[k-1:]
    
    # Build clusters using remaining edges
    uf = UnionFind(n)
    for u, v, _ in cluster_edges:
        uf.union(u, v)
    
    # Group points by cluster
    clusters = {}
    for i in range(n):
        root = uf.find(i)
        if root not in clusters:
            clusters[root] = []
        clusters[root].append(points[i])
    
    return list(clusters.values())

# Test clustering
points = [(0, 0), (1, 1), (5, 5), (6, 6), (10, 10)]
clusters = mst_clustering(points, 3)
print(f"3 clusters: {clusters}")
```

## Best Practices

1. **Choose Right Implementation**: Union by rank vs size
2. **Use Path Compression**: Dramatically improves performance
3. **Early Termination**: Stop when MST is complete (n-1 edges)
4. **Handle Disconnected Graphs**: Check if MST is possible
5. **Memory Efficiency**: Use appropriate data structures
6. **Preprocessing**: Sort edges once for multiple MST queries
7. **Validate Input**: Check for self-loops, negative weights