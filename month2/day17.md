# Day 17: Counting Sort, Radix Sort, Bucket Sort

## Mục tiêu học tập

Sau buổi học này, học sinh sẽ:
- Hiểu và implement counting sort cho dữ liệu có phạm vi giới hạn
- Nắm vững radix sort cho sắp xếp số nguyên và chuỗi
- Thành thạo bucket sort cho dữ liệu phân bố đều
- Phân tích độ phức tạp và ứng dụng của từng thuật toán
- Áp dụng vào các bài toán Olympic thực tế

## Phần 1: Counting Sort (45 phút)

### 1.1 Nguyên lý Counting Sort

Counting sort là thuật toán sắp xếp không so sánh, hoạt động bằng cách đếm số lần xuất hiện của mỗi phần tử.

**Ưu điểm:**
- Độ phức tạp O(n + k) với k là phạm vi giá trị
- Stable sorting (giữ thứ tự tương đối)
- Hiệu quả với dữ liệu có phạm vi nhỏ

**Nhược điểm:**
- Chỉ áp dụng được với số nguyên hoặc dữ liệu rời rạc
- Tốn bộ nhớ O(k) cho mảng đếm

### 1.2 Implementation Cơ bản

```python
def counting_sort(arr):
    if not arr:
        return arr
    
    # Tìm min, max để xác định phạm vi
    min_val, max_val = min(arr), max(arr)
    range_val = max_val - min_val + 1
    
    # Mảng đếm
    count = [0] * range_val
    
    # Đếm số lần xuất hiện
    for num in arr:
        count[num - min_val] += 1
    
    # Tái tạo mảng đã sắp xếp
    result = []
    for i in range(range_val):
        result.extend([i + min_val] * count[i])
    
    return result
```

### 1.3 Counting Sort Stable

```python
def counting_sort_stable(arr):
    if not arr:
        return arr
    
    min_val, max_val = min(arr), max(arr)
    range_val = max_val - min_val + 1
    
    count = [0] * range_val
    
    # Đếm tần suất
    for num in arr:
        count[num - min_val] += 1
    
    # Tính tổng tích lũy
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    # Xây dựng kết quả từ cuối về đầu
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        idx = arr[i] - min_val
        result[count[idx] - 1] = arr[i]
        count[idx] -= 1
    
    return result
```

## Phần 2: Radix Sort (45 phút)

### 2.1 Nguyên lý Radix Sort

Radix sort sắp xếp từng chữ số/ký tự từ phải sang trái (LSD) hoặc trái sang phải (MSD).

**Ưu điểm:**
- Độ phức tạp O(d × (n + k)) với d là số chữ số
- Stable sorting
- Hiệu quả với số nguyên lớn

### 2.2 LSD Radix Sort

```python
def radix_sort_lsd(arr):
    if not arr:
        return arr
    
    # Tìm số có nhiều chữ số nhất
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Đếm tần suất chữ số
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    # Tính tổng tích lũy
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Xây dựng mảng kết quả
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # Copy kết quả về mảng gốc
    for i in range(n):
        arr[i] = output[i]
```

### 2.3 MSD Radix Sort

```python
def radix_sort_msd(arr, exp=None):
    if len(arr) <= 1:
        return arr
    
    if exp is None:
        max_num = max(arr)
        exp = 1
        while max_num // exp >= 10:
            exp *= 10
    
    if exp < 1:
        return arr
    
    # Phân chia theo chữ số hiện tại
    buckets = [[] for _ in range(10)]
    
    for num in arr:
        digit = (num // exp) % 10
        buckets[digit].append(num)
    
    # Đệ quy sắp xếp từng bucket
    result = []
    for bucket in buckets:
        if bucket:
            result.extend(radix_sort_msd(bucket, exp // 10))
    
    return result
```

## Phần 3: Bucket Sort (45 phút)

### 3.1 Nguyên lý Bucket Sort

Bucket sort chia dữ liệu vào các bucket, sắp xếp từng bucket rồi nối lại.

**Ưu điểm:**
- Độ phức tạp trung bình O(n + k)
- Hiệu quả với dữ liệu phân bố đều
- Có thể song song hóa

### 3.2 Implementation Cơ bản

```python
def bucket_sort(arr, bucket_count=10):
    if len(arr) <= 1:
        return arr
    
    # Tìm min, max
    min_val, max_val = min(arr), max(arr)
    
    # Tạo buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Phân phối vào buckets
    range_val = max_val - min_val
    for num in arr:
        if range_val == 0:
            bucket_idx = 0
        else:
            bucket_idx = min(bucket_count - 1, 
                           int((num - min_val) * bucket_count / (range_val + 1)))
        buckets[bucket_idx].append(num)
    
    # Sắp xếp từng bucket và nối lại
    result = []
    for bucket in buckets:
        if bucket:
            bucket.sort()  # Có thể dùng insertion sort
            result.extend(bucket)
    
    return result
```

### 3.3 Bucket Sort cho Số Thực

```python
def bucket_sort_float(arr, bucket_count=10):
    if len(arr) <= 1:
        return arr
    
    # Tạo buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Phân phối (giả sử arr trong [0, 1))
    for num in arr:
        bucket_idx = min(bucket_count - 1, int(num * bucket_count))
        buckets[bucket_idx].append(num)
    
    # Sắp xếp từng bucket
    result = []
    for bucket in buckets:
        if bucket:
            bucket.sort()
            result.extend(bucket)
    
    return result
```

## Phần 4: So sánh và Ứng dụng (45 phút)

### 4.1 Bảng So sánh

| Thuật toán | Time Complexity | Space Complexity | Stable | Điều kiện |
|------------|----------------|------------------|--------|-----------|
| Counting Sort | O(n + k) | O(k) | Yes | Phạm vi nhỏ |
| Radix Sort | O(d × (n + k)) | O(n + k) | Yes | Số nguyên |
| Bucket Sort | O(n + k) avg | O(n + k) | Yes | Phân bố đều |

### 4.2 Khi nào sử dụng

**Counting Sort:**
- Dữ liệu số nguyên với phạm vi nhỏ
- Cần stable sorting
- Đếm tần suất

**Radix Sort:**
- Số nguyên lớn hoặc chuỗi
- Cần stable sorting
- Nhiều chữ số/ký tự

**Bucket Sort:**
- Dữ liệu phân bố đều
- Số thực trong khoảng [0, 1)
- Có thể song song hóa

### 4.3 Ứng dụng trong Olympic

1. **Sắp xếp theo tần suất:** Counting sort
2. **Sắp xếp chuỗi:** Radix sort
3. **Sắp xếp điểm số:** Bucket sort
4. **Histogram:** Counting sort
5. **Sắp xếp IP address:** Radix sort

## Bài tập thực hành

1. **[problem170101.py]** - Counting Sort implementations
2. **[problem170102.py]** - Counting Sort applications  
3. **[problem170201.py]** - Radix Sort implementations
4. **[problem170202.py]** - Radix Sort applications
5. **[problem170301.py]** - Bucket Sort implementations
6. **[problem170302.py]** - Bucket Sort applications
7. **[problem170401.py]** - Algorithm comparison và analysis
8. **[problem170402.py]** - Mixed sorting problems

## Tổng kết

- Counting sort hiệu quả với dữ liệu có phạm vi nhỏ
- Radix sort phù hợp với số nguyên và chuỗi
- Bucket sort tốt với dữ liệu phân bố đều
- Tất cả đều là stable sorting algorithms
- Độ phức tạp tuyến tính trong điều kiện phù hợp