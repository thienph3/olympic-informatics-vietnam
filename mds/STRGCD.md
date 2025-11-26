# BeginnerFreeContest 52 - STRGCD

**Thể loại:** String  
**Độ khó:** 500

## Đề bài

Với hai xâu s và t, ta định nghĩa xâu t chia hết xâu s khi và chỉ khi s = t + ··· + t. Nói cách khác, ta có thể tạo nên xâu s bằng cách ghép một hoặc nhiều bản sao của xâu t lại với nhau.

Cho hai xâu A và B chỉ gồm các chữ cái tiếng Anh viết thường. Tìm xâu x dài nhất chia hết cả A và B.

## Dữ liệu

- Dòng đầu tiên gồm xâu A (1 ≤ |A| ≤ 10⁵).
- Dòng thứ hai gồm xâu B (1 ≤ |B| ≤ 10⁵).
- A và B chỉ gồm các chữ cái tiếng Anh viết thường.

## Kết quả

- Nếu không tồn tại xâu x thỏa mãn, in ra "NOTFOUND" (không có dấu nháy kép).
- Ngược lại, in ra xâu x.

## Ví dụ

**Input:**
```
abcabc
ababab
```

**Output:**
```
ab
```

**Input:**
```
abcabcab
freecontest
```

**Output:**
```
NOTFOUND
```

## Chấm điểm

- Subtask 1 (20% số test): |A|, |B| ≤ 10²
- Subtask 2 (80% số test): Không có ràng buộc gì thêm