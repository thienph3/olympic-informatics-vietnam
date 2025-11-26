# Beginner Free Contest 48 - DATE

**Thể loại:** Graph  
**Độ khó:** 400

## Đề bài

Trong thành phố Freecontest có m con đường một chiều nối ngôi nhà a với ngôi nhà b. Naul là một tên trai nam còn cô bạn gái. Biết cô bạn gái thứ i sẽ ở ngôi nhà thứ i. Mặc dù vậy, Naul chỉ thích hẹn hò với cô thứ 1 và cô thứ n nên Naul cần biết có bao nhiêu cách để đi từ nhà cô thứ nhất đến nhà cô thứ n.

Hãy trở thành người bạn tốt của Naul và giúp Naul tìm xem có bao nhiêu cách nhé!

## Dữ liệu

- Dòng thứ nhất ghi hai số nguyên n, m (1 ≤ n ≤ 10⁵, 1 ≤ m ≤ 2 × 10⁵) - lần lượt là số cô bạn gái và số lượng con đường một chiều.
- m dòng tiếp theo, dòng thứ i gồm hai số nguyên a và b (1 ≤ a, b ≤ n) - con đường nối ngôi nhà a với ngôi nhà b.

Dữ liệu luôn đảm bảo không tồn tại cặp chỉ số (i, j) nào mà cả hai cô gái i và j đều có thể đi đến nhà của nhau.

## Kết quả

In ra số cách để đi từ nhà cô thứ nhất đến nhà cô thứ n. Kết quả lấy dư theo module 10⁹ + 7.

## Ví dụ

**Input:**
```
4 5
1 2
2 4
1 3
3 4
```

**Output:**
```
2
```