"""
Problem 200301: Data Structure Complexity
Phân tích độ phức tạp của các cấu trúc dữ liệu

Topics: Array, list, dict, set operations complexity
"""

def analyze_list_operations():
    """
    Phân tích complexity của Python list operations
    """
    def test_list_operations():
        # Access - O(1)
        arr = list(range(1000))
        element = arr[500]  # O(1)
        
        # Append - O(1) amortized
        arr.append(1001)  # O(1) amortized
        
        # Insert at beginning - O(n)
        arr.insert(0, -1)  # O(n)
        
        # Insert at middle - O(n)
        arr.insert(500, 999)  # O(n)
        
        # Remove by value - O(n)
        arr.remove(999)  # O(n)
        
        # Pop from end - O(1)
        arr.pop()  # O(1)
        
        # Pop from beginning - O(n)
        arr.pop(0)  # O(n)
        
        # Search - O(n)
        index = arr.index(500) if 500 in arr else -1  # O(n)
        
        return arr
    
    # TODO: Phân tích từng operation và đưa ra complexity
    pass

def analyze_dict_operations():
    """
    Phân tích complexity của Python dict operations
    """
    def test_dict_operations():
        # Create dict
        d = {}
        
        # Insert - O(1) average, O(n) worst case
        for i in range(1000):
            d[i] = i ** 2  # O(1) average
        
        # Access - O(1) average, O(n) worst case
        value = d.get(500, 0)  # O(1) average
        
        # Delete - O(1) average, O(n) worst case
        if 999 in d:
            del d[999]  # O(1) average
        
        # Membership test - O(1) average, O(n) worst case
        exists = 500 in d  # O(1) average
        
        # Iterate - O(n)
        for key, value in d.items():  # O(n)
            pass
        
        return d
    
    # TODO: Phân tích hash table collision và worst case
    pass

def analyze_set_operations():
    """
    Phân tích complexity của Python set operations
    """
    def test_set_operations():
        # Create sets
        s1 = set(range(1000))
        s2 = set(range(500, 1500))
        
        # Add - O(1) average
        s1.add(2000)  # O(1) average
        
        # Remove - O(1) average
        s1.discard(2000)  # O(1) average
        
        # Membership test - O(1) average
        exists = 500 in s1  # O(1) average
        
        # Union - O(len(s1) + len(s2))
        union_set = s1 | s2  # O(len(s1) + len(s2))
        
        # Intersection - O(min(len(s1), len(s2)))
        intersection_set = s1 & s2  # O(min(len(s1), len(s2)))
        
        # Difference - O(len(s1))
        diff_set = s1 - s2  # O(len(s1))
        
        return s1, s2
    
    # TODO: Phân tích set operations complexity
    pass

def analyze_string_operations():
    """
    Phân tích complexity của string operations
    """
    def test_string_operations():
        # String concatenation - O(n + m)
        s1 = "Hello"
        s2 = "World"
        s3 = s1 + s2  # O(len(s1) + len(s2))
        
        # String multiplication - O(n * k)
        s4 = "A" * 1000  # O(1000)
        
        # String slicing - O(k) where k is slice length
        substring = s4[100:200]  # O(100)
        
        # String search - O(n * m) worst case
        index = s4.find("A")  # O(n * m) worst case, O(n) average
        
        # String replace - O(n * m)
        s5 = s4.replace("A", "B")  # O(n)
        
        # String split - O(n)
        words = "a b c d e".split()  # O(n)
        
        # String join - O(n)
        joined = " ".join(words)  # O(n)
        
        return s3, s4, s5
    
    # TODO: Phân tích string immutability impact
    pass

def compare_data_structures():
    """
    So sánh complexity của các data structures cho các operations
    """
    def operation_comparison():
        operations = {
            'Access': {
                'List': 'O(1)',
                'Dict': 'O(1) avg',
                'Set': 'N/A'
            },
            'Search': {
                'List': 'O(n)',
                'Dict': 'O(1) avg',
                'Set': 'O(1) avg'
            },
            'Insert': {
                'List': 'O(1) end, O(n) beginning',
                'Dict': 'O(1) avg',
                'Set': 'O(1) avg'
            },
            'Delete': {
                'List': 'O(1) end, O(n) by value',
                'Dict': 'O(1) avg',
                'Set': 'O(1) avg'
            }
        }
        return operations
    
    # TODO: Tạo bảng so sánh chi tiết
    pass

def analyze_nested_structures():
    """
    Phân tích complexity của nested data structures
    """
    def test_nested_operations():
        # 2D list - O(n²) space
        matrix = [[0] * 100 for _ in range(100)]
        
        # Access element - O(1)
        element = matrix[50][50]  # O(1)
        
        # Dict of lists - O(n) space per key
        dict_of_lists = {i: list(range(10)) for i in range(100)}
        
        # Access list in dict - O(1) + O(1) = O(1)
        sublist = dict_of_lists[50]  # O(1)
        element = sublist[5]  # O(1)
        
        # List of dicts - O(n) space
        list_of_dicts = [{'key': i, 'value': i**2} for i in range(100)]
        
        # Search in list of dicts - O(n)
        for d in list_of_dicts:  # O(n)
            if d['key'] == 50:  # O(1)
                break
        
        return matrix, dict_of_lists, list_of_dicts
    
    # TODO: Phân tích nested structure complexity
    pass

def memory_efficient_alternatives():
    """
    Các alternatives tiết kiệm memory
    """
    def compare_memory_usage():
        # List vs Generator
        def create_list(n):
            return [i**2 for i in range(n)]  # O(n) space
        
        def create_generator(n):
            return (i**2 for i in range(n))  # O(1) space
        
        # Dict vs defaultdict
        from collections import defaultdict
        
        def regular_dict_grouping(items):
            groups = {}
            for item in items:
                key = item % 10
                if key not in groups:
                    groups[key] = []
                groups[key].append(item)
            return groups
        
        def defaultdict_grouping(items):
            groups = defaultdict(list)
            for item in items:
                key = item % 10
                groups[key].append(item)
            return dict(groups)
        
        return create_list, create_generator, regular_dict_grouping, defaultdict_grouping
    
    # TODO: So sánh memory efficiency
    pass

# Test cases
def test_data_structure_complexity():
    print("Data Structure Complexity Analysis")
    print("=" * 45)
    
    # Test list operations
    print("1. List Operations Complexity:")
    analyze_list_operations()
    
    # Test dict operations
    print("\n2. Dictionary Operations Complexity:")
    analyze_dict_operations()
    
    # Test set operations
    print("\n3. Set Operations Complexity:")
    analyze_set_operations()
    
    # Test string operations
    print("\n4. String Operations Complexity:")
    analyze_string_operations()
    
    # Compare data structures
    print("\n5. Data Structure Comparison:")
    compare_data_structures()
    
    # Test nested structures
    print("\n6. Nested Structures Complexity:")
    analyze_nested_structures()
    
    # Memory efficient alternatives
    print("\n7. Memory Efficient Alternatives:")
    memory_efficient_alternatives()

if __name__ == "__main__":
    test_data_structure_complexity()