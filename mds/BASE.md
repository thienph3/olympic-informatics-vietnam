# Beginner Free Contest 41 - BASE

**Thể loại:** Math  
**Độ khó:** 600

## Đề bài

Một ngày nọ, sau khi Tus thi VOI xong thì Tus nhận ra mình quá gà vì không giải được bất kì một bài nào cả. Do vậy, Tus quyết định học mỗi ngày 180 phút. Quá trình tự học của Tus rất vất vả nên để Tus đỡ buồn thì anh Qa đã đến trò chuyện, tán gẫu cùng Tus.

Tus là một người không muốn lãng phí thời gian cho nên Tus chỉ muốn nghe những câu chuyện bổ ích. Biết được điều đó, anh Qa đã kể cho Tus nghe sự tích về những con số. Nhưng không may Tus chỉ biết các số ở hệ cơ số 10. Vì thế để Tus hiểu được câu chuyện anh Qa đã tốn rất nhiều công sức giảng lại cho Tus về khái niệm và các ví dụ về các hệ cơ số. Thế nhưng trong lúc đang lấy ví dụ cho Tus thì anh Qa nhận được cuộc gọi từ Zun. Thế là anh Qa đành phải đi chơi để Tus lại tự hiểu. Trước khi anh Qa rời đi anh đã viết ra giấy số n trong hệ cơ số 10 và số n trong hệ cơ số X nào đó. Vì anh Qa bận việc gấp nên chưa kịp bảo Tus hệ cơ số anh dùng là hệ nào. Tus đành nhờ các bạn giúp nhé!

## Dữ liệu

- Dòng đầu tiên là 2 số nguyên n, m (0 ≤ n ≤ 10¹⁸, 1 ≤ m ≤ 500000) - số được viết trong hệ cơ số 10 và độ dài của số đó sau khi chuyển sang hệ cơ số mới.
- Dòng thứ hai gồm m số nguyên ai (0 ≤ ai ≤ 10¹⁸, 0 ≤ i < m) - digit thứ i tính từ phải sang trái của số n sau khi chuyển thành hệ cơ số mới.

## Kết quả

In ra 1 số nguyên duy nhất là hệ cơ số mà anh Qa đã sử dụng. Nếu có nhiều hệ cơ số X thỏa thì xuất ra X nhỏ nhất có thể. Còn nếu không tồn tại X, in ra -1.

## Ví dụ

**Input:**
```
2532 3
4 14 9
```

**Output:**
```
16
```

**Subtask:**
- Subtask 1: 80% số tests đảm bảo 1 ≤ X ≤ 16 và 1 ≤ n ≤ 10⁴
- Subtask 2: 20% còn lại không có điều kiện gì thêm