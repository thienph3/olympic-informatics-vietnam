# Problem 06.04.01: Kỹ thuật tối ưu hóa

import time

print("=== KỸ THUẬT TỐI ƯU HÓA ===")

# Bài 1: So sánh hiệu suất thuật toán
def brute_force_two_sum(arr, target):
    """Thuật toán brute force O(n²)"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
    return -1, -1

def optimized_two_sum(arr, target):
    """Thuật toán tối ưu O(n)"""
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return -1, -1

# Test hiệu suất
large_array = list(range(1000))
target = 1500

# Brute force
start_time = time.time()
result1 = brute_force_two_sum(large_array, target)
brute_force_time = time.time() - start_time

# Optimized
start_time = time.time()
result2 = optimized_two_sum(large_array, target)
optimized_time = time.time() - start_time

print(f"Mảng có {len(large_array)} phần tử, target = {target}")
print(f"Brute force: {result1}, thời gian: {brute_force_time:.6f}s")
print(f"Optimized: {result2}, thời gian: {optimized_time:.6f}s")
print(f"Tăng tốc: {brute_force_time/optimized_time:.2f} lần")

# Bài 2: Sliding Window Technique
def max_sum_subarray_k(arr, k):
    """Tìm tổng lớn nhất của subarray có độ dài k"""
    if len(arr) < k:
        return None, []
    
    # Tính tổng window đầu tiên
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_start = 0
    
    # Trượt window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - k + 1
    
    return max_sum, arr[max_start:max_start + k]

def min_window_sum_greater_than_s(arr, s):
    """Tìm window nhỏ nhất có tổng >= s"""
    left = 0
    min_length = float('inf')
    window_sum = 0
    min_start = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        while window_sum >= s:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_start = left
            window_sum -= arr[left]
            left += 1
    
    if min_length == float('inf'):
        return None, []
    
    return min_length, arr[min_start:min_start + min_length]

test_array = [2, 1, 2, 4, 3, 1, 5, 2, 3]
k = 3
s = 7

max_sum, max_subarray = max_sum_subarray_k(test_array, k)
min_len, min_window = min_window_sum_greater_than_s(test_array, s)

print(f"\nMảng: {test_array}")
print(f"Subarray có độ dài {k} với tổng lớn nhất: {max_subarray} (tổng: {max_sum})")
print(f"Window nhỏ nhất có tổng >= {s}: {min_window} (độ dài: {min_len})")

# Bài 3: Two Pointers Technique
def two_pointers_pair_sum(arr, target):
    """Tìm cặp số có tổng = target trong mảng đã sắp xếp"""
    left, right = 0, len(arr) - 1
    pairs = []
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append((left, right, arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs

def remove_duplicates_two_pointers(arr):
    """Xóa phần tử trùng lặp trong mảng đã sắp xếp"""
    if not arr:
        return []
    
    write_index = 1
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    
    return arr[:write_index]

def is_palindrome_ignore_non_alphanumeric(s):
    """Kiểm tra palindrome, bỏ qua ký tự không phải chữ/số"""
    left, right = 0, len(s) - 1
    
    while left < right:
        # Bỏ qua ký tự không phải chữ/số từ trái
        while left < right and not s[left].isalnum():
            left += 1
        
        # Bỏ qua ký tự không phải chữ/số từ phải
        while left < right and not s[right].isalnum():
            right -= 1
        
        # So sánh (không phân biệt hoa thường)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Test two pointers
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
pairs = two_pointers_pair_sum(sorted_array, target)

print(f"\nMảng đã sắp xếp: {sorted_array}")
print(f"Các cặp có tổng = {target}: {pairs}")

# Test remove duplicates
duplicate_array = [1, 1, 2, 2, 2, 3, 4, 4, 5]
unique_array = remove_duplicates_two_pointers(duplicate_array.copy())
print(f"Mảng có trùng lặp: {duplicate_array}")
print(f"Sau khi xóa trùng lặp: {unique_array}")

# Test palindrome
test_strings = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "Madam",
    "No 'x' in Nixon"
]

print(f"\nKiểm tra palindrome:")
for s in test_strings:
    result = is_palindrome_ignore_non_alphanumeric(s)
    print(f"'{s}': {'Palindrome' if result else 'Không phải palindrome'}")