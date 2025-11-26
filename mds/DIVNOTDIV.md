# Beginner Free Contest 52 - DIVNOTDIV

**Thể loại:** Math  
**Độ khó:** 500

## Đề bài

Sau khi học xong bài về phép chia hết, thầy có ra cho lớp t câu đố, mỗi câu đố bao gồm:

- Cho 3 số nguyên dương a, b và n.
- Hãy tìm một số nguyên dương m nhỏ nhất nhưng không nhỏ hơn n sao cho m chia hết cho a và m không chia hết cho b.

Nếu không có số nguyên nào thỏa mãn thì gán m = -1.

## Dữ liệu

- Dòng đầu tiên gồm số nguyên dương t (t ≤ 10⁵).
- t dòng tiếp theo, dòng thứ i chứa 3 số nguyên dương aᵢ, bᵢ và nᵢ (aᵢ, bᵢ ≤ 10⁹; nᵢ ≤ 10¹⁸).

## Kết quả

In ra t số nguyên thỏa đề bài, mᵢ trên dòng thứ i.

## Ví dụ

**Input:**
```
2
2 3 7
8 4 2
```

**Output:**
```
8
-1
```

**Input:**
```
3
1 3 3
1 4 6
10 25 82
```

**Output:**
```
4
6
90
```