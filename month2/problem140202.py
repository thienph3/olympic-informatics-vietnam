"""
Day 14 - Problem 4: SortedList implementation
Thời gian: 25 phút
"""

import bisect

class SortedList:
    """
    Sorted list implementation using bisect module
    Maintains sorted order automatically
    """
    
    def __init__(self, iterable=None):
        """
        Initialize SortedList
        Input: iterable - optional initial values
        """
        # TODO: Initialize internal data structure
        pass
    
    def add(self, item):
        """
        Add item while maintaining sorted order
        Input: item - value to add
        Time complexity: O(n)
        """
        # TODO: Implement add using bisect.insort
        pass
    
    def remove(self, item):
        """
        Remove first occurrence of item
        Input: item - value to remove
        Output: True if removed, False if not found
        Time complexity: O(n)
        """
        # TODO: Implement remove using bisect.bisect_left
        pass
    
    def discard(self, item):
        """
        Remove item if exists (no error if not found)
        Input: item - value to remove
        """
        # TODO: Implement discard
        pass
    
    def __contains__(self, item):
        """
        Check if item exists in list
        Input: item - value to check
        Output: True if exists, False otherwise
        Time complexity: O(log n)
        """
        # TODO: Implement membership test using bisect
        pass
    
    def count(self, item):
        """
        Count occurrences of item
        Input: item - value to count
        Output: number of occurrences
        Time complexity: O(log n)
        """
        # TODO: Implement count using bisect_left và bisect_right
        pass
    
    def index(self, item):
        """
        Get index of first occurrence of item
        Input: item - value to find
        Output: index of item
        Raises: ValueError if not found
        """
        # TODO: Implement index using bisect_left
        pass
    
    def __getitem__(self, index):
        """
        Get item at index
        Input: index - position
        Output: item at position
        """
        # TODO: Implement indexing
        pass
    
    def __len__(self):
        """Get length of list"""
        # TODO: Implement length
        pass
    
    def __iter__(self):
        """Iterator over sorted list"""
        # TODO: Implement iterator
        pass
    
    def __repr__(self):
        """String representation"""
        # TODO: Implement string representation
        pass
    
    def range_query(self, low, high):
        """
        Get all items in range [low, high]
        Input: low, high - range bounds
        Output: list of items in range
        """
        # TODO: Implement range query using bisect
        pass
    
    def pop(self, index=-1):
        """
        Remove and return item at index
        Input: index - position (default last)
        Output: removed item
        """
        # TODO: Implement pop
        pass
    
    def clear(self):
        """Remove all items"""
        # TODO: Implement clear
        pass
    
    def copy(self):
        """Create shallow copy"""
        # TODO: Implement copy
        pass
    
    def extend(self, iterable):
        """
        Add all items from iterable
        Input: iterable - values to add
        """
        # TODO: Implement extend
        pass

class SortedDict:
    """
    Dictionary với keys được maintain sorted order
    """
    
    def __init__(self):
        # TODO: Initialize sorted dict
        pass
    
    def __setitem__(self, key, value):
        """Set key-value pair"""
        # TODO: Implement setitem maintaining sorted keys
        pass
    
    def __getitem__(self, key):
        """Get value by key"""
        # TODO: Implement getitem
        pass
    
    def __delitem__(self, key):
        """Delete key-value pair"""
        # TODO: Implement delitem
        pass
    
    def __contains__(self, key):
        """Check if key exists"""
        # TODO: Implement membership test
        pass
    
    def keys(self):
        """Get sorted keys"""
        # TODO: Return sorted keys
        pass
    
    def values(self):
        """Get values in key order"""
        # TODO: Return values in sorted key order
        pass
    
    def items(self):
        """Get (key, value) pairs in sorted order"""
        # TODO: Return sorted items
        pass
    
    def range_items(self, low_key, high_key):
        """Get items with keys in range [low_key, high_key]"""
        # TODO: Implement range query for dict
        pass

# Test cases
if __name__ == "__main__":
    # Test SortedList
    print("=== SORTED LIST TESTS ===")
    
    # Basic operations
    sl = SortedList([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Initial SortedList: {sl}")
    
    # Test add
    sl.add(7)
    sl.add(0)
    print(f"After adding 7, 0: {sl}")
    
    # Test membership
    print(f"5 in list: {5 in sl}")
    print(f"8 in list: {8 in sl}")
    
    # Test count
    print(f"Count of 1: {sl.count(1)}")
    print(f"Count of 5: {sl.count(5)}")
    
    # Test index
    try:
        print(f"Index of 4: {sl.index(4)}")
        print(f"Index of 8: {sl.index(8)}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Test remove
    print(f"Remove 1: {sl.remove(1)}")
    print(f"After removing 1: {sl}")
    print(f"Remove 10: {sl.remove(10)}")
    
    # Test range query
    range_result = sl.range_query(2, 6)
    print(f"Range [2, 6]: {range_result}")
    
    # Test indexing
    print(f"sl[0]: {sl[0]}")
    print(f"sl[-1]: {sl[-1]}")
    
    # Test pop
    popped = sl.pop()
    print(f"Popped: {popped}, List: {sl}")
    
    # Test extend
    sl.extend([8, 3, 1])
    print(f"After extending [8, 3, 1]: {sl}")
    
    # Test copy
    sl_copy = sl.copy()
    print(f"Copy: {sl_copy}")
    
    # Performance test
    print(f"\n=== PERFORMANCE TEST ===")
    import time
    
    # Test large dataset
    large_sl = SortedList()
    
    # Add performance
    start = time.time()
    for i in range(1000):
        large_sl.add(i % 100)
    add_time = time.time() - start
    print(f"Added 1000 items in {add_time:.4f}s")
    
    # Search performance
    start = time.time()
    for i in range(100):
        _ = i in large_sl
    search_time = time.time() - start
    print(f"100 searches in {search_time:.4f}s")
    
    # Test SortedDict
    print(f"\n=== SORTED DICT TESTS ===")
    
    sd = SortedDict()
    
    # Add items
    items = [("banana", 2), ("apple", 1), ("cherry", 3), ("date", 4)]
    for key, value in items:
        sd[key] = value
    
    print(f"Keys: {list(sd.keys())}")
    print(f"Values: {list(sd.values())}")
    print(f"Items: {list(sd.items())}")
    
    # Test range query
    range_items = sd.range_items("apple", "cherry")
    print(f"Range ['apple', 'cherry']: {range_items}")
    
    # Test membership
    print(f"'banana' in dict: {'banana' in sd}")
    print(f"'grape' in dict: {'grape' in sd}")
    
    # Test deletion
    del sd["banana"]
    print(f"After deleting 'banana': {list(sd.keys())}")
    
    print(f"\n=== COMPLEXITY ANALYSIS ===")
    print("SortedList operations:")
    print("  - add(): O(n) due to insertion")
    print("  - remove(): O(n) due to shifting")
    print("  - __contains__(): O(log n) using binary search")
    print("  - count(): O(log n) using bisect")
    print("  - range_query(): O(log n + k) where k is result size")
    
    print("\\nSortedDict operations:")
    print("  - __setitem__(): O(n) for new keys")
    print("  - __getitem__(): O(log n)")
    print("  - __contains__(): O(log n)")
    print("  - range_items(): O(log n + k)")