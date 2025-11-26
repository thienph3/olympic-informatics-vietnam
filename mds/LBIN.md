# Beginner Free Contest 41 - LBIN

**Thể loại:** Greedy  
**Độ khó:** 500

## Đề bài

Xâu nhị phân là một chuỗi gồm các ký tự 0 và 1, ví dụ như 010110, 1, 11101. Tèo được Tí cho một xâu nhị phân S không chứa các số 0 ở đầu. Tèo muốn chuyển đổi xâu S này thành một số thập phân bằng máy tính của cậu ta.

Tuy nhiên, do Tèo đã mua máy tính sale 1k của shopee nên máy chỉ có thể chuyển đổi được các số không vượt quá K. Vì vậy Tèo cần xóa đi một vài ký tự trong S (có thể không xóa ký tự nào) mà vẫn giữ nguyên thứ tự của các ký tự còn lại, sao cho biểu diễn thập phân của xâu kết quả không vượt quá K.

Xâu sau khi xóa cũng không được chứa các chữ số 0 ở đầu.

Bạn hãy giúp Tèo tính xem cần phải bỏ đi ít nhất bao nhiêu ký tự trong S để thỏa mãn điều kiện trên.

## Dữ liệu

- Dòng đầu tiên gồm số nguyên dương K (1 ≤ K ≤ 2⁶⁰) là giới hạn của máy tính.
- Dòng thứ hai gồm xâu S (1 ≤ |S| ≤ 60) là xâu mà Tèo nhận được. Đảm bảo xâu S không bắt đầu bằng các chữ số 0.

## Kết quả

Gồm một dòng duy nhất là số ký tự ít nhất cần loại bỏ trong S.

## Ví dụ

**Input:**
```
13
1100101
```

**Output:**
```
3
```

**Input:**
```
13
1111111
```

**Output:**
```
4
```