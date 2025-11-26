"""
Day 16 - Problem 8: Practical sorting applications
Thời gian: 30 phút
"""

def sort_students_multi_criteria(students):
    """
    Sắp xếp students theo multiple criteria: grade (desc), then name (asc)
    Input: students - list of (name, grade) tuples
    Output: sorted list
    """
    # TODO: Implement multi-criteria sorting using basic sorts
    pass

def sort_intervals_by_overlap(intervals):
    """
    Sắp xếp intervals để minimize overlaps
    Input: intervals - list of [start, end] pairs
    Output: sorted intervals
    """
    # TODO: Implement interval sorting
    pass

def tournament_bracket_sorting(players):
    """
    Sắp xếp players cho tournament bracket
    Input: players - list of (name, skill_level) tuples
    Output: tournament bracket arrangement
    """
    # TODO: Implement tournament bracket sorting
    pass

def sort_tasks_by_priority_and_deadline(tasks):
    """
    Sắp xếp tasks theo priority và deadline
    Input: tasks - list of (task_name, priority, deadline) tuples
    Output: sorted task list
    """
    # TODO: Implement task sorting
    pass

def sort_colors_dutch_flag(colors):
    """
    Sort colors (0=red, 1=white, 2=blue) - Dutch National Flag problem
    Input: colors - list of 0s, 1s, 2s
    Output: sorted list using basic sorting approach
    """
    # TODO: Implement Dutch flag sorting
    pass

def sort_linked_list_merge_k(lists):
    """
    Merge k sorted linked lists using basic sorting
    Input: lists - list of sorted linked list heads
    Output: merged sorted linked list head
    """
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    # TODO: Implement k-way merge using basic sorting
    pass

def sort_matrix_diagonally(matrix):
    """
    Sắp xếp matrix theo diagonals
    Input: matrix - 2D matrix
    Output: matrix với sorted diagonals
    """
    # TODO: Implement diagonal sorting
    pass

def sort_array_by_frequency_then_value(arr):
    """
    Sắp xếp array theo frequency (asc), then by value (asc)
    Input: arr - list of integers
    Output: sorted list
    """
    # TODO: Implement frequency-based sorting
    pass

def sort_strings_by_custom_alphabet(strings, alphabet):
    """
    Sắp xếp strings theo custom alphabet order
    Input: strings - list of strings, alphabet - custom order
    Output: sorted strings
    """
    # TODO: Implement custom alphabet sorting
    pass

def pancake_sorting(arr):
    """
    Pancake sorting - chỉ được flip prefix của array
    Input: arr - list of integers
    Output: tuple (sorted_arr, flip_sequence)
    """
    # TODO: Implement pancake sorting
    pass

# Helper functions
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    """Create linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_array(head):
    """Convert linked list to array"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def print_matrix(matrix):
    """Print matrix in readable format"""
    for row in matrix:
        print("  " + " ".join(f"{x:3}" for x in row))

# Test cases
if __name__ == "__main__":
    # Test sort_students_multi_criteria
    print("=== MULTI-CRITERIA STUDENT SORTING ===")
    
    students = [
        ("Alice", 85),
        ("Bob", 90),
        ("Charlie", 85),
        ("David", 92),
        ("Eve", 90),
        ("Frank", 85)
    ]
    
    sorted_students = sort_students_multi_criteria(students)
    print("Students sorted by grade (desc), then name (asc):")
    for name, grade in sorted_students:
        print(f"  {name}: {grade}")
    
    # Test sort_intervals_by_overlap
    print(f"\n=== INTERVAL SORTING ===")
    
    intervals_list = [
        [[1, 3], [6, 9], [2, 5], [15, 18]],
        [[1, 4], [4, 5], [0, 2]],
        [[7, 10], [2, 4], [1, 3], [5, 8]]
    ]
    
    for intervals in intervals_list:
        original = intervals.copy()
        sorted_intervals = sort_intervals_by_overlap(intervals)
        print(f"Intervals: {original}")
        print(f"  Sorted: {sorted_intervals}")
    
    # Test tournament_bracket_sorting
    print(f"\n=== TOURNAMENT BRACKET ===")
    
    players = [
        ("Alice", 1200),
        ("Bob", 1500),
        ("Charlie", 1100),
        ("David", 1800),
        ("Eve", 1300),
        ("Frank", 1600),
        ("Grace", 1400),
        ("Henry", 1700)
    ]
    
    bracket = tournament_bracket_sorting(players)
    print("Tournament bracket arrangement:")
    for i, player in enumerate(bracket):
        print(f"  Position {i+1}: {player[0]} (skill: {player[1]})")
    
    # Test sort_tasks_by_priority_and_deadline
    print(f"\n=== TASK SORTING ===")
    
    tasks = [
        ("Write report", 2, "2024-01-15"),
        ("Fix bug", 1, "2024-01-10"),
        ("Code review", 2, "2024-01-12"),
        ("Meeting prep", 3, "2024-01-14"),
        ("Deploy code", 1, "2024-01-11")
    ]
    
    sorted_tasks = sort_tasks_by_priority_and_deadline(tasks)
    print("Tasks sorted by priority (asc), then deadline (asc):")
    for task, priority, deadline in sorted_tasks:
        print(f"  {task} (P{priority}, {deadline})")
    
    # Test sort_colors_dutch_flag
    print(f"\n=== DUTCH FLAG PROBLEM ===")
    
    color_arrays = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [1, 1, 1, 0, 0, 2, 2],
        [2, 1, 0, 2, 1, 0, 1, 2, 0]
    ]
    
    for colors in color_arrays:
        original = colors.copy()
        sort_colors_dutch_flag(colors)
        print(f"Colors: {original} -> {colors}")
    
    # Test sort_linked_list_merge_k
    print(f"\n=== MERGE K SORTED LISTS ===")
    
    # Create test linked lists
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    
    lists = [list1, list2, list3]
    
    print("Input lists:")
    for i, head in enumerate(lists):
        arr = linked_list_to_array(head)
        print(f"  List {i+1}: {arr}")
    
    merged_head = sort_linked_list_merge_k(lists)
    merged_arr = linked_list_to_array(merged_head)
    print(f"Merged result: {merged_arr}")
    
    # Test sort_matrix_diagonally
    print(f"\n=== DIAGONAL MATRIX SORTING ===")
    
    matrices = [
        [
            [3, 3, 1, 1],
            [2, 2, 1, 2],
            [1, 1, 1, 2]
        ],
        [
            [11, 25, 66, 1, 69, 7],
            [23, 55, 17, 45, 15, 52],
            [75, 31, 36, 44, 58, 8],
            [22, 27, 33, 25, 68, 4],
            [84, 28, 14, 11, 5, 50]
        ]
    ]
    
    for i, matrix in enumerate(matrices):
        print(f"Matrix {i+1} before sorting:")
        print_matrix(matrix)
        
        sorted_matrix = sort_matrix_diagonally([row[:] for row in matrix])
        print(f"Matrix {i+1} after diagonal sorting:")
        print_matrix(sorted_matrix)
        print()
    
    # Test sort_array_by_frequency_then_value
    print(f"=== FREQUENCY-VALUE SORTING ===")
    
    frequency_arrays = [
        [4, 5, 6, 5, 4, 3],
        [1, 1, 1, 2, 2, 3],
        [1, 2, 3, 4, 5],
        [2, 3, 1, 3, 2, 4, 4, 5, 6, 7, 7, 8, 2, 3, 1, 1]
    ]
    
    for arr in frequency_arrays:
        original = arr.copy()
        sorted_arr = sort_array_by_frequency_then_value(arr)
        print(f"Original: {original}")
        print(f"By frequency then value: {sorted_arr}")
        print()
    
    # Test sort_strings_by_custom_alphabet
    print(f"=== CUSTOM ALPHABET SORTING ===")
    
    custom_cases = [
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz")
    ]
    
    for strings, alphabet in custom_cases:
        original = strings.copy()
        sort_strings_by_custom_alphabet(strings, alphabet)
        print(f"Strings: {original}")
        print(f"Custom alphabet: {alphabet}")
        print(f"Sorted: {strings}")
        print()
    
    # Test pancake_sorting
    print(f"=== PANCAKE SORTING ===")
    
    pancake_arrays = [
        [3, 2, 4, 1],
        [1, 2, 3],
        [4, 3, 2, 1, 5],
        [2, 1, 3]
    ]
    
    for arr in pancake_arrays:
        original = arr.copy()
        sorted_arr, flips = pancake_sorting(arr)
        print(f"Original: {original}")
        print(f"Sorted: {sorted_arr}")
        print(f"Flip sequence: {flips}")
        print()
    
    # Performance analysis
    print(f"=== PERFORMANCE ANALYSIS ===")
    
    import time
    import random
    
    # Test performance với practical applications
    print("Practical application performance:")
    
    # Large student dataset
    large_students = [(f"Student{i}", random.randint(60, 100)) for i in range(1000)]
    
    start = time.time()
    sort_students_multi_criteria(large_students.copy())
    end = time.time()
    print(f"  1000 students multi-criteria sort: {end-start:.4f}s")
    
    # Large color array
    large_colors = [random.randint(0, 2) for _ in range(10000)]
    
    start = time.time()
    sort_colors_dutch_flag(large_colors.copy())
    end = time.time()
    print(f"  10000 colors Dutch flag sort: {end-start:.4f}s")
    
    # Large frequency array
    large_freq_array = [random.randint(1, 100) for _ in range(1000)]
    
    start = time.time()
    sort_array_by_frequency_then_value(large_freq_array.copy())
    end = time.time()
    print(f"  1000 elements frequency sort: {end-start:.4f}s")
    
    print(f"\n=== PRACTICAL SORTING APPLICATIONS SUMMARY ===")
    print("Real-world Applications:")
    print("  - Multi-criteria sorting: Student grades, employee records")
    print("  - Interval sorting: Meeting scheduling, resource allocation")
    print("  - Tournament brackets: Sports competitions, game matchmaking")
    print("  - Task scheduling: Project management, OS scheduling")
    print("  - Color sorting: Image processing, data visualization")
    print("  - Linked list merging: Database operations, file merging")
    print("  - Matrix sorting: Image processing, data analysis")
    print("  - Frequency sorting: Data analysis, compression algorithms")
    print("  - Custom alphabet: Internationalization, domain-specific sorting")
    print("  - Pancake sorting: Robotics, mechanical sorting systems")
    
    print("\\nKey Techniques:")
    print("  - Custom comparators for complex criteria")
    print("  - Stable sorting for maintaining relative order")
    print("  - Multi-pass sorting for multiple criteria")
    print("  - Frequency analysis for statistical sorting")
    print("  - Constraint-based sorting (pancake flips)")
    
    print("\\nImplementation Considerations:")
    print("  - Choose appropriate basic algorithm based on data size")
    print("  - Consider stability requirements")
    print("  - Optimize for specific data patterns")
    print("  - Handle edge cases (empty arrays, single elements)")
    print("  - Balance simplicity vs. performance")