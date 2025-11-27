# CAMPING - Solution

## Phân tích

Bài toán yêu cầu tìm thứ tự khu trại của Anh dựa trên điểm số.

Quy tắc:
- Người có cùng điểm ở chung khu trại
- Người có điểm cao hơn ở khu trại có số thứ tự cao hơn
- Khu trại được đánh số từ 1

Vậy ta cần:
1. Tìm tất cả điểm số khác nhau
2. Sắp xếp tăng dần
3. Tìm vị trí của điểm X trong danh sách đã sắp xếp

## Thuật toán

1. Thu thập tất cả điểm số (bao gồm cả điểm của Anh)
2. Loại bỏ trùng lặp và sắp xếp
3. Tìm vị trí của điểm X

## Code

```python
n, x = map(int, input().split())
scores = list(map(int, input().split()))

# Thêm điểm của Anh vào danh sách
all_scores = scores + [x]

# Loại bỏ trùng lặp và sắp xếp
unique_scores = sorted(set(all_scores))

# Tìm vị trí của điểm x (1-indexed)
camp_number = unique_scores.index(x) + 1

print(camp_number)
```

## Code tối ưu hơn

```python
n, x = map(int, input().split())
scores = list(map(int, input().split()))

# Đếm số điểm khác nhau nhỏ hơn x
unique_lower = set()
for score in scores:
    if score < x:
        unique_lower.add(score)

# Thứ tự khu trại = số điểm nhỏ hơn + 1
camp_number = len(unique_lower) + 1

print(camp_number)
```

## Giải thích

1. Khu trại được sắp xếp theo điểm tăng dần
2. Thứ tự khu trại của Anh = số lượng điểm khác nhau nhỏ hơn điểm của Anh + 1
3. Sử dụng set để loại bỏ trùng lặp

**Độ phức tạp:** O(N) với cách 2, O(N log N) với cách 1