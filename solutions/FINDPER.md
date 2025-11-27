# FINDPER - Solution

## Phân tích

Bài toán mô phỏng quá trình:
1. Thêm phần tử vào cuối dãy B
2. Đảo ngược dãy B

Thay vì thực hiện đảo ngược thật, ta có thể tối ưu bằng cách theo dõi hướng thêm phần tử.

## Thuật toán tối ưu

- Sử dụng deque để thêm vào đầu/cuối hiệu quả
- Theo dõi biến `reverse` để biết hướng hiện tại
- Nếu `reverse = False`: thêm vào cuối
- Nếu `reverse = True`: thêm vào đầu

## Code

```python
from collections import deque

n = int(input())
a = list(map(int, input().split()))

B = deque()
reverse = False

for i in range(n):
    if not reverse:
        B.append(a[i])
    else:
        B.appendleft(a[i])
    reverse = not reverse

if reverse:
    B.reverse()

print(*B)
```

## Giải thích

1. Dùng deque để thêm vào đầu/cuối O(1)
2. Biến `reverse` theo dõi trạng thái đảo ngược
3. Cuối cùng nếu `reverse = True` thì đảo lại một lần

**Độ phức tạp:** O(N)