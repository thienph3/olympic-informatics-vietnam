# Beginner Free Contest 37 - MINDIST

**Thể loại:** Array  
**Độ khó:** 300

## Đề bài

Khoảng cách giữa hai phần tử trong một mảng là số phần tử nằm giữa hai phần tử cộng một. Cho mảng a, tìm khoảng cách nhỏ nhất giữa hai phần tử bằng nhau của mảng a.

## Dữ liệu

- Dòng đầu tiên mỗi test chứa số n là độ dài của mảng a (1 ≤ n ≤ 10³)
- Dòng thứ hai chứa n số là các phần tử của mảng a (1 ≤ ai ≤ 10⁵)

## Kết quả

In ra một số là khoảng cách nhỏ nhất giữa hai phần tử bằng nhau của a, nếu không tồn tại in ra -1.

## Ví dụ

**Input:**
```
6
7 1 3 4 1 7
```

**Output:**
```
3
```

## Giải thích

Có hai cặp phần tử bằng nhau đó là 7 và 1. Khoảng cách giữa hai phần tử 1 là |1 - 4| = 3, khoảng cách giữa hai phần tử 7 là |0 - 5| = 5.