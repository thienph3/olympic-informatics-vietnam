# BeginnerFreeContest 49 - SALES

**Thể loại:** Greedy  
**Độ khó:** 450

## Đề bài

Vừa mới đi làm trở lại sau Tết, Khoa đã bị sếp giao một công việc vô cùng hóc búa: Công ty của Khoa còn tồn đọng N sản phẩm từ năm ngoái, sản phẩm thứ i có chủng loại là cᵢ.

Do đặc thù kỹ thuật, các sản phẩm này không thể bán lẻ mà phải bán theo bộ 2 hoặc 3 sản phẩm cùng chủng loại. Để giải quyết số hàng tồn đọng nhanh nhất có thể, sếp muốn Khoa chia N sản phẩm này thành ít nhất có thể các bộ 2 hoặc 3 sản phẩm cùng chủng loại.

Sau những ngày nghỉ Tết chỉ biết ăn và ngủ, đầu óc Khoa bây giờ không còn khả năng "nhảy số" nhanh nhẹn như trước nữa. Cậu chỉ biết nghĩ về những món ăn ngon mà mình đã ăn trong những ngày nghỉ Tết.

Những công việc sếp giao thì bắt buộc phải hoàn thành ngay hôm nay, nếu không sếp sẽ đuổi việc Khoa! Bị đuổi việc đầu năm quả là điều không may mắn chút nào. Các bạn hãy giúp Khoa hoàn thành công việc sếp giao nhé.

## Dữ liệu

- Dòng đầu tiên chứa số nguyên dương N (1 ≤ N ≤ 10⁵) là số lượng sản phẩm tồn đọng.
- Dòng thứ hai chứa N số nguyên c₁, c₂, ..., cₙ (1 ≤ cᵢ ≤ 10⁹) là chủng loại của các sản phẩm.

## Kết quả

In ra một số nguyên duy nhất là số bộ sản phẩm ít nhất có thể.
Nếu không tồn tại cách chia, in ra -1.

## Ví dụ

**Input:**
```
10
2 2 3 3 2 3 4 4 4 4
```

**Output:**
```
4
```

**Input:**
```
3
2 3 4
```

**Output:**
```
-1
```

## Giải thích

- Ở ví dụ thứ nhất, chia thành 4 bộ sản phẩm: {2, 2, 2}, {3, 3}, {4, 4, 4}, {4, 4}.
- Ở ví dụ thứ hai, không có cách chia nào do chỉ có một sản phẩm có chủng loại 2.