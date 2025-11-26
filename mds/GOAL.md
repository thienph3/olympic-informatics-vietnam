# Beginner Free Contest 50 - GOAL

**Thể loại:** Simulation  
**Độ khó:** 350

## Đề bài

Một xưởng máy chuẩn bị đưa vào sản xuất dây chuyền một loại thiết bị nhắm bắn tự động. Trước đó họ phải khảo nghiệm xem mẫu thử nghiệm này bắn được bao nhiêu điểm trong n phát bắn đầu tiên.

Biết rằng cách tính điểm như sau:
- Nếu bắn trúng thì sẽ được tính 1 điểm, ngược lại thì được 0 điểm.
- Sau 9 phát bắn thì lần bắn tiếp theo nếu trúng sẽ được thêm 2 điểm thưởng.

Những người tiến hành khảo nghiệm nhận ra rằng máy sau khi bắn trúng 14 phát sẽ bị lệch quỹ đạo và chắc chắn hụt ở lần bắn tiếp theo, sau đó nó sẽ tự thiết lập lại để về lại đúng quỹ đạo ban đầu.

Bạn hãy tính xem trong n phát bắn đầu tiên chiếc máy này sẽ ghi được cho mình bao nhiêu điểm.

## Dữ liệu

Chứa duy nhất một số nguyên dương n (n ≤ 10⁹).

## Kết quả

In ra số điểm mà chiếc máy này đạt được.

## Ví dụ

**Input:**
```
5
```

**Output:**
```
5
```

**Input:**
```
10
```

**Output:**
```
12
```

**Input:**
```
15
```

**Output:**
```
16
```

## Giải thích

- Ở ví dụ thứ nhất, chiếc máy bắn trúng 5 phát bắn nên được 5 điểm.
- Ở ví dụ thứ hai, chiếc máy bắn trúng 10 phát bắn nên được 10 điểm. Và ở phát bắn thứ 10 chiếc máy bắn trúng nên đã ghi thêm được 2 điểm.
- Ở ví dụ thứ ba, chiếc máy chỉ bắn trúng 14 phát bắn (hụt ở phát bắn thứ 15) nên được 14 điểm. Và ở phát bắn thứ 10 chiếc máy này bắn trúng nên đã ghi thêm được 2 điểm.

## Chấm điểm

- Subtask 1 (50% số test): n ≤ 10⁶
- Subtask 2 (50% số test): Không có ràng buộc gì thêm