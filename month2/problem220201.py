"""
Problem 220201: String Recursion
Đệ quy trong xử lý chuỗi

Topics: String manipulation, palindromes, pattern matching
"""

def reverse_string_recursive(s):
    """
    Đảo ngược chuỗi bằng đệ quy
    Time: O(n), Space: O(n)
    """
    # TODO: Reverse string recursively
    pass

def is_palindrome_recursive(s):
    """
    Kiểm tra palindrome bằng đệ quy
    Time: O(n), Space: O(n)
    """
    # TODO: Check if string is palindrome recursively
    pass

def count_vowels_recursive(s):
    """
    Đếm số nguyên âm trong chuỗi
    """
    # TODO: Count vowels recursively
    pass

def remove_character_recursive(s, char):
    """
    Loại bỏ tất cả ký tự char khỏi chuỗi
    """
    # TODO: Remove all occurrences of character
    pass

def string_length_recursive(s):
    """
    Tính độ dài chuỗi bằng đệ quy (không dùng len())
    """
    # TODO: Calculate string length recursively
    pass

def count_substring_recursive(s, sub):
    """
    Đếm số lần xuất hiện của substring
    """
    # TODO: Count substring occurrences recursively
    pass

def replace_character_recursive(s, old_char, new_char):
    """
    Thay thế ký tự trong chuỗi
    """
    # TODO: Replace character recursively
    pass

def is_subsequence_recursive(s, t):
    """
    Kiểm tra s có phải subsequence của t không
    """
    # TODO: Check if s is subsequence of t
    pass

def longest_common_prefix_recursive(strs):
    """
    Tìm prefix chung dài nhất của danh sách chuỗi
    """
    # TODO: Find longest common prefix
    pass

def generate_binary_strings_recursive(n):
    """
    Sinh tất cả chuỗi nhị phân độ dài n
    """
    # TODO: Generate all binary strings of length n
    pass

# Test cases
def test_string_recursion():
    print("String Recursion")
    print("=" * 20)
    
    # Test reverse string
    print("1. Reverse String:")
    test_strings = ["hello", "world", "python", "recursion"]
    for s in test_strings:
        reversed_s = reverse_string_recursive(s)
        print(f"reverse('{s}') = '{reversed_s}'")
    
    # Test palindrome
    print("\n2. Palindrome Check:")
    palindrome_tests = ["racecar", "hello", "madam", "python", "level"]
    for s in palindrome_tests:
        is_pal = is_palindrome_recursive(s)
        print(f"'{s}' is palindrome: {is_pal}")
    
    # Test count vowels
    print("\n3. Count Vowels:")
    vowel_tests = ["hello", "programming", "aeiou", "xyz"]
    for s in vowel_tests:
        count = count_vowels_recursive(s)
        print(f"vowels in '{s}': {count}")
    
    # Test remove character
    print("\n4. Remove Character:")
    remove_tests = [("hello", "l"), ("programming", "m"), ("aabbcc", "b")]
    for s, char in remove_tests:
        result = remove_character_recursive(s, char)
        print(f"remove '{char}' from '{s}': '{result}'")
    
    # Test string length
    print("\n5. String Length:")
    for s in test_strings:
        length = string_length_recursive(s)
        print(f"length of '{s}': {length}")
    
    # Test count substring
    print("\n6. Count Substring:")
    substring_tests = [("hello", "l"), ("programming", "mm"), ("aaaa", "aa")]
    for s, sub in substring_tests:
        count = count_substring_recursive(s, sub)
        print(f"'{sub}' in '{s}': {count} times")
    
    # Test replace character
    print("\n7. Replace Character:")
    replace_tests = [("hello", "l", "x"), ("programming", "m", "n")]
    for s, old, new in replace_tests:
        result = replace_character_recursive(s, old, new)
        print(f"replace '{old}' with '{new}' in '{s}': '{result}'")
    
    # Test subsequence
    print("\n8. Subsequence Check:")
    subseq_tests = [("ace", "abcde"), ("aec", "abcde"), ("abc", "def")]
    for s, t in subseq_tests:
        is_subseq = is_subsequence_recursive(s, t)
        print(f"'{s}' is subsequence of '{t}': {is_subseq}")
    
    # Test longest common prefix
    print("\n9. Longest Common Prefix:")
    prefix_tests = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["hello", "help", "hero"]
    ]
    for strs in prefix_tests:
        prefix = longest_common_prefix_recursive(strs)
        print(f"common prefix of {strs}: '{prefix}'")
    
    # Test binary strings generation
    print("\n10. Generate Binary Strings:")
    for n in range(1, 4):
        binary_strings = generate_binary_strings_recursive(n)
        print(f"binary strings of length {n}: {binary_strings}")

if __name__ == "__main__":
    test_string_recursion()