# BeginnerFreeContest 40 - POSSIBLE

**Thể loại:** Math  
**Độ khó:** 400

## Đề bài

Bạn A được cho một dãy các số từ 1 tới N. A được phép thực hiện một vài phép biến đổi (hoặc không làm gì cả). Ở mỗi phép biến đổi, bạn ấy chọn một số bất kỳ và đặt một dấu trừ phía trước số đó.

Sau khi thực hiện việc này, A tiến hành tính tổng các số vừa biến đổi. Hãy cho biết, A có thể tạo nên tổng bằng S sau biến đổi hay không?

Cũng như việc bạn làm bài tập về nhà, A phải trả lời rất nhiều câu hỏi như trên, mỗi câu hỏi lại có một số N và số S khác nhau. A lười trả lời lắm, mà bạn lại biết code. Bạn hãy giúp A nhé!

## Dữ liệu

- Dòng đầu tiên chứa số T (1 ≤ T ≤ 10⁵) là số lượng câu hỏi.
- T dòng tiếp theo, dòng thứ i lần lượt chứa hai số Nᵢ, Sᵢ biểu thị truy vấn gồm số phần tử của dãy và tổng cần đạt được.

## Kết quả

In ra T dòng, dòng thứ i là đáp án cho câu hỏi thứ i. In ra "YES" (không bao gồm ngoặc kép) có thể biến đổi ra tổng Sᵢ, còn không thì in ra "NO" (không bao gồm ngoặc kép).

## Ví dụ

**Input:**
```
2
3 5
12 -48
```

**Output:**
```
NO
YES
```

## Giới hạn

- |S| ≤ 10¹⁸
- 20% số điểm có dữ liệu thỏa mãn T ≤ 10², N ≤ 20
- 30% số điểm có dữ liệu thỏa mãn T ≤ 10³, N ≤ 10³
- 50% số điểm có dữ liệu thỏa mãn T ≤ 10⁵, N ≤ 10⁵