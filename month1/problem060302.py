# Problem 06.03.02: Xử lý dãy số Olympic

print("=== XỬ LÝ DÃY SỐ OLYMPIC ===")

# Bài 1: Kadane's Algorithm - Tìm dãy con có tổng lớn nhất
def max_subarray_sum(arr):
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

test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start, end = max_subarray_sum(test_array)

print(f"Mảng: {test_array}")
print(f"Dãy con có tổng lớn nhất: {test_array[start:end+1]}")
print(f"Tổng lớn nhất: {max_sum}")
print(f"Vị trí: từ {start} đến {end}")

# Bài 2: Tìm dãy con tăng dài nhất
def longest_increasing_subsequence_length(arr):
    if not arr:
        return 0
    
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def longest_increasing_subsequence(arr):
    if not arr:
        return []
    
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    # Tìm vị trí có độ dài lớn nhất
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # Xây dựng dãy con
    result = []
    current = max_index
    while current != -1:
        result.append(arr[current])
        current = parent[current]
    
    return result[::-1]

sequence = [10, 9, 2, 5, 3, 7, 101, 18]
lis_length = longest_increasing_subsequence_length(sequence)
lis = longest_increasing_subsequence(sequence)

print(f"\nDãy số: {sequence}")
print(f"Độ dài dãy con tăng dài nhất: {lis_length}")
print(f"Dãy con tăng dài nhất: {lis}")

# Bài 3: Tìm chu kỳ trong dãy số
def find_cycle_length(arr):
    """Tìm chu kỳ lặp trong dãy số"""
    n = len(arr)
    
    for cycle_len in range(1, n // 2 + 1):
        is_cycle = True
        
        # Kiểm tra chu kỳ có độ dài cycle_len
        for i in range(cycle_len, n):
            if arr[i] != arr[i % cycle_len]:
                is_cycle = False
                break
        
        if is_cycle:
            return cycle_len
    
    return 0  # Không có chu kỳ

def detect_pattern(arr):
    """Phát hiện pattern trong dãy số"""
    cycle_len = find_cycle_length(arr)
    
    if cycle_len > 0:
        pattern = arr[:cycle_len]
        repetitions = len(arr) // cycle_len
        remainder = len(arr) % cycle_len
        
        return {
            'has_cycle': True,
            'cycle_length': cycle_len,
            'pattern': pattern,
            'repetitions': repetitions,
            'remainder': remainder
        }
    else:
        return {'has_cycle': False}

# Test với các dãy khác nhau
test_sequences = [
    [1, 2, 3, 1, 2, 3, 1, 2, 3],  # Chu kỳ 3
    [1, 2, 1, 2, 1, 2, 1, 2],     # Chu kỳ 2
    [1, 2, 3, 4, 5, 6, 7, 8],     # Không có chu kỳ
    [5, 5, 5, 5, 5, 5]            # Chu kỳ 1
]

for i, seq in enumerate(test_sequences, 1):
    pattern_info = detect_pattern(seq)
    print(f"\nDãy {i}: {seq}")
    
    if pattern_info['has_cycle']:
        print(f"  Có chu kỳ độ dài {pattern_info['cycle_length']}")
        print(f"  Pattern: {pattern_info['pattern']}")
        print(f"  Lặp lại {pattern_info['repetitions']} lần")
        if pattern_info['remainder'] > 0:
            print(f"  Còn dư {pattern_info['remainder']} phần tử")
    else:
        print("  Không có chu kỳ")

# Bài 4: Tìm peak và valley
def find_peaks_and_valleys(arr):
    """Tìm đỉnh (peak) và thung lũng (valley)"""
    if len(arr) < 3:
        return [], []
    
    peaks = []
    valleys = []
    
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peaks.append((i, arr[i]))
        elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            valleys.append((i, arr[i]))
    
    return peaks, valleys

wave_data = [1, 3, 2, 4, 1, 5, 2, 6, 3, 7, 1]
peaks, valleys = find_peaks_and_valleys(wave_data)

print(f"\nDữ liệu sóng: {wave_data}")
print(f"Các đỉnh (peaks): {peaks}")
print(f"Các thung lũng (valleys): {valleys}")

# Vẽ biểu đồ đơn giản
print("\nBiểu đồ:")
max_val = max(wave_data)
for level in range(max_val, 0, -1):
    line = ""
    for val in wave_data:
        if val >= level:
            line += "* "
        else:
            line += "  "
    print(f"{level} |{line}")

print("  +" + "--" * len(wave_data))
print("   " + "".join(f"{i%10} " for i in range(len(wave_data))))