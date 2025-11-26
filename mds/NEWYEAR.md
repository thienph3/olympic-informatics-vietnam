# Beginner Free Contest 39 - NEWYEAR

**Thể loại:** Simulation  
**Độ khó:** 400

## Đề bài

Hôm nay là ngày đầu tiên của năm 2022, hoạt động tại các cửa hàng tiện lợi và siêu thị rất tấp nập. Tường là một nhân viên của cửa hàng, hôm nay cửa hàng gặp một vị khách thú vị.

Nếu Tường có thể trả lời câu đố của vị khách này chính xác, cô bé sẽ được mừng tuổi từ người này.

Vị khách cho Tường một mảng a có n phần tử bất kì. Ở mỗi bước chọn ra một số x (x = aₙ). Sau đó mảng a bị chia làm hai phần: trái và phải. Phần bên trái bao gồm các phần tử không vượt quá x (≤ x) trong khi đó phần bên phải sẽ là những số lớn hơn hẳn x (> x). Thứ tự của mỗi phần tử trong mỗi phần được giữ nguyên như trong mảng ban đầu.

Ví dụ, với mảng [2, 4, 1, 5, 3] sẽ chọn x = 3, sau đó mảng trở thành [2, 1, 3], [4, 5] -> [2, 1, 3, 4, 5]

Vị khách cho biết sau một số lần nhất định mảng sẽ không thay đổi. Tường được hỏi rằng số bước biến đổi ít nhất là bao nhiêu để sau đó mảng được giữ nguyên.

## Dữ liệu

- Dòng thứ nhất là số tự nhiên n (1 ≤ n ≤ 10⁵)
- Dòng thứ hai chứa n số nguyên a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 10⁹)

## Kết quả

In ra một số k là số bước biến đổi ít nhất để mảng không thay đổi.

## Ví dụ

**Input:**
```
5
2 4 1 5 3
```

**Output:**
```
1
```

**Input:**
```
5
1 1 1 1 1
```

**Output:**
```
0
```

## Giải thích

Ví dụ thứ nhất đã được trình bày trong đề, sau khi chọn x = 3 thì mảng không thay đổi nên số lần biến đổi là 1.