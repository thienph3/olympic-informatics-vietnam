# Beginner Free Contest 43 - ICPC

**Thể loại:** Greedy  
**Độ khó:** 400

## Đề bài

Một trường đại học may mắn kiếm được 3 bạn xuất sắc nhất từ trước tới nay lập thành một đội DreamTeam tham dự ICPC năm 3000. Đội tuyển này rất kỳ khôi, đấm đầu trúng đó, không hề có penalty. Mỗi tội là đội đánh không có chiến thuật, lại thêm cái tôi cao nên toàn làm bài khó trước, dẫn tới việc ranking rất thấp.

Luật thi ICPC khi đó như sau:
- Có n bài toán với các độ khó khác nhau với thời gian làm bài là l phút.
- Bài nộp của một bài được tính là đã giải thành công, hay AC(cepted), nếu bài đó vượt qua các test case của bài đó.
- Penalty của một bài bằng thời gian AC bài đó lần đầu tiên, cộng với 20 phút cho mỗi lần nộp sai trước đó. Lưu ý: nếu đội không AC bài đó, sẽ không bị tính penalty.
- Tất nhiên, khi hết thời gian làm bài, các đội bỏ tay ra khỏi bàn phím và ngừng làm bài ngay lập tức.
- Tổng penalty của một đội bằng tổng penalty của cả n bài đó.
- Đội có thứ hạng cao hơn là đội giải được nhiều bài hơn. Trong trường hợp hai đội giải cùng số bài, đội có penalty thấp hơn là đội có thứ hạng cao hơn.

Như đã nói ở trên, đội thi này rất giỏi nên không có bài nộp nào làm sai. Biết rằng, ở bài thứ i, tính từ lúc đọc đề đến lúc nộp bài là Aᵢ phút. Đội chỉ có khả năng làm một bài tại một thời điểm nhất định, và thời gian chuyển bài không đáng kể.

Hãy tìm chiến thuật sao cho đội giải được nhiều bài nhất, và penalty thấp nhất.

## Dữ liệu

Gồm 2 dòng:
- Dòng đầu tiên chứa hai số lần lượt là n, l (n ≤ 10⁶, l ≤ 10⁹)
- Dòng sau chứa n số lần lượt là A₁, A₂, A₃, ..., Aₙ (1 ≤ Aᵢ ≤ l).

## Kết quả

In ra 2 số là số lượng bài làm được và tổng penalty của tất cả các bài khi đội sử dụng chiến thuật tối ưu.

## Ví dụ

**Input:**
```
5 10
7 3 2 6 5
```

**Output:**
```
3 17
```

## Giải thích

Làm các bài thứ 3, 2 và 5 theo thứ tự làm bài như vậy.