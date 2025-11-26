# BeginnerFreeContest 41 - SELLING

**Thể loại:** Greedy  
**Độ khó:** 400

## Đề bài

Anh là một người hâm mộ cuồng nhiệt của một nữ ca sĩ nổi tiếng toàn thế giới. Khi nghe tin nữ thần sẽ có chuyến lưu diễn tại nước mình, Anh lập tức tìm cách để kiếm đủ tiền để mua vé.

Anh cần cho mình làm một khoản tiền T đồng, và anh chọn cách bán những món hàng của mình. Anh còn mó nhàng, và có Q khách hàng sẵn sàng mua những món hàng của anh. Người thứ i sẽ mua món hàng aᵢ với giá là vᵢ và ong ày thứ i.

Món hàng nào đã bán cho khách thì anh không thể bán lại cho khách khác được, và anh có thể lựa chọn khách hàng nào để bán cho phù hợp với nhu cầu của mình.

Anh muốn mua vé sớm nhất có thể. Hãy cho biết ít nhất Anh cần phải đợi đến ngày thứ bao nhiêu để có thể mua vé.

## Dữ liệu

- Dòng đầu chứa 3 số nguyên N, T, Q tương ứng với số món hàng của Anh, số tiền Anh cần để mua vé và số lượng khách mua hàng. (1 ≤ N, Q ≤ 10³, 1 ≤ T ≤ 10⁷)
- Q dòng sau, mỗi dòng gồm 2 số nguyên, dòng thứ i chứa hai số nguyên aᵢ và vᵢ tương ứng với món hàng khách muốn mua với mức giá của nó. (1 ≤ aᵢ ≤ N, 1 ≤ vᵢ ≤ 10⁷)

## Kết quả

Gồm một dòng duy nhất là là ngày sớm nhất mà Anh đủ tiền để mua vé. Nếu bán hết cho khách mà vẫn không đủ tiền thì xuất -1.

## Ví dụ

**Input:**
```
2 3 3
1 2
1 1
2 3
```

**Output:**
```
3
```

**Input:**
```
1 1 1
1 1
```

**Output:**
```
1
```

**Input:**
```
1 2 1
1 1
```

**Output:**
```
-1
```

## Giải thích

- Ở ví dụ 1, Anh cần phải đợi đến ngày 3 để bán món hàng 1 cho khách và bán món hàng 2 cho khách ngày thứ 2.
- Ở ví dụ 2, dù thế nào đi nữa Anh cũng không đủ tiền mua vé.