# BeginnerFreeContest 42 - SOCOLA

**Thể loại:** Greedy  
**Độ khó:** 450

## Đề bài

Hôm nay Lộc muốn ăn socola nên đã đến cửa hàng để mua. Cửa hàng bán N loại socola khác nhau. Loại thứ i có aᵢ viên socola có thể bán.

Lộc là thiếu gia tiền nhiều vô kể. Vì thế Lộc không bị giới hạn bởi bất kỳ giá tiền nào và muốn mua nhiều socola nhất có thể. Tuy nhiên, nếu Lộc mua xᵢ socola loại i (0 ≤ xᵢ ≤ aᵢ) thì số lượng mua socola các loại j từ 1 đến i - 1 (1 ≤ j < i) phải thỏa một trong hai điều kiện:

- xⱼ = 0. Lộc không mua socola loại j.
- xⱼ < xᵢ. Lộc mua được ít socola loại j hơn loại i.

Ví dụ: Cửa hàng trưng bày số lượng socola các loại từ 1 đến N là: [6, 5, 4, 2, 5]
Mảng x = [0, 0, 1, 2, 5] là số lượng mua được socola các loại từ 1 đến N.

Bạn hãy tính số socola tối đa mà Lộc mua được ở cửa hàng.

## Dữ liệu

- Dòng đầu chứa số nguyên N (1 ≤ N ≤ 2 × 10⁵) là số loại socola.
- Dòng tiếp theo chứ N số nguyên aᵢ (1 ≤ aᵢ ≤ 10⁹) là số socola của mỗi loại.

## Kết quả

In ra số socola tối đa mà Lộc có thể mua.

## Ví dụ

**Input:**
```
5
1 2 3 6 10
```

**Output:**
```
10
```

**Input:**
```
4
1 1 1 1
```

**Output:**
```
1
```

**Input:**
```
5
10 20 4 1 1
```

**Output:**
```
20
```

## Giải thích

Ví dụ 1: số socola tối đa mua được là: 0 + 0 + 1 + 3 + 6 = 10.
Ví dụ 2: số socola tối đa mua được là: 1 + 2 + 3 + 4 + 10 = 20.
Ví dụ 3: số socola tối đa mua được là: 0 + 0 + 0 + 1 = 1.