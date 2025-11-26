# Beginner Free Contest 46 - FENCES

**Thể loại:** Math  
**Độ khó:** 200

## Đề bài

Một khu đất hình chữ nhật kích thước m × n, gồm m hàng, mỗi hàng gồm n ô vuông độ dài cạnh là 1. Người ta cần làm hàng rào để ngăn cách từng ô vuông riêng biệt. Đường biên xung quanh khu đất cũng cần được rào lại.

Cho biết m và n. Hãy tính tổng độ dài cần rào (độ dày hàng rào là không đáng kể).

## Dữ liệu

Gồm một dòng duy nhất chứa hai số nguyên dương m và n (1 ≤ m, n ≤ 10⁴).

## Kết quả

In ra một số duy nhất là tổng độ dài cần rào.

## Ví dụ

**Input:**
```
2 3
```

**Output:**
```
17
```

## Giải thích

Hình minh họa khu đất với kích thước m = 2, n = 3 có tổng độ dài cần rào là 17 (3 hàng rào ngang độ dài 3 và 4 hàng rào dọc độ dài 2).

```
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
```

Tổng độ dài: 3×3 + 4×2 = 9 + 8 = 17.