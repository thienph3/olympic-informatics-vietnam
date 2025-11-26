# Beginner Free Contest 46 - MULTIDSEQ

**Thể loại:** Dynamic Programming  
**Độ khó:** 700

## Đề bài

Cho hai số nguyên dương k và n (k ≤ n). Đếm số bộ số nguyên dương A₁, A₂, A₃, ..., Aₖ sao cho:

- 1 ≤ Aᵢ ≤ n, với mọi i thỏa mãn 1 ≤ i ≤ k,
- Aᵢ là ước của Aᵢ₊₁, với mọi i thỏa mãn 1 ≤ i < k.

## Dữ liệu

Gồm một dòng duy nhất lần lượt chứa hai số n và k.

## Kết quả

In ra 1 số duy nhất là đáp án sau khi đã chia lấy dư cho 10⁹ + 7.

## Ví dụ

**Input:**
```
4 2
```

**Output:**
```
8
```

**Input:**
```
6 3
```

**Output:**
```
25
```

## Giải thích

Ở test ví dụ đầu, có 8 cặp số thỏa mãn: {1, 1}, {1, 2}, {1, 3}, {1, 4}, {2, 2}, {2, 4}, {3, 3}, {4, 4}.

## Điểm số

- Subtask 1 (25%): n ≤ 15
- Subtask 2 (35%): n ≤ 10⁴, k ≤ 50
- Subtask 3 (40%): n ≤ 10⁵, k ≤ 50