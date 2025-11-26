# Beginner Free Contest 39 - MEDIAN

**Thể loại:** Array  
**Độ khó:** 550

## Đề bài

Nông dân John xếp N con bò của mình (đánh số từ 1 đến N) thành một hàng ngang để đo chiều cao của chúng, kết quả đo được là con bò thứ i có chiều cao là hᵢ. Sau đó anh ta muốn chụp ảnh một số dãy con của hàng (mỗi dãy con gồm những con bò liên tiếp nhau) để mang đến dự thi cuộc thi nhiếp ảnh tại một hội chợ.

Cuộc thi này có một quy định là chỉ những bức ảnh có trung vị chiều cao của những con bò trong ảnh lớn hơn hoặc bằng K thì mới hợp lệ và được dự thi.

Số trung vị của một dãy số A₁...Aₓ có X phần tử được ban tổ chức cuộc thi định nghĩa như sau:
- Là số A_{X/2 + 1} khi dãy A được sắp xếp không giảm nếu X chẵn.
- Là số A_{(X+1)/2} khi dãy A được sắp xếp không giảm nếu X lẻ.

Bạn hãy đếm số bức ảnh hợp lệ mà nông dân John có thể chụp.

## Dữ liệu

- Dòng thứ nhất gồm hai số nguyên N và K (1 ≤ N ≤ 10⁵; 1 ≤ K ≤ 10⁹)
- Dòng thứ hai gồm N số nguyên h₁, h₂, h₃, ..., hₙ (1 ≤ hᵢ ≤ 10⁹) lần lượt là chiều cao của từng con bò trong hàng.

## Kết quả

In ra số bức ảnh mà nông dân John có thể chụp.

## Ví dụ

**Input:**
```
4 6
10 5 6 2
```

**Output:**
```
7
```

## Giải thích

Những dãy con hợp lệ là {10}, {6}, {10, 5}, {5, 6}, {6, 2}, {10, 5, 6}, {10, 5, 6, 2}.

## Chấm điểm

- Subtask 1 (30% số test): 1 ≤ N ≤ 500, 1 ≤ K ≤ 10⁹
- Subtask 2 (70% số test): Không có ràng buộc gì thêm