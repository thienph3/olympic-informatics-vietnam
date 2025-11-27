# INCMAT - Math (250 points)

## Phân tích bài toán

Tăng tất cả phần tử trong ma trận lên k đơn vị và tính tổng mới.

### Input
- n, m: kích thước ma trận
- Ma trận A[n][m]
- k: giá trị tăng thêm

### Output
- Tổng các phần tử sau khi tăng k

### Ý tưởng
1. Tổng ban đầu = sum(tất cả phần tử)
2. Sau khi tăng k: mỗi phần tử tăng k
3. Tổng mới = tổng ban đầu + k × (số phần tử)
4. Số phần tử = n × m

## Solution

```python
# Đọc kích thước ma trận
n, m = map(int, input().split())

# Đọc ma trận và tính tổng ban đầu
total_sum = 0
for i in range(n):
    row = list(map(int, input().split()))
    total_sum += sum(row)

# Đọc k
k = int(input())

# Tính tổng sau khi tăng k cho tất cả phần tử
# Mỗi phần tử tăng k, có n*m phần tử
new_sum = total_sum + k * n * m

print(new_sum)
```

## Cách khác (đơn giản hơn)

```python
# Đọc input
n, m = map(int, input().split())

# Đọc và tính tổng trực tiếp
matrix_sum = 0
for i in range(n):
    row = list(map(int, input().split()))
    matrix_sum += sum(row)

k = int(input())

# Kết quả
result = matrix_sum + k * n * m
print(result)
```

## Độ phức tạp
- **Time Complexity:** O(n×m)
- **Space Complexity:** O(m) - chỉ lưu một hàng tại một thời điểm

## Test cases
```
Input:
2 3
1 2 3
4 5 6
2

Output:
33

Giải thích:
- Tổng ban đầu: 1+2+3+4+5+6 = 21
- Sau khi tăng 2: 21 + 2×(2×3) = 21 + 12 = 33
```