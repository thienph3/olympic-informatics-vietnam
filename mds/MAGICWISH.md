# Beginner Free Contest 55 - MAGICWISH

**Thể loại:** Greedy  
**Độ khó:** 650

## Đề bài

Ma thuật thực sự rất đơn giản, bạn chỉ cần muốn điều gì bạn sẽ có được nó. Rex và người bạn pháp sư Zatara của mình đang khám phá khu rừng phù thủy vào đêm Halloween.

Khi Rex vô tình phát hiện một mảng các số kỳ diệu A có độ dài N, nó đưa anh ta vào một thế giới khác. Rex nhớ rằng Zatara đã đưa cho anh ta hai số nguyên P và Q để sử dụng trong tình huống như này.

Khi sử dụng các số nguyên này, Rex có thể sửa đổi mảng A như sau:

- Tối đa P lần, thực hiện thao tác sau:
  1. Chọn hai phần tử x và y từ A, xóa cả hai phần tử này khỏi A, và chèn x + y vào A.
  2. Thao tác này chỉ có thể thực hiện nếu A có ít nhất hai phần tử.

- Tối đa Q lần, thực hiện thao tác sau:
  1. Chọn hai phần tử x và y từ A, xóa cả hai phần tử này khỏi A, và chèn x - y vào A.
  2. Thao tác này cũng chỉ có thể thực hiện nếu A có ít nhất hai phần tử.

Lưu ý rằng mỗi thao tác làm giảm kích thước của A đi một. Hai loại thao tác (cộng và trừ) có thể thực hiện theo bất kỳ thứ tự nào, miễn là tối đa P thao tác cộng và Q thao tác trừ được thực hiện.

Gọi B là mảng số kỳ diệu sau khi thực hiện một số lượng thao tác. Để trở lại thế giới ban đầu của mình, Rex phải tìm giá trị lớn nhất có thể của: max(B) - min(B) trên tất cả các trường hợp khả thi của B.

Bạn có thể giúp Rex tìm giá trị này không?

## Dữ liệu

- Dòng thứ nhất chứa số nguyên T (1 ≤ T ≤ 10⁵) - số lượng test.
- Dòng đầu tiên của mỗi test chứa số nguyên N (1 ≤ N ≤ 10⁵) - kích thước mảng.
- Dòng thứ hai của mỗi test chứa 2 số nguyên P, Q (0 ≤ P, Q ≤ N - 1) - số lượng thao tác cộng và trừ tối đa Rex có thể thực hiện.
- Dòng thứ ba của mỗi test chứa N số nguyên A₁, A₂, ..., Aₙ (|Aᵢ| ≤ 10⁹).

Tổng của N trong tất cả các trường hợp thử sẽ không vượt quá 3 × 10⁵.

## Kết quả

Gồm T dòng, tại test thứ i in ra duy nhất một số nguyên là số có thể đưa Rex trở lại thế giới ban đầu.

## Ví dụ

**Input:**
```
3
2
0 0
5 1
6
1 2
8 -1 -4 2 6 -3
7
6 6
-2 -4 2 -2 -3 -1 -1
```

**Output:**
```
4
23
15
```

## Giải thích

Mảng là A = [8, -1, -4, 2, 6, -3]. Dãy thao tác sau có thể được thực hiện:

1. Chọn 2 và -3, loại bỏ chúng và chèn 2 - (-3) = 5 vào mảng. Kết quả là mảng: [8, -1, -4, 6, 5]
2. Chọn 8 và 5, loại bỏ chúng và chèn 8 + 5 = 13 vào mảng. Kết quả là mảng: [13, -1, -4, 6]
3. Chọn -4 và 6, loại bỏ chúng và chèn (-4) - 6 vào mảng. Kết quả là mảng: [13, -1, -10]

Hiệu giữa giá trị lớn nhất và giá trị nhỏ nhất trong mảng này là 13 - (-10) = 23.