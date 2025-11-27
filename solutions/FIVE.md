# FIVE - Implementation (200 points)

## Phân tích bài toán

Đếm số lượng chữ số 5 trong một số nguyên.

### Input
- n: số nguyên cần đếm

### Output
- Số lượng chữ số 5 trong n

### Ý tưởng
1. Chuyển số thành chuỗi
2. Đếm ký tự '5' trong chuỗi
3. Hoặc dùng phép chia lấy dư để tách từng chữ số

## Solution 1 (String approach)

```python
# Đọc input
n = input().strip()

# Đếm số lượng chữ số 5
count = n.count('5')

print(count)
```

## Solution 2 (Mathematical approach)

```python
# Đọc input
n = int(input())

# Xử lý số âm
n = abs(n)

# Đếm chữ số 5
count = 0
if n == 0:
    count = 0
else:
    while n > 0:
        if n % 10 == 5:
            count += 1
        n //= 10

print(count)
```

## Solution 3 (Pythonic)

```python
# Đọc input
n = input().strip()

# Đếm chữ số 5 (bỏ qua dấu âm nếu có)
count = sum(1 for digit in n if digit == '5')

print(count)
```

## Độ phức tạp
- **Time Complexity:** O(log n) - số chữ số của n
- **Space Complexity:** O(1) hoặc O(log n) nếu dùng string

## Test cases
```
Input:
12555

Output:
3

Input:
-505

Output:
2

Input:
123

Output:
0
```