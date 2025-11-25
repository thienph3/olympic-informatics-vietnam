"""
Problem 120102: Custom modules và packages
Tạo custom modules, organize code thành packages

Bài 1: Custom Module Creation
- Math utilities module
- String processing module
- Data structures module

Bài 2: Package Organization
- Create package structure
- Import patterns
- Module documentation
"""

# This file demonstrates custom module creation and usage
# In a real project, these would be separate files

# ============= MATH UTILITIES MODULE =============
# File: math_utils.py (would be separate file)

"""
Math utilities module for Olympic programming
Provides common mathematical functions and algorithms
"""

import math
from typing import List, Tuple, Union

def gcd(a: int, b: int) -> int:
    """
    Calculate Greatest Common Divisor using Euclidean algorithm
    
    Args:
        a, b: Two integers
        
    Returns:
        GCD of a and b
        
    Example:
        >>> gcd(48, 18)
        6
    """
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """Calculate Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

def is_prime(n: int) -> bool:
    """
    Check if a number is prime
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(n: int) -> List[int]:
    """Get prime factorization of a number"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def fibonacci_sequence(n: int) -> List[int]:
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def factorial(n: int) -> int:
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n: int, r: int) -> int:
    """Calculate C(n,r) = n! / (r! * (n-r)!)"""
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    
    r = min(r, n - r)  # Take advantage of symmetry
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result

def permutation(n: int, r: int) -> int:
    """Calculate P(n,r) = n! / (n-r)!"""
    if r > n or r < 0:
        return 0
    
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result

# Module constants
PI = 3.141592653589793
E = 2.718281828459045
GOLDEN_RATIO = 1.618033988749895

# ============= STRING PROCESSING MODULE =============
# File: string_utils.py (would be separate file)

"""
String processing utilities for text manipulation and analysis
"""

import re
from collections import Counter
from typing import Dict, List

def is_palindrome(s: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """
    Check if string is palindrome
    
    Args:
        s: String to check
        ignore_case: Whether to ignore case differences
        ignore_spaces: Whether to ignore spaces and punctuation
        
    Returns:
        True if string is palindrome
    """
    if ignore_spaces:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
    
    if ignore_case:
        s = s.lower()
    
    return s == s[::-1]

def word_frequency(text: str) -> Dict[str, int]:
    """Count frequency of words in text"""
    # Remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

def char_frequency(text: str) -> Dict[str, int]:
    """Count frequency of characters in text"""
    return dict(Counter(text.lower()))

def longest_word(text: str) -> str:
    """Find longest word in text"""
    words = re.findall(r'\b\w+\b', text)
    return max(words, key=len) if words else ""

def reverse_words(text: str) -> str:
    """Reverse order of words in text"""
    return ' '.join(text.split()[::-1])

def caesar_cipher(text: str, shift: int) -> str:
    """Apply Caesar cipher to text"""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def remove_duplicates(text: str) -> str:
    """Remove duplicate characters while preserving order"""
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def count_vowels_consonants(text: str) -> Tuple[int, int]:
    """Count vowels and consonants in text"""
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

def text_statistics(text: str) -> Dict[str, Union[int, float]]:
    """Get comprehensive text statistics"""
    words = text.split()
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    return {
        'characters': len(text),
        'characters_no_spaces': len(text.replace(' ', '')),
        'words': len(words),
        'sentences': len(sentences),
        'paragraphs': len([p for p in text.split('\n\n') if p.strip()]),
        'avg_word_length': sum(len(word) for word in words) / len(words) if words else 0,
        'avg_sentence_length': len(words) / len(sentences) if sentences else 0
    }

# ============= DATA STRUCTURES MODULE =============
# File: data_structures.py (would be separate file)

"""
Custom data structures for competitive programming
"""

class Stack:
    """Simple stack implementation"""
    
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self._items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items in stack"""
        return len(self._items)
    
    def __str__(self):
        return f"Stack({self._items})"

class Queue:
    """Simple queue implementation"""
    
    def __init__(self):
        self._items = []
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)
    
    def front(self):
        """Return front item without removing"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items in queue"""
        return len(self._items)
    
    def __str__(self):
        return f"Queue({self._items})"

class CircularBuffer:
    """Fixed-size circular buffer"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self._buffer = [None] * capacity
        self._head = 0
        self._tail = 0
        self._size = 0
    
    def put(self, item):
        """Add item to buffer"""
        self._buffer[self._tail] = item
        self._tail = (self._tail + 1) % self.capacity
        
        if self._size < self.capacity:
            self._size += 1
        else:
            self._head = (self._head + 1) % self.capacity
    
    def get(self):
        """Remove and return oldest item"""
        if self.is_empty():
            raise IndexError("get from empty buffer")
        
        item = self._buffer[self._head]
        self._head = (self._head + 1) % self.capacity
        self._size -= 1
        return item
    
    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size == self.capacity
    
    def size(self):
        return self._size
    
    def __str__(self):
        if self.is_empty():
            return "CircularBuffer([])"
        
        items = []
        current = self._head
        for _ in range(self._size):
            items.append(self._buffer[current])
            current = (current + 1) % self.capacity
        
        return f"CircularBuffer({items})"

class LRUCache:
    """Least Recently Used Cache"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self._cache = {}
        self._order = []
    
    def get(self, key):
        """Get value by key"""
        if key in self._cache:
            # Move to end (most recently used)
            self._order.remove(key)
            self._order.append(key)
            return self._cache[key]
        return None
    
    def put(self, key, value):
        """Put key-value pair"""
        if key in self._cache:
            # Update existing
            self._cache[key] = value
            self._order.remove(key)
            self._order.append(key)
        else:
            # Add new
            if len(self._cache) >= self.capacity:
                # Remove least recently used
                oldest = self._order.pop(0)
                del self._cache[oldest]
            
            self._cache[key] = value
            self._order.append(key)
    
    def size(self):
        return len(self._cache)
    
    def __str__(self):
        return f"LRUCache({dict(self._cache)})"

# ============= PACKAGE DEMONSTRATION =============

def demonstrate_math_utils():
    """Demonstrate math utilities"""
    print("=== Math Utilities Demo ===")
    
    # GCD and LCM
    a, b = 48, 18
    print(f"GCD({a}, {b}) = {gcd(a, b)}")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
    
    # Prime operations
    numbers = [17, 25, 29, 100]
    for n in numbers:
        print(f"{n} is prime: {is_prime(n)}")
    
    print(f"Prime factors of 60: {prime_factors(60)}")
    
    # Sequences
    print(f"First 10 Fibonacci: {fibonacci_sequence(10)}")
    print(f"5! = {factorial(5)}")
    
    # Combinatorics
    print(f"C(5,2) = {combination(5, 2)}")
    print(f"P(5,2) = {permutation(5, 2)}")
    
    # Constants
    print(f"π ≈ {PI}")
    print(f"e ≈ {E}")
    print(f"φ ≈ {GOLDEN_RATIO}")

def demonstrate_string_utils():
    """Demonstrate string utilities"""
    print("\n=== String Utilities Demo ===")
    
    # Palindrome check
    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
    for s in test_strings:
        print(f"'{s}' is palindrome: {is_palindrome(s)}")
    
    # Text analysis
    text = "Hello world! This is a sample text for analysis. Hello again!"
    print(f"\nText: {text}")
    print(f"Word frequency: {word_frequency(text)}")
    print(f"Longest word: {longest_word(text)}")
    print(f"Reversed words: {reverse_words(text)}")
    
    # Caesar cipher
    message = "Hello World"
    encrypted = caesar_cipher(message, 3)
    decrypted = caesar_cipher(encrypted, -3)
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Text statistics
    stats = text_statistics(text)
    print(f"Text statistics: {stats}")

def demonstrate_data_structures():
    """Demonstrate custom data structures"""
    print("\n=== Data Structures Demo ===")
    
    # Stack
    stack = Stack()
    for i in [1, 2, 3, 4, 5]:
        stack.push(i)
    print(f"Stack after pushes: {stack}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    print(f"Stack size: {stack.size()}")
    
    # Queue
    queue = Queue()
    for i in [1, 2, 3, 4, 5]:
        queue.enqueue(i)
    print(f"\nQueue after enqueues: {queue}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Front: {queue.front()}")
    print(f"Queue size: {queue.size()}")
    
    # Circular Buffer
    buffer = CircularBuffer(3)
    for i in range(5):
        buffer.put(i)
        print(f"After putting {i}: {buffer}")
    
    # LRU Cache
    cache = LRUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(f"\nCache after puts: {cache}")
    
    print(f"Get 'a': {cache.get('a')}")
    cache.put("d", 4)  # Should evict 'b'
    print(f"After putting 'd': {cache}")

def module_documentation_example():
    """Demonstrate module documentation practices"""
    print("\n=== Module Documentation ===")
    
    # Function with comprehensive docstring
    def complex_function(data: List[int], threshold: float = 0.5, 
                        normalize: bool = True) -> Dict[str, float]:
        """
        Process numerical data with various options.
        
        This function demonstrates comprehensive documentation practices
        including type hints, parameter descriptions, and examples.
        
        Args:
            data: List of integers to process
            threshold: Minimum value threshold (default: 0.5)
            normalize: Whether to normalize results (default: True)
            
        Returns:
            Dictionary containing processed statistics:
            - 'mean': Average value
            - 'max': Maximum value
            - 'min': Minimum value
            - 'count': Number of values above threshold
            
        Raises:
            ValueError: If data is empty
            TypeError: If data contains non-numeric values
            
        Examples:
            >>> complex_function([1, 2, 3, 4, 5])
            {'mean': 3.0, 'max': 5, 'min': 1, 'count': 5}
            
            >>> complex_function([1, 2, 3], threshold=2.0)
            {'mean': 2.0, 'max': 3, 'min': 1, 'count': 1}
        """
        if not data:
            raise ValueError("Data cannot be empty")
        
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Data must contain only numeric values")
        
        filtered_data = [x for x in data if x >= threshold]
        
        if not filtered_data:
            return {'mean': 0, 'max': 0, 'min': 0, 'count': 0}
        
        result = {
            'mean': sum(filtered_data) / len(filtered_data),
            'max': max(filtered_data),
            'min': min(filtered_data),
            'count': len(filtered_data)
        }
        
        if normalize and result['max'] != result['min']:
            # Normalize to 0-1 range
            range_val = result['max'] - result['min']
            result['mean'] = (result['mean'] - result['min']) / range_val
        
        return result
    
    # Test the documented function
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = complex_function(test_data, threshold=3.0)
    print(f"Function result: {result}")
    
    # Show docstring
    print(f"Function docstring preview:")
    print(f"  {complex_function.__doc__.split('.')[0]}.")

# Test all demonstrations
if __name__ == "__main__":
    demonstrate_math_utils()
    demonstrate_string_utils()
    demonstrate_data_structures()
    module_documentation_example()
    
    print("\n=== Bài tập thực hành ===")
    print("1. Tạo Olympic math library với advanced algorithms")
    print("2. Build text processing package cho competitive programming")
    print("3. Implement advanced data structures (Trie, Segment Tree)")
    print("4. Create package với proper documentation và testing")