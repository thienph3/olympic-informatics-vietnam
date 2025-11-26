# BeginnerFreeContest 45 - VENDOR

**Thể loại:** Bit Manipulation  
**Độ khó:** 550

## Đề bài

Từng là sinh viên, ai cũng biết cảnh trường Đại học lúc nào cũng sẽ có một phố đồ ăn vặt. Ta có thể coi dãy phố đó gồm các nhà được đánh số từ 1 tới n, và quán thứ i có độ ngon là ai. Tuy nhiên, không phải món nào ăn với nhau cũng phù hợp, nên khi ăn ở 2 quán khác nhau có thể "triệt tiêu" độ ngon của nhau. Nên độ ngon khi ăn ở quán i và quán j sẽ là ai XOR aj (nếu mọi người không biết về phép XOR, có thể tham khảo ở đây)

Theo nghiên cứu của tổ chức FC thì trung bình sinh viên có kì vọng về độ ngon trải nghiệm được phải lớn hơn K. Tuy nhiên, sinh viên cũng có rất ít thời gian nên chỉ muốn ăn ở một dãy các quán liền nhau trên khu phố.

Độ ngon của việc ăn các quán từ l tới r là: al XOR al+1 XOR ... XOR ar

Vậy nên nhiệm vụ của bạn là đếm xem có bao nhiêu cặp (l, r) sao cho độ ngon trải nghiệm được nếu ăn các quán từ l tới r lớn hơn K.

## Dữ liệu

- Dòng thứ nhất ghi 2 số n và K (1 ≤ n ≤ 10⁵, 0 ≤ K ≤ 2³¹ − 1)
- Dòng thứ hai ghi n số ai (0 ≤ ai ≤ 2³¹ − 1).

## Kết quả

In ra số duy nhất là số cặp (l, r) thoả mãn yêu cầu trong đề bài.

## Ví dụ

**Ví dụ 1:**

**Input:**
```
3 2
1 8 6
```

**Output:**
```
4
```

**Ví dụ 2:**

**Input:**
```
3 10
2 7 6
```

**Output:**
```
0
```

**Ví dụ 3:**

**Input:**
```
4 1
1 4 2 3
```

**Output:**
```
10
```

## Chấm điểm

- Subtask 1 (20% số test): n ≤ 10³
- Subtask 2 (30% số test): K ≤ 10
- Subtask 3 (50% số test): Không có ràng buộc gì thêm