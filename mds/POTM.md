# BeginnerFreeContest 53 - POTM

**Thể loại:** Array  
**Độ khó:** 300

## Đề bài

Một ngày nọ, Doraemon muốn Nobita chứng minh khả năng toán học của mình với Shizuka. Mèo máy cố tình tạo ra một câu đố khó và tin chắc rằng Nobita sẽ giải được, từ đó lấy lòng Shizuka.

Doraemon ghi ra tờ giấy trắng một dãy N số nguyên dương tăng dần. Tiếp theo đó, Shizuka đưa cho Nobita Q câu hỏi. Câu hỏi thứ i chứa 3 giá trị typeᵢ, xᵢ, kᵢ.

- Nếu typeᵢ = 0, Nobita cần đưa ra tổng của k số bé nhất trong x số đầu tiên.
- Nếu typeᵢ = 1, Nobita cần đưa ra tổng của k số lớn nhất trong x số đầu tiên.

Bạn hãy giúp Nobita trả lời các câu hỏi để gây ấn tượng với Shizuka nhé.

## Dữ liệu

- Dòng thứ nhất chứa hai số nguyên dương n, q (1 ≤ n, q ≤ 10⁵)
- Dòng thứ hai gồm n số nguyên aᵢ (1 ≤ aᵢ ≤ 10⁹) - Dãy số Doraemon cung cấp cho Nobita.
- q dòng sau, mỗi dòng gồm 3 số nguyên typeᵢ (0 ≤ typeᵢ ≤ 1), xᵢ, kᵢ (1 ≤ kᵢ ≤ xᵢ ≤ n)

## Kết quả

In ra kết quả trên mỗi dòng là câu hỏi mà Shizuka đố Nobita.

## Ví dụ

**Input:**
```
5 3
1 3 4 6 9
0 3 1
1 4 2
1 5 3
```

**Output:**
```
1
10
19
```

## Chấm điểm

- Subtask 1 (50% số test): n, m ≤ 10³.
- Subtask 2 (50% số test): Giới hạn như đề bài.