# Day 8: List nâng cao - list comprehension, nested lists

**Thời gian:** 195 phút (3h15')

---

## Phần 1: List comprehension cơ bản (45')

### 📚 Lý thuyết (15')

#### Khái niệm List Comprehension
```python
# Cú pháp: [expression for item in iterable]
# Thay thế cho vòng lặp for truyền thống

# Cách truyền thống
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)  # [0, 1, 4, 9, 16]

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

#### List comprehension với điều kiện
```python
# Cú pháp: [expression for item in iterable if condition]

# Số chẵn từ 0 đến 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Bình phương của số lẻ
odd_squares = [x**2 for x in range(10) if x % 2 == 1]
print(odd_squares)  # [1, 9, 25, 49, 81]

# Lọc chuỗi
words = ["apple", "banana", "cherry", "date"]
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['banana', 'cherry']
```

#### Biến đổi dữ liệu
```python
# Chuyển đổi kiểu dữ liệu
numbers_str = ["1", "2", "3", "4", "5"]
numbers_int = [int(x) for x in numbers_str]
print(numbers_int)  # [1, 2, 3, 4, 5]

# Xử lý chuỗi
names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names]
print(capitalized)  # ['Alice', 'Bob', 'Charlie']

# Tính toán phức tạp
prices = [100, 200, 150, 300]
prices_with_tax = [price * 1.1 for price in prices]
print(prices_with_tax)  # [110.0, 220.0, 165.0, 330.0]
```

### 💻 Thực hành (30')

#### Bài tập 1: List comprehension cơ bản

**Yêu cầu:** Thực hành tạo list với comprehension: số học, xử lý chuỗi, lọc dữ liệu.

**File thực hành:** [problem080101.py](problem080101.py)

#### Bài tập 2: Biến đổi và lọc dữ liệu

**Yêu cầu:** Sử dụng list comprehension để xử lý dữ liệu thực tế: điểm số, sản phẩm, từ điển.

**File thực hành:** [problem080102.py](problem080102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: List comprehension nâng cao (45')

### 📚 Lý thuyết (20')

#### Nested list comprehension
```python
# Tạo ma trận với nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6]

# Tạo bảng cửu chương
multiplication_table = [[i*j for j in range(1, 11)] for i in range(1, 11)]
```

#### Conditional expression trong comprehension
```python
# Cú pháp: [expr1 if condition else expr2 for item in iterable]

# Phân loại số
numbers = [1, 2, 3, 4, 5, 6]
labels = ["odd" if x % 2 == 1 else "even" for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd', 'even']

# Xử lý giá trị None
data = [1, None, 3, None, 5]
cleaned = [x if x is not None else 0 for x in data]
print(cleaned)  # [1, 0, 3, 0, 5]

# Cắt chuỗi dài
texts = ["short", "this is a very long text", "medium text"]
truncated = [text if len(text) <= 10 else text[:10] + "..." for text in texts]
print(truncated)  # ['short', 'this is a ...', 'medium text']
```

#### Multiple iterables
```python
# Kết hợp nhiều iterable
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = [f"{name} is {age} years old" for name, age in zip(names, ages)]
print(combined)  # ['Alice is 25 years old', 'Bob is 30 years old', 'Charlie is 35 years old']

# Cartesian product
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
products = [f"{color}-{size}" for color in colors for size in sizes]
print(products)  # ['red-S', 'red-M', 'red-L', 'blue-S', 'blue-M', 'blue-L']
```

#### Set và Dictionary comprehension
```python
# Set comprehension
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}

# Dictionary comprehension
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}

# Đảo ngược dictionary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}
```

### 💻 Thực hành (25')

#### Bài tập 1: Nested comprehension và ma trận

**Yêu cầu:** Tạo ma trận, xử lý nested lists, flatten và reshape dữ liệu.

**File thực hành:** [problem080201.py](problem080201.py)

#### Bài tập 2: Set và Dictionary comprehension

**Yêu cầu:** Sử dụng set/dict comprehension để xử lý dữ liệu phức tạp.

**File thực hành:** [problem080202.py](problem080202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Nested lists - danh sách lồng nhau (45')

### 📚 Lý thuyết (15')

#### Tạo và truy cập nested lists
```python
# Tạo nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])     # [1, 2, 3] - hàng đầu tiên
print(matrix[1][2])  # 6 - phần tử hàng 1, cột 2

# Tạo ma trận với giá trị mặc định
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# CẢNH BÁO: Không làm như này!
# wrong_matrix = [[0] * cols] * rows  # Tất cả hàng cùng tham chiếu!
```

#### Duyệt nested lists
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Duyệt từng phần tử
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# Duyệt với enumerate
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        print(f"({i},{j}): {value}")

# Duyệt tất cả phần tử
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
```

#### Thao tác với ma trận
```python
# Tính tổng hàng
def sum_rows(matrix):
    return [sum(row) for row in matrix]

# Tính tổng cột
def sum_cols(matrix):
    if not matrix:
        return []
    return [sum(matrix[i][j] for i in range(len(matrix))) 
            for j in range(len(matrix[0]))]

# Chuyển vị ma trận
def transpose(matrix):
    if not matrix:
        return []
    return [[matrix[i][j] for i in range(len(matrix))] 
            for j in range(len(matrix[0]))]

# Tìm phần tử trong ma trận
def find_in_matrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return i, j
    return -1, -1
```

### 💻 Thực hành (30')

#### Bài tập 1: Thao tác ma trận cơ bản

**Yêu cầu:** Tạo, duyệt và thao tác với ma trận: tính tổng, chuyển vị, tìm kiếm.

**File thực hành:** [problem080301.py](problem080301.py)

#### Bài tập 2: Xử lý dữ liệu 2D

**Yêu cầu:** Xử lý bảng điểm, ma trận ảnh và dữ liệu bán hàng 2D.

**File thực hành:** [problem080302.py](problem080302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Ứng dụng trong Olympic (45')

### 📚 Lý thuyết (15')

#### Dynamic Programming với nested lists
```python
# Fibonacci với memoization
def fibonacci_dp(n):
    dp = [0] * (n + 1)
    if n >= 1:
        dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Longest Common Subsequence
def lcs_length(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

#### Ma trận trong thuật toán
```python
# Floyd-Warshall - đường đi ngắn nhất
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Khởi tạo
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Thuật toán chính
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Pascal Triangle
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
```

#### Xử lý grid/maze
```python
# Tìm đường trong mê cung (DFS)
def find_path_dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    path = []
    
    def dfs(x, y):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        if maze[x][y] == 1 or visited[x][y]:  # 1 = tường
            return False
        if (x, y) == end:
            path.append((x, y))
            return True
        
        visited[x][y] = True
        path.append((x, y))
        
        # Thử 4 hướng
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if dfs(x + dx, y + dy):
                return True
        
        path.pop()  # Backtrack
        return False
    
    if dfs(start[0], start[1]):
        return path
    return []
```

### 💻 Thực hành (30')

#### Bài tập 1: Dynamic Programming với ma trận

**Yêu cầu:** Implement các thuật toán DP: Fibonacci, LCS, Pascal triangle.

**File thực hành:** [problem080401.py](problem080401.py)

#### Bài tập 2: Thuật toán trên grid

**Yêu cầu:** Xử lý mê cung, tìm đường đi, flood fill và thuật toán trên lưới.

**File thực hành:** [problem080402.py](problem080402.py)

---

## Bài tập về nhà

### Bài 1: Sudoku Solver
Viết chương trình giải Sudoku:
- Đọc bảng Sudoku 9x9 (0 = ô trống)
- Sử dụng backtracking để điền số
- Kiểm tra tính hợp lệ của từng nước đi
- In ra lời giải hoặc "No solution"

### Bài 2: Matrix Multiplication
Implement phép nhân ma trận:
- Nhập 2 ma trận A(m×n) và B(n×p)
- Tính ma trận tích C = A × B
- Tối ưu hóa với list comprehension
- So sánh hiệu suất với vòng lặp thường

### Bài 3: Image Processing
Xử lý ảnh đơn giản với ma trận:
- Tạo ma trận đại diện cho ảnh grayscale
- Implement các filter: blur, edge detection
- Rotate và flip ảnh
- Histogram equalization

### Gợi ý làm bài
1. Sử dụng nested list comprehension cho ma trận
2. Áp dụng backtracking cho Sudoku
3. Tối ưu hóa với numpy-like operations bằng list comprehension
4. Kiểm tra boundary conditions cẩn thận

---

## Tổng kết Day 8

**Đã học:**
- List comprehension: cơ bản và nâng cao
- Nested comprehension và conditional expressions
- Set/Dictionary comprehension
- Nested lists: tạo, duyệt, thao tác ma trận
- Ứng dụng trong Dynamic Programming
- Thuật toán trên grid và ma trận
- Tối ưu hóa code với comprehension

**Chuẩn bị cho Day 9:**
- Ôn lại list comprehension và nested lists
- Thực hành với ma trận và thuật toán 2D
- Làm xong bài tập về nhà
- Chuẩn bị học Tuple và String methods