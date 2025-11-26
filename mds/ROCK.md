# BeginnerFreeContest 54 - ROCK

**Thể loại:** Greedy  
**Độ khó:** 550

## Đề bài

Một ngày nọ, các công nhân xây dựng đang làm việc hăng say thì xuất hiện N tảng đá xếp dọc trên đường. Tảng đá thứ i có trọng lượng aᵢ. Họ được cho thêm một số k luôn chia hết bởi n.

Chủ thầu nhân cơ hội này đã đố các người công nhân của mình (ai giải được lương sẽ tăng gấp đôi). Chủ thầu yêu cầu các công nhân của mình hãy tìm một cách sắp xếp là hoán vị của các tảng đá sao cho phương trình dưới đây đạt giá trị nhỏ nhất:

∑ᵢ₌₁ⁿ⁻ᵏ |Aᵢ - Aᵢ₊ₖ|

Bạn hãy giúp các người công nhân giải bài toán hóc búa này bằng cách in ra giá trị nhỏ nhất tìm được nhé.

## Dữ liệu

- Dòng thứ nhất chứa hai số nguyên dương n, k (1 ≤ k ≤ n ≤ 10⁵)
- Dòng thứ hai gồm n số nguyên aᵢ (1 ≤ aᵢ ≤ 10⁹) - Trọng lượng các tảng đá.

## Kết quả

In ra kết quả là giá trị nhỏ nhất tìm được.

## Ví dụ

**Input:**
```
6 3
5 2 7 1 10 3
```

**Output:**
```
6
```

## Giải thích

Ta có thể sắp xếp dãy trên thành [10, 1, 3, 7, 2, 5]

## Chấm điểm

- Subtask 1 (50% số test): n, k ≤ 10³.
- Subtask 2 (50% số test): Giới hạn như đề bài.