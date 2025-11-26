# Day 7: Graph Representation

## Graph Theory Basics

### Khái niệm Graph
Graph G = (V, E) gồm:
- **V**: Tập hợp các đỉnh (vertices/nodes)
- **E**: Tập hợp các cạnh (edges) nối các đỉnh

### Phân loại Graph
```python
# Directed Graph (Có hướng)
# A → B (chỉ đi từ A đến B)

# Undirected Graph (Vô hướng) 
# A — B (đi được cả 2 chiều)

# Weighted Graph (Có trọng số)
# A —5— B (cạnh có trọng số 5)

# Unweighted Graph (Không trọng số)
# A — B (tất cả cạnh có trọng số = 1)
```

### Thuật ngữ cơ bản
```python
# Degree (Bậc): Số cạnh nối với đỉnh
# In-degree: Số cạnh đi vào (directed graph)
# Out-degree: Số cạnh đi ra (directed graph)

# Path (Đường đi): Dãy đỉnh liên tiếp
# Cycle (Chu trình): Đường đi bắt đầu và kết thúc tại cùng 1 đỉnh
# Connected Graph: Có đường đi giữa mọi cặp đỉnh
```

## Adjacency List Implementation

### Unweighted Graph
```python
class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        """Thêm đỉnh"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v):
        """Thêm cạnh"""
        # Thêm đỉnh nếu chưa có
        self.add_vertex(u)
        self.add_vertex(v)
        
        # Thêm cạnh
        self.graph[u].append(v)
        
        # Nếu vô hướng, thêm cạnh ngược lại
        if not self.directed:
            self.graph[v].append(u)
    
    def remove_edge(self, u, v):
        """Xóa cạnh"""
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        
        if not self.directed and v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)
    
    def get_neighbors(self, vertex):
        """Lấy danh sách láng giềng"""
        return self.graph.get(vertex, [])
    
    def get_vertices(self):
        """Lấy tất cả đỉnh"""
        return list(self.graph.keys())
    
    def get_edges(self):
        """Lấy tất cả cạnh"""
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                if self.directed or u <= v:  # Tránh trùng lặp với undirected
                    edges.append((u, v))
        return edges
    
    def display(self):
        """Hiển thị graph"""
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Ví dụ sử dụng
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.display()
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'D']
# D: ['B', 'C']
```

### Weighted Graph
```python
class WeightedGraph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v, weight):
        """Thêm cạnh có trọng số"""
        self.add_vertex(u)
        self.add_vertex(v)
        
        self.graph[u].append((v, weight))
        
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def get_neighbors(self, vertex):
        """Trả về list (neighbor, weight)"""
        return self.graph.get(vertex, [])
    
    def get_edge_weight(self, u, v):
        """Lấy trọng số cạnh u-v"""
        for neighbor, weight in self.graph.get(u, []):
            if neighbor == v:
                return weight
        return None
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Ví dụ
wg = WeightedGraph()
wg.add_edge('A', 'B', 5)
wg.add_edge('A', 'C', 3)
wg.add_edge('B', 'D', 2)
wg.display()
# A: [('B', 5), ('C', 3)]
# B: [('A', 5), ('D', 2)]
# C: [('A', 3)]
# D: [('B', 2)]
```

### Using Dictionary of Sets (Faster lookup)
```python
class FastGraph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set()
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        
        self.graph[u].add(v)
        if not self.directed:
            self.graph[v].add(u)
    
    def has_edge(self, u, v):
        """Kiểm tra cạnh tồn tại - O(1)"""
        return u in self.graph and v in self.graph[u]
    
    def remove_edge(self, u, v):
        if u in self.graph:
            self.graph[u].discard(v)
        if not self.directed and v in self.graph:
            self.graph[v].discard(u)
```

## Adjacency Matrix Representation

### Basic Adjacency Matrix
```python
class GraphMatrix:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        # Khởi tạo ma trận 0
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertex_map = {}  # Map vertex name to index
        self.reverse_map = {}  # Map index to vertex name
        self.next_index = 0
    
    def add_vertex(self, vertex):
        """Thêm đỉnh mới"""
        if vertex not in self.vertex_map:
            if self.next_index >= self.num_vertices:
                raise ValueError("Exceeded maximum number of vertices")
            
            self.vertex_map[vertex] = self.next_index
            self.reverse_map[self.next_index] = vertex
            self.next_index += 1
    
    def add_edge(self, u, v, weight=1):
        """Thêm cạnh"""
        # Thêm đỉnh nếu chưa có
        self.add_vertex(u)
        self.add_vertex(v)
        
        u_idx = self.vertex_map[u]
        v_idx = self.vertex_map[v]
        
        self.matrix[u_idx][v_idx] = weight
        
        if not self.directed:
            self.matrix[v_idx][u_idx] = weight
    
    def has_edge(self, u, v):
        """Kiểm tra cạnh tồn tại"""
        if u not in self.vertex_map or v not in self.vertex_map:
            return False
        
        u_idx = self.vertex_map[u]
        v_idx = self.vertex_map[v]
        return self.matrix[u_idx][v_idx] != 0
    
    def get_neighbors(self, vertex):
        """Lấy danh sách láng giềng"""
        if vertex not in self.vertex_map:
            return []
        
        vertex_idx = self.vertex_map[vertex]
        neighbors = []
        
        for i in range(self.num_vertices):
            if self.matrix[vertex_idx][i] != 0:
                neighbors.append(self.reverse_map[i])
        
        return neighbors
    
    def display(self):
        """Hiển thị ma trận"""
        print("Adjacency Matrix:")
        
        # Header
        vertices = [self.reverse_map.get(i, f"V{i}") for i in range(self.next_index)]
        print("   ", " ".join(f"{v:>3}" for v in vertices))
        
        # Rows
        for i in range(self.next_index):
            vertex = self.reverse_map.get(i, f"V{i}")
            row = " ".join(f"{self.matrix[i][j]:>3}" for j in range(self.next_index))
            print(f"{vertex:>3} {row}")

# Ví dụ sử dụng
gm = GraphMatrix(5)
gm.add_edge('A', 'B', 5)
gm.add_edge('A', 'C', 3)
gm.add_edge('B', 'D', 2)
gm.display()
```

### Weighted Matrix
```python
class WeightedMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.V = len(vertices)
        self.vertex_to_index = {v: i for i, v in enumerate(vertices)}
        
        # Khởi tạo với infinity (không có cạnh)
        self.matrix = [[float('inf')] * self.V for _ in range(self.V)]
        
        # Đường chéo = 0 (khoảng cách từ đỉnh đến chính nó)
        for i in range(self.V):
            self.matrix[i][i] = 0
    
    def add_edge(self, u, v, weight):
        u_idx = self.vertex_to_index[u]
        v_idx = self.vertex_to_index[v]
        self.matrix[u_idx][v_idx] = weight
    
    def get_weight(self, u, v):
        u_idx = self.vertex_to_index[u]
        v_idx = self.vertex_to_index[v]
        return self.matrix[u_idx][v_idx]
```

## When to Use Each Method

### Adjacency List
**Ưu điểm:**
- Tiết kiệm bộ nhớ: O(V + E)
- Nhanh khi duyệt neighbors: O(degree)
- Tốt cho sparse graphs (ít cạnh)

**Nhược điểm:**
- Kiểm tra cạnh tồn tại: O(degree)
- Phức tạp hơn để implement

**Khi nào dùng:**
- Graph có ít cạnh (E << V²)
- Cần duyệt neighbors thường xuyên
- Bộ nhớ hạn chế

### Adjacency Matrix
**Ưu điểm:**
- Kiểm tra cạnh tồn tại: O(1)
- Đơn giản để implement
- Tốt cho dense graphs (nhiều cạnh)
- Dễ làm việc với algorithms như Floyd-Warshall

**Nhược điểm:**
- Tốn bộ nhớ: O(V²)
- Duyệt neighbors: O(V)

**Khi nào dùng:**
- Graph có nhiều cạnh (E ≈ V²)
- Cần kiểm tra cạnh tồn tại thường xuyên
- Algorithms yêu cầu matrix operations

## Comparison Example
```python
import time
import random

def compare_representations():
    # Tạo graph test
    vertices = list(range(1000))
    edges = [(random.randint(0, 999), random.randint(0, 999)) 
             for _ in range(5000)]
    
    # Adjacency List
    start = time.time()
    adj_list = Graph()
    for u, v in edges:
        adj_list.add_edge(u, v)
    list_build_time = time.time() - start
    
    # Test neighbor lookup
    start = time.time()
    for _ in range(1000):
        vertex = random.randint(0, 999)
        neighbors = adj_list.get_neighbors(vertex)
    list_lookup_time = time.time() - start
    
    # Adjacency Matrix
    start = time.time()
    adj_matrix = GraphMatrix(1000)
    for u, v in edges:
        adj_matrix.add_edge(u, v)
    matrix_build_time = time.time() - start
    
    # Test edge existence
    start = time.time()
    for _ in range(1000):
        u, v = random.randint(0, 999), random.randint(0, 999)
        exists = adj_matrix.has_edge(u, v)
    matrix_check_time = time.time() - start
    
    print(f"Build time - List: {list_build_time:.4f}s, Matrix: {matrix_build_time:.4f}s")
    print(f"Lookup time - List: {list_lookup_time:.4f}s, Matrix: {matrix_check_time:.4f}s")

compare_representations()
```

## Input/Output Formats

### Reading Graph from Input
```python
def read_graph_adjacency_list():
    """
    Input format:
    n m
    u1 v1
    u2 v2
    ...
    """
    n, m = map(int, input().split())  # n vertices, m edges
    graph = Graph()
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    
    return graph

def read_weighted_graph():
    """
    Input format:
    n m
    u1 v1 w1
    u2 v2 w2
    ...
    """
    n, m = map(int, input().split())
    graph = WeightedGraph()
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, w)
    
    return graph

def read_adjacency_matrix():
    """
    Input format:
    n
    matrix[0][0] matrix[0][1] ... matrix[0][n-1]
    matrix[1][0] matrix[1][1] ... matrix[1][n-1]
    ...
    """
    n = int(input())
    matrix = []
    
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    return matrix
```

### Converting Between Representations
```python
def adjacency_list_to_matrix(adj_list, vertices):
    """Chuyển từ adjacency list sang matrix"""
    n = len(vertices)
    vertex_to_idx = {v: i for i, v in enumerate(vertices)}
    matrix = [[0] * n for _ in range(n)]
    
    for u in adj_list.graph:
        u_idx = vertex_to_idx[u]
        for v in adj_list.graph[u]:
            v_idx = vertex_to_idx[v]
            matrix[u_idx][v_idx] = 1
    
    return matrix

def adjacency_matrix_to_list(matrix, vertices):
    """Chuyển từ matrix sang adjacency list"""
    adj_list = Graph()
    n = len(vertices)
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                adj_list.add_edge(vertices[i], vertices[j])
    
    return adj_list
```

## Common Graph Properties
```python
def graph_properties(graph):
    """Tính các thuộc tính cơ bản của graph"""
    vertices = graph.get_vertices()
    edges = graph.get_edges()
    
    print(f"Number of vertices: {len(vertices)}")
    print(f"Number of edges: {len(edges)}")
    
    # Degree của mỗi đỉnh
    degrees = {}
    for v in vertices:
        degrees[v] = len(graph.get_neighbors(v))
    
    print(f"Degrees: {degrees}")
    print(f"Max degree: {max(degrees.values())}")
    print(f"Min degree: {min(degrees.values())}")
    
    # Density
    max_edges = len(vertices) * (len(vertices) - 1)
    if not graph.directed:
        max_edges //= 2
    
    density = len(edges) / max_edges if max_edges > 0 else 0
    print(f"Density: {density:.3f}")
```