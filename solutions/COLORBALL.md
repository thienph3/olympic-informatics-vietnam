# COLORBALL - Solution

## Phân tích

Trò chơi ném bi với quy tắc:
- Bảng n×m, ban đầu toàn trắng (0)
- An ném bi đỏ (1), Bình ném bi xanh (2)
- Khi ném vào (i,j), ảnh hưởng đến ô (i,j) và 8 ô xung quanh
- Quy tắc thay đổi màu:
  - Trắng → màu người ném
  - Màu bản thân → giữ nguyên
  - Màu đối thủ → trắng

## Thuật toán

1. Khởi tạo bảng toàn 0 (trắng)
2. Với mỗi lượt ném:
   - Tìm 9 ô bị ảnh hưởng (ô trung tâm + 8 ô xung quanh)
   - Áp dụng quy tắc thay đổi màu
3. Đếm số ô đỏ và xanh cuối cùng

## Code

```python
n, m, k = map(int, input().split())

# Khởi tạo bảng: 0=trắng, 1=đỏ, 2=xanh
board = [[0] * m for _ in range(n)]

# Hướng di chuyển cho 8 ô xung quanh + ô trung tâm
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]

for round_num in range(k):
    # Lượt An (đỏ = 1)
    i, j = map(int, input().split())
    i -= 1  # Chuyển về 0-indexed
    j -= 1
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj] == 0:  # Trắng → đỏ
                board[ni][nj] = 1
            elif board[ni][nj] == 1:  # Đỏ → đỏ (giữ nguyên)
                pass
            elif board[ni][nj] == 2:  # Xanh → trắng
                board[ni][nj] = 0
    
    # Lượt Bình (xanh = 2)
    i, j = map(int, input().split())
    i -= 1  # Chuyển về 0-indexed
    j -= 1
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj] == 0:  # Trắng → xanh
                board[ni][nj] = 2
            elif board[ni][nj] == 1:  # Đỏ → trắng
                board[ni][nj] = 0
            elif board[ni][nj] == 2:  # Xanh → xanh (giữ nguyên)
                pass

# Đếm số ô màu
red_count = 0
blue_count = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            red_count += 1
        elif board[i][j] == 2:
            blue_count += 1

print(red_count, blue_count)
```

## Code tối ưu hơn

```python
def update_board(board, row, col, player_color, n, m):
    """Cập nhật bảng khi ném bi"""
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]
    
    for di, dj in directions:
        ni, nj = row + di, col + dj
        if 0 <= ni < n and 0 <= nj < m:
            current = board[ni][nj]
            if current == 0:  # Trắng
                board[ni][nj] = player_color
            elif current == player_color:  # Màu bản thân
                pass  # Giữ nguyên
            else:  # Màu đối thủ
                board[ni][nj] = 0  # Về trắng

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

for _ in range(k):
    # An ném (đỏ = 1)
    i, j = map(int, input().split())
    update_board(board, i-1, j-1, 1, n, m)
    
    # Bình ném (xanh = 2)
    i, j = map(int, input().split())
    update_board(board, i-1, j-1, 2, n, m)

# Đếm kết quả
red = sum(row.count(1) for row in board)
blue = sum(row.count(2) for row in board)

print(red, blue)
```

## Giải thích

1. Mô phỏng từng lượt ném bi
2. Với mỗi lượt, cập nhật 9 ô (ô trung tâm + 8 ô xung quanh)
3. Áp dụng quy tắc thay đổi màu theo đề bài
4. Cuối cùng đếm số ô mỗi màu

**Độ phức tạp:** O(K × 9) = O(K)