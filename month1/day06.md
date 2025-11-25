# Day 6: Pattern printing và ứng dụng vòng lặp trong Olympic

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Pattern printing cơ bản (45')

### 📚 Lý thuyết (15')

#### Nguyên lý pattern printing
```python
# Pattern cơ bản: hình chữ nhật
rows, cols = 4, 6
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()  # Xuống dòng

# Kết quả:
# ******
# ******
# ******
# ******
```

#### Các loại pattern cơ bản
```python
# 1. Tam giác vuông
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# 2. Tam giác vuông ngược
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# 3. Tam giác cân
for i in range(1, n + 1):
    # In khoảng trắng
    for j in range(n - i):
        print(" ", end="")
    # In sao
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```

#### Phân tích pattern
```python
# Để tạo pattern, cần phân tích:
# 1. Số hàng (rows)
# 2. Mỗi hàng có gì: khoảng trắng, ký tự, số lượng
# 3. Quy luật thay đổi theo hàng

# Ví dụ: Tam giác số
# 1
# 12
# 123
# 1234

n = 4
for i in range(1, n + 1):      # Hàng từ 1 đến n
    for j in range(1, i + 1):  # Số từ 1 đến i
        print(j, end="")
    print()
```

### 💻 Thực hành (30')

#### Bài tập 1: Các pattern cơ bản

**Yêu cầu:** Tạo các pattern cơ bản: hình vuông rỗng, tam giác số, tam giác cân, hình thoi và pattern chữ X.

**File thực hành:** [problem060101.py](problem060101.py)

#### Bài tập 2: Pattern với chữ cái

**Yêu cầu:** Tạo pattern với chữ cái: tam giác chữ cái, tam giác cân đối, pattern lặp và hình thoi chữ cái.

**File thực hành:** [problem060102.py](problem060102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Pattern số học và toán học (45')

### 📚 Lý thuyết (20')

#### Pattern số học
```python
# 1. Tam giác Pascal
def pascal_triangle(n):
    for i in range(n):
        # In khoảng trắng
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Tính và in số Pascal
        num = 1
        for j in range(i + 1):
            print(f"{num:2d}", end="")
            num = num * (i - j) // (j + 1)
        print()

# 2. Dãy Fibonacci trong pattern
def fibonacci_pattern(n):
    fib = [0, 1]
    while len(fib) < n * (n + 1) // 2:
        fib.append(fib[-1] + fib[-2])
    
    index = 0
    for i in range(1, n + 1):
        for j in range(i):
            print(f"{fib[index]:3d}", end=" ")
            index += 1
        print()
```

#### Pattern toán học phức tạp
```python
# 1. Ma phương (Magic Square)
def create_magic_square(n):
    # Chỉ hoạt động với n lẻ
    if n % 2 == 0:
        return None
    
    magic_square = [[0] * n for _ in range(n)]
    
    # Bắt đầu từ giữa hàng đầu
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        
        # Di chuyển lên trên và sang phải
        next_i, next_j = (i - 1) % n, (j + 1) % n
        
        # Nếu ô đã có số, di chuyển xuống dưới
        if magic_square[next_i][next_j] != 0:
            i = (i + 1) % n
        else:
            i, j = next_i, next_j
    
    return magic_square

# 2. Xoắn ốc (Spiral)
def create_spiral(n):
    matrix = [[0] * n for _ in range(n)]
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while top <= bottom and left <= right:
        # Đi từ trái sang phải
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1
        
        # Đi từ trên xuống dưới
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Đi từ phải sang trái
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
        
        # Đi từ dưới lên trên
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    return matrix
```

### 💻 Thực hành (25')

#### Bài tập 1: Pattern số học nâng cao

**Yêu cầu:** Tạo pattern số học phức tạp: tam giác Pascal, Fibonacci, số nguyên tố, số chính phương và tổng hàng.

**File thực hành:** [problem060201.py](problem060201.py)

#### Bài tập 2: Ma trận đặc biệt

**Yêu cầu:** Tạo các ma trận đặc biệt: xoắn ốc, ma phương, đối xứng và đường chéo.

**File thực hành:** [problem060202.py](problem060202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Ứng dụng vòng lặp trong bài toán Olympic (45')

### 📚 Lý thuyết (15')

#### Thuật toán tìm kiếm
```python
# 1. Tìm kiếm tuyến tính với điều kiện
def linear_search_condition(arr, condition):
    for i, element in enumerate(arr):
        if condition(element):
            return i, element
    return -1, None

# 2. Tìm tất cả phần tử thỏa mãn
def find_all_matching(arr, condition):
    results = []
    for i, element in enumerate(arr):
        if condition(element):
            results.append((i, element))
    return results

# 3. Tìm kiếm với nhiều điều kiện
def complex_search(arr, conditions):
    for i, element in enumerate(arr):
        if all(condition(element) for condition in conditions):
            return i, element
    return -1, None
```

#### Thuật toán xử lý dãy số
```python
# 1. Tìm dãy con có tổng lớn nhất (Kadane's algorithm)
def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0
    
    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end

# 2. Tìm dãy con tăng dài nhất
def longest_increasing_subsequence(arr):
    if not arr:
        return []
    
    n = len(arr)
    lengths = [1] * n
    parents = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                parents[i] = j
    
    # Tìm vị trí có độ dài lớn nhất
    max_length = max(lengths)
    max_index = lengths.index(max_length)
    
    # Xây dựng dãy con
    result = []
    current = max_index
    while current != -1:
        result.append(arr[current])
        current = parents[current]
    
    return result[::-1]
```

### 💻 Thực hành (30')

#### Bài tập 1: Thuật toán tìm kiếm Olympic

**Yêu cầu:** Implement các thuật toán tìm kiếm: Two Sum, tìm phần tử xuất hiện nhiều nhất, missing number và intersection.

**File thực hành:** [problem060301.py](problem060301.py)

#### Bài tập 2: Xử lý dãy số Olympic

**Yêu cầu:** Implement các thuật toán xử lý dãy số: Kadane's algorithm, LIS, cycle detection và tìm peak/valley.

**File thực hành:** [problem060302.py](problem060302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Tối ưu hóa và kỹ thuật nâng cao (45')

### 📚 Lý thuyết (15')

#### Tối ưu hóa vòng lặp
```python
# 1. Early termination
def find_first_match(arr, condition):
    for i, element in enumerate(arr):
        if condition(element):
            return i, element  # Dừng ngay khi tìm thấy
    return -1, None

# 2. Skip unnecessary iterations
def process_even_numbers(arr):
    for i in range(0, len(arr), 2):  # Chỉ xét index chẵn
        process(arr[i])

# 3. Reduce nested loops
def optimized_pair_search(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False
```

#### Kỹ thuật sliding window
```python
# Sliding window cho subarray
def max_sum_subarray_k(arr, k):
    """Tìm tổng lớn nhất của subarray có độ dài k"""
    if len(arr) < k:
        return None
    
    # Tính tổng window đầu tiên
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Trượt window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Sliding window cho string
def longest_substring_without_repeating(s):
    """Tìm substring dài nhất không có ký tự lặp"""
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

#### Two pointers technique
```python
# Two pointers cho sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return -1, -1

# Two pointers cho palindrome
def is_palindrome_two_pointers(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

### 💻 Thực hành (30')

#### Bài tập 1: Kỹ thuật tối ưu hóa

**Yêu cầu:** So sánh hiệu suất thuật toán, sliding window technique và two pointers technique.

**File thực hành:** [problem060401.py](problem060401.py)

#### Bài tập 2: Ứng dụng tổng hợp

**Yêu cầu:** Phân tích dữ liệu bán hàng và tạo game tìm kho báu với các kỹ thuật đã học.

**File thực hành:** [problem060402.py](problem060402.py)

---

## Bài tập về nhà

### Bài 1: Tạo ASCII Art Generator
Viết chương trình tạo ASCII art:
- Nhập text và chọn font (small, medium, large)
- Tạo các ký tự bằng pattern *
- Hỗ trợ ít nhất 5 ký tự: A, B, C, D, E
- Có thể ghép nhiều ký tự thành từ

### Bài 2: Thuật toán sắp xếp với visualization
Implement bubble sort với visualization:
- In từng bước sắp xếp
- Highlight các phần tử đang so sánh
- Đếm số lần so sánh và hoán đổi
- So sánh với selection sort

### Bài 3: Game Snake đơn giản (text-based)
Tạo game rắn săn mồi trong terminal:
- Bản đồ 20x10 với viền
- Rắn di chuyển theo hướng (W/A/S/D)
- Mồi xuất hiện ngẫu nhiên
- Rắn tăng độ dài khi ăn mồi
- Game over khi đâm tường hoặc tự cắn

### Gợi ý làm bài
1. Sử dụng nested loops cho pattern phức tạp
2. Break down bài toán lớn thành các function nhỏ
3. Sử dụng clear screen cho animation (import os; os.system('clear'))
4. Test kỹ với các edge cases

---

## Tổng kết Day 6

**Đã học:**
- Pattern printing: cơ bản đến nâng cao
- Ma trận đặc biệt: xoắn ốc, ma phương, đối xứng
- Thuật toán tìm kiếm Olympic: two sum, missing number, intersection
- Xử lý dãy số: Kadane's algorithm, LIS, cycle detection
- Kỹ thuật tối ưu hóa: sliding window, two pointers
- Ứng dụng thực tế: phân tích dữ liệu, game

**Chuẩn bị cho Tuần 3:**
- Ôn lại tất cả vòng lặp (for, while, nested)
- Thực hành pattern printing và thuật toán
- Làm xong bài tập về nhà
- Chuẩn bị học List và Tuple (Day 7)