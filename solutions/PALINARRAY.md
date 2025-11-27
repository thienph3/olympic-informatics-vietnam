# PALINARRAY - Solution

## Phân tích

Tìm xem có tồn tại dãy con palindrome có ít nhất 3 phần tử không.

Dãy con palindrome có thể:
- Độ dài 3: a[i] = a[k] với i < j < k
- Độ dài lớn hơn: sử dụng DP

## Thuật toán

### Cách 1: Kiểm tra palindrome độ dài 3
Tìm 3 vị trí i < j < k sao cho a[i] = a[k].

### Cách 2: Dynamic Programming
dp[i][j] = true nếu dãy con từ i đến j là palindrome.

## Code đơn giản (kiểm tra độ dài 3)

```python
def has_palindrome_subsequence(arr):
    n = len(arr)
    
    # Kiểm tra palindrome độ dài 3: a[i] = a[k] với i < j < k
    for i in range(n):
        for k in range(i + 2, n):
            if arr[i] == arr[k]:
                return True
    
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if has_palindrome_subsequence(a):
        print("YES")
    else:
        print("NO")
```

## Code tối ưu hơn

```python
def solve(arr):
    n = len(arr)
    
    # Sử dụng hash để tối ưu
    last_pos = {}
    
    for i in range(n):
        if arr[i] in last_pos:
            # Nếu đã gặp arr[i] trước đó và có ít nhất 1 phần tử ở giữa
            if i - last_pos[arr[i]] >= 2:
                return True
        last_pos[arr[i]] = i
    
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if solve(a):
        print("YES")
    else:
        print("NO")
```

## Code DP (cho trường hợp tổng quát)

```python
def has_palindrome_dp(arr):
    n = len(arr)
    
    # dp[i][j] = True nếu có palindrome subsequence từ i đến j
    dp = [[False] * n for _ in range(n)]
    
    # Palindrome độ dài 1
    for i in range(n):
        dp[i][i] = True
    
    # Palindrome độ dài 2
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = True
    
    # Palindrome độ dài >= 3
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if arr[i] == arr[j]:
                if length == 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            
            # Kiểm tra subsequence
            dp[i][j] = dp[i][j] or dp[i + 1][j] or dp[i][j - 1]
            
            if dp[i][j] and length >= 3:
                return True
    
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if has_palindrome_dp(a):
        print("YES")
    else:
        print("NO")
```

## Code chính xác nhất

```python
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Kiểm tra có palindrome subsequence độ dài >= 3
    # Đơn giản nhất: tìm a[i] = a[j] với j - i >= 2
    
    for i in range(n):
        for j in range(i + 2, n):
            if a[i] == a[j]:
                return "YES"
    
    return "NO"

t = int(input())
for _ in range(t):
    print(solve())
```

## Giải thích

1. Palindrome subsequence ngắn nhất có độ dài 3: a[i] = a[k] với i < j < k
2. Nếu tồn tại 2 phần tử bằng nhau cách nhau ít nhất 2 vị trí → có palindrome độ dài 3
3. Duyệt tất cả cặp (i,j) với j-i >= 2 và kiểm tra a[i] = a[j]

**Độ phức tạp:** O(N²) cho mỗi test case