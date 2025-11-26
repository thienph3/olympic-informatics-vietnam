# Beginner Free Contest 16 - NYTRAVEL

**Thể loại:** Graph  
**Độ khó:** 600

## Đề bài

Đất nước FreeContest đang trong quá trình xây dựng nên mạng lưới giao thông còn chưa hoàn thiện. Mạng lưới giao thông của đất nước này kết tối n thành phố bởi m con đường hai chiều. Các thành phố được đánh số từ 1 đến n.

Đội tình nguyện viên của FreeContest đang ở thành phố 1. Nhân dịp tết cổ truyền đang đến gần, đội tình nguyện viên muốn đi thăm nhiều thành phố nhất có thể. Nhưng vì mạng lưới giao thông chưa hoàn thiện, số thành phố các tình nguyện viên có thể thăm là khá ít.

Họ quyết định xây thêm một con đường một chiều kết nối hai thành phố nào đó để tăng số lượng thành phố có thể đến thăm nhiều nhất có thể.

Tony nhận ra bài toán đếm số lượng tối đa thành phố có thể đến thăm sau khi xây dựng thêm một con đường rất thú vị, vì vậy anh ta quyết định đưa bài toán này vào contest sắp tới.

Bạn sẽ giải quyết được bài toán này chứ?

## Dữ liệu

- Dòng đầu tiên chứa 2 số nguyên dương n, m lần lượt là số lượng thành phố và số lượng con đường hai chiều trong mạng lưới giao thông (1 ≤ n, m ≤ 10⁵).
- m dòng tiếp theo, mỗi dòng chứa hai số nguyên dương u, v miêu tả rằng có một đường hai chiều kết nối giữa hai thành phố u và v trong mạng lưới giao thông (u, v ≤ n).

## Kết quả

Đưa ra một số nguyên duy nhất là số lượng thành phố tối đa đội tình nguyện viên có thể đến thăm.

## Chấm điểm

- 30% số test ứng với 30% số điểm có n ≤ 500
- 70% số test còn lại không có giới hạn gì thêm

## Ví dụ

**Input:**
```
3 2
1 2
2 3
```

**Output:**
```
3
```

**Input:**
```
4 1
1 4
```

**Output:**
```
4
```