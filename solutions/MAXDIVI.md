# MAXDIVI - Solution

## Phân tích

Để tất cả phần tử có cùng số dư khi chia cho M, ta cần:
a₁ ≡ a₂ ≡ ... ≡ aₙ (mod M)

Điều này có nghĩa là M phải chia hết hiệu của bất kỳ 2 phần tử nào:
M | (aᵢ - aⱼ) với mọi i, j

Vậy M phải là ước chung của tất cả hiệu số. M lớn nhất chính là GCD của tất cả hiệu số.

## Thuật toán

1. Tính tất cả hiệu số |aᵢ - aⱼ| với i < j
2. Tìm GCD của tất cả hiệu số đó
3. Hoặc tối ưu: GCD của tất cả |aᵢ - a₁|

## Code

```python
import math

n = int(input())
a = list(map(int, input().split()))

# Tính GCD của tất cả hiệu với phần tử đầu tiên
result = 0
for i in range(1, n):
    diff = abs(a[i] - a[0])
    result = math.gcd(result, diff)

print(result)
```

## Giải thích

1. Thay vì tính tất cả hiệu số O(n²), ta chỉ cần tính hiệu với a[0]
2. GCD của |a₁-a₀|, |a₂-a₀|, ..., |aₙ₋₁-a₀| = GCD của tất cả hiệu số
3. Sử dụng tính chất: gcd(0, x) = x

**Độ phức tạp:** O(N log(max(a)))