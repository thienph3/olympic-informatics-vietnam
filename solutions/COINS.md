# COINS - Solution

## Phân tích

Bài toán yêu cầu chia M đồng vàng (mỗi đồng giá trị K) cho 2 em sao cho chênh lệch tổng giá trị nhỏ nhất.

Ban đầu:
- Linh có A đồng (giá trị 1 mỗi đồng) 
- Lan có B đồng (giá trị 1 mỗi đồng)

Gọi x là số đồng vàng (giá trị K) cho Linh, thì Lan được (M-x) đồng.

Tổng giá trị:
- Linh: A + x*K
- Lan: B + (M-x)*K

Chênh lệch = |A + x*K - B - (M-x)*K| = |A - B + 2*x*K - M*K|

Để tối thiểu hóa, ta cần tìm x sao cho |A - B + K*(2*x - M)| nhỏ nhất.

## Code

```python
M, K, A, B = map(int, input().split())

min_diff = float('inf')

for x in range(M + 1):
    linh_total = A + x * K
    lan_total = B + (M - x) * K
    diff = abs(linh_total - lan_total)
    min_diff = min(min_diff, diff)

print(min_diff)
```

## Giải thích

1. Duyệt tất cả cách chia từ 0 đến M đồng cho Linh
2. Tính tổng giá trị của mỗi em
3. Tìm chênh lệch nhỏ nhất

**Độ phức tạp:** O(M)