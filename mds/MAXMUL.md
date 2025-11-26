# Beginner Free Contest 55 - MAXMUL

**Thể loại:** Array  
**Độ khó:** 350

## Đề bài

Trong vườn trái cây FreeContest có một hàng gồm N cây cam. Mỗi cây cam có độ "dẻo dai" aᵢ nhất định. Hôm nay, bạn được giao một nhiệm vụ gồm nhiều câu hỏi. Mỗi câu hỏi bao gồm các số uᵢ, kᵢ. Bạn cần tính toán xem tích độ dẻo dai của kᵢ cây liên tiếp, bắt đầu từ cây thứ uᵢ là bao nhiêu.

Đáp án cuối cùng chia lấy dư cho 10⁹ + 7.

## Dữ liệu

- Dòng thứ nhất chứa số nguyên dương n (1 ≤ n ≤ 10⁵)
- Dòng thứ hai gồm n số nguyên aᵢ (1 ≤ aᵢ ≤ 10⁹) - độ "dẻo dai" của cây cam thứ i.
- Dòng thứ ba gồm một số T - số câu hỏi của nhiệm vụ.
- T dòng tiếp theo, mỗi dòng gồm 2 số uᵢ, kᵢ (1 ≤ uᵢ, kᵢ ≤ n). Dữ liệu đảm bảo uᵢ + kᵢ - 1 ≤ n.

## Kết quả

In ra T dòng, mỗi dòng là đáp án cho từng câu hỏi modulo 10⁹ + 7.

## Ví dụ

**Input:**
```
6
5 2 7 1 10 3
3
1 2
2 3
3 4
```

**Output:**
```
10
14
70
```

## Giải thích

Ba dãy cây cần tính lần lượt là [5, 2], [2, 7, 1], [7, 1, 10, 3].

## Chấm điểm

- Subtask 1 (50% số test): n, T ≤ 10³
- Subtask 2 (50% số test): Giới hạn như đề bài