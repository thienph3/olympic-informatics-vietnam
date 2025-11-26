# Lộ trình 6 tháng ôn luyện Olympic Tin học THPT Quốc gia

## Giới thiệu

Repository này cung cấp lộ trình ôn luyện dồn dập 6 tháng (3 buổi/tuần, 3h15'/buổi) dành cho học sinh THPT muốn tham gia Olympic Tin học và **đạt giải cao**. Lộ trình được thiết kế để từ zero đến có thể giải được các đề thi Olympic thực tế.

**Ngôn ngữ chính:** Python 3.10  
**IDE:** Visual Studio Code  
**Thư viện:** Chỉ standard library (không pip install)  
**Thời lượng:** 72 buổi × 3h15' = 234 giờ học

## Đối tượng

- Học sinh THPT chưa biết gì về lập trình
- Học sinh muốn đạt giải Olympic Tin học cấp trường, tỉnh, quốc gia
- Người có quyết tâm cao, sẵn sàng ôn luyện dồn dập

## Cấu trúc lộ trình

### Tháng 1: Nền tảng Python (12 buổi) ✅

- **Tuần 1:**
  - [Day 1](month1/day01.md): Python 3.10 cơ bản, biến, kiểu dữ liệu, I/O, VSCode setup
  - [Day 2](month1/day02.md): Toán tử và biểu thức, math module, bitwise operations
  - [Day 3](month1/day03.md): Cấu trúc điều khiển if-else, nested if, conditional expressions
- **Tuần 2:**
  - [Day 4](month1/day04.md): Vòng lặp for cơ bản, range(), enumerate(), nested loops
  - [Day 5](month1/day05.md): Vòng lặp while, break/continue, else trong vòng lặp
  - [Day 6](month1/day06.md): Pattern printing, ứng dụng vòng lặp trong Olympic
- **Tuần 3:**
  - [Day 7](month1/day07.md): List cơ bản, indexing, slicing, methods
  - [Day 8](month1/day08.md): List nâng cao, list comprehension, nested lists
  - [Day 9](month1/day09.md): Tuple, string methods, string formatting
- **Tuần 4:**
  - [Day 10](month1/day10.md): Function cơ bản, parameters, return values
  - [Day 11](month1/day11.md): Function nâng cao, lambda, scope, recursion
  - [Day 12](month1/day12.md): Module, file I/O, exception handling, debugging

### Tháng 2: Thuật toán cơ bản (12 buổi)

- **Tuần 5:**
  - [Day 13](month2/day13.md): Tìm kiếm tuyến tính, binary search cơ bản
  - [Day 14](month2/day14.md): Binary search nâng cao, bisect module, search variants
  - [Day 15](month2/day15.md): Ternary search, exponential search, interpolation search
- **Tuần 6:**
  - [Day 16](month2/day16.md): Sắp xếp cơ bản (bubble, selection, insertion) + 8 file problem
  - [Day 17](month2/day17.md): Counting sort, radix sort, bucket sort + 8 file problem
  - [Day 18](month2/day18.md): Sắp xếp ứng dụng, stable sorting, custom comparators + 8 file problem
- **Tuần 7:**
  - [Day 19](month2/day19.md): Merge sort, quick sort, heap sort + 8 file problem
  - [Day 20](month2/day20.md): Độ phức tạp thuật toán, Big O notation + 8 file problem
  - [Day 21](month2/day21.md): Phân tích hiệu suất, space complexity + 8 file problem
- **Tuần 8:**
  - [Day 22](month2/day22.md): Đệ quy cơ bản, base cases, recursive thinking + 8 file problem
  - [Day 23](month2/day23.md): Chia để trị, divide and conquer algorithms + 8 file problem
  - [Day 24](month2/day24.md): Giải đề Olympic cơ bản + Mock test tháng 2 + 8 file problem

### Tháng 3: Cấu trúc dữ liệu (12 buổi)

- **Tuần 9:**
  - Day 25: collections.deque, double-ended queue operations
  - Day 26: collections.Counter, frequency analysis và statistics
  - Day 27: collections.defaultdict, OrderedDict, ChainMap
- **Tuần 10:**
  - Day 28: heapq module, binary heap operations
  - Day 29: Priority queue, heap applications trong Olympic
  - Day 30: Heap sort implementation, k-way merge
- **Tuần 11:**
  - Day 31: Stack implementation và applications
  - Day 32: Queue implementation, circular queue, deque
  - Day 33: Stack/Queue trong thuật toán (DFS, BFS preview)
- **Tuần 12:**
  - Day 34: Cây nhị phân cơ bản, tree traversal
  - Day 35: Binary Search Tree (BST) implementation
  - Day 36: **Giải đề Olympic trung bình** + Mock test tháng 3

### Tháng 4: Đồ thị và cây (12 buổi)

- **Tuần 13:**
  - Day 37: Biểu diễn đồ thị (adjacency list, matrix), graph input/output
  - Day 38: DFS (Depth-First Search) cơ bản với dict và list
  - Day 39: DFS nâng cao, connected components, cycle detection
- **Tuần 14:**
  - Day 40: BFS (Breadth-First Search) cơ bản với collections.deque
  - Day 41: BFS nâng cao, shortest path trong unweighted graph
  - Day 42: Bipartite graph, graph coloring với BFS/DFS
- **Tuần 15:**
  - Day 43: Dijkstra algorithm cho shortest path trong weighted graph
  - Day 44: Union-Find (Disjoint Set Union) data structure
  - Day 45: Kruskal's algorithm cho Minimum Spanning Tree
- **Tuần 16:**
  - Day 46: Prim's algorithm cho MST, so sánh với Kruskal
  - Day 47: Trie (Prefix Tree) implementation và applications
  - Day 48: **Giải đề Olympic trung bình về đồ thị** + Mock test tháng 4

### Tháng 5: Thuật toán nâng cao (12 buổi)

- **Tuần 17:**
  - Day 49: Quy hoạch động cơ bản, memoization với dict và functools.lru_cache
  - Day 50: DP 1D problems (Fibonacci, climbing stairs, coin change)
  - Day 51: DP 2D problems (grid paths, longest common subsequence)
- **Tuần 18:**
  - Day 52: DP nâng cao (knapsack, edit distance, palindrome)
  - Day 53: itertools module (permutations, combinations, product)
  - Day 54: Bitmask DP và state compression techniques
- **Tuần 19:**
  - Day 55: Thuật toán tham lam cơ bản (activity selection, fractional knapsack)
  - Day 56: Greedy nâng cao (Huffman coding, interval scheduling)
  - Day 57: Proof techniques cho greedy algorithms
- **Tuần 20:**
  - Day 58: Backtracking cơ bản (N-Queens, Sudoku solver)
  - Day 59: Backtracking nâng cao với pruning và optimization
  - Day 60: **Giải đề Olympic khó** + Mock test tháng 5

### Tháng 6: Luyện thi Olympic (12 buổi)

- **Tuần 21:** **Giải đề Olympic 2018-2020**
  - Day 61: Giải đề Olympic Tin học 2018 (cấp trường, tỉnh)
  - Day 62: Giải đề Olympic Tin học 2019 (cấp trường, tỉnh)
  - Day 63: Giải đề Olympic Tin học 2020 (cấp trường, tỉnh)
- **Tuần 22:** **Giải đề Olympic 2021-2024**
  - Day 64: Giải đề Olympic Tin học 2021 (cấp quốc gia)
  - Day 65: Giải đề Olympic Tin học 2022 (cấp quốc gia)
  - Day 66: Giải đề Olympic Tin học 2023-2024 (cấp quốc gia)
- **Tuần 23:** **Mock test, kỹ thuật thi với VSCode**
  - Day 67: Mock test 1 - Simulation đề thi thực tế (3 tiếng)
  - Day 68: Mock test 2 - Kỹ thuật thi, quản lý thời gian với VSCode
  - Day 69: Mock test 3 - Debug và optimize code trong thời gian giới hạn
- **Tuần 24:** **Ôn tập tổng hợp, luyện thi cuối**
  - Day 70: Ôn tập tổng hợp - Review toàn bộ kiến thức 5 tháng
  - Day 71: Final Mock test - Đề thi thử cuối cùng
  - Day 72: Chiến lược thi, tâm lý thi cử, chuẩn bị cuối

## Cách sử dụng

1. **Lịch học:** 3 buổi/tuần (Thứ 2, 4, 6 hoặc Thứ 3, 5, 7)
2. **Mỗi buổi:** 3h15' (lý thuyết + thực hành + nghỉ giải lao 5')
3. **Bài tập:** Hoàn thành 100% bài tập mỗi tuần
4. **Giải đề:** Từ tuần 8 bắt đầu giải đề thực tế
5. **Mock test:** Tuần cuối mỗi tháng

## Cấu trúc thư mục

```
olympic/
├── month1/            # Nền tảng Python (✅ Hoàn thành Day 1-12)
│   ├── day01.md       # Python cơ bản + 7 file problem
│   ├── day02.md       # Toán tử và biểu thức + 8 file problem
│   ├── day03.md       # Cấu trúc điều khiển + 8 file problem
│   ├── day04.md       # Vòng lặp for + 8 file problem
│   ├── day05.md       # Vòng lặp while + 7 file problem
│   ├── day06.md       # Pattern printing + 8 file problem
│   ├── day07.md       # List cơ bản + 8 file problem
│   ├── day08.md       # List nâng cao + 8 file problem
│   ├── day09.md       # Tuple và String methods + 8 file problem
│   ├── day10.md       # Function cơ bản + 8 file problem
│   ├── day11.md       # Function nâng cao + 8 file problem
│   ├── day12.md       # Module, file I/O, exception handling + 8 file problem
│   └── problem*.py    # 94 file bài tập thực hành
├── month2/            # Thuật toán cơ bản (✅ Hoàn thành Day 13-24)
│   ├── day13.md       # Tìm kiếm tuyến tính, binary search + 8 file problem
│   ├── day14.md       # Binary search nâng cao, bisect module + 8 file problem
│   ├── day15.md       # Ternary search, exponential search + 8 file problem
│   ├── day16.md       # Sắp xếp cơ bản (bubble, selection, insertion) + 8 file problem
│   ├── day17.md       # Counting sort, radix sort, bucket sort + 8 file problem
│   ├── day18.md       # Sắp xếp ứng dụng, stable sorting + 8 file problem
│   ├── day19.md       # Merge sort, quick sort, heap sort + 8 file problem
│   ├── day20.md       # Độ phức tạp thuật toán, Big O notation + 8 file problem
│   ├── day21.md       # Phân tích hiệu suất, space complexity + 8 file problem
│   ├── day22.md       # Đệ quy cơ bản, recursive thinking + 8 file problem
│   ├── day23.md       # Chia để trị, divide and conquer + 8 file problem
│   ├── day24.md       # Giải đề Olympic cơ bản + Mock test + 8 file problem
│   └── problem*.py    # 96 file bài tập thuật toán
├── month3/            # Cấu trúc dữ liệu
│   ├── day25.md       # collections.deque, double-ended queue + 8 file problem
│   ├── day26.md       # collections.Counter, frequency analysis + 8 file problem
│   ├── day27.md       # defaultdict, OrderedDict, ChainMap + 8 file problem
│   ├── day28.md       # heapq module, binary heap operations + 8 file problem
│   ├── day29.md       # Priority queue, heap applications + 8 file problem
│   ├── day30.md       # Heap sort implementation, k-way merge + 8 file problem
│   ├── day31.md       # Stack implementation và applications + 8 file problem
│   ├── day32.md       # Queue implementation, circular queue + 8 file problem
│   ├── day33.md       # Stack/Queue trong thuật toán + 8 file problem
│   ├── day34.md       # Cây nhị phân, tree traversal + 8 file problem
│   ├── day35.md       # Binary Search Tree (BST) + 8 file problem
│   ├── day36.md       # Giải đề Olympic trung bình + Mock test + 8 file problem
│   └── problem*.py    # 96 file bài tập cấu trúc dữ liệu
├── month4/            # Đồ thị và cây
│   ├── day37.md       # Biểu diễn đồ thị, adjacency list/matrix + 8 file problem
│   ├── day38.md       # DFS cơ bản với dict và list + 8 file problem
│   ├── day39.md       # DFS nâng cao, connected components + 8 file problem
│   ├── day40.md       # BFS cơ bản với collections.deque + 8 file problem
│   ├── day41.md       # BFS nâng cao, shortest path + 8 file problem
│   ├── day42.md       # Bipartite graph, graph coloring + 8 file problem
│   ├── day43.md       # Dijkstra algorithm cho weighted graph + 8 file problem
│   ├── day44.md       # Union-Find (Disjoint Set Union) + 8 file problem
│   ├── day45.md       # Kruskal's algorithm cho MST + 8 file problem
│   ├── day46.md       # Prim's algorithm cho MST + 8 file problem
│   ├── day47.md       # Trie (Prefix Tree) implementation + 8 file problem
│   ├── day48.md       # Giải đề Olympic đồ thị + Mock test + 8 file problem
│   └── problem*.py    # 96 file bài tập đồ thị và cây
├── month5/            # Thuật toán nâng cao
│   ├── day49.md       # Quy hoạch động cơ bản, memoization + 8 file problem
│   ├── day50.md       # DP 1D problems (Fibonacci, coin change) + 8 file problem
│   ├── day51.md       # DP 2D problems (grid paths, LCS) + 8 file problem
│   ├── day52.md       # DP nâng cao (knapsack, edit distance) + 8 file problem
│   ├── day53.md       # itertools module (permutations, combinations) + 8 file problem
│   ├── day54.md       # Bitmask DP và state compression + 8 file problem
│   ├── day55.md       # Thuật toán tham lam cơ bản + 8 file problem
│   ├── day56.md       # Greedy nâng cao (Huffman, interval) + 8 file problem
│   ├── day57.md       # Proof techniques cho greedy + 8 file problem
│   ├── day58.md       # Backtracking cơ bản (N-Queens, Sudoku) + 8 file problem
│   ├── day59.md       # Backtracking nâng cao với pruning + 8 file problem
│   ├── day60.md       # Giải đề Olympic khó + Mock test + 8 file problem
│   └── problem*.py    # 96 file bài tập thuật toán nâng cao
├── month6/            # Luyện thi Olympic
│   ├── day61.md       # Giải đề Olympic 2018 + 4 đề thi thực tế
│   ├── day62.md       # Giải đề Olympic 2019 + 4 đề thi thực tế
│   ├── day63.md       # Giải đề Olympic 2020 + 4 đề thi thực tế
│   ├── day64.md       # Giải đề Olympic 2021 + 4 đề thi thực tế
│   ├── day65.md       # Giải đề Olympic 2022 + 4 đề thi thực tế
│   ├── day66.md       # Giải đề Olympic 2023-2024 + 4 đề thi thực tế
│   ├── day67.md       # Mock test 1 - Simulation đề thi + 4 đề mock
│   ├── day68.md       # Mock test 2 - Kỹ thuật thi VSCode + 4 đề mock
│   ├── day69.md       # Mock test 3 - Debug và optimize + 4 đề mock
│   ├── day70.md       # Ôn tập tổng hợp - Review kiến thức + 4 đề ôn tập
│   ├── day71.md       # Final Mock test + 4 đề thi thử cuối
│   ├── day72.md       # Chiến lược thi, tâm lý + 4 đề luyện tập
│   └── contest*.py    # 48 đề thi thực tế và mock test
├── problems/          # Bài tập theo chủ đề
├── contests/          # Đề thi Olympic các năm
├── solutions/         # Lời giải chi tiết
└── mock-tests/        # Đề thi thử
```

## Yêu cầu hệ thống

- Python 3.10
- Visual Studio Code
- **Chỉ sử dụng thư viện chuẩn Python** (math, collections, itertools, heapq, bisect, etc.)
- **Không được cài đặt thêm package qua pip**

## Tiến độ hoàn thành

- ✅ **Tháng 1:** Day 1-12 hoàn thành (94 file bài tập) - Nền tảng Python vững chắc
- ✅ **Tháng 2:** Day 13-24 hoàn thành (96 file bài tập) - Thuật toán cơ bản và giải đề Olympic
- 🔄 **Tháng 3:** Day 25-36 chuẩn bị (96 file bài tập) - Cấu trúc dữ liệu
- 🔄 **Tháng 4:** Day 37-48 chuẩn bị (96 file bài tập) - Đồ thị và cây
- 🔄 **Tháng 5:** Day 49-60 chuẩn bị (96 file bài tập) - Thuật toán nâng cao
- 🔄 **Tháng 6:** Day 61-72 chuẩn bị (48 đề thi thực tế) - Luyện thi Olympic

## Cài đặt

```bash
git clone https://github.com/thienph3/olympic-informatics-vietnam.git
cd olympic-informatics-vietnam
# Bắt đầu từ month1/day01.md
```

## Đóng góp

Mọi đóng góp để cải thiện lộ trình đều được hoan nghênh. Vui lòng tạo issue hoặc pull request.

## Liên hệ

Nếu có thắc mắc, vui lòng tạo issue trong repository này.

---

**Chúc các bạn học tập hiệu quả và đạt kết quả cao trong Olympic Tin học!** 🏆
