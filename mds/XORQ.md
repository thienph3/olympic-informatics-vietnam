# BeginnerFreeContest 48 - XORQ

**Thể loại:** Data Structures  
**Độ khó:** 650

## Đề bài

Cho một dãy a gồm n số nguyên không âm a1, a2, ..., an. Bạn được phép thực hiện một trong hai truy vấn sau đây:

1. Tính tổng đoạn con từ l đến r trong mảng a hiện tại (al + al+1 + ··· + ar).
2. Thực hiện phép toán xor với x cho các phần tử nằm trong đoạn con từ l đến r (al = al ⊕ x, al+1 = al+1 ⊕ x, ..., ar = ar ⊕ x).

Cho trước dãy số a và m truy vấn. Bạn hãy thực hiện các phép truy vấn này, và in ra kết quả đối với loại truy vấn 1.

## Dữ liệu

- Dòng đầu tiên gồm một số nguyên dương n (1 ≤ n ≤ 10⁵).
- Dòng thứ hai gồm n số nguyên không âm ai (0 ≤ ai ≤ 10⁶).
- Dòng thứ ba gồm một số nguyên dương m (1 ≤ m ≤ 5 · 10⁴).
- m dòng tiếp theo thuộc một trong hai loại truy vấn sau:
  - 1 l r (1 ≤ l ≤ r ≤ n).
  - 2 l r x (1 ≤ l ≤ r ≤ n, 1 ≤ x ≤ 10⁶).

## Kết quả

Với mỗi truy vấn loại 1, in ra màn hình kết quả là tổng của đoạn con tương ứng. Lưu ý các kết quả được in theo đúng thứ tự dữ liệu được nhập vào.

## Ràng buộc

- Subtask 1 (60%): 1 ≤ n, m ≤ 1,000.
- Subtask 2 (40%): 1 ≤ n ≤ 10⁵; 1 ≤ m ≤ 50,000.

## Ví dụ

**Input:**
```
5
1 2 3 4 5
8
1 1 5
2 2 4 1
1 1 5
2 1 3 2
1 1 5
2 3 5 4
1 1 5
1 3 5
```

**Output:**
```
15
14
12
18
14
```