"""
Problem 220302: Nested Structure Recursion
Đệ quy với cấu trúc dữ liệu lồng nhau

Topics: Nested lists, trees, JSON-like structures, recursive data processing
"""

def sum_nested_list(nested_list):
    """
    Tính tổng tất cả số trong cấu trúc lồng nhau
    """
    # TODO: Sum all numbers in nested structure
    pass

def flatten_nested_list(nested_list):
    """
    Làm phẳng danh sách lồng nhau
    """
    # TODO: Flatten arbitrarily nested list
    pass

def count_elements_nested(nested_list):
    """
    Đếm tổng số phần tử (không phải list) trong cấu trúc lồng nhau
    """
    # TODO: Count all non-list elements
    pass

def max_depth_nested(nested_list):
    """
    Tìm độ sâu tối đa của cấu trúc lồng nhau
    """
    # TODO: Find maximum nesting depth
    pass

def find_in_nested(nested_list, target):
    """
    Tìm kiếm phần tử trong cấu trúc lồng nhau
    """
    # TODO: Search for element in nested structure
    pass

def replace_in_nested(nested_list, old_val, new_val):
    """
    Thay thế tất cả giá trị old_val bằng new_val
    """
    # TODO: Replace all occurrences in nested structure
    pass

def nested_list_to_string(nested_list):
    """
    Chuyển cấu trúc lồng nhau thành chuỗi
    """
    # TODO: Convert nested structure to string representation
    pass

def mirror_nested_structure(nested_list):
    """
    Tạo mirror (đảo ngược) của cấu trúc lồng nhau
    """
    # TODO: Create mirror of nested structure
    pass

def validate_nested_brackets(nested_structure):
    """
    Kiểm tra tính hợp lệ của cấu trúc ngoặc lồng nhau
    """
    # TODO: Validate nested bracket structure
    pass

def json_like_processing(data):
    """
    Xử lý cấu trúc giống JSON (dict + list lồng nhau)
    """
    # TODO: Process JSON-like nested structure
    pass

# Test cases
def test_nested_structure_recursion():
    print("Nested Structure Recursion")
    print("=" * 35)
    
    # Test sum nested list
    print("1. Sum Nested List:")
    nested_lists = [
        [1, [2, 3], 4],
        [1, [2, [3, 4]], 5],
        [[1, 2], [3, [4, 5]]],
        [1, 2, 3]
    ]
    for nested in nested_lists:
        result = sum_nested_list(nested)
        print(f"sum({nested}) = {result}")
    
    # Test flatten nested list
    print("\n2. Flatten Nested List:")
    for nested in nested_lists:
        flattened = flatten_nested_list(nested)
        print(f"flatten({nested}) = {flattened}")
    
    # Test count elements
    print("\n3. Count Elements:")
    for nested in nested_lists:
        count = count_elements_nested(nested)
        print(f"count_elements({nested}) = {count}")
    
    # Test max depth
    print("\n4. Maximum Depth:")
    depth_tests = [
        [1, 2, 3],
        [1, [2, 3]],
        [1, [2, [3, [4]]]],
        [[[[1]]]]
    ]
    for nested in depth_tests:
        depth = max_depth_nested(nested)
        print(f"max_depth({nested}) = {depth}")
    
    # Test find in nested
    print("\n5. Find in Nested:")
    find_tests = [
        ([1, [2, 3], 4], 3),
        ([1, [2, [3, 4]], 5], 6),
        ([[1, 2], [3, [4, 5]]], 4)
    ]
    for nested, target in find_tests:
        found = find_in_nested(nested, target)
        print(f"find {target} in {nested}: {found}")
    
    # Test replace in nested
    print("\n6. Replace in Nested:")
    replace_tests = [
        ([1, [2, 3], 2], 2, 9),
        ([1, [1, [1, 2]], 1], 1, 0)
    ]
    for nested, old, new in replace_tests:
        result = replace_in_nested(nested.copy(), old, new)
        print(f"replace {old} with {new} in {nested}: {result}")
    
    # Test nested to string
    print("\n7. Nested to String:")
    string_tests = [
        [1, [2, 3], 4],
        [[1, 2], [3, 4]],
        [1, [2, [3]]]
    ]
    for nested in string_tests:
        string_repr = nested_list_to_string(nested)
        print(f"to_string({nested}) = '{string_repr}'")
    
    # Test mirror structure
    print("\n8. Mirror Structure:")
    mirror_tests = [
        [1, [2, 3], 4],
        [[1, 2], [3, [4, 5]]]
    ]
    for nested in mirror_tests:
        mirrored = mirror_nested_structure(nested)
        print(f"mirror({nested}) = {mirrored}")
    
    # Test validate brackets
    print("\n9. Validate Nested Brackets:")
    bracket_tests = [
        "((()))",
        "((())",
        "(()())",
        "(()(()))"
    ]
    for brackets in bracket_tests:
        is_valid = validate_nested_brackets(brackets)
        print(f"'{brackets}' is valid: {is_valid}")
    
    # Test JSON-like processing
    print("\n10. JSON-like Processing:")
    json_tests = [
        {"name": "John", "scores": [85, 90, 78]},
        {"users": [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]},
        {"data": {"nested": {"deep": [1, 2, 3]}}}
    ]
    for data in json_tests:
        processed = json_like_processing(data)
        print(f"process({data}) = {processed}")

if __name__ == "__main__":
    test_nested_structure_recursion()