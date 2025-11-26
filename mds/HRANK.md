# Beginner Free Contest 51 - HRANK

**Thể loại:** Array  
**Độ khó:** 450

## Đề bài

Tại buổi tựu trường đầu năm, một lớp gồm n học sinh đứng xếp thành một hàng dọc quay mặt về phía trước để nghe thông báo. Các học sinh đứng sau có thể nhìn thấy được những người đứng trước mình, ngược lại thì không, người đứng đầu hàng đương nhiên không thể thấy được những người xếp hàng sau mình.

Các học sinh thường thích so kè nhau về chiều cao nên hay nhìn xem những ai cao hơn mình để sắp thứ hạng chiều cao trong hàng. Tuy nhiên, điều này hơi khó khăn vì mỗi người chỉ nhìn thấy được số người đứng đằng trước mà cao hơn mình chứ không biết được những người đứng đằng sau.

Bạn hãy giúp từng học sinh biết được mình cao thứ hạng mấy trong hàng. Không có 2 học sinh nào có cùng chiều cao.

**Yêu cầu:** Cho dãy aᵢ ứng với số người cao hơn mình mà học sinh đứng ở vị trí thứ i (2 ≤ i ≤ n) nhìn thấy được, hãy cho biết chiều cao của học sinh đứng ở vị trí i xếp thứ hạng mấy trong hàng.

## Dữ liệu

- Dòng đầu tiên chứa số nguyên n, q (n ≤ 10³, 1 ≤ q ≤ 10⁶) - số lượng học sinh và số lượng truy vấn
- Dòng thứ hai chứa dãy gồm n - 1 số nguyên: a₂, ..., aₙ (aᵢ ≥ 0).
- Mỗi dòng trong q dòng tiếp theo chứa số nguyên dương i (1 ≤ i ≤ n) ứng với truy vấn thứ hạng chiều cao của học sinh đứng ở vị trí i trong hàng.

## Kết quả

In ra q dòng, dòng thứ i trả lời truy vấn thứ i.

## Ví dụ

**Input:**
```
7 4
1 0 3 0 2 1
1
4
6
1
```

**Output:**
```
7
3
1
7
```