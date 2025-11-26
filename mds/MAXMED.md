# Beginner Free Contest 36 - MAXMED

**Thể loại:** Greedy  
**Độ khó:** 500

## Đề bài

Bạn được cấp một mảng a với N số nguyên, trong đó N là số lẻ. Bạn có thể thực hiện các thao tác sau với mảng:

- Chọn một phần tử aᵢ.
- Tăng aᵢ lên một đơn vị (aᵢ = aᵢ + 1).

Bạn cần làm cho giá trị trung vị của mảng lớn nhất có thể bằng cách sử dụng tối đa k thao tác.

Trung vị của mảng có kích thước lẻ là phần tử ở chính giữa sau khi mảng được sắp xếp theo thứ tự không giảm. Ví dụ, trung vị của mảng [1, 5, 2, 3, 5] là 3.

## Dữ liệu

- Dòng đầu tiên chứa hai số nguyên N (1 ≤ N ≤ 2 × 10⁵, N là số lẻ) và k (1 ≤ k ≤ 10⁹) - số phần tử trong mảng và số thao tác lớn nhất mà bạn có thể thực hiện.
- Dòng thứ hai chứa N số nguyên a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 10⁹).

## Kết quả

In một số nguyên duy nhất - giá trị trung vị lớn nhất có thể có sau các thao tác.

## Ví dụ

**Input:**
```
3 2
1 3 5
```

**Output:**
```
5
```

**Input:**
```
5 5
1 2 1 1 1
```

**Output:**
```
3
```

**Input:**
```
7 7
1 2 3 5 6 6 6
```

**Output:**
```
5
```

## Giải thích

**Ví dụ 1:** Bạn có thể tăng phần tử thứ hai lên hai lần. Mảng trở thành [1, 5, 5] và giá trị trung vị là 5.

**Ví dụ 2:** Sau khi thực hiện 5 thao tác. Mảng trở thành [1, 1, 3, 3, 3] và giá trị trung vị là 3.

**Ví dụ 3:** Sau khi thực hiện 7 thao tác. Mảng trở thành [1, 2, 3, 5, 6, 6, 6] và giá trị trung vị là 5.