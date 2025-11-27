# POTM - Solution

## Phân tích

Bài toán yêu cầu:
- Type 0: Tổng k số nhỏ nhất trong x số đầu tiên
- Type 1: Tổng k số lớn nhất trong x số đầu tiên

Vì mảng đã tăng dần:
- k số nhỏ nhất trong x số đầu = a[0] + a[1] + ... + a[k-1]
- k số lớn nhất trong x số đầu = a[x-k] + a[x-k+1] + ... + a[x-1]

## Thuật toán

Sử dụng prefix sum để tính tổng nhanh:
- prefix[i] = a[0] + a[1] + ... + a[i-1]
- Tổng từ l đến r = prefix[r+1] - prefix[l]

## Code

```python
n, q = map(int, input().split())
a = list(map(int, input().split()))

# Tính prefix sum
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + a[i]

for _ in range(q):
    type_query, x, k = map(int, input().split())
    
    if type_query == 0:
        # k số nhỏ nhất trong x số đầu tiên
        # Tức là từ vị trí 0 đến k-1
        result = prefix[k] - prefix[0]
    else:
        # k số lớn nhất trong x số đầu tiên  
        # Tức là từ vị trí x-k đến x-1
        result = prefix[x] - prefix[x - k]
    
    print(result)
```

## Code đơn giản hơn

```python
n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    type_query, x, k = map(int, input().split())
    
    if type_query == 0:
        # k số nhỏ nhất trong x số đầu tiên
        result = sum(a[:k])
    else:
        # k số lớn nhất trong x số đầu tiên
        result = sum(a[x-k:x])
    
    print(result)
```

## Giải thích

1. Mảng đã sắp xếp tăng dần nên không cần sort
2. k số nhỏ nhất = k số đầu tiên
3. k số lớn nhất trong x số đầu = k số cuối trong x số đầu
4. Dùng prefix sum để tối ưu từ O(Q×K) xuống O(N+Q)

**Độ phức tạp:** O(N+Q) với prefix sum, O(Q×K) không tối ưu