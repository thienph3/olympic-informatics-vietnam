# BeginnerFreeContest 45 - TRUNGTHU

**Thể loại:** Greedy  
**Độ khó:** 400

## Đề bài

Nhân dịp tết trung thu, vì muốn tạo ấn tượng với các bạn nữ trong lớp. Hiếu quyết định mua một số bánh trung thu để làm quà tặng. Biết rằng còn n loại bánh trung thu, bánh trung thu loại i có giá ai đồng. Biết rằng mẹ Hiếu chỉ cho Hiếu đúng M đồng tiền tiêu vặt. Biết rằng với M đồng này Hiếu có thể mua tất cả các loại bánh với mỗi loại ít nhất một bánh. Hiếu dự định sẽ mua tất cả các loại bánh và tìm cách mua được nhiều số bánh nhất có thể. Bạn hãy lập trình để giúp Hiếu tính số bánh nhiều nhất mà Hiếu có thể mua nhé.

## Dữ liệu

- Dòng thứ nhất ghi hai số nguyên n, M - số loại bánh trung thu và tổng số tiền Hiếu có.
- Dòng thứ hai ghi n số a1, a2, ..., an, với ai là giá tiền của bánh trung thu loại i.

## Ràng buộc

- 2 ≤ n ≤ 10⁵
- 1 ≤ ai ≤ 10⁶
- a1 + a2 + ... + an ≤ M ≤ 10⁹
- Tất cả dữ liệu được cho là số nguyên

## Kết quả

In ra số bánh nhiều nhất mà Hiếu có thể mua.

## Ví dụ

**Ví dụ 1:**

**Input:**
```
4 100
10 15 20 30
```

**Output:**
```
10
```

**Ví dụ 2:**

**Input:**
```
3 150
50 60 80
```

**Output:**
```
3
```

**Ví dụ 3:**

**Input:**
```
5 100
1 1 1 1 1
```

**Output:**
```
95
```