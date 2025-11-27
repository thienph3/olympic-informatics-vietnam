# LINEUP - Solution

## Phân tích

Bài toán yêu cầu xếp N cặp figure thành 2 hàng sao cho tổng mỗi hàng là số chẵn.

Quan sát:
- Tổng chẵn khi có số chẵn số lẻ
- Mỗi cặp (a,b) có thể đóng góp: a (hàng 1), b (hàng 2) hoặc ngược lại
- Cần phân loại cặp theo tính chẵn lẻ

## Phân loại cặp

1. **EE**: cả 2 đều chẵn → luôn đóng góp chẵn cho cả 2 hàng
2. **OO**: cả 2 đều lẻ → luôn đóng góp lẻ cho cả 2 hàng  
3. **EO**: 1 chẵn 1 lẻ → có thể chọn đóng góp chẵn hoặc lẻ

## Thuật toán

Để 2 hàng đều chẵn:
- Số lẻ ở mỗi hàng phải chẵn
- Dùng cặp OO để cân bằng (mỗi cặp OO đóng góp 1 lẻ cho mỗi hàng)
- Dùng cặp EO để điều chỉnh

## Code

```python
n = int(input())
pairs = []
for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

# Phân loại cặp
ee_count = 0  # Cả 2 chẵn
oo_count = 0  # Cả 2 lẻ  
eo_count = 0  # 1 chẵn 1 lẻ

for a, b in pairs:
    if a % 2 == 0 and b % 2 == 0:
        ee_count += 1
    elif a % 2 == 1 and b % 2 == 1:
        oo_count += 1
    else:
        eo_count += 1

# Kiểm tra khả năng
# Mỗi cặp OO đóng góp 1 lẻ cho mỗi hàng
# Cần số lẻ ở mỗi hàng là chẵn
# Tổng số lẻ = oo_count * 2 + eo_count (tối đa)

total_odd = oo_count * 2
if total_odd % 2 != 0:
    # Tổng lẻ là lẻ, không thể chia đều
    print(-1)
else:
    # Có thể chia đều
    # Mỗi hàng cần oo_count số lẻ
    # Nếu oo_count lẻ, cần thêm 1 lẻ từ EO cho mỗi hàng
    
    if oo_count % 2 == 0:
        # oo_count chẵn, mỗi hàng có số lẻ chẵn
        print(0)
    else:
        # oo_count lẻ, cần thêm 1 lẻ cho mỗi hàng
        if eo_count >= 2:
            # Có đủ EO để cân bằng
            print(0)
        else:
            # Không đủ EO
            print(-1)
```

## Code chính xác hơn

```python
n = int(input())
pairs = []
for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

# Đếm các loại cặp
both_even = 0
both_odd = 0  
mixed = 0

for a, b in pairs:
    if a % 2 == b % 2 == 0:
        both_even += 1
    elif a % 2 == b % 2 == 1:
        both_odd += 1
    else:
        mixed += 1

# Để 2 hàng đều có tổng chẵn:
# Số phần tử lẻ ở mỗi hàng phải chẵn

# both_odd cặp: mỗi cặp đóng góp 1 lẻ cho mỗi hàng
# mixed cặp: có thể chọn đóng góp 0 hoặc 1 lẻ cho mỗi hàng

if both_odd % 2 == 0:
    # both_odd chẵn → mỗi hàng đã có số lẻ chẵn
    print(0)
else:
    # both_odd lẻ → cần thêm 1 lẻ cho mỗi hàng
    if mixed >= 2:
        # Dùng 2 cặp mixed: 1 cặp cho hàng 1, 1 cặp cho hàng 2
        print(0)
    elif mixed == 1:
        # Chỉ có 1 cặp mixed → không thể cân bằng
        print(-1)
    else:
        # Không có cặp mixed
        print(-1)
```

## Giải thích

1. Phân loại cặp theo tính chẵn lẻ
2. Cặp (chẵn,chẵn): không ảnh hưởng tính chẵn lẻ
3. Cặp (lẻ,lẻ): mỗi hàng nhận 1 số lẻ
4. Cặp (chẵn,lẻ): linh hoạt chọn hàng nhận số lẻ

**Độ phức tạp:** O(N)