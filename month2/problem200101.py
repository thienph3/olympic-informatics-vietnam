"""
Problem 200101: Basic Complexity Analysis
Phân tích độ phức tạp cơ bản của các đoạn code

Topics: Time complexity, Big O notation, algorithm analysis
"""

def analyze_complexity_1():
    """
    Phân tích độ phức tạp của đoạn code này
    """
    def mystery_function(arr):
        n = len(arr)
        for i in range(n):
            print(arr[i])
    
    # TODO: Xác định time complexity và space complexity
    pass

def analyze_complexity_2():
    """
    Phân tích độ phức tạp của nested loops
    """
    def mystery_function(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n):
                print(arr[i] + arr[j])
    
    # TODO: Xác định time complexity và space complexity
    pass

def analyze_complexity_3():
    """
    Phân tích độ phức tạp của loop với step
    """
    def mystery_function(n):
        i = 1
        while i < n:
            print(i)
            i *= 2
    
    # TODO: Xác định time complexity
    pass

def analyze_complexity_4():
    """
    Phân tích độ phức tạp của multiple loops
    """
    def mystery_function(arr1, arr2):
        for item in arr1:
            print(item)
        
        for item in arr2:
            print(item)
        
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                print(arr1[i], arr2[j])
    
    # TODO: Xác định time complexity với len(arr1)=n, len(arr2)=m
    pass

def analyze_complexity_5():
    """
    Phân tích độ phức tạp của binary search
    """
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
    
    # TODO: Xác định time complexity và space complexity
    pass

def analyze_complexity_6():
    """
    Phân tích độ phức tạp của string operations
    """
    def mystery_function(s):
        result = ""
        for char in s:
            result += char  # String concatenation
        return result
    
    # TODO: Xác định time complexity (chú ý string immutable)
    pass

def analyze_complexity_7():
    """
    Phân tích độ phức tạp của list operations
    """
    def mystery_function(n):
        arr = []
        for i in range(n):
            arr.append(i)      # O(1) amortized
        
        for i in range(n):
            arr.insert(0, i)   # O(n) operation
        
        return arr
    
    # TODO: Xác định time complexity tổng
    pass

def compare_algorithms():
    """
    So sánh độ phức tạp của các thuật toán tìm duplicate
    """
    def find_duplicate_v1(arr):
        # Brute force approach
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    return arr[i]
        return None
    
    def find_duplicate_v2(arr):
        # Using set
        seen = set()
        for num in arr:
            if num in seen:
                return num
            seen.add(num)
        return None
    
    def find_duplicate_v3(arr):
        # Using sorting
        arr_sorted = sorted(arr)
        for i in range(len(arr_sorted) - 1):
            if arr_sorted[i] == arr_sorted[i + 1]:
                return arr_sorted[i]
        return None
    
    # TODO: So sánh time và space complexity của 3 approaches
    pass

# Test cases
def test_complexity_analysis():
    print("Analyzing complexity of different algorithms...")
    
    # Test data
    test_arr = list(range(1000))
    test_arr2 = list(range(500))
    
    print("1. Single loop analysis:")
    analyze_complexity_1()
    
    print("2. Nested loops analysis:")
    analyze_complexity_2()
    
    print("3. Logarithmic loop analysis:")
    analyze_complexity_3()
    
    print("4. Multiple loops analysis:")
    analyze_complexity_4()
    
    print("5. Binary search analysis:")
    analyze_complexity_5()
    
    print("6. String operations analysis:")
    analyze_complexity_6()
    
    print("7. List operations analysis:")
    analyze_complexity_7()
    
    print("8. Algorithm comparison:")
    compare_algorithms()

if __name__ == "__main__":
    test_complexity_analysis()