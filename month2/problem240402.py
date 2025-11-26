"""
Problem 240402: Chiến lược làm bài thi Olympic
Học cách quản lý thời gian và chiến lược làm bài hiệu quả

Time management:
- Đọc đề và phân tích (15-20 phút)
- Lập kế hoạch giải (10 phút)
- Cài đặt và test (120-130 phút)
- Review và tối ưu (15-20 phút)

Strategy:
- Làm bài dễ trước
- Partial scoring
- Code template
- Testing strategy
"""

def contest_time_management():
    """Quản lý thời gian trong thi 180 phút"""
    
    schedule = {
        "0-20 min": "Đọc tất cả đề, phân loại độ khó",
        "20-30 min": "Lập kế hoạch làm bài, chọn thứ tự",
        "30-90 min": "Làm bài dễ nhất (60 phút)",
        "90-150 min": "Làm bài trung bình (60 phút)", 
        "150-170 min": "Làm bài khó hoặc tối ưu (20 phút)",
        "170-180 min": "Review, check edge cases (10 phút)"
    }
    
    for time_slot, activity in schedule.items():
        print(f"{time_slot}: {activity}")

def problem_classification():
    """Phân loại bài toán theo độ khó"""
    
    easy_problems = [
        "Tìm kiếm, sắp xếp cơ bản",
        "Xử lý mảng, chuỗi đơn giản",
        "Toán học cơ bản (GCD, LCM, prime)",
        "Simulation problems",
        "Greedy đơn giản"
    ]
    
    medium_problems = [
        "Dynamic Programming cơ bản",
        "Graph traversal (DFS, BFS)",
        "Binary search variants",
        "Two pointers, sliding window",
        "Divide and conquer"
    ]
    
    hard_problems = [
        "Advanced DP (bitmask, tree DP)",
        "Graph algorithms (shortest path, MST)",
        "Advanced data structures",
        "Number theory nâng cao",
        "Geometry algorithms"
    ]
    
    print("EASY:", easy_problems)
    print("MEDIUM:", medium_problems) 
    print("HARD:", hard_problems)

def partial_scoring_strategy():
    """Chiến lược ghi điểm từng phần"""
    
    def implement_partial_solution():
        """Cài đặt solution từng phần"""
        
        # Bước 1: Brute force cho subtask nhỏ
        def solve_small(n):
            if n <= 100:
                # O(n²) solution for small input
                pass
            else:
                return None
        
        # Bước 2: Tối ưu cho subtask lớn
        def solve_large(n):
            # O(n log n) solution for large input
            pass
        
        # Bước 3: Combine solutions
        def solve_all(n):
            if n <= 100:
                return solve_small(n)
            else:
                return solve_large(n)
    
    def scoring_priorities():
        """Ưu tiên ghi điểm"""
        priorities = [
            "1. Làm đúng subtask dễ nhất (20-30%)",
            "2. Cải thiện độ phức tạp (40-60%)",
            "3. Xử lý edge cases (70-80%)",
            "4. Tối ưu hoàn toàn (100%)"
        ]
        
        for priority in priorities:
            print(priority)

def code_templates():
    """Template code thường dùng"""
    
    def input_template():
        """Template đọc input"""
        template = '''
# Single integer
n = int(input())

# Multiple integers on one line  
a, b, c = map(int, input().split())

# Array of integers
arr = list(map(int, input().split()))

# Multiple lines of input
data = []
for _ in range(n):
    line = input().strip()
    data.append(line)
'''
        print("INPUT TEMPLATE:", template)
    
    def algorithm_templates():
        """Template các thuật toán cơ bản"""
        
        # Binary search template
        def binary_search_template(arr, target):
            left, right = 0, len(arr) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        
        # DFS template
        def dfs_template(graph, start, visited):
            visited.add(start)
            
            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs_template(graph, neighbor, visited)
        
        # DP template
        def dp_template(n):
            dp = [0] * (n + 1)
            dp[0] = base_case
            
            for i in range(1, n + 1):
                dp[i] = transition_function(dp, i)
            
            return dp[n]

def testing_strategy():
    """Chiến lược test code"""
    
    def create_test_cases():
        """Tạo test cases"""
        test_cases = [
            "1. Sample input/output từ đề",
            "2. Edge cases: n=1, n=max, empty input",
            "3. Corner cases: all same, all different",
            "4. Random cases: medium size",
            "5. Stress test: maximum constraints"
        ]
        
        for case in test_cases:
            print(case)
    
    def debugging_checklist():
        """Checklist debug"""
        checklist = [
            "✓ Đọc input đúng format?",
            "✓ Xử lý edge cases?", 
            "✓ Array bounds checking?",
            "✓ Integer overflow?",
            "✓ Output format đúng?",
            "✓ Time limit OK?",
            "✓ Memory limit OK?"
        ]
        
        for item in checklist:
            print(item)

def common_mistakes():
    """Lỗi thường gặp trong thi"""
    
    mistakes = [
        "1. Không đọc kỹ đề bài",
        "2. Nhầm lẫn 0-indexed vs 1-indexed", 
        "3. Integer overflow với số lớn",
        "4. Không xử lý edge cases",
        "5. Sai format output",
        "6. Quên flush output buffer",
        "7. Infinite loop hoặc TLE",
        "8. Không backup code"
    ]
    
    for mistake in mistakes:
        print(mistake)

def contest_simulation():
    """Mô phỏng kỳ thi thực tế"""
    
    print("=== MÔ PHỎNG KỲ THI OLYMPIC ===")
    print("Thời gian: 180 phút")
    print("Số bài: 3 bài")
    
    # Bài 1: Dễ (60 phút)
    def problem_1_easy():
        """Bài 1: Tìm số lớn thứ k"""
        print("\nBài 1: Tìm số lớn thứ k trong mảng")
        print("Độ khó: Dễ")
        print("Thời gian dự kiến: 30-45 phút")
        print("Thuật toán: Sorting hoặc QuickSelect")
        
        # TODO: Implement solution
        def kth_largest(arr, k):
            pass
    
    # Bài 2: Trung bình (60 phút)  
    def problem_2_medium():
        """Bài 2: Đường đi ngắn nhất"""
        print("\nBài 2: Đường đi ngắn nhất trong grid")
        print("Độ khó: Trung bình")
        print("Thời gian dự kiến: 45-60 phút")
        print("Thuật toán: BFS hoặc Dijkstra")
        
        # TODO: Implement solution
        def shortest_path_grid(grid):
            pass
    
    # Bài 3: Khó (60 phút)
    def problem_3_hard():
        """Bài 3: Dynamic Programming"""
        print("\nBài 3: Longest Increasing Subsequence")
        print("Độ khó: Khó")
        print("Thời gian dự kiến: 60+ phút")
        print("Thuật toán: DP O(n²) hoặc Binary Search O(n log n)")
        
        # TODO: Implement solution
        def longest_increasing_subsequence(arr):
            pass

def final_tips():
    """Lời khuyên cuối cùng"""
    
    tips = [
        "1. Đọc đề 2-3 lần trước khi code",
        "2. Bắt đầu với solution đơn giản nhất",
        "3. Test với sample input trước",
        "4. Không bỏ cuộc với bài khó",
        "5. Quản lý thời gian chặt chẽ",
        "6. Giữ bình tĩnh và tự tin",
        "7. Backup code thường xuyên",
        "8. Review code trước khi submit"
    ]
    
    print("FINAL TIPS:")
    for tip in tips:
        print(tip)

def practice_schedule():
    """Lịch luyện tập chuẩn bị thi"""
    
    schedule = {
        "4 tuần trước thi": "Ôn lý thuyết, làm bài cũ",
        "3 tuần trước thi": "Mock test 2-3 lần/tuần",
        "2 tuần trước thi": "Tập trung vào điểm yếu",
        "1 tuần trước thi": "Mock test, ôn nhẹ",
        "1 ngày trước thi": "Nghỉ ngơi, chuẩn bị tinh thần"
    }
    
    print("PRACTICE SCHEDULE:")
    for time, activity in schedule.items():
        print(f"{time}: {activity}")

# Main contest strategy function
def olympic_contest_strategy():
    """Tổng hợp chiến lược thi Olympic"""
    
    print("=== CHIẾN LƯỢC THI OLYMPIC TIN HỌC ===\n")
    
    print("1. QUẢN LÝ THỜI GIAN:")
    contest_time_management()
    
    print("\n2. PHÂN LOẠI BÀI TOÁN:")
    problem_classification()
    
    print("\n3. CHIẾN LƯỢC GHI ĐIỂM:")
    partial_scoring_strategy()
    
    print("\n4. CHIẾN LƯỢC TEST:")
    testing_strategy()
    
    print("\n5. LỖI THƯỜNG GẶP:")
    common_mistakes()
    
    print("\n6. LỊCH LUYỆN TẬP:")
    practice_schedule()
    
    print("\n7. LỜI KHUYÊN CUỐI:")
    final_tips()

if __name__ == "__main__":
    olympic_contest_strategy()
    contest_simulation()