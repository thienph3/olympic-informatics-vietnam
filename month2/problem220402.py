"""
Problem 220402: Advanced Recursive Problems
Bài toán đệ quy nâng cao cho Olympic

Topics: Complex recursive problems, optimization, real contest problems
"""

def edit_distance_recursive(s1, s2):
    """
    Tính edit distance (Levenshtein distance) bằng đệ quy
    Time: O(3^max(m,n)) without memoization
    """
    # TODO: Calculate edit distance recursively
    pass

def longest_palindromic_subsequence(s):
    """
    Tìm độ dài subsequence palindrome dài nhất
    """
    # TODO: Find longest palindromic subsequence length
    pass

def count_ways_to_climb_stairs(n, steps=[1, 2, 3]):
    """
    Đếm số cách leo cầu thang với các bước cho phép
    """
    # TODO: Count ways to climb stairs with given step sizes
    pass

def partition_equal_sum_recursive(arr):
    """
    Kiểm tra có thể chia mảng thành 2 phần có tổng bằng nhau không
    """
    # TODO: Check if array can be partitioned into equal sum subsets
    pass

def word_break_recursive(s, word_dict):
    """
    Kiểm tra có thể chia chuỗi thành các từ trong dictionary không
    """
    # TODO: Check if string can be segmented into dictionary words
    pass

def decode_ways_recursive(s):
    """
    Đếm số cách decode chuỗi số thành chữ cái (A=1, B=2, ..., Z=26)
    """
    # TODO: Count ways to decode numeric string
    pass

def unique_paths_recursive(m, n):
    """
    Đếm số đường đi duy nhất trong lưới m×n (chỉ đi xuống và phải)
    """
    # TODO: Count unique paths in grid
    pass

def coin_change_recursive(coins, amount):
    """
    Tìm số coin tối thiểu để tạo thành amount
    """
    # TODO: Find minimum coins needed for amount
    pass

def house_robber_recursive(houses):
    """
    Bài toán house robber - không được cướp 2 nhà liền kề
    """
    # TODO: Find maximum money that can be robbed
    pass

def expression_evaluation_recursive(expression):
    """
    Tính giá trị biểu thức với dấu ngoặc bằng đệ quy
    """
    # TODO: Evaluate mathematical expression recursively
    pass

# Test cases
def test_advanced_recursive_problems():
    print("Advanced Recursive Problems")
    print("=" * 35)
    
    # Test edit distance
    print("1. Edit Distance:")
    edit_tests = [
        ("kitten", "sitting"),
        ("horse", "ros"),
        ("intention", "execution")
    ]
    for s1, s2 in edit_tests:
        distance = edit_distance_recursive(s1, s2)
        print(f"edit_distance('{s1}', '{s2}') = {distance}")
    
    # Test longest palindromic subsequence
    print("\n2. Longest Palindromic Subsequence:")
    palindrome_tests = ["bbbab", "cbbd", "racecar", "abcdef"]
    for s in palindrome_tests:
        length = longest_palindromic_subsequence(s)
        print(f"LPS('{s}') = {length}")
    
    # Test climbing stairs
    print("\n3. Climbing Stairs:")
    stair_tests = [
        (4, [1, 2]),
        (5, [1, 2, 3]),
        (6, [1, 3, 5])
    ]
    for n, steps in stair_tests:
        ways = count_ways_to_climb_stairs(n, steps)
        print(f"climb {n} stairs with steps {steps}: {ways} ways")
    
    # Test partition equal sum
    print("\n4. Partition Equal Sum:")
    partition_tests = [
        [1, 5, 11, 5],
        [1, 2, 3, 5],
        [1, 1, 1, 1]
    ]
    for arr in partition_tests:
        can_partition = partition_equal_sum_recursive(arr)
        print(f"partition {arr}: {can_partition}")
    
    # Test word break
    print("\n5. Word Break:")
    word_break_tests = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple", "pen"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"])
    ]
    for s, word_dict in word_break_tests:
        can_break = word_break_recursive(s, word_dict)
        print(f"word_break('{s}', {word_dict}): {can_break}")
    
    # Test decode ways
    print("\n6. Decode Ways:")
    decode_tests = ["12", "226", "0", "06", "10"]
    for s in decode_tests:
        ways = decode_ways_recursive(s)
        print(f"decode_ways('{s}') = {ways}")
    
    # Test unique paths
    print("\n7. Unique Paths:")
    path_tests = [(3, 7), (3, 2), (7, 3), (3, 3)]
    for m, n in path_tests:
        paths = unique_paths_recursive(m, n)
        print(f"unique_paths({m}, {n}) = {paths}")
    
    # Test coin change
    print("\n8. Coin Change:")
    coin_tests = [
        ([1, 3, 4], 6),
        ([2], 3),
        ([1, 2, 5], 11)
    ]
    for coins, amount in coin_tests:
        min_coins = coin_change_recursive(coins, amount)
        print(f"coin_change({coins}, {amount}) = {min_coins}")
    
    # Test house robber
    print("\n9. House Robber:")
    house_tests = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 1, 1, 2]
    ]
    for houses in house_tests:
        max_money = house_robber_recursive(houses)
        print(f"house_robber({houses}) = {max_money}")
    
    # Test expression evaluation
    print("\n10. Expression Evaluation:")
    expression_tests = [
        "2+3*4",
        "(2+3)*4",
        "2*(3+4)",
        "((2+3)*4)+5"
    ]
    for expr in expression_tests:
        try:
            result = expression_evaluation_recursive(expr)
            print(f"eval('{expr}') = {result}")
        except:
            print(f"eval('{expr}') = Error")
    
    # Performance tips for Olympic
    print("\n11. Olympic Performance Tips:")
    tips = [
        "1. Always add memoization for overlapping subproblems",
        "2. Consider iterative DP if recursion is too deep",
        "3. Use @lru_cache for quick memoization",
        "4. Be aware of Python's recursion limit (default ~1000)",
        "5. Profile recursive solutions to find bottlenecks",
        "6. Sometimes bottom-up DP is faster than memoized recursion",
        "7. Consider space optimization for large inputs"
    ]
    for tip in tips:
        print(tip)

if __name__ == "__main__":
    test_advanced_recursive_problems()