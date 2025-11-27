# STRGCD - Solution

## Phân tích

Tìm xâu x dài nhất sao cho:
- A = x + x + ... + x (k lần)
- B = x + x + ... + x (m lần)

Tương tự GCD của số, ta cần tìm "GCD" của xâu.

## Thuật toán

1. Độ dài của x phải là ước chung của |A| và |B|
2. x phải là tiền tố của cả A và B
3. Kiểm tra từ độ dài lớn nhất xuống nhỏ nhất

## Code

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def can_divide(s, pattern):
    """Kiểm tra xem pattern có chia hết s không"""
    if len(s) % len(pattern) != 0:
        return False
    
    times = len(s) // len(pattern)
    return pattern * times == s

def solve(A, B):
    len_a, len_b = len(A), len(B)
    
    # Độ dài GCD phải là ước chung của len_a và len_b
    gcd_len = gcd(len_a, len_b)
    
    # Kiểm tra từ độ dài lớn nhất xuống
    for length in range(gcd_len, 0, -1):
        if gcd_len % length == 0:
            # Lấy tiền tố có độ dài length
            candidate = A[:length]
            
            # Kiểm tra xem candidate có chia hết cả A và B không
            if can_divide(A, candidate) and can_divide(B, candidate):
                return candidate
    
    return "NOTFOUND"

A = input().strip()
B = input().strip()
print(solve(A, B))
```

## Code tối ưu hơn

```python
import math

def string_gcd(A, B):
    """Tìm GCD của 2 xâu"""
    len_a, len_b = len(A), len(B)
    
    # Độ dài GCD phải là GCD của 2 độ dài
    gcd_length = math.gcd(len_a, len_b)
    
    # Ứng viên GCD là tiền tố có độ dài gcd_length
    candidate = A[:gcd_length]
    
    # Kiểm tra xem candidate có tạo nên cả A và B không
    if (candidate * (len_a // gcd_length) == A and 
        candidate * (len_b // gcd_length) == B):
        return candidate
    
    return "NOTFOUND"

A = input().strip()
B = input().strip()
print(string_gcd(A, B))
```

## Code đơn giản nhất

```python
import math

A = input().strip()
B = input().strip()

# Tìm GCD của độ dài
gcd_len = math.gcd(len(A), len(B))

# Ứng viên là tiền tố có độ dài gcd_len của A
candidate = A[:gcd_len]

# Kiểm tra
if (candidate * (len(A) // gcd_len) == A and 
    candidate * (len(B) // gcd_len) == B):
    print(candidate)
else:
    print("NOTFOUND")
```

## Giải thích

1. GCD của 2 xâu có độ dài = GCD của 2 độ dài xâu
2. GCD phải là tiền tố chung của cả 2 xâu
3. Kiểm tra xem tiền tố này có tạo nên được cả 2 xâu không

**Độ phức tạp:** O(|A| + |B|)