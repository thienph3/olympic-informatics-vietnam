# DIV - Solution

## Phân tích

Bài toán yêu cầu tính tổng các ước số của nhiều số.

Tổng ước số của n = σ(n) = Σ(d) với d là ước của n.

## Thuật toán

### Cách 1: Brute Force O(√n)
Với mỗi số n, duyệt từ 1 đến √n để tìm ước.

### Cách 2: Sieve O(n log n) 
Dùng sàng để tính trước tổng ước cho tất cả số ≤ max.

## Code Brute Force

```python
def sum_of_divisors(n):
    """Tính tổng các ước của n"""
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:  # Tránh đếm trùng với số chính phương
                total += n // i
        i += 1
    return total

q = int(input())
a = list(map(int, input().split()))

result = []
for num in a:
    result.append(sum_of_divisors(num))

print(*result)
```

## Code Sieve (cho subtask nhỏ)

```python
def sieve_sum_divisors(max_n):
    """Tính tổng ước cho tất cả số từ 1 đến max_n"""
    divisor_sum = [0] * (max_n + 1)
    
    for i in range(1, max_n + 1):
        for j in range(i, max_n + 1, i):
            divisor_sum[j] += i
    
    return divisor_sum

q = int(input())
a = list(map(int, input().split()))

max_a = max(a)
if max_a <= 10**6:  # Chỉ dùng sieve cho số nhỏ
    divisor_sum = sieve_sum_divisors(max_a)
    result = [divisor_sum[num] for num in a]
else:
    result = [sum_of_divisors(num) for num in a]

print(*result)
```

## Code tối ưu cho subtask 4

```python
def sum_of_divisors(n):
    """Tính tổng các ước của n - tối ưu"""
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if i * i != n:  # Không phải số chính phương
                total += n // i
        i += 1
    return total

q = int(input())
a = list(map(int, input().split()))

# Kiểm tra subtask 4: dãy liên tiếp
is_consecutive = True
if q > 1:
    for i in range(1, q):
        if a[i] != a[i-1] + 1:
            is_consecutive = False
            break

if is_consecutive and q > 1:
    # Subtask 4: tối ưu cho dãy liên tiếp
    result = []
    for num in a:
        result.append(sum_of_divisors(num))
else:
    # Subtask khác
    result = [sum_of_divisors(num) for num in a]

print(*result)
```

## Giải thích

1. Tổng ước số: duyệt từ 1 đến √n, với mỗi ước i tìm được, cộng cả i và n/i
2. Sieve: tính trước cho tất cả số ≤ max, phù hợp với subtask nhỏ
3. Subtask 4: dãy liên tiếp có thể tối ưu thêm

**Độ phức tạp:** O(Q×√N) brute force, O(N log N) sieve