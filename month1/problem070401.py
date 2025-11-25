# Problem 07.04.01: Thuật toán cơ bản với list

print("=== THUẬT TOÁN CƠ BẢN VỚI LIST ===")

# Bài 1: Tìm kiếm tuyến tính
def linear_search(arr, target):
    """Tìm kiếm tuyến tính - trả về index đầu tiên"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linear_search_all(arr, target):
    """Tìm tất cả vị trí của target"""
    positions = []
    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)
    return positions

# Test tìm kiếm
numbers = [3, 7, 2, 9, 7, 1, 7, 5]
target = 7
print(f"Mảng: {numbers}")
print(f"Tìm {target}:")
print(f"  Vị trí đầu tiên: {linear_search(numbers, target)}")
print(f"  Tất cả vị trí: {linear_search_all(numbers, target)}")

# Bài 2: Tìm min/max với vị trí
def find_min_max_with_index(arr):
    """Tìm min/max cùng với vị trí"""
    if not arr:
        return None, None, None, None
    
    min_val = max_val = arr[0]
    min_idx = max_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    
    return min_val, min_idx, max_val, max_idx

min_val, min_idx, max_val, max_idx = find_min_max_with_index(numbers)
print(f"\nTìm min/max:")
print(f"  Min: {min_val} tại vị trí {min_idx}")
print(f"  Max: {max_val} tại vị trí {max_idx}")

# Bài 3: Loại bỏ phần tử trùng lặp
def remove_duplicates_keep_order(arr):
    """Loại bỏ trùng lặp, giữ thứ tự xuất hiện đầu tiên"""
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    return result

def remove_duplicates_count(arr):
    """Loại bỏ trùng lặp và đếm số lần xuất hiện"""
    unique_items = []
    counts = []
    
    for item in arr:
        if item in unique_items:
            index = unique_items.index(item)
            counts[index] += 1
        else:
            unique_items.append(item)
            counts.append(1)
    
    return unique_items, counts

print(f"\nLoại bỏ trùng lặp từ {numbers}:")
unique = remove_duplicates_keep_order(numbers)
print(f"  Không trùng lặp: {unique}")

unique_items, counts = remove_duplicates_count(numbers)
print(f"  Với số lần xuất hiện:")
for item, count in zip(unique_items, counts):
    print(f"    {item}: {count} lần")

# Bài 4: Sắp xếp bubble sort
def bubble_sort(arr):
    """Thuật toán sắp xếp nổi bọt"""
    arr = arr.copy()  # Không thay đổi mảng gốc
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:  # Đã sắp xếp xong
            break
    
    return arr, comparisons, swaps

unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"\nSắp xếp bubble sort:")
print(f"  Mảng gốc: {unsorted}")
sorted_arr, comps, swaps = bubble_sort(unsorted)
print(f"  Đã sắp xếp: {sorted_arr}")
print(f"  Số lần so sánh: {comps}")
print(f"  Số lần hoán đổi: {swaps}")

# Bài 5: Tìm dãy con tăng dài nhất
def longest_increasing_subsequence_length(arr):
    """Tìm độ dài dãy con tăng dài nhất"""
    if not arr:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length

def find_longest_increasing_subsequence(arr):
    """Tìm dãy con tăng dài nhất"""
    if not arr:
        return []
    
    max_length = 0
    max_start = 0
    current_length = 1
    current_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start = current_start
            current_length = 1
            current_start = i
    
    # Kiểm tra lần cuối
    if current_length > max_length:
        max_length = current_length
        max_start = current_start
    
    return arr[max_start:max_start + max_length]

test_sequence = [1, 3, 2, 4, 5, 1, 6, 7, 8, 2, 3]
print(f"\nDãy con tăng dài nhất:")
print(f"  Dãy gốc: {test_sequence}")
lis_length = longest_increasing_subsequence_length(test_sequence)
lis = find_longest_increasing_subsequence(test_sequence)
print(f"  Độ dài: {lis_length}")
print(f"  Dãy con: {lis}")

# Bài 6: Tìm cặp số có tổng bằng target
def find_pair_sum(arr, target):
    """Tìm cặp số có tổng bằng target"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j, arr[i], arr[j]
    return None

def find_all_pairs_sum(arr, target):
    """Tìm tất cả cặp số có tổng bằng target"""
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((i, j, arr[i], arr[j]))
    return pairs

test_array = [2, 7, 11, 15, 3, 6]
target_sum = 9
print(f"\nTìm cặp số có tổng = {target_sum}:")
print(f"  Mảng: {test_array}")

pair = find_pair_sum(test_array, target_sum)
if pair:
    i, j, num1, num2 = pair
    print(f"  Cặp đầu tiên: {num1} + {num2} = {target_sum} (vị trí {i}, {j})")
else:
    print(f"  Không tìm thấy cặp nào")

all_pairs = find_all_pairs_sum(test_array, target_sum)
print(f"  Tất cả các cặp: {len(all_pairs)} cặp")
for i, j, num1, num2 in all_pairs:
    print(f"    {num1} + {num2} = {target_sum} (vị trí {i}, {j})")