# Problem 06.03.01: Thuật toán tìm kiếm Olympic

print("=== THUẬT TOÁN TÌM KIẾM OLYMPIC ===")

# Bài 1: Tìm cặp số có tổng bằng target (Two Sum)
def two_sum(arr, target):
    """Tìm cặp số có tổng bằng target"""
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None

def two_sum_all_pairs(arr, target):
    """Tìm tất cả cặp số có tổng bằng target"""
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((i, j, arr[i], arr[j]))
    return pairs

numbers = [2, 7, 11, 15, 3, 6, 9, 1, 8, 4]
target = int(input(f"Tìm cặp số có tổng bằng (trong {numbers}): "))

# Tìm cặp đầu tiên
pair = two_sum(numbers, target)
if pair:
    i, j = pair
    print(f"Cặp đầu tiên: {numbers[i]} + {numbers[j]} = {target} (vị trí {i}, {j})")
else:
    print("Không tìm thấy cặp nào")

# Tìm tất cả cặp
all_pairs = two_sum_all_pairs(numbers, target)
print(f"Tất cả các cặp có tổng = {target}:")
for i, j, num1, num2 in all_pairs:
    print(f"  {num1} + {num2} = {target} (vị trí {i}, {j})")

# Bài 2: Tìm phần tử xuất hiện nhiều nhất
def find_most_frequent(arr):
    frequency = {}
    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1
    
    max_freq = max(frequency.values())
    most_frequent = [key for key, value in frequency.items() if value == max_freq]
    
    return most_frequent, max_freq

test_array = [1, 3, 2, 3, 4, 1, 3, 2, 3, 5]
most_freq, freq = find_most_frequent(test_array)
print(f"\nMảng: {test_array}")
print(f"Phần tử xuất hiện nhiều nhất: {most_freq} ({freq} lần)")

# Bài 3: Tìm missing number
def find_missing_number(arr, n):
    """Tìm số bị thiếu trong dãy 1 đến n"""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def find_all_missing_numbers(arr, n):
    """Tìm tất cả số bị thiếu"""
    present = set(arr)
    missing = []
    for i in range(1, n + 1):
        if i not in present:
            missing.append(i)
    return missing

incomplete_array = [1, 2, 4, 6, 3, 7, 8]
n = 8
missing = find_missing_number(incomplete_array, n)
all_missing = find_all_missing_numbers(incomplete_array, n)

print(f"\nMảng không đầy đủ: {incomplete_array}")
print(f"Số bị thiếu (nếu chỉ thiếu 1 số): {missing}")
print(f"Tất cả số bị thiếu từ 1 đến {n}: {all_missing}")

# Bài 4: Tìm intersection của hai mảng
def find_intersection(arr1, arr2):
    """Tìm giao của hai mảng"""
    set1 = set(arr1)
    intersection = []
    
    for element in arr2:
        if element in set1:
            intersection.append(element)
            set1.remove(element)  # Tránh trùng lặp
    
    return intersection

def find_union(arr1, arr2):
    """Tìm hợp của hai mảng"""
    return list(set(arr1) | set(arr2))

array1 = [1, 2, 2, 1, 3, 4]
array2 = [2, 2, 3, 5, 6]

intersection = find_intersection(array1, array2)
union = find_union(array1, array2)

print(f"\nMảng 1: {array1}")
print(f"Mảng 2: {array2}")
print(f"Giao: {intersection}")
print(f"Hợp: {sorted(union)}")