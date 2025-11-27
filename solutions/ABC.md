# ABC - Math (250 points)

## Phân tích bài toán

Tìm giá trị của biểu thức A + B × C với các ràng buộc cho trước.

### Input
- A, B, C: ba số nguyên

### Output
- Giá trị của A + B × C

### Ý tưởng
Đây là bài toán đơn giản về thứ tự thực hiện phép toán:
1. Thực hiện phép nhân trước: B × C
2. Thực hiện phép cộng sau: A + (B × C)

## Solution

```python
# Đọc input
A, B, C = map(int, input().split())

# Tính theo thứ tự ưu tiên: nhân trước, cộng sau
result = A + B * C

print(result)
```

## Độ phức tạp
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Test cases
```
Input:
1 2 3

Output:
7

Giải thích: 1 + 2×3 = 1 + 6 = 7
```

## Lưu ý
- Python tự động tuân theo thứ tự ưu tiên phép toán (nhân/chia trước, cộng/trừ sau)
- Không cần dấu ngoặc đơn trong trường hợp này