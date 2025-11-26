# BeginnerFreeContest 28 - SALE

**Thể loại:** Dynamic Programming  
**Độ khó:** 700

## Đề bài

Một cửa hàng còn mó nhàng được bày bán trên quầy theo thứ tự từ trái sang phải, đánh số từ 1..N. Mó nhàng thứ i có giá tiền là Aᵢ.

Nhân một dịp nào đó, chủ cửa hàng quyết định thực hiện chính sách giảm giá. Cụ thể với mó nhàng thứ i, gọi B là mảng giá tiền của các mó nhàng còn trên quầy nằm bên trái i có giá tiền rẻ hơn Aᵢ, sau khi sắp xếp B tăng dần, nếu số lượng phần tử của B không nhỏ hơn K thì có thể mua mó nhàng i với giá Bₖ. Ngược lại, nếu số lượng phần tử của B nhỏ hơn K thì mó nhàng i sẽ vẫn giữ giá cũ.

Một mó nhàng khi được bán thì sẽ được đem đi khỏi quầy. Anh là một người đam mê mua sắm. Anh đứng đây từ chiều và muốn mua hết tất cả các mó nhàng. Thật may mắn cho anh là ngoài Anh ra không ai mua cả, nên anh có thể tự do chọn mua mó nhàng nào trước mà không sợ mó nhàng bị mua mất.

Tuy nhiên, Anh vẫn là người chi tiêu hợp lý, anh muốn mua hết tất cả mó nhàng với số tiền bỏ ra là ít nhất. Hãy tính số tiền nhỏ nhất mà Anh bỏ ra để mua hết tất cả mó nhàng.

## Dữ liệu

- Dòng đầu chứa 2 số nguyên dương N và K (1 ≤ N ≤ 3000, 1 ≤ K ≤ N)
- Dòng thứ 2 chứa N số nguyên dương Aᵢ là giá tiền của mó nhàng thứ i (1 ≤ Aᵢ ≤ 10⁹)

## Kết quả

Số tiền nhỏ nhất mà Anh phải trả để mua hết tất cả các mó nhàng

## Ví dụ

**Input:**
```
5 2
1 3 2 4 3
```

**Output:**
```
10
```

## Giải thích

Anh chọn mua các mó nhàng theo vị trí lần lượt là: 5, 4, 3, 2, 1 với giá tiền mua từng mó nhàng lần lượt là: 2, 2, 2, 3, 1. Tổng giá tiền Anh phải trả là 10.