"""
Day 14 - Problem 7: Matrix search algorithms
Thời gian: 30 phút
"""

def search_sorted_matrix_staircase(matrix, target):
    """
    Tìm kiếm trong ma trận sorted theo hàng và cột (staircase search)
    Input: matrix - 2D matrix sorted row-wise và column-wise, target - giá trị cần tìm
    Output: (row, col) nếu tìm thấy, (-1, -1) nếu không
    Time complexity: O(m + n)
    """
    # TODO: Implement staircase search từ top-right hoặc bottom-left
    pass

def search_row_sorted_matrix(matrix, target):
    """
    Tìm kiếm trong ma trận mỗi hàng được sorted
    Input: matrix - 2D matrix với mỗi row sorted, target - giá trị cần tìm
    Output: (row, col) nếu tìm thấy, (-1, -1) nếu không
    Time complexity: O(m log n)
    """
    # TODO: Implement binary search trên từng row
    pass

def search_fully_sorted_matrix(matrix, target):
    """
    Tìm kiếm trong ma trận hoàn toàn sorted (treat as 1D array)
    Input: matrix - 2D matrix sorted như 1D array, target - giá trị cần tìm
    Output: (row, col) nếu tìm thấy, (-1, -1) nếu không
    Time complexity: O(log(mn))
    """
    # TODO: Implement binary search treating matrix as 1D
    pass

def find_kth_smallest_in_sorted_matrix(matrix, k):
    """
    Tìm phần tử thứ k nhỏ nhất trong sorted matrix
    Input: matrix - n×n matrix sorted row và column, k - thứ tự (1-indexed)
    Output: giá trị thứ k nhỏ nhất
    Time complexity: O(n log(max-min))
    """
    # TODO: Implement using binary search on value range
    pass

def count_negative_numbers_sorted_matrix(matrix):
    """
    Đếm số âm trong ma trận sorted (decreasing từ trái sang phải, trên xuống dưới)
    Input: matrix - sorted matrix (decreasing)
    Output: số lượng số âm
    Time complexity: O(m + n)
    """
    # TODO: Implement efficient counting
    pass

def search_peak_2d(matrix):
    """
    Tìm peak element trong ma trận 2D
    Input: matrix - 2D matrix
    Output: (row, col) của một peak element
    Time complexity: O(n log m)
    """
    # TODO: Implement 2D peak finding
    pass

def median_in_row_sorted_matrix(matrix):
    """
    Tìm median trong ma trận mỗi hàng được sorted
    Input: matrix - m×n matrix với mỗi row sorted
    Output: median value
    Time complexity: O(32 * m * log n) = O(m log n)
    """
    # TODO: Implement using binary search on answer
    pass

def search_in_young_tableau(matrix, target):
    """
    Tìm kiếm trong Young Tableau (sorted rows và columns)
    Input: matrix - Young Tableau, target - giá trị cần tìm
    Output: (row, col) nếu tìm thấy, (-1, -1) nếu không
    """
    # TODO: Implement Young Tableau search
    pass

# Test cases
if __name__ == "__main__":
    # Test search_sorted_matrix_staircase
    print("=== STAIRCASE SEARCH ===")
    
    matrix1 = [
        [1,  4,  7,  11, 15],
        [2,  5,  8,  12, 19],
        [3,  6,  9,  16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    
    targets = [5, 14, 20, 25]
    for target in targets:
        result = search_sorted_matrix_staircase(matrix1, target)
        print(f"Tìm {target}: {result}")
    
    # Test search_row_sorted_matrix
    print(f"\n=== ROW SORTED MATRIX ===")
    
    matrix2 = [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [9, 10, 11, 12]
    ]
    
    targets = [6, 9, 13]
    for target in targets:
        result = search_row_sorted_matrix(matrix2, target)
        print(f"Tìm {target}: {result}")
    
    # Test search_fully_sorted_matrix
    print(f"\n=== FULLY SORTED MATRIX ===")
    
    matrix3 = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12]
    ]
    
    targets = [7, 10, 13]
    for target in targets:
        result = search_fully_sorted_matrix(matrix3, target)
        print(f"Tìm {target}: {result}")
    
    # Test find_kth_smallest_in_sorted_matrix
    print(f"\n=== KTH SMALLEST IN SORTED MATRIX ===")
    
    matrix4 = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    
    for k in range(1, 10):
        kth_smallest = find_kth_smallest_in_sorted_matrix(matrix4, k)
        print(f"{k}th smallest: {kth_smallest}")
    
    # Test count_negative_numbers_sorted_matrix
    print(f"\n=== COUNT NEGATIVE NUMBERS ===")
    
    matrices_with_negatives = [
        [
            [4,  3,  2,  -1],
            [3,  2,  1,  -1],
            [1,  1,  -1, -2],
            [-1, -1, -2, -3]
        ],
        [
            [3, 2],
            [1, 0]
        ],
        [
            [1, -1],
            [-1, -1]
        ]
    ]
    
    for i, matrix in enumerate(matrices_with_negatives):
        count = count_negative_numbers_sorted_matrix(matrix)
        print(f"Matrix {i+1}: {count} negative numbers")
    
    # Test search_peak_2d
    print(f"\n=== 2D PEAK FINDING ===")
    
    peak_matrices = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [10, 20, 15],
            [21, 30, 14],
            [7,  16, 32]
        ]
    ]
    
    for i, matrix in enumerate(peak_matrices):
        peak = search_peak_2d(matrix)
        if peak != (-1, -1):
            row, col = peak
            value = matrix[row][col]
            print(f"Matrix {i+1}: Peak tại ({row}, {col}) = {value}")
        else:
            print(f"Matrix {i+1}: No peak found")
    
    # Test median_in_row_sorted_matrix
    print(f"\n=== MEDIAN IN ROW SORTED MATRIX ===")
    
    row_sorted_matrices = [
        [
            [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
    ]
    
    for i, matrix in enumerate(row_sorted_matrices):
        median = median_in_row_sorted_matrix(matrix)
        print(f"Matrix {i+1}: Median = {median}")
    
    # Test search_in_young_tableau
    print(f"\n=== YOUNG TABLEAU SEARCH ===")
    
    young_tableau = [
        [1,  3,  5,  7],
        [2,  4,  6,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    targets = [6, 10, 17]
    for target in targets:
        result = search_in_young_tableau(young_tableau, target)
        print(f"Tìm {target} trong Young Tableau: {result}")
    
    # Performance comparison
    print(f"\n=== PERFORMANCE COMPARISON ===")
    
    # Create large test matrix
    import time
    
    large_matrix = []
    for i in range(100):
        row = []
        for j in range(100):
            row.append(i * 100 + j)
        large_matrix.append(row)
    
    target = 5050
    
    # Test different algorithms
    algorithms = [
        ("Staircase", lambda: search_sorted_matrix_staircase(large_matrix, target)),
        ("Row Binary", lambda: search_row_sorted_matrix(large_matrix, target)),
        ("Fully Sorted", lambda: search_fully_sorted_matrix(large_matrix, target))
    ]
    
    for name, func in algorithms:
        start = time.time()
        result = func()
        end = time.time()
        print(f"{name}: {end-start:.6f}s, result: {result}")
    
    print(f"\n=== COMPLEXITY SUMMARY ===")
    print("Matrix Search Algorithms (m×n matrix):")
    print("  - Staircase Search: O(m + n)")
    print("  - Row Binary Search: O(m log n)")
    print("  - Fully Sorted Binary: O(log(mn))")
    print("  - Kth Smallest: O(n log(max-min))")
    print("  - 2D Peak Finding: O(n log m)")
    print("  - Median Row Sorted: O(m log n)")
    
    print("\\nWhen to use:")
    print("  - Staircase: Matrix sorted both ways")
    print("  - Row Binary: Each row sorted independently")
    print("  - Fully Sorted: Matrix sorted as 1D array")
    print("  - Kth Smallest: Need rank-based queries")
    print("  - Peak Finding: Local maximum problems")