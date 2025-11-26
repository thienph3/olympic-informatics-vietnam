# Beginner Free Contest 49 - CLOSEST

**Thể loại:** Data Structures  
**Độ khó:** 550

## Đề bài

Cho một dãy n số nguyên a₁, a₂, ..., aₙ và m truy vấn lⱼ, rⱼ (1 ≤ lⱼ ≤ rⱼ ≤ n). Với mỗi truy vấn, bạn cần tìm khoảng cách nhỏ nhất giữa hai phần tử ax và ay sao cho:

- Cả hai phần tử đều nằm trong đoạn [lⱼ, rⱼ] (lⱼ ≤ x, y ≤ rⱼ);
- Hai phần tử đều có giá trị bằng nhau (ax = ay).

## Dữ liệu

- Dòng đầu tiên gồm hai số nguyên dương n và m (1 ≤ n, m ≤ 5 × 10⁵).
- Dòng thứ hai gồm n số nguyên ai (-10⁹ ≤ ai ≤ 10⁹).
- m dòng tiếp theo gồm các truy vấn, mỗi truy vấn gồm hai số nguyên dương li, ri (1 ≤ li ≤ ri ≤ n).

## Kết quả

Gồm m dòng, trong đó dòng thứ i là khoảng cách |x - y| nhỏ nhất tìm được trong truy vấn thứ i. Nếu không có cặp nào thỏa điều kiện thì in ra -1.

## Ràng buộc

- Subtask 1 (20%): 1 ≤ n, m ≤ 10³
- Subtask 2 (20%): 1 ≤ n, m ≤ 10⁴
- Subtask 3 (60%): Không có ràng buộc gì thêm

## Ví dụ

**Input:**
```
5 3
2 3 1 3 5
1 3
2 4
1 5
```

**Output:**
```
2
1
2
```