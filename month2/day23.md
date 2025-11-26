# Day 23: Chia để trị, Divide and Conquer Algorithms

## Mục tiêu học tập

Sau buổi học này, học sinh sẽ:
- Hiểu paradigm chia để trị (divide and conquer)
- Phân tích độ phức tạp bằng Master Theorem
- Implement các thuật toán chia để trị cổ điển
- Áp dụng chia để trị vào bài toán thực tế
- Tối ưu hóa thuật toán chia để trị
- Giải quyết bài toán Olympic bằng divide and conquer

## Phần 1: Khái niệm Divide and Conquer (45 phút)

### 1.1 Paradigm Chia để trị

**Nguyên lý:** Chia bài toán lớn thành các bài toán con nhỏ hơn, giải quyết từng bài toán con, rồi kết hợp kết quả.

**Ba bước cơ bản:**
1. **Divide:** Chia bài toán thành subproblems
2. **Conquer:** Giải quyết subproblems (đệ quy hoặc trực tiếp)
3. **Combine:** Kết hợp kết quả của subproblems

```python
def divide_and_conquer(problem):
    # Base case
    if problem_is_small(problem):
        return solve_directly(problem)
    
    # Divide
    subproblems = divide(problem)
    
    # Conquer
    results = []
    for subproblem in subproblems:
        results.append(divide_and_conquer(subproblem))
    
    # Combine
    return combine(results)
```

### 1.2 Ví dụ cơ bản - Maximum Subarray

```python
def max_subarray_divide_conquer(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    # Base case
    if low == high:
        return arr[low]
    
    # Divide
    mid = (low + high) // 2
    
    # Conquer
    left_sum = max_subarray_divide_conquer(arr, low, mid)
    right_sum = max_subarray_divide_conquer(arr, mid + 1, high)
    
    # Combine - find max crossing sum
    cross_sum = max_crossing_sum(arr, low, mid, high)
    
    return max(left_sum, right_sum, cross_sum)

def max_crossing_sum(arr, low, mid, high):
    # Find max sum for left side
    left_sum = float('-inf')
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        left_sum = max(left_sum, current_sum)
    
    # Find max sum for right side
    right_sum = float('-inf')
    current_sum = 0
    for i in range(mid + 1, high + 1):
        current_sum += arr[i]
        right_sum = max(right_sum, current_sum)
    
    return left_sum + right_sum
```

### 1.3 Master Theorem

**Dạng tổng quát:** T(n) = aT(n/b) + f(n)

**Ba trường hợp:**
1. **Case 1:** f(n) = O(n^c) với c < log_b(a) → T(n) = Θ(n^log_b(a))
2. **Case 2:** f(n) = Θ(n^c × log^k(n)) với c = log_b(a) → T(n) = Θ(n^c × log^(k+1)(n))
3. **Case 3:** f(n) = Ω(n^c) với c > log_b(a) → T(n) = Θ(f(n))

```python
def analyze_complexity():
    """Phân tích độ phức tạp các thuật toán chia để trị"""
    
    examples = {
        "Merge Sort": {
            "recurrence": "T(n) = 2T(n/2) + O(n)",
            "a": 2, "b": 2, "f(n)": "O(n)",
            "case": 2, "complexity": "O(n log n)"
        },
        "Binary Search": {
            "recurrence": "T(n) = T(n/2) + O(1)",
            "a": 1, "b": 2, "f(n)": "O(1)",
            "case": 2, "complexity": "O(log n)"
        },
        "Karatsuba Multiplication": {
            "recurrence": "T(n) = 3T(n/2) + O(n)",
            "a": 3, "b": 2, "f(n)": "O(n)",
            "case": 1, "complexity": "O(n^log_2(3)) ≈ O(n^1.585)"
        }
    }
    
    return examples
```

## Phần 2: Thuật toán Sorting (45 phút)

### 2.1 Merge Sort Chi tiết

```python
def merge_sort(arr):
    """
    Merge sort implementation
    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Combine
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_inplace(arr, temp_arr, left, right):
    """In-place merge sort to save space"""
    if left < right:
        mid = (left + right) // 2
        
        merge_sort_inplace(arr, temp_arr, left, mid)
        merge_sort_inplace(arr, temp_arr, mid + 1, right)
        merge_inplace(arr, temp_arr, left, mid, right)

def merge_inplace(arr, temp_arr, left, mid, right):
    """In-place merge operation"""
    # Copy to temp array
    for i in range(left, right + 1):
        temp_arr[i] = arr[i]
    
    i, j, k = left, mid + 1, left
    
    while i <= mid and j <= right:
        if temp_arr[i] <= temp_arr[j]:
            arr[k] = temp_arr[i]
            i += 1
        else:
            arr[k] = temp_arr[j]
            j += 1
        k += 1
    
    while i <= mid:
        arr[k] = temp_arr[i]
        i += 1
        k += 1
```

### 2.2 Quick Sort Variants

```python
def quick_sort_divide_conquer(arr):
    """Quick sort using divide and conquer approach"""
    if len(arr) <= 1:
        return arr
    
    # Divide
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Conquer and Combine
    return quick_sort_divide_conquer(left) + middle + quick_sort_divide_conquer(right)

def quick_sort_3way(arr, low=0, high=None):
    """3-way quick sort for arrays with duplicates"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition into 3 parts: <pivot, =pivot, >pivot
        lt, gt = partition_3way(arr, low, high)
        
        quick_sort_3way(arr, low, lt - 1)
        quick_sort_3way(arr, gt + 1, high)

def partition_3way(arr, low, high):
    """3-way partitioning"""
    pivot = arr[low]
    i = low
    lt = low
    gt = high
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt
```

## Phần 3: Thuật toán Tìm kiếm và Tính toán (45 phút)

### 3.1 Binary Search Variants

```python
def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive binary search"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def find_peak_element(arr):
    """Find peak element using divide and conquer"""
    def find_peak_helper(left, right):
        if left == right:
            return left
        
        mid = (left + right) // 2
        
        if arr[mid] > arr[mid + 1]:
            return find_peak_helper(left, mid)
        else:
            return find_peak_helper(mid + 1, right)
    
    return find_peak_helper(0, len(arr) - 1)

def search_rotated_array(arr, target):
    """Search in rotated sorted array"""
    def search_helper(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                return search_helper(left, mid - 1)
            else:
                return search_helper(mid + 1, right)
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                return search_helper(mid + 1, right)
            else:
                return search_helper(left, mid - 1)
    
    return search_helper(0, len(arr) - 1)
```

### 3.2 Fast Exponentiation

```python
def power_divide_conquer(base, exp):
    """
    Fast exponentiation using divide and conquer
    Time: O(log exp), Space: O(log exp)
    """
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    # Divide
    half = power_divide_conquer(base, exp // 2)
    
    # Combine
    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base

def matrix_power(matrix, n):
    """Matrix exponentiation using divide and conquer"""
    def matrix_multiply(A, B):
        rows_A, cols_A = len(A), len(A[0])
        rows_B, cols_B = len(B), len(B[0])
        
        result = [[0] * cols_B for _ in range(rows_A)]
        
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]
        
        return result
    
    def matrix_power_helper(mat, exp):
        if exp == 1:
            return mat
        
        half = matrix_power_helper(mat, exp // 2)
        result = matrix_multiply(half, half)
        
        if exp % 2 == 1:
            result = matrix_multiply(result, mat)
        
        return result
    
    if n == 0:
        # Return identity matrix
        size = len(matrix)
        identity = [[0] * size for _ in range(size)]
        for i in range(size):
            identity[i][i] = 1
        return identity
    
    return matrix_power_helper(matrix, n)
```

## Phần 4: Ứng dụng nâng cao (45 phút)

### 4.1 Closest Pair of Points

```python
import math

def closest_pair_points(points):
    """
    Find closest pair of points using divide and conquer
    Time: O(n log n), Space: O(n)
    """
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def closest_pair_rec(px, py):
        n = len(px)
        
        # Base case
        if n <= 3:
            min_dist = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    min_dist = min(min_dist, distance(px[i], px[j]))
            return min_dist
        
        # Divide
        mid = n // 2
        midpoint = px[mid]
        
        pyl = [point for point in py if point[0] <= midpoint[0]]
        pyr = [point for point in py if point[0] > midpoint[0]]
        
        # Conquer
        dl = closest_pair_rec(px[:mid], pyl)
        dr = closest_pair_rec(px[mid:], pyr)
        
        # Find minimum of the two
        d = min(dl, dr)
        
        # Combine - check points near the dividing line
        strip = [point for point in py if abs(point[0] - midpoint[0]) < d]
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
                d = min(d, distance(strip[i], strip[j]))
                j += 1
        
        return d
    
    # Sort points by x and y coordinates
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    
    return closest_pair_rec(px, py)
```

### 4.2 Convex Hull (Graham Scan)

```python
def convex_hull_divide_conquer(points):
    """Convex hull using divide and conquer"""
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    def merge_hulls(left_hull, right_hull):
        # Find upper and lower tangents
        # This is a simplified version
        return left_hull + right_hull
    
    def convex_hull_rec(points):
        n = len(points)
        
        if n <= 3:
            # Base case - return all points for small sets
            return points
        
        # Divide
        mid = n // 2
        left_points = points[:mid]
        right_points = points[mid:]
        
        # Conquer
        left_hull = convex_hull_rec(left_points)
        right_hull = convex_hull_rec(right_points)
        
        # Combine
        return merge_hulls(left_hull, right_hull)
    
    # Sort points by x-coordinate
    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
    return convex_hull_rec(sorted_points)
```

### 4.3 Karatsuba Multiplication

```python
def karatsuba_multiply(x, y):
    """
    Karatsuba algorithm for fast multiplication
    Time: O(n^log_2(3)) ≈ O(n^1.585)
    """
    # Base case
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split the numbers
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)
    
    # Three recursive calls
    z0 = karatsuba_multiply(low1, low2)
    z1 = karatsuba_multiply(low1 + high1, low2 + high2)
    z2 = karatsuba_multiply(high1, high2)
    
    # Combine the results
    return z2 * (10**(2*m)) + (z1 - z2 - z0) * (10**m) + z0
```

### 4.4 Inversion Count

```python
def count_inversions(arr):
    """
    Count inversions using divide and conquer
    Time: O(n log n), Space: O(n)
    """
    def merge_and_count(arr, temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)  # All elements from i to mid are greater than arr[j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        
        # Copy back to original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
        
        return inv_count
    
    def merge_sort_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            
            inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge_and_count(arr, temp_arr, left, mid, right)
        
        return inv_count
    
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr.copy(), temp_arr, 0, len(arr) - 1)
```

## Bài tập thực hành

1. **[problem230101.py]** - Basic divide and conquer patterns
2. **[problem230102.py]** - Master theorem analysis
3. **[problem230201.py]** - Sorting algorithms (merge sort, quick sort)
4. **[problem230202.py]** - Advanced sorting applications
5. **[problem230301.py]** - Search algorithms và variants
6. **[problem230302.py]** - Mathematical algorithms (power, multiplication)
7. **[problem230401.py]** - Geometric algorithms (closest pair, convex hull)
8. **[problem230402.py]** - Olympic-level divide and conquer problems

## Tổng kết

- Divide and conquer chia bài toán thành subproblems nhỏ hơn
- Master theorem giúp phân tích độ phức tạp
- Merge sort và quick sort là ví dụ điển hình
- Ứng dụng rộng rãi: tìm kiếm, tính toán, hình học
- Thường đạt độ phức tạp O(n log n) cho nhiều bài toán
- Quan trọng trong Olympic programming và competitive programming