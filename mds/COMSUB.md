# Beginner Free Contest 45 - COMSUB

**Thể loại:** Dynamic Programming  
**Độ khó:** 700

## Đề bài

Bạn được cho hai mảng số nguyên A, B với độ dài tương ứng N, M. Mỗi mảng chỉ chứa các số nguyên dương từ 1 đến 10⁵. Bạn hãy đếm xem có bao nhiêu cặp dãy con không liên tiếp của A và dãy con không liên tiếp của B, sao cho giá trị từng phần tử xét từ đầu đến cuối của hai dãy con này y hệt nhau.

Ở đây, một dãy con không liên tiếp của mảng là một dãy con được tạo thành từ việc xóa một số phần tử trong mảng mà không thay đổi thứ tự của những phần tử còn lại.

Hai cặp dãy con không liên tiếp được xem là phân biệt và thêm vào kết quả, nếu như chỉ số của những phần tử xóa ở dãy A hoặc B ở cặp này, phân biệt với chỉ số của những phần tử xóa ở dãy A hoặc B ở cặp kia.

Do kết quả có thể khá lớn, in ra số cặp tính được modulo 10⁹ + 7.

## Dữ liệu

- Dòng đầu tiên gồm hai số nguyên N và M (1 ≤ N, M ≤ 2 × 10³) - biểu diễn độ dài mảng A và B.
- Dòng tiếp theo gồm N số nguyên Ai (1 ≤ Ai ≤ 10⁵) - biểu diễn giá trị của mảng A.
- Dòng tiếp theo gồm M số nguyên Bi (1 ≤ Bi ≤ 10⁵) - biểu diễn giá trị của mảng B.

## Kết quả

In ra một số nguyên là số cặp thỏa mãn modulo 10⁹ + 7.

## Ví dụ

**Input:**
```
2 2
1 2
2 1
```

**Output:**
```
2
```

**Input:**
```
2 2
1 1
1 1
```

**Output:**
```
6
```

## Giải thích

Ở test ví dụ 1:
- A có những dãy con (), (1), (2), (1, 2)
- B có những dãy con (), (2), (1), (2, 1)
- Những cặp dãy con thỏa mãn là: ((), ()), ((1), (1)), ((2), (2))
- ((1, 2), (2, 1)) không thỏa, vì nếu xét từ đầu tới cuối của hai dãy con, ta có A₁ = 1 ≠ B₁ = 2 và A₂ = 2 ≠ B₂ = 1.

Ở test ví dụ 2:
- A có những dãy con (), (1), (1), (1, 1)
- B có những dãy con (), (1), (1), (1, 1)
- Những cặp dãy con thỏa mãn là: ((), ()), 4 cặp ((1), (1)), ((1, 1), (1, 1)). Vì thế, có tổng cộng 6 cặp thỏa.