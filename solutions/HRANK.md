# HRANK - Solution

## Phân tích

Bài toán cho biết số người cao hơn mà mỗi học sinh nhìn thấy phía trước, yêu cầu tìm thứ hạng chiều cao.

Quan sát:
- Học sinh i nhìn thấy a[i] người cao hơn phía trước
- Thứ hạng của học sinh i = a[i] + 1 + số người phía sau cao hơn i

## Thuật toán

1. Tính thứ hạng từ cuối về đầu
2. Với mỗi vị trí i, thứ hạng = a[i] + 1 + số người phía sau cao hơn
3. Sử dụng mảng để đếm số người cao hơn

## Code

```python
n, q = map(int, input().split())

if n == 1:
    a = []
else:
    a = [0] + list(map(int, input().split()))  # a[1] = a2, a[2] = a3, ...

# Tính thứ hạng cho từng vị trí
rank = [0] * (n + 1)

# Xử lý từ cuối về đầu
for i in range(n, 0, -1):
    if i == 1:
        # Vị trí đầu tiên: thứ hạng = 1 + số người phía sau cao hơn
        rank[i] = 1
        for j in range(2, n + 1):
            if rank[j] <= rank[i]:
                rank[i] += 1
    else:
        # Vị trí i: có a[i] người phía trước cao hơn
        # Thứ hạng tạm thời = a[i] + 1
        rank[i] = a[i] + 1
        
        # Cộng thêm số người phía sau cao hơn
        for j in range(i + 1, n + 1):
            if rank[j] <= rank[i]:
                rank[i] += 1

# Xử lý lại để đảm bảo tính nhất quán
rank = [0] * (n + 1)

# Thuật toán chính xác hơn
for i in range(n, 0, -1):
    if i == n:
        rank[i] = a[i] + 1 if i > 1 else 1
    else:
        if i == 1:
            rank[i] = 1
            for j in range(2, n + 1):
                if rank[j] >= rank[i]:
                    rank[i] += 1
        else:
            rank[i] = a[i] + 1
            for j in range(i + 1, n + 1):
                if rank[j] >= rank[i]:
                    rank[i] += 1

# Trả lời truy vấn
for _ in range(q):
    i = int(input())
    print(rank[i])
```

## Code đơn giản hơn

```python
n, q = map(int, input().split())

if n == 1:
    a = [0]
else:
    a = [0] + list(map(int, input().split()))

# Tính thứ hạng
rank = [0] * (n + 1)

# Với mỗi vị trí, tính số người cao hơn tổng cộng
for i in range(1, n + 1):
    if i == 1:
        rank[i] = n  # Người đầu tiên cao nhất
    else:
        # Có a[i] người phía trước cao hơn
        # Thứ hạng = tổng số người - a[i]
        rank[i] = n - a[i]

# Điều chỉnh để đảm bảo thứ hạng hợp lệ
used = [False] * (n + 1)
final_rank = [0] * (n + 1)

for i in range(1, n + 1):
    target_rank = rank[i]
    actual_rank = target_rank
    
    # Tìm thứ hạng chưa được sử dụng
    while actual_rank <= n and used[actual_rank]:
        actual_rank += 1
    
    if actual_rank <= n:
        used[actual_rank] = True
        final_rank[i] = actual_rank

for _ in range(q):
    i = int(input())
    print(final_rank[i])
```

## Giải thích

1. Mỗi học sinh i nhìn thấy a[i] người cao hơn phía trước
2. Thứ hạng chiều cao = n - a[i] (gần đúng)
3. Cần điều chỉnh để tránh trùng lặp thứ hạng

**Độ phức tạp:** O(N²) cho việc tính toán, O(1) cho mỗi truy vấn