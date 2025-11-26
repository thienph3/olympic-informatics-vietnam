# BeginnerContest 05 - TREE

**Thể loại:** Graph  
**Độ khó:** 600

## Đề bài

Ở một vùng đất xa xôi, có một bầy kiến đang xây tổ. Theo như bản thiết kế của kiến kỹ sư, các kiến thợ phải đào N - 1 đường hầm sao cho từ một khu vực có thể đi đến tất cả các khu vực còn lại.

Mặt khác, theo phong thủy, mỗi khu vực u phải cách khu vực v xa nhất đúng bằng khoảng Au. Liệu có thể xây dựng được tổ đảm bảo những yêu cầu trên hay không? Bạn hãy giúp kiến kỹ sư kiểm tra nhé.

## Dữ liệu

- Dòng đầu gồm một số nguyên dương N.
- Dòng tiếp theo, gồm N số Au - khoảng cách giữa đỉnh u và đỉnh xa nhất.

## Giới hạn

- 1 ≤ N ≤ 10⁵.
- 1 ≤ Aᵢ < N

## Kết quả

In ra "Possible" nếu tồn tại cách xây. Ngược lại, in ra "Impossible".

## Ví dụ

**Input:**
```
5
3 2 2 3 3
```

**Output:**
```
Possible
```

**Input:**
```
3
1 1 2
```

**Output:**
```
Impossible
```