# Beginner Free Contest 51 - COLORBALL

**Thể loại:** Simulation  
**Độ khó:** 500

## Đề bài

An và Bình cùng tham gia một lễ hội do trường tổ chức. Dạo quanh khắp các gian hàng thì họ bỗng thấy một trò chơi đố khá vô cùng thú vị, đó chính là trò "Ném bi màu".

Trò chơi vô cùng đơn giản như sau:
- Bảng là một lưới cảm biến chứa các ô vuông màu trắng, có kích thước là n dòng và m cột.
- An sẽ là người ném bi đỏ và Bình sẽ ném bi xanh.
- Sau khi ném viên bi trúng ô ở hàng i và cột j thì ô đó và các ô có chung đỉnh với ô (i, j) sẽ được cài đặt lại màu:
  - Nếu như ô được cài đặt lại có màu trắng thì sẽ trở thành màu của người ném.
  - Nếu như ô được cài đặt lại có màu của bản thân thì sẽ giữ nguyên như cũ.
  - Nếu như ô được cài đặt lại có màu của đối thủ thì sẽ trở lại thành màu trắng.
- Mỗi vòng đấu gồm 2 lượt ném, lượt đầu là An và lượt sau là Bình. Trò chơi sẽ kết thúc sau k vòng đấu.

## Dữ liệu

- Dòng đầu tiên chứa 3 số nguyên m, n, k (1 ≤ m, n, k ≤ 10³) lần lượt là số dòng, số cột của bảng và số vòng đấu.
- 2·k dòng tiếp theo chứa 2 số nguyên i, j (1 ≤ i ≤ n, 1 ≤ j ≤ m) lần lượt là tọa độ dòng và cột của viên bi được ném.

## Kết quả

In ra 2 số nguyên là số ô màu đỏ và số ô màu xanh.

## Ví dụ

**Input:**
```
4 4 1
2 2
3 3
```

**Output:**
```
5 4
```