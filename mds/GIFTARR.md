# Beginner Free Contest 43 - GIFTARR

**Thể loại:** Math  
**Độ khó:** 400

## Đề bài

Tại thế giới Tobacco có một kho lưu trữ số Strong đó chứa số phân biệt với nhau (nghĩa là sẽ không có hai số nào trong S có cùng giá trị). Tại thế giới này toán học là thứ mà người ta trân quý nhất vậy nên việc tặng một dãy số mà trung bình cộng của dãy số bằng đúng một số X là một món quà xinh đẹp tuyệt vời đối với người dân nơi đây.

Tiger là một nhân viên gói quà trong cửa hàng số. Hãy xác định xem Tiger có thể tạo ra một dãy số với độ dài tùy thích mà trung bình cộng của dãy số đó bằng đúng số X.

Nếu Tiger có khả năng làm được in ra YES, ngược lại in ra NO.

## Dữ liệu

- Dòng đầu tiên chứa số nguyên T (1 ≤ T ≤ 10³).
- Dòng đầu tiên chứa số nguyên N, X (1 ≤ N ≤ 10⁵, 1 ≤ X ≤ 10⁹).
- Dòng thứ hai chứa N số nguyên là giá trị của các số trong kho lưu trữ S (1 ≤ Si ≤ 10⁹) (Si ≠ Sj, i ≠ j).
- Tổng của N trong các test không vượt quá 2 × 10⁵.

## Kết quả

In ra YES, nếu Tiger có khả năng tạo được một món quà là một dãy số với độ dài tùy thích mà trung bình cộng của dãy số bằng X, ngược lại in ra NO.

## Ví dụ

**Input:**
```
4
3 2
1 2 3
2 3
1 5
3 4
5 6 3
4 5
10 2 5 3
```

**Output:**
```
YES
NO
YES
YES
```

## Giải thích

- Ở test đầu tiên một trong các dãy số phù hợp là [2, 2, 2]. Vì trung bình cộng là (2 + 2 + 2)/3 = 2 = X.
- Ở test thứ hai, không có dãy số nào phù hợp.
- Ở test thứ ba, một trong các dãy số phù hợp là [4, 6]. Vì trung bình cộng là (4 + 6)/2 = 5 = X.
- Ở test thứ tư, một trong các dãy số phù hợp là [5].