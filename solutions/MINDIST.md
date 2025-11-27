# MINDIST - Solution

## Phân tích

Bài toán yêu cầu tìm khoảng cách nhỏ nhất giữa hai phần tử bằng nhau trong mảng.

Khoảng cách giữa vị trí i và j được định nghĩa là |i - j| + 1.

## Thuật toán

### Cách 1: Brute Force O(N²)
Duyệt tất cả cặp (i, j) với i < j, kiểm tra a[i] == a[j].

### Cách 2: Hash Map O(N)
Lưu vị trí cuối cùng của mỗi giá trị, cập nhật khoảng cách tối thiểu.

## Code

```python
n = int(input())
a = list(map(int, input().split()))

min_dist = float('inf')
last_pos = {}

for i in range(n):
    if a[i] in last_pos:
        # Tính khoảng cách với lần xuất hiện trước đó
        dist = i - last_pos[a[i]] + 1
        min_dist = min(min_dist, dist)
    
    # Cập nhật vị trí cuối cùng của a[i]
    last_pos[a[i]] = i

if min_dist == float('inf'):
    print(-1)
else:
    print(min_dist)
```

## Code Brute Force

```python
n = int(input())
a = list(map(int, input().split()))

min_dist = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            dist = j - i + 1
            min_dist = min(min_dist, dist)

if min_dist == float('inf'):
    print(-1)
else:
    print(min_dist)
```

## Giải thích

1. Duyệt mảng từ trái sang phải
2. Với mỗi phần tử, kiểm tra xem đã gặp trước đó chưa
3. Nếu có, tính khoảng cách và cập nhật minimum
4. Lưu vị trí hiện tại của phần tử

**Độ phức tạp:** O(N) với hash map, O(N²) với brute force