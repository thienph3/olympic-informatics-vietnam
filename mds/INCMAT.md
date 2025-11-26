# Beginner Free Contest 54 - INCMAT

**Thể loại:** Math  
**Độ khó:** 250

## Đề bài

Gần đây trong lớp tin học của mình, Rex được cô giáo của mình dạy về mảng hai chiều, và bài tập Rex được giao sau buổi học là tính tổng phần tử của các mảng mà cậu ấy nhận được.

Sau khi về nhà Rex phát hiện các mảng mà giáo viên giao cho có một đặc điểm rất đặc biệt như sau:

- Mảng 2 chiều mà Rex được nhận sẽ có M hàng và N cột.
- Gọi x là phần tử đầu tiên của mảng - a[1][1].
- Mảng mà Rex được nhận sẽ luôn có dạng như sau:

```
x       x+1     x+2     ...  x+N-1
x+1     x+2     x+3     ...  x+N
x+2     x+3     x+4     ...  x+N+1
...     ...     ...     ...  ...
x+M-1   x+M     x+M+1   ...  x+N+M-2
```

Vì bận về quê, nên Rex rất mong muốn tìm một người có thể hỗ trợ cậu lúc này. Bạn hãy giúp cậu ấy nhé!

## Dữ liệu

- Dòng thứ nhất chứa số nguyên T (1 ≤ T ≤ 10⁵) - số lượng test.
- Dòng đầu tiên của mỗi test chứa 2 số nguyên M, N (1 ≤ M, N ≤ 10⁵) - kích thước mảng.
- Dòng thứ hai của mỗi test chứa số nguyên x (1 ≤ x ≤ 10³) - phần tử đầu tiên của mảng đó.

## Kết quả

Gồm T dòng, tại test thứ i in ra duy nhất một số nguyên là tổng các phần tử của mảng thứ i.

## Ví dụ

**Input:**
```
3
1 1 10
2 1 50
4 6 100
```

**Output:**
```
10
101
2520
```

## Giải thích

Ở ví dụ thứ ba, mảng của Rex đang nhận được như sau:

```
100  101  102  103  104  105
101  102  103  104  105  106
102  103  104  105  106  107
103  104  105  106  107  108
```

và nó có tổng các phần tử là 2520.