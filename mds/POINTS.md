# BeginnerFreeContest 49 - POINTS

**Thể loại:** Implementation  
**Độ khó:** 250

## Đề bài

Nhận dịp các bạn lớp 11A1 đi học trở lại sau Tết, vì có một số bạn chưa làm bài tập Tết nên thầy Phú quyết định đưa ra hình phạt như sau: nếu một bạn bất kì không làm bài tập Tết thì số điểm cộng của các bạn khác trong lớp sẽ được cộng thêm 1 đơn vị.

Yêu cầu: Cho số lượng học sinh trong lớp, danh sách điểm cộng trước Tết của các bạn và số bạn chưa làm bài tập Tết. Đưa ra danh sách điểm cộng mới của các bạn lớp 11A1.

## Dữ liệu

- Dòng thứ nhất ghi 2 số nguyên dương n, k (1 ≤ n ≤ 2 × 10⁵, 1 ≤ k ≤ 2 × 10⁵) - số lượng học sinh trong lớp và số học sinh không làm bài tập Tết.
- Dòng thứ hai chứa dãy a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 10⁶) - điểm cộng của các bạn lớp 11A1 trước Tết.
- Tiếp theo là k dòng, dòng thứ i chứa số nguyên Kᵢ (1 ≤ Kᵢ ≤ n) - thứ tự của bạn học sinh không làm bài tập Tết.

Dữ liệu đảm bảo danh sách các bạn không làm bài tập tết là đôi một khác nhau.

## Kết quả

In ra danh sách điểm cộng mới trên một dòng.

## Ví dụ

**Input:**
```
6 4
3 5 3 1 7 8
3
4
5
6
```

**Output:**
```
7 9 7 1 7 8
```