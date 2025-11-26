# Beginner Free Contest 43 - GAME

**Thể loại:** Game Theory  
**Độ khó:** 550

## Đề bài

Một dãy số hợp lệ là dãy số gồm 11 chữ số và số bắt đầu là số 8. Hôm nay, Yasuo rủ Yone chơi một trò chơi. Cho xâu S chứa toàn ký tự số có độ dài N với N là số lẻ. Yasuo sẽ là người đi đầu tiên, tiếp đến là Yone và họ sẽ luân phiên nhau cho đến hết trò chơi. Ở mỗi lượt chơi, người chơi sẽ chọn 1 ký tự trong xâu S và xóa ký tự đó ra khỏi xâu. Trò chơi sẽ kết thúc khi xâu S còn lại có độ dài là 11.

Khi trò chơi kết thúc, nếu S là một dãy số hợp lệ thì Yasuo sẽ thắng. Ngược lại Yone sẽ là người chiến thắng.

Yasuo nhờ bạn xác định xem, liệu có cách nào Yasuo có thể chiến thắng không biết rằng Yone sẽ luôn chọn cách tối ưu để chiến thắng.

## Dữ liệu

- Dòng đầu tiên chứa hai số nguyên N (13 ≤ N < 10⁵) và N là số lẻ.
- Dòng tiếp theo chứa N ký tự số.

## Kết quả

Nếu Yasuo thắng, hãy in ra YES và ngược lại thì in ra NO.

## Ví dụ

**Input:**
```
19
8181818181111111111
```

**Output:**
```
YES
```