"""
Problem 110302: Recursion với data structures
Sử dụng đệ quy để xử lý lists, strings và nested structures

Bài 1: Advanced List Processing
- Merge sort, quick sort
- Permutations và combinations
- Subset generation

Bài 2: Tree và Nested Structure Operations
- Binary tree operations
- JSON-like structure processing
- Graph traversal basics
"""

# Advanced Sorting
def merge_sort_recursive(arr):
    """Merge sort đệ quy"""
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    
    # Conquer (merge)
    return merge_sorted_arrays(left, right)

def merge_sorted_arrays(left, right):
    """Merge hai arrays đã sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort_recursive(arr):
    """Quick sort đệ quy"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

def quick_sort_inplace(arr, low=0, high=None):
    """Quick sort in-place đệ quy"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """Partition function for quick sort"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Permutations và Combinations
def generate_permutations(arr):
    """Generate tất cả permutations đệ quy"""
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        # Take current element
        current = arr[i]
        # Get remaining elements
        remaining = arr[:i] + arr[i+1:]
        
        # Generate permutations of remaining
        for perm in generate_permutations(remaining):
            result.append([current] + perm)
    
    return result

def generate_combinations(arr, r):
    """Generate combinations of r elements đệ quy"""
    if r == 0:
        return [[]]
    if len(arr) < r:
        return []
    
    result = []
    
    # Include first element
    first = arr[0]
    rest = arr[1:]
    
    # Combinations including first element
    for combo in generate_combinations(rest, r - 1):
        result.append([first] + combo)
    
    # Combinations not including first element
    result.extend(generate_combinations(rest, r))
    
    return result

def generate_subsets(arr):
    """Generate tất cả subsets đệ quy"""
    if not arr:
        return [[]]
    
    first = arr[0]
    rest = arr[1:]
    
    # Get subsets of rest
    subsets_without_first = generate_subsets(rest)
    
    # Add subsets with first element
    subsets_with_first = [[first] + subset for subset in subsets_without_first]
    
    return subsets_without_first + subsets_with_first

def generate_subsets_with_sum(arr, target_sum):
    """Generate subsets có tổng bằng target_sum"""
    def backtrack(index, current_subset, current_sum):
        if current_sum == target_sum:
            return [current_subset[:]]
        
        if index >= len(arr) or current_sum > target_sum:
            return []
        
        result = []
        
        # Include current element
        current_subset.append(arr[index])
        result.extend(backtrack(index + 1, current_subset, current_sum + arr[index]))
        current_subset.pop()
        
        # Exclude current element
        result.extend(backtrack(index + 1, current_subset, current_sum))
        
        return result
    
    return backtrack(0, [], 0)

# Binary Tree Operations
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

def tree_height(root):
    """Tính chiều cao cây đệ quy"""
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

def tree_size(root):
    """Đếm số nodes trong cây đệ quy"""
    if not root:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)

def tree_sum(root):
    """Tính tổng values trong cây đệ quy"""
    if not root:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

def inorder_traversal(root):
    """In-order traversal đệ quy"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def preorder_traversal(root):
    """Pre-order traversal đệ quy"""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def postorder_traversal(root):
    """Post-order traversal đệ quy"""
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

def find_in_tree(root, target):
    """Tìm value trong cây đệ quy"""
    if not root:
        return False
    if root.val == target:
        return True
    return find_in_tree(root.left, target) or find_in_tree(root.right, target)

def tree_paths(root):
    """Tìm tất cả paths từ root đến leaves"""
    if not root:
        return []
    
    if not root.left and not root.right:
        return [[root.val]]
    
    paths = []
    
    # Paths through left subtree
    for path in tree_paths(root.left):
        paths.append([root.val] + path)
    
    # Paths through right subtree
    for path in tree_paths(root.right):
        paths.append([root.val] + path)
    
    return paths

def is_symmetric_tree(root):
    """Kiểm tra cây có symmetric không"""
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    if not root:
        return True
    return is_mirror(root.left, root.right)

# Nested Structure Processing
def deep_sum(obj):
    """Tính tổng tất cả numbers trong nested structure"""
    if isinstance(obj, (int, float)):
        return obj
    elif isinstance(obj, list):
        return sum(deep_sum(item) for item in obj)
    elif isinstance(obj, dict):
        return sum(deep_sum(value) for value in obj.values())
    else:
        return 0

def deep_count(obj, target_type):
    """Đếm số elements của target_type trong nested structure"""
    if isinstance(obj, target_type):
        return 1
    elif isinstance(obj, list):
        return sum(deep_count(item, target_type) for item in obj)
    elif isinstance(obj, dict):
        return sum(deep_count(value, target_type) for value in obj.values())
    else:
        return 0

def deep_find(obj, target):
    """Tìm target trong nested structure"""
    if obj == target:
        return True
    elif isinstance(obj, list):
        return any(deep_find(item, target) for item in obj)
    elif isinstance(obj, dict):
        return any(deep_find(value, target) for value in obj.values())
    else:
        return False

def deep_transform(obj, transform_func):
    """Transform tất cả values trong nested structure"""
    if isinstance(obj, list):
        return [deep_transform(item, transform_func) for item in obj]
    elif isinstance(obj, dict):
        return {key: deep_transform(value, transform_func) for key, value in obj.items()}
    else:
        return transform_func(obj)

def flatten_dict(d, parent_key='', sep='.'):
    """Flatten nested dictionary đệ quy"""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Graph Traversal Basics
def dfs_recursive(graph, start, visited=None):
    """Depth-First Search đệ quy"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    path = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path.extend(dfs_recursive(graph, neighbor, visited))
    
    return path

def find_path_dfs(graph, start, end, path=None):
    """Tìm path từ start đến end bằng DFS đệ quy"""
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return path
    
    for neighbor in graph.get(start, []):
        if neighbor not in path:  # Avoid cycles
            new_path = find_path_dfs(graph, neighbor, end, path)
            if new_path:
                return new_path
    
    return None

def find_all_paths_dfs(graph, start, end, path=None):
    """Tìm tất cả paths từ start đến end"""
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in path:  # Avoid cycles
            new_paths = find_all_paths_dfs(graph, neighbor, end, path)
            paths.extend(new_paths)
    
    return paths

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Advanced List Processing ===")
    
    # Test sorting
    unsorted = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Original: {unsorted}")
    print(f"Merge sort: {merge_sort_recursive(unsorted.copy())}")
    print(f"Quick sort: {quick_sort_recursive(unsorted.copy())}")
    
    # Test permutations
    arr = [1, 2, 3]
    perms = generate_permutations(arr)
    print(f"\nPermutations of {arr}: {perms}")
    
    # Test combinations
    combos = generate_combinations([1, 2, 3, 4], 2)
    print(f"Combinations of [1,2,3,4] choose 2: {combos}")
    
    # Test subsets
    subsets = generate_subsets([1, 2, 3])
    print(f"All subsets of [1,2,3]: {subsets}")
    
    # Test subset sum
    target_subsets = generate_subsets_with_sum([1, 2, 3, 4, 5], 5)
    print(f"Subsets with sum 5: {target_subsets}")
    
    print("\n=== Bài 2: Tree Operations ===")
    
    # Create test tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Tree height: {tree_height(root)}")
    print(f"Tree size: {tree_size(root)}")
    print(f"Tree sum: {tree_sum(root)}")
    print(f"Inorder: {inorder_traversal(root)}")
    print(f"Preorder: {preorder_traversal(root)}")
    print(f"Postorder: {postorder_traversal(root)}")
    print(f"Find 3: {find_in_tree(root, 3)}")
    print(f"Find 6: {find_in_tree(root, 6)}")
    print(f"All paths: {tree_paths(root)}")
    
    # Test nested structures
    nested_data = {
        'numbers': [1, 2, [3, 4]],
        'more': {
            'nested': [5, 6],
            'value': 7
        }
    }
    
    print(f"\nNested structure: {nested_data}")
    print(f"Deep sum: {deep_sum(nested_data)}")
    print(f"Count integers: {deep_count(nested_data, int)}")
    print(f"Find 5: {deep_find(nested_data, 5)}")
    
    # Transform all numbers
    doubled = deep_transform(nested_data, lambda x: x * 2 if isinstance(x, int) else x)
    print(f"Doubled numbers: {doubled}")
    
    # Test graph traversal
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print(f"\nGraph: {graph}")
    print(f"DFS from A: {dfs_recursive(graph, 'A')}")
    print(f"Path A to F: {find_path_dfs(graph, 'A', 'F')}")
    print(f"All paths A to F: {find_all_paths_dfs(graph, 'A', 'F')}")

    print("\n=== Bài tập thực hành ===")
    print("1. Implement N-Queens solver")
    print("2. Solve Sudoku puzzle recursively")
    print("3. Generate maze paths")
    print("4. Build expression tree evaluator")