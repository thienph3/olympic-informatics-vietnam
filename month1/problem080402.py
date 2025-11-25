# Problem 08.04.02: Thuật toán trên grid

print("=== THUẬT TOÁN TRÊN GRID ===")

# Bài 1: Tìm đường trong mê cung (DFS)
print("1. Tìm đường trong mê cung:")

def print_maze(maze, path=None, title="Mê cung"):
    """In mê cung với đường đi (nếu có)"""
    print(f"{title}:")
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if path and (i, j) in path:
                print(".", end=" ")  # Đường đi
            elif maze[i][j] == 1:
                print("#", end=" ")  # Tường
            else:
                print(" ", end=" ")  # Đường trống
        print()

def find_path_dfs(maze, start, end):
    """Tìm đường đi bằng DFS"""
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    path = []
    
    def dfs(x, y):
        # Kiểm tra biên
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False
        
        # Kiểm tra tường hoặc đã thăm
        if maze[x][y] == 1 or visited[x][y]:
            return False
        
        # Đến đích
        if (x, y) == end:
            path.append((x, y))
            return True
        
        # Đánh dấu đã thăm
        visited[x][y] = True
        path.append((x, y))
        
        # Thử 4 hướng: lên, xuống, trái, phải
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            if dfs(x + dx, y + dy):
                return True
        
        # Backtrack
        path.pop()
        return False
    
    if dfs(start[0], start[1]):
        return path
    return []

# Test mê cung
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

print_maze(maze, title="Mê cung gốc (# = tường, khoảng trắng = đường)")
path = find_path_dfs(maze, start, end)

if path:
    print(f"Tìm thấy đường đi từ {start} đến {end}:")
    print(f"Đường đi: {path}")
    print_maze(maze, path, "Mê cung với đường đi (. = đường đi)")
else:
    print(f"Không tìm thấy đường đi từ {start} đến {end}")

# Bài 2: Flood Fill
print("\n2. Flood Fill:")

def flood_fill(image, sr, sc, new_color):
    """Thuật toán flood fill (tô màu vùng liên thông)"""
    if not image or sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
        return image
    
    original_color = image[sr][sc]
    if original_color == new_color:
        return image
    
    def fill(r, c):
        if (r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or 
            image[r][c] != original_color):
            return
        
        image[r][c] = new_color
        
        # Tô 4 hướng
        fill(r + 1, c)
        fill(r - 1, c)
        fill(r, c + 1)
        fill(r, c - 1)
    
    fill(sr, sc)
    return image

def print_image(image, title="Ảnh"):
    """In ảnh màu"""
    print(f"{title}:")
    for row in image:
        print(" ".join(str(pixel) for pixel in row))

# Test flood fill
original_image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

print_image(original_image, "Ảnh gốc")

# Copy để test
test_image = [row[:] for row in original_image]
flood_fill(test_image, 1, 1, 2)
print_image(test_image, "Sau flood fill tại (1,1) với màu 2")

# Bài 3: Đếm số đảo (Islands)
print("\n3. Đếm số đảo:")

def count_islands(grid):
    """Đếm số đảo trong lưới (1 = đất, 0 = nước)"""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = 0
    
    def dfs_island(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            visited[r][c] or grid[r][c] == 0):
            return
        
        visited[r][c] = True
        
        # Thăm 4 hướng
        dfs_island(r + 1, c)
        dfs_island(r - 1, c)
        dfs_island(r, c + 1)
        dfs_island(r, c - 1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs_island(i, j)
                islands += 1
    
    return islands

# Test đếm đảo
island_grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]

print("Lưới đảo (1 = đất, 0 = nước):")
print_image(island_grid)
num_islands = count_islands(island_grid)
print(f"Số đảo: {num_islands}")

# Bài 4: Tìm đường đi ngắn nhất (BFS)
print("\n4. Tìm đường đi ngắn nhất (BFS):")

from collections import deque

def shortest_path_bfs(grid, start, end):
    """Tìm đường đi ngắn nhất bằng BFS"""
    if not grid or grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1, []
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    parent = {}
    
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited[start[0]][start[1]] = True
    parent[start] = None
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == end:
            # Truy vết đường đi
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            return dist, path[::-1]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and 
                not visited[nr][nc] and grid[nr][nc] == 0):
                visited[nr][nc] = True
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc, dist + 1))
    
    return -1, []

# Test BFS
bfs_grid = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start_bfs = (0, 0)
end_bfs = (4, 4)

print("Grid cho BFS (0 = đường, 1 = tường):")
print_image(bfs_grid)

distance, shortest_path = shortest_path_bfs(bfs_grid, start_bfs, end_bfs)
if distance != -1:
    print(f"Đường đi ngắn nhất từ {start_bfs} đến {end_bfs}:")
    print(f"Khoảng cách: {distance}")
    print(f"Đường đi: {shortest_path}")
    print_maze(bfs_grid, shortest_path, "Grid với đường đi ngắn nhất")
else:
    print("Không tìm thấy đường đi")

# Bài 5: Rotting Oranges
print("\n5. Rotting Oranges:")

def oranges_rotting(grid):
    """Tính thời gian để tất cả cam bị thối"""
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # Tìm tất cả cam thối ban đầu và đếm cam tươi
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:  # Cam thối
                queue.append((i, j, 0))
            elif grid[i][j] == 1:  # Cam tươi
                fresh_count += 1
    
    if fresh_count == 0:
        return 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_time = 0
    
    while queue:
        r, c, time = queue.popleft()
        max_time = max(max_time, time)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                grid[nr][nc] = 2  # Cam tươi bị thối
                fresh_count -= 1
                queue.append((nr, nc, time + 1))
    
    return max_time if fresh_count == 0 else -1

# Test rotting oranges
orange_grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print("Grid cam (0 = trống, 1 = cam tươi, 2 = cam thối):")
print_image(orange_grid)

# Copy để test
test_orange_grid = [row[:] for row in orange_grid]
time_to_rot = oranges_rotting(test_orange_grid)

if time_to_rot != -1:
    print(f"Thời gian để tất cả cam thối: {time_to_rot} phút")
else:
    print("Không thể làm thối hết tất cả cam")

# Bài 6: Word Search
print("\n6. Word Search:")

def word_search(board, word):
    """Tìm từ trong bảng chữ cái"""
    if not board or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs_word(r, c, index):
        if index == len(word):
            return True
        
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            board[r][c] != word[index]):
            return False
        
        # Đánh dấu tạm thời
        temp = board[r][c]
        board[r][c] = '#'
        
        # Tìm ký tự tiếp theo ở 4 hướng
        found = (dfs_word(r + 1, c, index + 1) or
                dfs_word(r - 1, c, index + 1) or
                dfs_word(r, c + 1, index + 1) or
                dfs_word(r, c - 1, index + 1))
        
        # Khôi phục
        board[r][c] = temp
        return found
    
    # Thử từ mỗi ô
    for i in range(rows):
        for j in range(cols):
            if dfs_word(i, j, 0):
                return True
    
    return False

# Test word search
char_board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

print("Bảng chữ cái:")
for row in char_board:
    print(" ".join(row))

test_words = ["ABCCED", "SEE", "ABCB"]
for word in test_words:
    found = word_search([row[:] for row in char_board], word)
    print(f"Từ '{word}': {'Tìm thấy' if found else 'Không tìm thấy'}")