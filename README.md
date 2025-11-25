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

- **Tuần 5:** Tìm kiếm tuyến tính, nhị phân, bisect module
- **Tuần 6:** Sắp xếp cơ bản (bubble, selection, insertion)
- **Tuần 7:** Sắp xếp nâng cao (merge, quick), độ phức tạp
- **Tuần 8:** Đệ quy, chia để trị + **Giải đề cơ bản**

### Tháng 3: Cấu trúc dữ liệu (12 buổi)

- **Tuần 9:** collections module (deque, Counter, defaultdict)
- **Tuần 10:** heapq module, priority queue
- **Tuần 11:** Stack, Queue implementation
- **Tuần 12:** Cây nhị phân, BST (tự implement)

### Tháng 4: Đồ thị và cây (12 buổi)

- **Tuần 13:** Biểu diễn đồ thị, DFS với dict/list
- **Tuần 14:** BFS, tìm đường đi ngắn nhất
- **Tuần 15:** Dijkstra, Union-Find
- **Tuần 16:** MST, Trie + **Giải đề trung bình**

### Tháng 5: Thuật toán nâng cao (12 buổi)

- **Tuần 17:** Quy hoạch động cơ bản, memoization
- **Tuần 18:** DP nâng cao, itertools module
- **Tuần 19:** Thuật toán tham lam
- **Tuần 20:** Backtracking, brute force + **Giải đề khó**

### Tháng 6: Luyện thi Olympic (12 buổi)

- **Tuần 21:** **Giải đề Olympic 2018-2020**
- **Tuần 22:** **Giải đề Olympic 2021-2024**
- **Tuần 23:** **Mock test, kỹ thuật thi với VSCode**
- **Tuần 24:** **Ôn tập tổng hợp, luyện thi cuối**

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
├── month2/            # Thuật toán cơ bản
├── month3/            # Cấu trúc dữ liệu
├── month4/            # Đồ thị và cây
├── month5/            # Thuật toán nâng cao
├── month6/            # Luyện thi Olympic
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
- 🔄 **Tháng 2:** Chuẩn bị bắt đầu - Thuật toán cơ bản
- ⏳ **Tháng 3-6:** Chưa bắt đầu

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
