# BeginnerFreeContest 46 - TRIPLET

**Thể loại:** Combinatorics  
**Độ khó:** 350

## Đề bài

Lộc vừa được cho hai số nguyên dương n và S. Lộc muốn tìm số lượng bộ ba (a, b, c) thỏa điều kiện 0 ≤ a, b, c ≤ n và a + b + c = S.

## Dữ liệu

Duy nhất một dòng gồm hai số nguyên dương n và S (0 ≤ n ≤ 7000, 0 ≤ S ≤ 3 × n).

## Kết quả

In ra duy nhất một số nguyên dương là số lượng bộ ba (a, b, c) thỏa điều kiện mà Lộc muốn tìm.

## Ví dụ

**Input:**
```
3 7
```

**Output:**
```
6
```

**Input:**
```
10 0
```

**Output:**
```
1
```

**Input:**
```
37 137
```

**Output:**
```
7482
```

## Giải thích

Ở test ví dụ thứ nhất, các bộ ba (a, b, c) thỏa mãn điều kiện mà Lộc cần tìm là các cặp sau đây:
- a = 1, b = 3, c = 3
- a = 2, b = 2, c = 3
- a = 2, b = 3, c = 2
- a = 3, b = 1, c = 3
- a = 3, b = 2, c = 2
- a = 3, b = 3, c = 1

## Chấm điểm

- Subtask 1 (40% số test): n ≤ 300.
- Subtask 2 (40% số test): n ≤ 2000.
- Subtask 3 (20% số test): Không có ràng buộc gì thêm.