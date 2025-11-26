# Beginner Free Contest 48 - FALLFILL

**Thể loại:** Dynamic Programming  
**Độ khó:** 700

## Đề bài

Được một ngày chủ nhật thoải mái không bài tập, không việc nhà, Fuso đắm mình vào tự a game 2D mang tên PaToWi. Nhân vật của Fuso ban đầu đứng ở vị trí (0, 0) và cần vượt mọi chướng ngại vật để tới vị trí (n, 0) chính là nơi chứa đựng rương kho báu.

Chướng ngại vật của màn chơi hôm nay chính là n cột đánh số từ 1 đến n với cột thứ i có chiều cao hi, tức là một hình chữ nhật có góc trái dưới ở tọa độ (i-1, 0) và góc phải trên ở tọa độ (i, hi).

Trước khi bắt đầu trò chơi, Fuso cần phải qua một bước thay đổi địa hình bằng cách tiêu f coin, sau đó chọn 1 cột i bất kỳ và thả một viên gạch từ trên trời xuống cột đó, và nâng chiều cao hi lên một đơn vị. Lưu ý có thể thực hiện thao tác này số lần tùy thích (có thể bằng 0).

Khi bắt đầu Fuso có 3 thao tác di chuyển là:
- u: trèo lên từ vị trí hiện tại là (x, y) đến vị trí (x, y+1) với tiêu hao thể lực là a.
- w: đi bộ từ vị trí hiện tại là (x, y) đến vị trí (x+1, y) với tiêu hao thể lực là b.
- d: leo xuống từ vị trí hiện tại là (x, y) đến vị trí (x, y-1) với tiêu hao thể lực là c.

Là một rich kid chính hiệu, Fuso không ngại chi coin để nhân vật của mình tiêu hao thể lực tối thiểu. Tuy nhiên trong trường hợp có nhiều phương án tối ưu, Fuso sẽ chọn cách tiêu xài coin ít nhất có thể.

## Dữ liệu

- Dòng đầu tiên chứa duy nhất 1 số nguyên n (1 ≤ n ≤ 10⁶) là số lượng cột.
- Dòng thứ 2 chứa n số nguyên, với số thứ i là hi (0 ≤ hi ≤ 10⁹) là chiều cao cột thứ i.
- Dòng thứ 3 chứa 4 số nguyên a, b, c, f (1 ≤ a, b, c, f ≤ 10⁶).

## Kết quả

In ra 2 số nguyên là thể lực nhân vật tiêu hao ít nhất và số lượng coin tối thiểu Fuso phải chi ra để đạt được điều đó.

## Ví dụ

**Input:**
```
5
1 2 2 1 1
2 1 1 4
```

**Output:**
```
18 0
```

**Input:**
```
7
1 2 3 4 18 14 0
2 1 1 4
```

**Output:**
```
22 1
```

## Giải thích

- Ở ví dụ thứ nhất:
  - Tiêu hao thể lực của nhân vật khi chưa thay đổi địa hình là 22 (Hình 1).
  - Tiêu hao thể lực của nhân vật khi đã tối ưu là 18 (Hình 2).

- Ở ví dụ thứ hai:
  - Tiêu hao thể lực của nhân vật khi chưa thay đổi địa hình cũng như là đã tối ưu là 14 (nhân vật chỉ việc đi thẳng từ vị trí (0, 0) đến vị trí (7, 0)).

## Chấm điểm

- Subtask 1 (40% số test): n ≤ 10 và hi ≤ 4
- Subtask 2 (60% số test): Không có ràng buộc gì thêm