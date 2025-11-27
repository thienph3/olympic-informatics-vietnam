# DIVNOTDIV - Solution

## Phân tích

Tìm số m nhỏ nhất sao cho:
- m >= n
- m chia hết cho a
- m không chia hết cho b

## Thuật toán

1. Tìm số nhỏ nhất >= n chia hết cho a
2. Kiểm tra xem có chia hết cho b không
3. Nếu có, tìm số tiếp theo chia hết cho a

Trường hợp đặc biệt: Nếu gcd(a,b) = a (tức a chia hết cho b), thì mọi bội của a đều chia hết cho b → không có đáp án.

## Code

```python
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(a, b, n):
    # Nếu a chia hết cho b, thì mọi bội của a đều chia hết cho b
    if a % b == 0:
        return -1
    
    # Tìm số nhỏ nhất >= n chia hết cho a
    start = ((n - 1) // a + 1) * a
    
    # Kiểm tra từ start
    current = start
    
    # Giới hạn số lần thử để tránh vòng lặp vô hạn
    for _ in range(b):
        if current % b != 0:
            return current
        current += a
    
    return -1

t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    print(solve(a, b, n))
```

## Code tối ưu hơn

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(a, b, n):
    # Nếu gcd(a, b) = a, tức a | b, thì không có đáp án
    if gcd(a, b) == a:
        return -1
    
    # Tìm số nhỏ nhất >= n chia hết cho a
    start = ((n - 1) // a + 1) * a
    
    # LCM của a và b
    lcm_ab = lcm(a, b)
    
    # Trong mỗi chu kỳ lcm_ab, có đúng b/gcd(a,b) số chia hết cho cả a và b
    # Và có a/gcd(a,b) số chia hết cho a
    
    # Kiểm tra trong phạm vi hợp lý
    for i in range(min(b, 100)):  # Giới hạn để tránh TLE
        candidate = start + i * a
        if candidate % b != 0:
            return candidate
    
    return -1

t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    print(solve(a, b, n))
```

## Code đơn giản và chính xác

```python
def solve(a, b, n):
    # Nếu a chia hết cho b, không có đáp án
    if a % b == 0:
        return -1
    
    # Tìm số nhỏ nhất >= n chia hết cho a
    m = ((n - 1) // a + 1) * a
    
    # Kiểm tra tối đa b lần
    for _ in range(b):
        if m % b != 0:
            return m
        m += a
    
    return -1

t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    print(solve(a, b, n))
```

## Giải thích

1. Nếu a chia hết cho b, thì mọi bội của a đều chia hết cho b → không có đáp án
2. Tìm bội nhỏ nhất của a >= n
3. Kiểm tra từng bội của a cho đến khi tìm được số không chia hết cho b
4. Trong chu kỳ lcm(a,b), luôn tồn tại bội của a không chia hết cho b

**Độ phức tạp:** O(T × min(b, lcm(a,b)/a))