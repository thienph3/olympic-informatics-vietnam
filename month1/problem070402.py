# Problem 07.04.02: Bài toán Olympic với list

print("=== BÀI TOÁN OLYMPIC VỚI LIST ===")

# Bài 1: Sàng Eratosthenes - tìm số nguyên tố
def sieve_of_eratosthenes(n):
    """Sàng Eratosthenes tìm tất cả số nguyên tố <= n"""
    if n < 2:
        return []
    
    # Tạo mảng boolean, ban đầu tất cả đều True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sàng
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Đánh dấu tất cả bội số của i
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # Thu thập số nguyên tố
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes

n = int(input("Nhập n để tìm số nguyên tố <= n: "))
primes = sieve_of_eratosthenes(n)
print(f"Các số nguyên tố <= {n}: {primes}")
print(f"Tổng cộng: {len(primes)} số nguyên tố")

# Bài 2: Prefix Sum - tổng tiền tố
def calculate_prefix_sum(arr):
    """Tính mảng tổng tiền tố"""
    if not arr:
        return []
    
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix

def range_sum_query(prefix_sum, left, right):
    """Truy vấn tổng đoạn [left, right] sử dụng prefix sum"""
    if left == 0:
        return prefix_sum[right]
    else:
        return prefix_sum[right] - prefix_sum[left - 1]

# Test prefix sum
array = [1, 3, 5, 7, 9, 11]
print(f"\nPrefix Sum:")
print(f"Mảng gốc: {array}")

prefix = calculate_prefix_sum(array)
print(f"Prefix sum: {prefix}")

# Một số truy vấn
queries = [(0, 2), (1, 4), (2, 5), (0, 5)]
print("Truy vấn tổng đoạn:")
for left, right in queries:
    result = range_sum_query(prefix, left, right)
    subarray = array[left:right+1]
    print(f"  Đoạn [{left}, {right}]: {subarray} -> Tổng: {result}")

# Bài 3: Sliding Window Maximum
def sliding_window_maximum(arr, k):
    """Tìm giá trị lớn nhất trong mỗi cửa sổ trượt kích thước k"""
    if not arr or k <= 0:
        return []
    
    result = []
    for i in range(len(arr) - k + 1):
        window = arr[i:i+k]
        window_max = max(window)
        result.append(window_max)
    
    return result

def sliding_window_sum(arr, k):
    """Tính tổng trong mỗi cửa sổ trượt kích thước k"""
    if not arr or k <= 0:
        return []
    
    result = []
    # Tính tổng cửa sổ đầu tiên
    window_sum = sum(arr[:k])
    result.append(window_sum)
    
    # Trượt cửa sổ
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        result.append(window_sum)
    
    return result

# Test sliding window
data = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(f"\nSliding Window (k={k}):")
print(f"Dữ liệu: {data}")

max_values = sliding_window_maximum(data, k)
sum_values = sliding_window_sum(data, k)

print("Cửa sổ trượt:")
for i in range(len(max_values)):
    window = data[i:i+k]
    print(f"  {window} -> Max: {max_values[i]}, Sum: {sum_values[i]}")

# Bài 4: Kadane's Algorithm - Maximum Subarray Sum
def kadane_algorithm(arr):
    """Tìm tổng lớn nhất của dãy con liên tiếp"""
    if not arr:
        return 0, 0, 0
    
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

# Test Kadane's algorithm
test_arrays = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4],
    [5, -3, 2, -1, 4]
]

print(f"\nKadane's Algorithm - Maximum Subarray Sum:")
for i, arr in enumerate(test_arrays, 1):
    max_sum, start, end = kadane_algorithm(arr)
    subarray = arr[start:end+1]
    print(f"Test {i}: {arr}")
    print(f"  Max subarray: {subarray} (vị trí {start}-{end})")
    print(f"  Tổng lớn nhất: {max_sum}")

# Bài 5: Two Pointers - Tìm cặp số có tổng bằng target (mảng đã sắp xếp)
def two_pointers_sum(arr, target):
    """Tìm cặp số có tổng = target trong mảng đã sắp xếp"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return left, right, arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

def find_all_pairs_two_pointers(arr, target):
    """Tìm tất cả cặp số có tổng = target"""
    arr_sorted = sorted(arr)
    pairs = []
    left, right = 0, len(arr_sorted) - 1
    
    while left < right:
        current_sum = arr_sorted[left] + arr_sorted[right]
        
        if current_sum == target:
            pairs.append((arr_sorted[left], arr_sorted[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs

# Test two pointers
sorted_array = [1, 2, 3, 4, 6, 8, 9, 14, 15]
target = 10
print(f"\nTwo Pointers (mảng đã sắp xếp):")
print(f"Mảng: {sorted_array}")
print(f"Target: {target}")

result = two_pointers_sum(sorted_array, target)
if result:
    left, right, num1, num2 = result
    print(f"Tìm thấy: {num1} + {num2} = {target} (vị trí {left}, {right})")
else:
    print("Không tìm thấy cặp nào")

all_pairs = find_all_pairs_two_pointers(sorted_array, target)
print(f"Tất cả các cặp: {all_pairs}")

# Bài 6: Frequency Analysis
def frequency_analysis(arr):
    """Phân tích tần suất xuất hiện"""
    frequency = {}
    for item in arr:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Sắp xếp theo tần suất giảm dần
    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    return frequency, sorted_items

# Test frequency analysis
data = [1, 2, 3, 2, 1, 3, 1, 4, 5, 1, 2]
print(f"\nPhân tích tần suất:")
print(f"Dữ liệu: {data}")

freq_dict, sorted_freq = frequency_analysis(data)
print("Tần suất xuất hiện:")
for item, count in sorted_freq:
    print(f"  {item}: {count} lần")

most_frequent = sorted_freq[0][0]
print(f"Phần tử xuất hiện nhiều nhất: {most_frequent} ({sorted_freq[0][1]} lần)")