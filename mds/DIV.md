# Beginner Free Contest 51 - DIV

**Thể loại:** Math  
**Độ khó:** 450

## Đề bài

Bạn đang chơi một trò chơi một người chơi, mà trong đó bạn sẽ phải chơi 10¹² màn chơi khác nhau để tiêu diệt 10¹² con Boss khác nhau. Màn chơi thứ i sẽ xuất hiện con Boss thứ i có chỉ số sức mạnh bằng tổng của các ước nguyên dương của i.

Bạn đang cần xem lại thống kê của các màn chơi q màn chơi: a₁, a₂, ..., aᵩ. Hãy cho biết sức mạnh của Boss của mỗi màn chơi đang xem nhé!

## Dữ liệu

- Dòng thứ nhất chứa duy nhất số q.
- Dòng thứ hai lần lượt in ra q số: a₁, a₂, ..., aᵩ.

## Kết quả

In ra một dòng gồm q số, số thứ i in ra sức mạnh của con Boss thứ aᵢ (1 ≤ i ≤ q). Các số được in ra cách nhau một khoảng trống.

## Ví dụ

**Input:**
```
4
2 4 10 9
```

**Output:**
```
3 7 18 13
```

**Input:**
```
4
10 11 12 13
```

**Output:**
```
18 12 28 14
```

## Giải thích

Gọi G(x) là tổng các ước của x.

Test ví dụ 1 có:
- G(2) = 1 + 2 = 3
- G(4) = 1 + 2 + 4 = 7
- G(10) = 1 + 2 + 5 + 10 = 18
- G(9) = 1 + 3 + 9 = 13

Test ví dụ 2 là một ví dụ cho Subtask 4. Ta có:
- G(10) = 18
- G(11) = 1 + 11 = 12
- G(12) = 1 + 2 + 3 + 4 + 6 + 12 = 28
- G(13) = 1 + 13 = 14

## Điểm số

- Subtask 1 (15%): q ≤ 10⁴; aᵢ ≤ 10³ (1 ≤ i ≤ q)
- Subtask 2 (25%): q ≤ 10⁵; aᵢ ≤ 10⁵ (1 ≤ i ≤ q)
- Subtask 3 (35%): q ≤ 10⁵; aᵢ ≤ 10⁶ (1 ≤ i ≤ q)
- Subtask 4 (25%): q ≤ 10⁶; aᵢ ≤ 10¹² (1 ≤ i ≤ q); aᵢ₊₁ = aᵢ + 1 (1 ≤ i < q)