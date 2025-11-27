# MAZE - Solution

## Phân tích

Long cần đi từ phòng 1 đến phòng n+1. Cửa i mở mỗi a[i] giây.

Tại thời điểm t, cửa i mở khi t % a[i] == 0.

Long đến phòng i tại thời điểm current_time, cần đợi đến lần mở cửa tiếp theo.

## Thuật toán

1. Bắt đầu tại phòng 1, thời điểm 0
2. Với mỗi cửa i:
   - Tính thời điểm mở cửa tiếp theo >= current_time
   - Cập nhật current_time

## Code

```python
n = int(input())
a = list(map(int, input().split()))

current_time = 0

for i in range(n):
    # Cửa i mở tại các thời điểm: a[i], 2*a[i], 3*a[i], ...
    # Tìm thời điểm mở cửa đầu tiên >= current_time
    
    if current_time % a[i] == 0:
        # Cửa đang mở
        next_open = current_time
    else:
        # Tìm lần mở tiếp theo
        next_open = ((current_time // a[i]) + 1) * a[i]
    
    current_time = next_open

print(current_time)
```

## Code tối ưu hơn

```python
import math

n = int(input())
a = list(map(int, input().split()))

current_time = 0

for period in a:
    # Tìm thời điểm mở cửa tiếp theo >= current_time
    # Cửa mở tại: period, 2*period, 3*period, ...
    
    # Số lần mở cần thiết
    cycles_needed = math.ceil(current_time / period)
    next_open_time = cycles_needed * period
    
    current_time = next_open_time

print(current_time)
```

## Code đơn giản nhất

```python
n = int(input())
a = list(map(int, input().split()))

time = 0

for period in a:
    # Nếu thời gian hiện tại không chia hết cho period
    # thì phải đợi đến lần mở tiếp theo
    if time % period != 0:
        time = ((time // period) + 1) * period

print(time)
```

## Giải thích

1. Long bắt đầu tại thời điểm 0
2. Với mỗi cửa có chu kỳ a[i]:
   - Nếu thời gian hiện tại chia hết cho a[i]: cửa đang mở
   - Ngược lại: đợi đến lần mở tiếp theo
3. Cập nhật thời gian và tiếp tục

**Độ phức tạp:** O(N)