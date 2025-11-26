# Free Contest 144 - H9DNBD

**Thể loại:** Hash Table  
**Độ khó:** 300

## Đề bài

Cho dãy số A gồm có n số nguyên dương {A₁, A₂, ..., Aₙ}. Hãy cho biết có bao nhiêu giá trị xuất hiện ít nhất k lần trong dãy A, tổng của các giá trị khác nhau đó?

## Dữ liệu

- Dòng đầu tiên chứa hai số n (1 ≤ n, k ≤ 10⁵)
- Dòng tiếp theo lần lượt chứa n số A₁, A₂, ..., Aₙ (1 ≤ Aᵢ ≤ 10⁹)

## Kết quả

In ra một dòng duy nhất chứa hai số, lần lượt là số lượng giá trị xuất hiện ít nhất k lần trong dãy A, và tổng của k giá trị đó.

## Ví dụ

**Input:**
```
6 2
3 1 2 3 2 5
```

**Output:**
```
2 5
```

## Giải thích

Ở test ví dụ trên, n = 6, k = 2. Dãy A có một phần tử giá trị 1, hai phần tử giá trị 2, hai phần tử giá trị 3 và một phần tử giá trị 5. Vì thế, có 2 giá trị thỏa mãn là 2 và 3, tổng của chúng là 5.

## Điểm số

- Subtask 1 (80%): Aᵢ ≤ 10⁶
- Subtask 2 (20%): Không có giới hạn gì thêm