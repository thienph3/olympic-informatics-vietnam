# GOAL - Solution

## Phân tích

Quy tắc bắn:
- Bắn trúng: 1 điểm
- Sau 9 phát, nếu trúng: thêm 2 điểm thưởng (tổng 3 điểm)
- Sau 14 phát trúng liên tiếp: phát tiếp theo chắc chắn hụt, sau đó reset

Pattern lặp lại:
- 14 phát trúng + 1 phát hụt = 15 phát/chu kỳ
- Điểm mỗi chu kỳ: 14 + 2 = 16 điểm (phát thứ 10 có thưởng)

## Thuật toán

1. Tính số chu kỳ hoàn chỉnh (15 phát/chu kỳ)
2. Tính điểm cho phần còn lại
3. Xử lý trường hợp đặc biệt cho phát thứ 10

## Code

```python
n = int(input())

if n == 0:
    print(0)
else:
    # Mỗi chu kỳ: 14 trúng + 1 hụt = 15 phát
    # Điểm mỗi chu kỳ: 14 + 2 (thưởng phát 10) = 16 điểm
    
    full_cycles = n // 15
    remaining = n % 15
    
    total_score = full_cycles * 16
    
    # Xử lý phần còn lại
    if remaining > 0:
        if remaining <= 14:
            # Tất cả đều trúng
            hits = remaining
            total_score += hits
            
            # Kiểm tra có phát thứ 10 không
            if remaining >= 10:
                total_score += 2  # Thưởng phát thứ 10
        else:
            # remaining = 15, có 14 trúng + 1 hụt
            total_score += 14 + 2  # 14 trúng + thưởng phát 10
    
    print(total_score)
```

## Code đơn giản hơn

```python
n = int(input())

total_score = 0
shots = 0
consecutive_hits = 0

while shots < n:
    shots += 1
    
    if consecutive_hits < 14:
        # Bắn trúng
        total_score += 1
        consecutive_hits += 1
        
        # Thưởng sau 9 phát
        if consecutive_hits == 10:
            total_score += 2
    else:
        # Phát thứ 15: hụt và reset
        consecutive_hits = 0

print(total_score)
```

## Giải thích

1. Mỗi 15 phát tạo thành 1 chu kỳ: 14 trúng + 1 hụt
2. Điểm mỗi chu kỳ: 14 (cơ bản) + 2 (thưởng phát 10) = 16
3. Xử lý phần dư theo quy tắc tương tự

**Độ phức tạp:** O(1) với cách tối ưu, O(N) với simulation