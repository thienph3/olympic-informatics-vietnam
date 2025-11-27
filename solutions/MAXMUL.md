# MAXMUL - Solution

## Phân tích

Bài toán yêu cầu tính tích của k phần tử liên tiếp bắt đầu từ vị trí u.

Với mỗi query (u, k), ta cần tính: a[u-1] × a[u] × ... × a[u+k-2] (chuyển về 0-indexed)

## Thuật toán

### Cách 1: Brute Force (O(T×K))
Với mỗi query, duyệt k phần tử và tính tích.

### Cách 2: Prefix Product (O(N+T))
Sử dụng mảng tích tiền tố để tính nhanh.

## Code

```python
MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))
t = int(input())

# Prefix product array
prefix = [1] * (n + 1)
for i in range(n):
    prefix[i + 1] = (prefix[i] * a[i]) % MOD

# Modular inverse function
def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)

for _ in range(t):
    u, k = map(int, input().split())
    u -= 1  # Convert to 0-indexed
    
    # Product from u to u+k-1
    numerator = prefix[u + k]
    denominator = prefix[u]
    
    if denominator == 0:
        # Handle case where there's a 0 in the range
        result = 0
        for i in range(u, u + k):
            if a[i] == 0:
                result = 0
                break
            result = (result * a[i]) % MOD if result != 0 else a[i]
    else:
        result = (numerator * mod_inverse(denominator, MOD)) % MOD
    
    print(result)
```

## Code đơn giản hơn

```python
MOD = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))
t = int(input())

for _ in range(t):
    u, k = map(int, input().split())
    u -= 1  # Convert to 0-indexed
    
    result = 1
    for i in range(u, u + k):
        result = (result * a[i]) % MOD
    
    print(result)
```

## Giải thích

1. Với mỗi query (u, k), tính tích từ vị trí u-1 đến u+k-2 (0-indexed)
2. Sử dụng modulo để tránh overflow
3. Cách 1 dùng prefix product, cách 2 đơn giản hơn

**Độ phức tạp:** O(T×K) hoặc O(N+T) với prefix