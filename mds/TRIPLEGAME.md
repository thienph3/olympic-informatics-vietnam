# BeginnerFreeContest 40 - TRIPLEGAME

**Thể loại:** Game Theory  
**Độ khó:** 700

## Đề bài

Vì đang chán, Đề Mèn đã rủ Mondeus chơi trò chơi sau: Đề Mèn sẽ chọn một số nguyên không âm S và sau đó Mondeus sẽ chọn ra 3 số nguyên không âm (a, b, c) sao cho a + b + c = S.

Mỗi lượt chơi, người chơi sẽ chọn một số nguyên dương k, tăng 1 số trong bộ (a, b, c) lên k và giảm 2 số còn lại đi k và Đề Mèn sẽ là người đi trước.

Một người chơi được xem là thua nếu người chơi đó không thể chọn số nguyên dương k bất kỳ sao cho sau lượt chơi của mình thì min(a, b, c) ≥ 0.

Vì hai bạn rất thông minh nên luôn chơi tối ưu. Biết rằng Đề Mèn chọn số S, các bạn giúp Mondeus đếm xem có bao nhiêu bộ 3 (a, b, c) Mondeus có thể chọn để đánh chiến thắng nhé.

## Dữ liệu

Dòng đầu tiên chứa một số nguyên không âm S. (S ≤ 10⁹)

## Kết quả

In ra số cách chọn bộ 3 (a, b, c). Vì đáp án có thể rất lớn nên hãy in ra phần dư của đáp án với phép chia 10⁹ + 7.

## Ví dụ

**Input:**
```
0
```

**Output:**
```
1
```

**Input:**
```
1
```

**Output:**
```
3
```

**Input:**
```
3
```

**Output:**
```
9
```

## Giải thích

- Với S = 0, chỉ có một bộ thỏa là: (0, 0, 0).
- Với S = 1, có 3 bộ thỏa là: (0, 0, 1), (0, 1, 0), (1, 0, 0).

## Chấm điểm

Bài chỉ có duy nhất một Subtask.