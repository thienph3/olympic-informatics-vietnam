# Beginner Free Contest 41 - MEETING

**Thể loại:** Math  
**Độ khó:** 450

## Đề bài

Sau khi chú bé Tus qua Nga định cư tại nhà của người quen thì cậu bắt đầu dành ra vài ngày để khám phá hàng xóm nơi đây. Nhờ đó, cậu đã phát hiện con đường cậu đang sinh sống có một phong tục rất độc đáo.

Trên con đường này có n ngôi nhà, các ngôi nhà được đánh số từ 1 tới n, trong đó nhà thứ i có tọa độ nguyên dương là xi và chứa ai người. Và ở ngày 26/5 hàng năm, mọi người trên con đường này sẽ chọn ra 1 căn nhà để tụ họp tất cả mọi người lại. Sau đó, mọi người sẽ cùng nhau ăn uống và chia sẻ những mẩu chuyện của bản thân.

Nhưng những người sinh sống trên con đường này khá lười nên ai cũng muốn quãng đường mình di chuyển là ít nhất. Vì vậy, mọi người đã thống nhất chọn ngôi nhà mà tổng quãng đường di chuyển của tất cả mọi người tới đó là nhỏ nhất.

Tuy nhiên, Tus vì mới tới đây nên cậu chẳng biết mọi người đã chọn căn nhà nào để tụ họp. Nên Tus đành phải nhờ các bạn hãy giúp Tus tìm ra ngôi nhà đã được chọn.

## Dữ liệu

- Dòng đầu tiên gồm số nguyên dương n là số lượng ngôi nhà (1 ≤ n ≤ 200000).
- n dòng tiếp theo mỗi dòng chứa 2 số nguyên xi và ai là tọa độ và số lượng người trong ngôi nhà đó (1 ≤ xi, ai ≤ 10⁹, xi ≠ xj ∀ i ≠ j).

## Kết quả

In ra chỉ số nhà được chọn. Nếu có nhiều nhà thỏa đáp án in ra chỉ số nhà có tọa độ lớn nhất.

## Ví dụ

**Input:**
```
4
1 1
3 1
4 1
2 2
```

**Output:**
```
2
```