# Beginner Free Contest 38 - MAXGRID

**Thể loại:** Graph  
**Độ khó:** 600

## Đề bài

Anh có một bàn cờ ma thuật hình chữ nhật N hàng, M cột, giao giữa hàng thứ i và cột thứ j là ô (i, j). Thay vì những quân cờ, với mỗi ô (i, j), bàn cờ sẽ tạo ra một giá trị Aᵢ,ⱼ tương ứng. Anh muốn bán bàn cờ này đi, với giá tiền chính là tổng các giá trị các ô trên bàn cờ.

Tuy nhiên, suy nghĩ lại, cậu thấy nếu không thay đổi gì, bàn cờ có thể sẽ không được giá trị cao. May thay, Anh là một pháp sư, và anh có thể thay đổi giá trị của các ô của bàn cờ, nhưng vì chỉ học pháp thuật nửa vời, cậu không thể thay đổi các con số theo ý mình.

Cụ thể, phép thuật mà Anh học được không đủ để thay đổi giá trị của một ô cụ thể, mà chỉ có thể thay đổi dấu của giá trị 2 ô kề nhau (có một cạnh chung). Tuy hạn chế về kỹ thuật, nhưng Anh lại rất dư "mana", cậu có thể thực hiện phép thuật này bao nhiêu lần cũng được, thậm chí nếu không cần thiết, cậu có thể không thực hiện.

Anh muốn biết giá trị lớn nhất mà cậu có thể bán bàn cờ này đi là bao nhiêu?

## Dữ liệu

- Dòng đầu chứa 2 số nguyên N, M tương ứng là số hàng và số cột của bàn cờ. (1 ≤ N × M ≤ 10⁶)
- N dòng sau, mỗi dòng gồm M số nguyên, số thứ j của dòng thứ i là Aᵢ,ⱼ. (-10⁴ ≤ Aᵢ,ⱼ ≤ 10⁴)

## Kết quả

Gồm một dòng duy nhất là tổng giá trị lớn nhất của bàn cờ có thể đạt được sau khi Anh thực hiện các thay đổi.

## Ví dụ

**Input:**
```
2 2
1 -1
1 1
```

**Output:**
```
2
```

**Input:**
```
3 3
-3 -2 3
2 -2 1
1 2 3
```

**Output:**
```
17
```

## Giải thích

- Ở ví dụ 1, dù thực hiện bao nhiêu lần thay đổi thì vẫn tồn tại một ô có giá trị là -1.
- Ở ví dụ 2, ta có thể thực hiện thay đổi giá trị ô (1, 1) với ô (1, 2) và giá trị ô (2, 2) và ô (2, 3). Tổng lúc này là 17. Kết quả này là lớn nhất có thể.