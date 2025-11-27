# NUMRECT - Math (200 points)

## Phân tích bài toán

Đếm số hình chữ nhật có thể tạo thành từ lưới m×n.

### Input
- m, n: kích thước lưới

### Output
- Số hình chữ nhật có thể tạo thành

### Ý tưởng
Với lưới m×n, số hình chữ nhật = số cách chọn 2 đường ngang × số cách chọn 2 đường dọc
- Có (m+1) đường ngang → C(m+1, 2) cách chọn
- Có (n+1) đường dọc → C(n+1, 2) cách chọ

Công thức: C(m+1, 2) × C(n+1, 2) = m(m+1)/2 × n(n+1)/2

## Solution

```python
# Đọc input
m, n = map(int, input().split())

# Tính số hình chữ nhật
# Số cách chọn 2 đường ngang từ (m+1) đường
horizontal_ways = m * (m + 1) // 2

# Số cách chọn 2 đường dọc từ (n+1) đường  
vertical_ways = n * (n + 1) // 2

# Tổng số hình chữ nhật
result = horizontal_ways * vertical_ways

print(result)
```

## Độ phức tạp
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Test cases
```
Input:
2 3

Output:
18

Giải thích: 
- Horizontal: 2×3/2 = 3 cách
- Vertical: 3×4/2 = 6 cách  
- Total: 3×6 = 18
```