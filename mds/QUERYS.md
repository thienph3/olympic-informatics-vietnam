# BeginnerFreeContest 50 - QUERYS

**Thể loại:** Data Structures  
**Độ khó:** 700

## Đề bài

Cho một dãy số nguyên a₁, a₂, ..., aₙ và số nguyên m. Bạn hãy thực hiện truy vấn thuộc một trong hai dạng sau:

- 1 l r x: cộng thêm x vào các phần tử aₗ, aₗ₊₁, ..., aᵣ.
- 2 l r: tính tổng của (aₗᵐ + aₗ₊₁ᵐ + ... + aᵣᵐ) mod m.

## Dữ liệu

- Dòng đầu tiên gồm ba số nguyên dương m, n và q.
- Dòng thứ hai gồm n số nguyên aᵢ (1 ≤ aᵢ ≤ 10⁶).
- q dòng tiếp theo gồm các truy vấn, mỗi truy vấn thuộc một trong hai dạng như trên (1 ≤ lᵢ ≤ rᵢ ≤ n, 1 ≤ x ≤ 10⁶).

## Kết quả

Với mỗi truy vấn loại 2, in ra tổng tìm được.

## Ràng buộc

- Subtask 1 (30%): 1 ≤ n, q ≤ 10², m = 2.
- Subtask 2 (30%): 1 ≤ n, q ≤ 10⁵, m = 5.
- Subtask 3 (40%): 1 ≤ n, q ≤ 2 × 10⁵, m = 10⁷.

## Ví dụ

**Input:**
```
2 5 3
3 2 4 1 5
2 1 4
1 2 5 6
2 1 5
```

**Output:**
```
1
0
```