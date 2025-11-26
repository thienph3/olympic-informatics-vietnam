# Beginner Free Contest 51 - LINEUP

**Thể loại:** Math  
**Độ khó:** 400

## Đề bài

Anh có n cặp đồ chơi, mỗi cặp đồ chơi bao gồm 2 Figure nhân vật hoạt hình và chúng luôn đi cặp với nhau, mỗi Figure sẽ có một con số thể hiện giá trị của sản phẩm. Anh muốn xếp N cặp đồ chơi thành 2 hàng dọc, mỗi hàng ngang bao gồm một cặp Figure.

Để trưng bày các Figure được đẹp hơn, Anh muốn mỗi hàng dọc có tổng giá trị các sản phẩm là một số chẵn. Anh có thể thay đổi vị trí của các cặp Figure, cũng có thể thay đổi vị trí của 2 Figure trong một cặp, nhưng không thể tách một cặp ra với nhau (vì tách cặp ra thì nó xấu hơn).

Mỗi lần thay đổi thì anh phải tốn thời gian để mở tủ, thay đổi và đóng tủ lại để xem xét coi cách trình bày bộ sưu tập của mình đã đẹp chưa, vì thế mà anh muốn chỉ nhỉ nhất có thể.

Anh muốn biết mình cần ít nhất bao nhiêu thao tác thay đổi để bộ sưu trình được trình bày đẹp.

## Dữ liệu

- Dòng đầu bao gồm 1 số nguyên dương N trong đó N là số cặp Figure mà Anh đã sưu tập. (1 ≤ N ≤ 5 × 10⁵)
- N dòng tiếp theo, dòng thứ i bao gồm 2 số nguyên aᵢ, bᵢ tương ứng là giá trị của 2 Figure trong cặp Figure thứ i (1 ≤ aᵢ, bᵢ ≤ 10⁹)

## Kết quả

Gồm một số nguyên duy nhất là số thao tác thay đổi ít nhất để bộ sưu tập của Anh đẹp. Nếu Anh thấy không có cách nào để đẹp hơn thì xuất -1.

## Ví dụ

**Input:**
```
4
1 2
3 4
6 4
4 5
```

**Output:**
```
2
```