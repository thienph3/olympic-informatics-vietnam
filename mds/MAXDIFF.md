# Beginner Free Contest 47 - MAXDIFF

**Thể loại:** Greedy  
**Độ khó:** 550

## Đề bài

Lộc được cho một mảng A gồm 3N phần tử, anh có thể tạo ra một mảng A' là dãy con gồm 2N phần tử từ mảng A. Lưu ý, dãy con của một mảng có thể được tạo bằng cách xóa đi một vài phần tử (hoặc không xóa đi phần tử nào) trong mảng mà vẫn giữ thứ tự xuất hiện của các phần tử.

**Yêu cầu:** Gọi F = Σᵢ₌₁ᴺ A'ᵢ - Σⱼ₌ₙ₊₁²ᴺ A'ⱼ. Hãy giúp Lộc tạo ra một mảng A' sao cho giá trị của F là lớn nhất có thể.

## Dữ liệu

- Dòng đầu tiên gồm một số nguyên dương N (1 ≤ N ≤ 10⁵).
- Dòng thứ hai gồm 3N phần tử A₁, A₂, ..., A₃ₙ (|Aᵢ| ≤ 10⁹).

## Kết quả

Gồm duy nhất một số nguyên là kết quả của yêu cầu bài toán trên.

## Ví dụ

**Input:**
```
3
1 3 4 2 9 7 5 3 2
```

**Output:**
```
10
```

**Input:**
```
2
4 10 1 7 6 2
```

**Output:**
```
11
```

## Giải thích

- Ở test ví dụ đầu tiên, mảng A' mà Lộc tạo ra được chính là A' = {4, 9, 7, 5, 3, 2} có F = (4 + 9 + 7) - (5 + 3 + 2) = 10 và đây là giá trị F lớn nhất mà Lộc tạo được.
- Ở test ví dụ thứ hai, mảng A' mà Lộc tạo ra được chính là A' = {4, 10, 1, 2} có F = (4 + 10) - (1 + 2) = 11 và đây là giá trị F lớn nhất mà Lộc tạo được.

## Chấm điểm

- Subtask 1 (40% số test): N ≤ 2000
- Subtask 2 (60% số test): Không có ràng buộc gì thêm