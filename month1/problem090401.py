# Problem 09.04.01: String algorithms cho Olympic

print("=== STRING ALGORITHMS CHO OLYMPIC ===")

# Bài 1: Palindrome algorithms
print("1. Palindrome algorithms:")

def is_palindrome_simple(s):
    """Kiểm tra palindrome đơn giản"""
    return s == s[::-1]

def is_palindrome_ignore_case_space(s):
    """Kiểm tra palindrome bỏ qua case và space"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def longest_palindromic_substring(s):
    """Tìm substring palindrome dài nhất"""
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    for i in range(len(s)):
        # Palindrome lẻ (center tại i)
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > max_len:
                start = left
                max_len = current_len
            left -= 1
            right += 1
        
        # Palindrome chẵn (center giữa i và i+1)
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > max_len:
                start = left
                max_len = current_len
            left -= 1
            right += 1
    
    return s[start:start + max_len]

# Test palindrome
test_strings = [
    "racecar",
    "A man a plan a canal Panama",
    "race a car",
    "abcdef",
    "Madam",
    "babad"
]

print("Palindrome tests:")
for s in test_strings:
    simple = is_palindrome_simple(s)
    ignore_case = is_palindrome_ignore_case_space(s)
    longest = longest_palindromic_substring(s)
    print(f"'{s}':")
    print(f"  Simple: {simple}")
    print(f"  Ignore case/space: {ignore_case}")
    print(f"  Longest palindrome: '{longest}'")

# Bài 2: Anagram algorithms
print("\n2. Anagram algorithms:")

def are_anagrams(s1, s2):
    """Kiểm tra 2 chuỗi có phải anagram"""
    return sorted(s1.lower()) == sorted(s2.lower())

def find_anagrams(word, word_list):
    """Tìm tất cả anagram của word trong word_list"""
    word_sorted = sorted(word.lower())
    anagrams = []
    
    for w in word_list:
        if sorted(w.lower()) == word_sorted and w.lower() != word.lower():
            anagrams.append(w)
    
    return anagrams

def group_anagrams(words):
    """Nhóm các từ thành các nhóm anagram"""
    groups = {}
    
    for word in words:
        key = ''.join(sorted(word.lower()))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return [group for group in groups.values() if len(group) > 1]

# Test anagram
word_list = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
target_word = "eat"

print(f"Anagrams of '{target_word}': {find_anagrams(target_word, word_list)}")

anagram_groups = group_anagrams(word_list)
print("Anagram groups:")
for i, group in enumerate(anagram_groups, 1):
    print(f"  Group {i}: {group}")

# Bài 3: String matching algorithms
print("\n3. String matching algorithms:")

def naive_string_match(text, pattern):
    """Thuật toán naive string matching"""
    positions = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            positions.append(i)
    
    return positions

def kmp_search(text, pattern):
    """Thuật toán KMP (Knuth-Morris-Pratt)"""
    def compute_lps(pattern):
        """Tính Longest Proper Prefix which is also Suffix"""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    positions = []
    n, m = len(text), len(pattern)
    
    if m == 0:
        return positions
    
    lps = compute_lps(pattern)
    i = j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return positions

# Test string matching
text = "ABABDABACDABABCABCABCABCABC"
pattern = "ABABCAB"

naive_result = naive_string_match(text, pattern)
kmp_result = kmp_search(text, pattern)

print(f"Text: {text}")
print(f"Pattern: {pattern}")
print(f"Naive algorithm: {naive_result}")
print(f"KMP algorithm: {kmp_result}")

# Bài 4: Caesar cipher
print("\n4. Caesar cipher:")

def caesar_encrypt(text, shift):
    """Mã hóa Caesar"""
    result = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    
    return result

def caesar_decrypt(text, shift):
    """Giải mã Caesar"""
    return caesar_encrypt(text, -shift)

def caesar_brute_force(ciphertext):
    """Thử tất cả các shift có thể"""
    results = []
    
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append((shift, decrypted))
    
    return results

# Test Caesar cipher
original_text = "Hello World! This is a secret message."
shift_value = 7

encrypted = caesar_encrypt(original_text, shift_value)
decrypted = caesar_decrypt(encrypted, shift_value)

print(f"Original: {original_text}")
print(f"Encrypted (shift {shift_value}): {encrypted}")
print(f"Decrypted: {decrypted}")

# Brute force example
mystery_cipher = "Khoor Zruog!"
print(f"\nBrute force attack on '{mystery_cipher}':")
brute_results = caesar_brute_force(mystery_cipher)
for shift, text in brute_results[:10]:  # Show first 10
    print(f"  Shift {shift:2d}: {text}")

# Bài 5: Longest Common Subsequence (LCS)
print("\n5. Longest Common Subsequence:")

def lcs_length(s1, s2):
    """Tính độ dài LCS"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def lcs_string(s1, s2):
    """Tìm chuỗi LCS thực tế"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Tính bảng DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Truy vết
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

# Test LCS
string1 = "ABCDGH"
string2 = "AEDFHR"
string3 = "PROGRAMMING"
string4 = "ALGORITHM"

print(f"LCS('{string1}', '{string2}'):")
print(f"  Length: {lcs_length(string1, string2)}")
print(f"  String: '{lcs_string(string1, string2)}'")

print(f"LCS('{string3}', '{string4}'):")
print(f"  Length: {lcs_length(string3, string4)}")
print(f"  String: '{lcs_string(string3, string4)}'")

# Bài 6: Edit Distance (Levenshtein)
print("\n6. Edit Distance:")

def edit_distance(s1, s2):
    """Tính khoảng cách chỉnh sửa"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Khởi tạo
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Tính DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Xóa
                    dp[i][j-1],    # Chèn
                    dp[i-1][j-1]   # Thay thế
                )
    
    return dp[m][n]

def find_similar_words(target, word_list, max_distance=2):
    """Tìm từ tương tự dựa trên edit distance"""
    similar = []
    
    for word in word_list:
        distance = edit_distance(target, word)
        if distance <= max_distance:
            similar.append((word, distance))
    
    return sorted(similar, key=lambda x: x[1])

# Test Edit Distance
word_pairs = [
    ("kitten", "sitting"),
    ("saturday", "sunday"),
    ("intention", "execution"),
    ("algorithm", "logarithm")
]

print("Edit distances:")
for w1, w2 in word_pairs:
    distance = edit_distance(w1, w2)
    print(f"  '{w1}' -> '{w2}': {distance}")

# Spell checker example
dictionary = ["python", "program", "algorithm", "computer", "science", "data", "structure"]
misspelled = "progam"

similar_words = find_similar_words(misspelled, dictionary)
print(f"\nSpell check for '{misspelled}':")
for word, distance in similar_words:
    print(f"  '{word}' (distance: {distance})")

# Bài 7: String compression
print("\n7. String compression:")

def run_length_encode(s):
    """Run-length encoding"""
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    encoded.append(f"{current_char}{count}")
    return ''.join(encoded)

def run_length_decode(encoded):
    """Run-length decoding"""
    decoded = []
    i = 0
    
    while i < len(encoded):
        char = encoded[i]
        i += 1
        
        # Đọc số
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        
        count = int(num_str) if num_str else 1
        decoded.append(char * count)
    
    return ''.join(decoded)

# Test compression
test_strings_compression = [
    "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnooopppqqqrrrssstttuuuvvvwwwxxxyyyzzz",
    "aabbcc",
    "abcdef",
    "aaaaaaaaaa"
]

print("Run-length encoding:")
for s in test_strings_compression:
    encoded = run_length_encode(s)
    decoded = run_length_decode(encoded)
    compression_ratio = len(encoded) / len(s) if s else 0
    
    print(f"Original ({len(s)}): {s[:50]}{'...' if len(s) > 50 else ''}")
    print(f"Encoded ({len(encoded)}): {encoded}")
    print(f"Compression ratio: {compression_ratio:.2f}")
    print(f"Decode correct: {decoded == s}")
    print()