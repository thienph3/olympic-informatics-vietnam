# Beginner Free Contest 52 - FINDBRACSEQ

**Thể loại:** Dynamic Programming  
**Độ khó:** 600

## Đề bài

Một xâu được gọi là dãy ngoặc đúng nếu nó thỏa mãn một trong ba điều kiện sau:

- Nếu S là xâu rỗng, S là dãy ngoặc đúng.
- Nếu S là dãy ngoặc đúng, (S) cũng là dãy ngoặc đúng.
- Nếu A và B là hai dãy ngoặc đúng, việc ghép hai dãy lại thành AB cũng tạo ra một dãy ngoặc đúng.

Sau đây là ví dụ của một số dãy ngoặc đúng: "()", "(())()", "((()(())))"

Một dãy con của một xâu S bất kỳ là một xâu có thể được tạo thành bằng cách xóa đi một số ký tự (có thể là không xóa ký tự nào, hoặc xóa hết tất cả), và ghép các ký tự còn lại vào với nhau theo thứ tự ban đầu.

Ví dụ, "abc" là dãy con của xâu "adbecf", hay "()(" là dãy con của dãy ngoặc "()))((".

Cho một xâu S có độ dài n, nhiệm vụ của bạn là hãy tìm ra dãy con T dài nhất của S sao cho T là một dãy ngoặc đúng.

## Dữ liệu

Gồm một dòng duy nhất chứa xâu S (n ≤ 10⁵). Các ký tự của xâu đều trong nằm trong dãy các ký tự ASCII có thể in được, ngoại trừ ký tự khoảng trắng (mã từ 33 tới 126).

## Kết quả

In ra một dòng là độ dài của dãy con T dài nhất có thể tìm được sao cho T là một dãy ngoặc đúng.

## Điểm số

- Subtask 1 (30%): n ≤ 20
- Subtask 2 (40%): n ≤ 500
- Subtask 3 (30%): n ≤ 10⁵

## Ví dụ

**Input:**
```
(())
```

**Output:**
```
4
```

**Input:**
```
(ab()c()
```

**Output:**
```
4
```

## Giải thích

Ở test ví dụ 1, ta lấy toàn bộ các ký tự trong xâu S.

Ở test ví dụ 2, ta có 3 cách chọn dãy con tốt nhất, đều với độ dài 4. Sau đây là 4 vị trí ký tự trên xâu S của 3 cách chọn đó: (1, 4, 5, 8); (1, 5, 7, 8); (4, 5, 7, 8).