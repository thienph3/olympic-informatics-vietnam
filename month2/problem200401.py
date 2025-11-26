"""
Problem 200401: Optimization Techniques
Kỹ thuật tối ưu hóa thuật toán dựa trên phân tích complexity

Topics: Algorithm optimization, performance tuning, complexity reduction
"""

def optimize_nested_loops():
    """
    Tối ưu hóa nested loops
    """
    def find_pair_sum_naive(arr, target):
        # O(n²) - brute force
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    return (i, j)
        return None
    
    def find_pair_sum_optimized(arr, target):
        # O(n) - using hash map
        seen = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return None
    
    def find_pair_sum_sorted(arr, target):
        # O(n log n) + O(n) = O(n log n) - two pointers on sorted array
        indexed_arr = [(val, i) for i, val in enumerate(arr)]
        indexed_arr.sort()
        
        left, right = 0, len(indexed_arr) - 1
        while left < right:
            current_sum = indexed_arr[left][0] + indexed_arr[right][0]
            if current_sum == target:
                return (indexed_arr[left][1], indexed_arr[right][1])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None
    
    # TODO: So sánh 3 approaches và chọn optimal cho từng case
    pass

def optimize_string_operations():
    """
    Tối ưu hóa string operations
    """
    def concatenate_strings_naive(strings):
        # O(n²) - string concatenation in loop
        result = ""
        for s in strings:
            result += s  # Creates new string each time
        return result
    
    def concatenate_strings_optimized(strings):
        # O(n) - using join
        return "".join(strings)
    
    def concatenate_strings_list(strings):
        # O(n) - using list then join
        result_list = []
        for s in strings:
            result_list.append(s)
        return "".join(result_list)
    
    def reverse_words_naive(sentence):
        # O(n²) - multiple string operations
        words = sentence.split()
        result = ""
        for i in range(len(words) - 1, -1, -1):
            result += words[i]
            if i > 0:
                result += " "
        return result
    
    def reverse_words_optimized(sentence):
        # O(n) - single pass with list
        words = sentence.split()
        return " ".join(reversed(words))
    
    # TODO: Measure performance difference
    pass

def optimize_data_structure_choice():
    """
    Tối ưu hóa bằng cách chọn data structure phù hợp
    """
    def count_frequency_list(arr):
        # O(n²) - using list of tuples
        frequencies = []
        for num in arr:
            found = False
            for i, (val, count) in enumerate(frequencies):
                if val == num:
                    frequencies[i] = (val, count + 1)
                    found = True
                    break
            if not found:
                frequencies.append((num, 1))
        return frequencies
    
    def count_frequency_dict(arr):
        # O(n) - using dictionary
        frequencies = {}
        for num in arr:
            frequencies[num] = frequencies.get(num, 0) + 1
        return frequencies
    
    def count_frequency_counter(arr):
        # O(n) - using Counter
        from collections import Counter
        return Counter(arr)
    
    def find_unique_elements_list(arr1, arr2):
        # O(n * m) - nested loops
        unique = []
        for item in arr1:
            if item not in arr2 and item not in unique:
                unique.append(item)
        return unique
    
    def find_unique_elements_set(arr1, arr2):
        # O(n + m) - using sets
        set1 = set(arr1)
        set2 = set(arr2)
        return list(set1 - set2)
    
    # TODO: Compare performance với different data sizes
    pass

def optimize_algorithm_choice():
    """
    Tối ưu hóa bằng cách chọn thuật toán phù hợp
    """
    def sort_small_array(arr):
        # For small arrays, insertion sort can be faster
        if len(arr) < 50:
            return insertion_sort(arr.copy())
        else:
            return sorted(arr)
    
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def search_strategy(arr, target, is_sorted=False):
        # Choose search algorithm based on array properties
        if is_sorted:
            return binary_search(arr, target)
        elif len(set(arr)) < len(arr) * 0.1:  # Many duplicates
            return linear_search_early_exit(arr, target)
        else:
            return linear_search(arr, target)
    
    def binary_search(arr, target):
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
    
    def linear_search(arr, target):
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    def linear_search_early_exit(arr, target):
        # Optimized for arrays with many duplicates
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1
    
    # TODO: Implement adaptive algorithm selection
    pass

def optimize_memory_usage():
    """
    Tối ưu hóa memory usage
    """
    def process_large_file_memory_intensive(filename):
        # Bad: Load entire file into memory
        with open(filename, 'r') as f:
            lines = f.readlines()  # O(n) memory
        
        processed = []
        for line in lines:
            processed.append(line.strip().upper())
        return processed
    
    def process_large_file_memory_efficient(filename):
        # Good: Process line by line
        def line_generator():
            with open(filename, 'r') as f:
                for line in f:  # O(1) memory per line
                    yield line.strip().upper()
        return line_generator()
    
    def calculate_sum_memory_intensive(n):
        # Bad: Store all numbers
        numbers = list(range(n))  # O(n) memory
        return sum(numbers)
    
    def calculate_sum_memory_efficient(n):
        # Good: Mathematical formula
        return n * (n - 1) // 2  # O(1) memory
    
    def fibonacci_sequence_memory_intensive(n):
        # Bad: Store all values
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    def fibonacci_sequence_memory_efficient(n):
        # Good: Only store last two values
        if n <= 1:
            return [0] if n == 1 else []
        
        a, b = 0, 1
        result = [0, 1]
        for _ in range(2, n):
            a, b = b, a + b
            result.append(b)
        return result
    
    # TODO: Compare memory usage
    pass

def early_termination_optimization():
    """
    Tối ưu hóa bằng early termination
    """
    def all_elements_positive_naive(arr):
        # Check all elements even if found negative
        positive_count = 0
        for num in arr:
            if num > 0:
                positive_count += 1
        return positive_count == len(arr)
    
    def all_elements_positive_optimized(arr):
        # Early termination when found negative
        for num in arr:
            if num <= 0:
                return False
        return True
    
    def find_max_in_sorted_rotated_naive(arr):
        # O(n) - check all elements
        return max(arr)
    
    def find_max_in_sorted_rotated_optimized(arr):
        # O(log n) - binary search approach
        if not arr:
            return None
        
        left, right = 0, len(arr) - 1
        
        # If array is not rotated
        if arr[left] <= arr[right]:
            return arr[right]
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        
        # left is the rotation point, max is at left-1
        return arr[left - 1] if left > 0 else arr[-1]
    
    # TODO: Implement more early termination examples
    pass

# Test cases
def test_optimization_techniques():
    print("Algorithm Optimization Techniques")
    print("=" * 40)
    
    # Test nested loop optimization
    print("1. Nested Loop Optimization:")
    optimize_nested_loops()
    
    # Test string operation optimization
    print("\n2. String Operation Optimization:")
    optimize_string_operations()
    
    # Test data structure optimization
    print("\n3. Data Structure Choice Optimization:")
    optimize_data_structure_choice()
    
    # Test algorithm choice optimization
    print("\n4. Algorithm Choice Optimization:")
    optimize_algorithm_choice()
    
    # Test memory optimization
    print("\n5. Memory Usage Optimization:")
    optimize_memory_usage()
    
    # Test early termination
    print("\n6. Early Termination Optimization:")
    early_termination_optimization()

if __name__ == "__main__":
    test_optimization_techniques()