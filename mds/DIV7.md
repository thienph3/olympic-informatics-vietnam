# Beginner Free Contest 53 - DIV7

**Thể loại:** Math  
**Độ khó:** 600

## Đề bài - Đoạn chia hết cho 7

Xét một dãy b₁, b₂, ..., bₘ gồm các số nguyên dương, ta định nghĩa giá trị của dãy là tổng của tích các cặp phần tử của dãy, hay nói cách khác là tổng của bᵢ · bⱼ với 1 ≤ i < j ≤ m.

Cho một dãy a₁, a₂, ..., aₙ, hãy tính số lượng cặp (l, r) với 1 ≤ l ≤ r ≤ n, thỏa điều kiện giá trị của dãy con aₗ, aₗ₊₁, ..., aᵣ chia hết cho 7.

## Dữ liệu

- Dòng đầu tiên gồm một số nguyên duy nhất là số nguyên dương n (1 ≤ n ≤ 10⁵) - độ dài của dãy.
- Dòng thứ hai gồm n số nguyên dương a₁, a₂, ..., aₙ (0 ≤ aᵢ ≤ 10⁹) - các phần tử của dãy a.

## Kết quả

In ra một số nguyên duy nhất là số cặp (l, r) với 1 ≤ l ≤ r ≤ n, thỏa điều kiện giá trị của dãy con tương ứng chia hết cho 7.

## Ví dụ

**Input:**
```
3
5 23 2021
```

**Output:**
```
2
```

**Input:**
```
3
5 0 15
```

**Output:**
```
0
```

**Input:**
```
3
7 7 7
```

**Output:**
```
3
```

## Chấm điểm

- Subtask 1 (15% số test): n ≤ 300
- Subtask 2 (35% số test): n ≤ 5000
- Subtask 3 (50% số test): Không có ràng buộc gì thêm