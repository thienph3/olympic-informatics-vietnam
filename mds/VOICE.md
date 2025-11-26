# BeginnerFreeContest 44 - VOICE

**Thể loại:** Array  
**Độ khó:** 450

## Đề bài

Để phục vụ cho việc nghiên cứu các phương ngữ của tiếng Anh, Việt đã nhờ một số tình nguyện viên từ khắp nơi trên thế giới thu âm một số âm quan trọng trong ngôn ngữ này như âm schwa, âm r, âm θ, ...

Mỗi bản thu âm do các tình nguyện viên gửi đến Việt có thể biểu diễn dưới dạng một dãy số nguyên dương độ dài n, mỗi số nguyên biểu diễn tần số âm thanh tại một thời điểm trong bản thu âm.

Do các tình nguyện viên không có điều kiện để thu âm giọng nói trong điều kiện chuyên nghiệp, các bản thu âm được gửi đến cho Việt thường có lẫn tạp âm và để dễ dàng so sánh các bảng âm, anh cần cắt phần giọng nói trong bản thu âm.

Anh định nghĩa phần giọng nói trong bản thu âm là một dãy con liên tiếp al, al+1, al+2, ..., ar (1 ≤ l ≤ r ≤ n) của dãy a dài nhất thỏa mãn điều kiện tồn tại số nguyên m nằm giữa al và ar (tức l ≤ m ≤ r) sao cho dãy con liên tiếp al, al+1, ..., am là dãy không giảm (tức phần tử sau lớn hơn hoặc bằng phần tử trước) và dãy con liên tiếp am, am+1, ..., ar là dãy không tăng (tức phần tử sau nhỏ hơn hoặc bằng phần tử trước).

Hãy giúp Việt tìm độ dài phần giọng nói trong mỗi bản âm.

## Dữ liệu

- Dòng đầu tiên là một số nguyên n (1 ≤ n ≤ 10³) là độ dài của bản âm.
- Dòng thứ hai gồm n số nguyên a1, a2, ..., an (1 ≤ ai ≤ 10⁹) mô tả tần số âm thanh của một thời điểm của bản thu âm.

## Kết quả

Gồm một dòng chứa một số nguyên là độ dài phần giọng nói của bản âm được cho ở dữ liệu vào.

## Ví dụ

**Ví dụ 1:**

**Input:**
```
11
1 2 3 4 5 5 4 2 1
```

**Output:**
```
9
```

**Ví dụ 2:**

**Input:**
```
5
1 3 4 5 2
```

**Output:**
```
5
```

**Ví dụ 3:**

**Input:**
```
3
4 2 1
```

**Output:**
```
3
```

## Giải thích

Phần giọng nói của bản âm là dãy con 1 2 3 4 5 5 4 2 1 có độ dài 9. Các dãy con khác cũng thỏa mãn các điều kiện được cho ngoại trừ điều kiện dài nhất.