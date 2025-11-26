# BeginnerFreeContest 54 - STRCNT

**Thể loại:** String  
**Độ khó:** 550

## Đề bài

Cho hai xâu S và T, bạn hãy đếm số lần xuất hiện của hoán vị xâu T trong xâu S.

Ví dụ:
- Với S = "aabcaba" và T = "aab", ta có các hoán vị của T là các xâu "aab", "aba", "baa". Như vậy, hoán vị của xâu T xuất hiện 2 lần trong xâu S tại vị trí 0 và 4.
- Với S = "aaaaa" và T = "aa", có 4 lần xâu T xuất hiện trong xâu S tại các vị trí 0, 1, 2 và 3.

## Dữ liệu

Dòng đầu tiên gồm xâu S (1 ≤ |S| ≤ 10⁶) chỉ chứa các ký tự in thường trong bảng chữ cái (từ a đến z).
Dòng thứ hai gồm xâu T (1 ≤ |T| ≤ |S|) chỉ chứa các ký tự in thường trong bảng chữ cái (từ a đến z).

Lưu ý, ký hiệu |S| là độ dài của xâu S ("abcde" có độ dài là 5).

## Kết quả

In ra một số nguyên duy nhất là số lượng lần hoán vị của T xuất hiện trong S.

## Ví dụ

**Input:**
```
aabcaba
aab
```

**Output:**
```
2
```

**Input:**
```
aaaaaaa
aa
```

**Output:**
```
4
```

**Input:**
```
vkxjzvdkzjxvkabcdvkxjz
abcd
```

**Output:**
```
4
```

## Chấm điểm

- Subtask 1 (10% số test): |T| = 1
- Subtask 2 (10% số test): |S| ≤ 3000, và tất cả ký tự trong T đều bằng nhau
- Subtask 3 (20% số test): Tất cả các ký tự trong T đều bằng nhau
- Subtask 4 (60% số test): Không có ràng buộc gì thêm.