# Day 15: Ternary search, exponential search, interpolation search

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Ternary Search chi tiết (45')

### 📚 Lý thuyết (15')

#### Ternary Search cho sorted arrays
```python
def ternary_search_array(arr, target):
    """
    Ternary search trong sorted array
    Time complexity: O(log₃ n) ≈ 0.63 * O(log₂ n)
    Space complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Chia array thành 3 phần
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # Loại bỏ 1/3 array
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

# Ternary search recursive
def ternary_search_recursive(arr, target, left=0, right=None):
    """Ternary search đệ quy"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    if target < arr[mid1]:
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)
```

#### Ternary Search cho optimization problems
```python
def ternary_search_maximum(func, left, right, epsilon=1e-9):
    """
    Tìm maximum của unimodal function
    Input: func - unimodal function, left/right - bounds, epsilon - precision
    Output: x tại đó func(x) maximum
    """
    while right - left > epsilon:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        
        if func(m1) < func(m2):
            left = m1
        else:
            right = m2
    
    return (left + right) / 2

def ternary_search_minimum(func, left, right, epsilon=1e-9):
    """
    Tìm minimum của unimodal function
    """
    while right - left > epsilon:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        
        if func(m1) > func(m2):
            left = m1
        else:
            right = m2
    
    return (left + right) / 2

# Ví dụ: tìm minimum của f(x) = x² - 4x + 5
def quadratic(x):
    return x*x - 4*x + 5

min_x = ternary_search_minimum(quadratic, 0, 5)
print(f"Minimum tại x = {min_x:.6f}, f(x) = {quadratic(min_x):.6f}")
```

#### Ternary Search applications
```python
def find_peak_ternary(arr):
    """
    Tìm peak element bằng ternary search
    Peak: arr[i] > arr[i-1] và arr[i] > arr[i+1]
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] < arr[mid2]:
            left = mid1 + 1
        else:
            right = mid2 - 1
    
    return left

def minimize_max_distance_ternary(positions, k):
    """
    Minimize maximum distance bằng ternary search
    """
    def max_distance_with_k_points(positions, k):
        # Function để tính max distance khi thêm k points
        pass
    
    # Ternary search trên số points để add
    left, right = 0, k
    
    while right - left > 2:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3
        
        dist1 = max_distance_with_k_points(positions, m1)
        dist2 = max_distance_with_k_points(positions, m2)
        
        if dist1 > dist2:
            left = m1
        else:
            right = m2
    
    # Check remaining candidates
    best_k = left
    best_dist = max_distance_with_k_points(positions, left)
    
    for i in range(left + 1, right + 1):
        dist = max_distance_with_k_points(positions, i)
        if dist < best_dist:
            best_dist = dist
            best_k = i
    
    return best_k, best_dist
```

### 💻 Thực hành (30')

#### Bài tập 1: Ternary search implementations

**Yêu cầu:** Implement ternary search cho arrays và optimization.

**File thực hành:** [problem150101.py](problem150101.py)

#### Bài tập 2: Ternary search applications

**Yêu cầu:** Ứng dụng ternary search trong Olympic problems.

**File thực hành:** [problem150102.py](problem150102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: Exponential Search (45')

### 📚 Lý thuyết (20')

#### Exponential Search cơ bản
```python
def exponential_search(arr, target):
    """
    Exponential search - tốt cho unbounded arrays
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    if not arr:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Tìm range cho binary search
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2
    
    # Binary search trong range [bound//2, min(bound, len(arr)-1)]
    return binary_search_range(arr, target, bound // 2, min(bound, len(arr) - 1))

def binary_search_range(arr, target, left, right):
    """Binary search trong range cụ thể"""
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

#### Exponential Search cho infinite arrays
```python
class InfiniteArray:
    """Simulate infinite array"""
    def __init__(self, arr):
        self.arr = arr
    
    def get(self, index):
        if index >= len(self.arr):
            return float('inf')  # Infinite value
        return self.arr[index]

def exponential_search_infinite(infinite_arr, target):
    """
    Exponential search cho infinite array
    """
    if infinite_arr.get(0) == target:
        return 0
    
    # Tìm upper bound
    bound = 1
    while infinite_arr.get(bound) < target:
        bound *= 2
    
    # Binary search trong range [bound//2, bound]
    left, right = bound // 2, bound
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = infinite_arr.get(mid)
        
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

#### Exponential Search variants
```python
def exponential_search_first_occurrence(arr, target):
    """
    Tìm first occurrence bằng exponential search
    """
    if not arr or arr[0] > target:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Tìm range
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2
    
    # Binary search cho first occurrence
    left = bound // 2
    right = min(bound, len(arr) - 1)
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Tìm bên trái
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def exponential_search_insertion_point(arr, target):
    """
    Tìm insertion point bằng exponential search
    """
    if not arr or target <= arr[0]:
        return 0
    
    # Tìm range
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2
    
    # Binary search cho insertion point
    left = bound // 2
    right = min(bound, len(arr))
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

#### Performance analysis
```python
def compare_exponential_vs_binary(arr, target):
    """
    So sánh exponential search vs binary search
    """
    import time
    
    # Binary search
    start = time.time()
    binary_result = binary_search_standard(arr, target)
    binary_time = time.time() - start
    
    # Exponential search
    start = time.time()
    exp_result = exponential_search(arr, target)
    exp_time = time.time() - start
    
    return {
        'binary': {'result': binary_result, 'time': binary_time},
        'exponential': {'result': exp_result, 'time': exp_time}
    }

def binary_search_standard(arr, target):
    """Standard binary search for comparison"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 💻 Thực hành (25')

#### Bài tập 1: Exponential search implementations

**Yêu cầu:** Implement exponential search và variants.

**File thực hành:** [problem150201.py](problem150201.py)

#### Bài tập 2: Infinite array problems

**Yêu cầu:** Giải problems với infinite/unbounded arrays.

**File thực hành:** [problem150202.py](problem150202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Interpolation Search (45')

### 📚 Lý thuyết (15')

#### Interpolation Search cơ bản
```python
def interpolation_search(arr, target):
    """
    Interpolation search - tốt cho uniformly distributed data
    Time complexity: O(log log n) average, O(n) worst case
    Space complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        # Tránh division by zero
        if arr[right] == arr[left]:
            if arr[left] == target:
                return left
            break
        
        # Interpolation formula
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        # Ensure pos is within bounds
        pos = max(left, min(pos, right))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1
```

#### Interpolation Search improvements
```python
def interpolation_search_improved(arr, target):
    """
    Improved interpolation search với better bounds checking
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        if left == right:
            return left if arr[left] == target else -1
        
        # Improved interpolation formula
        if arr[right] != arr[left]:
            # Linear interpolation
            pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
            
            # Clamp position
            pos = max(left, min(pos, right))
        else:
            # Fallback to middle when values are equal
            pos = (left + right) // 2
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1

def adaptive_interpolation_search(arr, target):
    """
    Adaptive interpolation search - fallback to binary khi cần
    """
    left, right = 0, len(arr) - 1
    interpolation_steps = 0
    max_interpolation_steps = 10  # Threshold để switch to binary
    
    while left <= right:
        if interpolation_steps < max_interpolation_steps and target >= arr[left] and target <= arr[right]:
            # Try interpolation
            if arr[right] != arr[left]:
                pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
                pos = max(left, min(pos, right))
                interpolation_steps += 1
            else:
                pos = (left + right) // 2
        else:
            # Fallback to binary search
            pos = (left + right) // 2
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1
```

#### Interpolation Search cho different distributions
```python
def interpolation_search_with_distribution_check(arr, target):
    """
    Interpolation search với distribution checking
    """
    def is_uniformly_distributed(arr, left, right, sample_size=10):
        """Check if data is approximately uniformly distributed"""
        if right - left < sample_size:
            return True
        
        step = (right - left) // sample_size
        differences = []
        
        for i in range(left, right - step, step):
            differences.append(arr[i + step] - arr[i])
        
        if not differences:
            return True
        
        avg_diff = sum(differences) / len(differences)
        variance = sum((d - avg_diff) ** 2 for d in differences) / len(differences)
        
        # If variance is low, data is uniform
        return variance < avg_diff * 0.5
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        if is_uniformly_distributed(arr, left, right):
            # Use interpolation
            if target < arr[left] or target > arr[right]:
                break
            
            if arr[right] != arr[left]:
                pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
                pos = max(left, min(pos, right))
            else:
                pos = left if arr[left] == target else -1
                return pos
        else:
            # Use binary search
            pos = (left + right) // 2
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1
```

### 💻 Thực hành (30')

#### Bài tập 1: Interpolation search implementations

**Yêu cầu:** Implement interpolation search và improvements.

**File thực hành:** [problem150301.py](problem150301.py)

#### Bài tập 2: Distribution-aware search

**Yêu cầu:** Adaptive search algorithms dựa trên data distribution.

**File thực hành:** [problem150302.py](problem150302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Advanced search techniques và Olympic applications (45')

### 📚 Lý thuyết (15')

#### Hybrid search algorithms
```python
def hybrid_search(arr, target):
    """
    Hybrid search: chọn algorithm dựa trên characteristics
    """
    n = len(arr)
    
    # Small arrays: linear search
    if n <= 10:
        return linear_search(arr, target)
    
    # Check if uniformly distributed
    if is_uniform_distribution(arr):
        return interpolation_search(arr, target)
    
    # Check if target is likely near beginning
    if n > 100 and target <= arr[min(20, n-1)]:
        return exponential_search(arr, target)
    
    # Default to binary search
    return binary_search_standard(arr, target)

def is_uniform_distribution(arr, sample_ratio=0.1):
    """Check if array has uniform distribution"""
    n = len(arr)
    sample_size = max(10, int(n * sample_ratio))
    
    if n < sample_size:
        return True
    
    step = n // sample_size
    differences = []
    
    for i in range(0, n - step, step):
        differences.append(arr[i + step] - arr[i])
    
    if not differences:
        return True
    
    avg = sum(differences) / len(differences)
    variance = sum((d - avg) ** 2 for d in differences) / len(differences)
    
    return variance < avg * 0.3  # Threshold for uniformity
```

#### Search trong special structures
```python
def search_in_sorted_rotated_array_advanced(arr, target):
    """
    Advanced search trong rotated sorted array
    Handles duplicates và multiple rotations
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Handle duplicates
        if arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
            continue
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def search_in_mountain_array_advanced(mountain_arr, target):
    """
    Advanced search trong mountain array
    """
    def find_peak():
        left, right = 0, len(mountain_arr) - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr[mid] < mountain_arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
    
    def binary_search_ascending(left, right):
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr[mid] == target:
                return mid
            elif mountain_arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def binary_search_descending(left, right):
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr[mid] == target:
                return mid
            elif mountain_arr[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    peak = find_peak()
    
    # Search in ascending part
    result = binary_search_ascending(0, peak)
    if result != -1:
        return result
    
    # Search in descending part
    return binary_search_descending(peak + 1, len(mountain_arr) - 1)
```

#### Olympic-level optimization problems
```python
def minimize_maximum_subarray_sum(arr, k):
    """
    Minimize maximum subarray sum khi split array thành k parts
    Using ternary search on answer space
    """
    def can_split_with_max_sum(max_sum):
        current_sum = 0
        splits = 1
        
        for num in arr:
            if current_sum + num > max_sum:
                splits += 1
                current_sum = num
                if splits > k:
                    return False
            else:
                current_sum += num
        
        return True
    
    # Ternary search on possible maximum sums
    left, right = max(arr), sum(arr)
    
    while right - left > 2:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3
        
        if can_split_with_max_sum(m1):
            right = m2
        else:
            left = m1
    
    # Check remaining candidates
    for candidate in range(left, right + 1):
        if can_split_with_max_sum(candidate):
            return candidate
    
    return right

def optimal_binary_search_tree_cost(keys, frequencies):
    """
    Tìm optimal cost cho binary search tree
    Using advanced search techniques
    """
    # This is a complex DP problem, but we can use search
    # to find optimal root for each subproblem
    
    n = len(keys)
    dp = [[0] * n for _ in range(n)]
    
    # Fill DP table using search optimization
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if i == j:
                dp[i][j] = frequencies[i]
            else:
                dp[i][j] = float('inf')
                freq_sum = sum(frequencies[i:j+1])
                
                # Use ternary search to find optimal root
                def cost_with_root(root):
                    cost = freq_sum
                    if root > i:
                        cost += dp[i][root-1]
                    if root < j:
                        cost += dp[root+1][j]
                    return cost
                
                # Search for optimal root
                best_cost = float('inf')
                for root in range(i, j + 1):
                    cost = cost_with_root(root)
                    best_cost = min(best_cost, cost)
                
                dp[i][j] = best_cost
    
    return dp[0][n-1]
```

### 💻 Thực hành (30')

#### Bài tập 1: Hybrid search algorithms

**Yêu cầu:** Implement hybrid search và adaptive algorithms.

**File thực hành:** [problem150401.py](problem150401.py)

#### Bài tập 2: Olympic optimization problems

**Yêu cầu:** Solve advanced Olympic problems using search techniques.

**File thực hành:** [problem150402.py](problem150402.py)

---

## Bài tập về nhà

### Bài 1: Advanced Search Library
Tạo comprehensive search library:
- All search algorithms (ternary, exponential, interpolation)
- Hybrid và adaptive search strategies
- Performance analysis tools
- Distribution detection algorithms
- Comprehensive benchmarking suite

### Bài 2: Olympic Search Contest
Giải advanced Olympic problems:
- Multi-dimensional optimization
- Complex constraint satisfaction
- Advanced data structure search
- Real-world optimization problems
- Performance-critical implementations

### Bài 3: Search Algorithm Analyzer
Tạo tool phân tích search algorithms:
- Data distribution analysis
- Algorithm recommendation system
- Performance prediction
- Visualization của search process
- Comparative analysis tools

### Gợi ý làm bài
1. Understand khi nào sử dụng từng algorithm
2. Practice với different data distributions
3. Focus on optimization applications
4. Master hybrid approach selection

---

## Tổng kết Day 15

**Đã học:**
- Ternary Search: arrays và optimization, unimodal functions
- Exponential Search: unbounded arrays, infinite data structures
- Interpolation Search: uniform distributions, adaptive approaches
- Advanced techniques: hybrid algorithms, Olympic applications

**Kỹ năng đạt được:**
- Choose optimal search algorithm cho specific data
- Implement advanced search variants efficiently
- Solve complex optimization problems
- Handle special data structures và distributions
- Build adaptive search systems

**So sánh algorithms:**
- **Binary Search:** O(log n), universal, most reliable
- **Ternary Search:** O(log₃ n), good for optimization, more comparisons
- **Exponential Search:** O(log n), excellent for unbounded data
- **Interpolation Search:** O(log log n) average, O(n) worst, best for uniform data

**Chuẩn bị Day 16:**
- Ôn tập search algorithms fundamentals
- Tìm hiểu sorting algorithms basics
- Chuẩn bị cho bubble, selection, insertion sort
- Review time complexity analysis