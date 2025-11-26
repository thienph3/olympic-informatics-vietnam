# Beginner Free Contest 44 - BBOX

**Thể loại:** Bit Manipulation  
**Độ khó:** 600

## Đề bài

Trong quá trình giải mã hộp đen của máy bay BFC43, các kỹ thuật viên đã gặp phải một lỗi trong vi mã của một trong các bộ điều khiển, dẫn đến làm sai lệch dữ liệu được ghi. Dựa trên các kết quả có được, người ta biết được rằng thay vì ghi lại dãy số nhị phân s (sₙ₋₁ sₙ₋₂ ... s₂s₁s₀), thì hộp đen ghi lại dãy nhị phân n-bit T là tổng của các dãy nhị phân s lần lượt dịch sang trái:

sₙ₋₁ sₙ₋₂ ... s₂s₁s₀ + sₙ₋₂ sₙ₋₃ ... s₁s₀0 + ... + s₁s₀ ... 000 + s₀0 ... 000

Do bộ ghi chỉ có thể lưu được n bit nên các bit tràn ra ngoài sẽ bị bỏ qua. Ví dụ dãy s ban đầu là 0101, trong hộp đen sẽ ghi lại dãy T là 1011:

0101 + 1010 + 0100 + 1000 = 1011

Bạn hãy giúp các kỹ thuật viên giải mã hộp đen từ dãy nhị phân n-bit T về lại dãy ban đầu s.

## Dữ liệu

- Dòng đầu tiên gồm số nguyên dương n (1 ≤ n ≤ 10⁶), là độ dài của dãy nhị phân.
- Dòng thứ hai gồm xâu nhị phân T độ dài n, chỉ gồm các ký tự 0 hoặc 1.

## Kết quả

Gồm một dòng duy nhất ghi dãy nhị phân ban đầu s.

## Ví dụ

**Input:**
```
4
1011
```

**Output:**
```
0101
```

**Input:**
```
7
1101001
```

**Output:**
```
0010111
```

## Chấm điểm

- Subtask 1 (60%): n ≤ 1000
- Subtask 2 (40%): Không có điều kiện gì thêm