# Beginner Free Contest 53 - DELIVERY

**Thể loại:** Greedy  
**Độ khó:** 650

## Đề bài

FCPost là một đơn vị chuyên cung cấp dịch vụ chuyển phát nhanh hàng hóa, bưu kiện trong nước cũng như quốc tế ở đất nước Free Contest. Ta sẽ xét mô hình bài toán giao hàng được đơn giản hóa, với các địa điểm nằm trên trục tọa độ Ox.

Kho hàng của trung tâm FCPost nằm ở tọa độ 0. Có n địa điểm cần giao hàng, địa điểm i nằm ở tọa độ xi và mỗi địa điểm có một kiện hàng cần giao. Ban đầu, tất cả các kiện hàng cần được giao đều nằm trong kho hàng.

Việc giao hàng sẽ được thực hiện bởi một chiếc xe tải có sức chứa tối đa là m kiện hàng, ban đầu có tọa độ 0 (nằm ngay kho hàng). Xe tải có thể di chuyển một đơn vị khoảng cách trong một đơn vị thời gian, bất kể đang chở bao nhiêu kiện hàng. Để chất kiện hàng từ kho hàng lên xe tải thì xe cần nằm ngay kho, và để có thể giao hàng đến một địa điểm thì tọa độ của xe cần trùng với tọa độ của địa điểm đó. Sau khi hoàn thành việc giao hàng cho tất cả địa điểm thì xe tải cần quay trở lại kho hàng.

Biết rằng thời gian để chất hàng lên xe tải và giao hàng cho một địa điểm (sau khi đã di chuyển đến địa điểm đó) là không đáng kể. Hãy tính toán thời gian tối thiểu mà FCPost cần để hoàn thành việc giao hàng cũng như đưa xe tải về lại kho nhé.

## Dữ liệu

- Dòng đầu tiên gồm hai số nguyên n và m (1 ≤ n ≤ 10⁵, 1 ≤ m ≤ n) - số địa điểm cần giao hàng và số kiện hàng tối đa mà xe tải có thể chở.
- n dòng tiếp theo, dòng thứ i gồm hai số nguyên xi và ci (-10⁹ ≤ xi ≤ 10⁹, xi ≠ 0) - tọa độ của địa điểm i. Lưu ý rằng có thể có nhiều địa điểm ở cùng một tọa độ.

## Kết quả

In ra một số nguyên duy nhất là thời gian tối thiểu để FCPost hoàn thành việc giao hàng và đưa xe tải về lại kho hàng.

## Ví dụ

**Input:**
```
5 2
-4
-2
1
3
-2
```

**Output:**
```
18
```

**Input:**
```
5 5
-4
-2
1
3
-2
```

**Output:**
```
14
```

**Input:**
```
3 1
30
20
10
```

**Output:**
```
120
```

## Giải thích

Ở ví dụ thứ nhất, một lộ trình để thực hiện việc giao hàng với thời gian tối thiểu như sau:
- Chất kiện hàng của địa điểm 3 và 4 lên xe tải.
- Di chuyển lần lượt đến tọa độ 1 và 3 (mất 3 đơn vị thời gian), giao hàng cho địa điểm 3 và 4.
- Di chuyển về nhà kho (mất 3 đơn vị thời gian), chất kiện hàng của địa điểm 2 và 5 lên xe tải.
- Di chuyển đến tọa độ -2 (mất 2 đơn vị thời gian), giao hàng cho địa điểm 2 và 5.
- Di chuyển về nhà kho (mất 2 đơn vị thời gian), chất kiện hàng của địa điểm 1 lên xe tải.
- Di chuyển đến tọa độ -4 (mất 4 đơn vị thời gian), giao hàng cho địa điểm 1.
- Di chuyển về nhà kho (mất 4 đơn vị thời gian).

Tổng thời gian là 3 + 3 + 2 + 2 + 4 + 4 = 18.

Ở ví dụ thứ hai, một lộ trình để thực hiện việc giao hàng với thời gian tối thiểu như sau:
- Chất toàn bộ các kiện hàng lên xe tải.
- Di chuyển lần lượt đến tọa độ -2 và -4 (mất 4 đơn vị thời gian), giao hàng cho các địa điểm 1, 2 và 5.
- Di chuyển lần lượt đến tọa độ 1 và 3 (mất 7 đơn vị thời gian), giao hàng cho các địa điểm 3 và 4.
- Di chuyển về nhà kho (mất 3 đơn vị thời gian).

Tổng thời gian là 4 + 7 + 3 = 14.

## Chấm điểm

- Subtask 1 (30% số test): m = 1
- Subtask 2 (30% số test): m = n
- Subtask 3 (40% số test): Không có ràng buộc gì thêm