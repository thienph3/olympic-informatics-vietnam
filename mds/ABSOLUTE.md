# Beginner Free Contest 47 - ABSOLUTE

**Thể loại:** Game Theory  
**Độ khó:** 650

## Đề bài

Long và Vũ được cho một bộ bài gồm N lá bài, giá trị của lá bài được thể hiện bởi một số được ghi trên lá bài đó, số được viết trên lá bài thứ i là ai. Long và Vũ nghĩ ra một trò chơi có luật như sau:

Ban đầu hai người được cho thêm hai lá bài (không nằm trong N lá bài được cho), lá bài trên tay Long có giá trị là Z, trên tay Vũ có giá trị là W. Long là người chơi trước, hai người chơi lần lượt, với mỗi lượt một trong hai người có thể thực hiện hành động như sau:

- Rút một số lá bài tùy thích từ trên đầu bộ bài, sau đó bỏ tất cả các lá rút ra và chỉ giữ lại lá bài ở cuối, thay đổi lá bài đang cầm trong tay bằng lá bài được giữ lại đó. Như vậy có thể thấy sau mỗi lượt, cả hai đều chỉ luôn cầm một lá bài.

Trò chơi kết thúc khi không còn lá bài nào có thể được rút nữa. Điểm của trò chơi được tính bằng giá trị tuyệt đối của chênh lệch giá trị giữa hai lá bài còn lại trên tay.

Giả sử ở mỗi lượt Long luôn biết cách chơi sao cho số điểm cuối cùng là cao nhất có thể, còn Vũ thì luôn biết cách chơi sao cho số điểm cuối cùng là thấp nhất có thể, hãy tính số điểm cuối cùng của trò chơi.

## Dữ liệu

- Dòng thứ nhất ghi ba số nguyên N, Z, W - lần lượt thể hiện số lá bài và giá trị của hai lá bài ban đầu mà hai người có.
- Dòng thứ hai gồm N số nguyên ai với ai thể hiện giá trị của lá bài thứ i.

**Ràng buộc:**
- 1 ≤ N ≤ 2000
- 1 ≤ Z, W, ai ≤ 10⁹
- Tất cả dữ liệu được cho là số nguyên

## Kết quả

In ra số điểm cuối cùng.

## Ví dụ

**Input:**
```
3 15 16
30 15 20
```

**Output:**
```
15
```

**Giải thích:**

Ở ví dụ đầu tiên, Long rút 2 lá bài đầu tiên, và Vũ rút lá bài cuối cùng, như vậy kết thúc trò chơi trên tay hai người có 2 lá bài có giá trị lần lượt là 30 và 15, số điểm cuối cùng là 15.