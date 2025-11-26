# Beginner Free Contest 47 - FIVE

**Thể loại:** Implementation  
**Độ khó:** 200

## Đề bài

Bé A đang học đếm tới 5. Một số bạn chắc cũng nghe tới trường mầm non SuperKids, với những mầm non cực kỳ siêu phẩm, và bài thi đầu vào cực gắt. Vì để luyện thi cho bé An, mẹ thường hay ra những bài toán rất dễ.

Ví dụ như, mẹ cho bé vài chữ số khác nhau nằm trong khoảng từ 1 tới 5. Bạn hãy cho biết số tốt nhất bé có thể tạo thành bằng cách ghép các chữ số lại với nhau là bao nhiêu?

## Dữ liệu

Gồm một dòng duy nhất chứa năm số a₁, a₂, a₃, a₄, a₅ lần lượt là trạng thái xuất hiện của các số 1, 2, 3, 4 và 5.

aᵢ = 1 tức là mẹ có cho bé một chữ số i, và ngược lại aᵢ = 0 tức là mẹ không cho bé số i.

Dữ liệu đảm bảo có ít nhất một số 1.

## Kết quả

In ra 1 số duy nhất là số tốt nhất bé A có thể tạo bằng cách ghép các chữ số đã cho.

## Ví dụ

**Input:**
```
1 0 0 1 0
```

**Output:**
```
41
```

**Input:**
```
1 1 1 1 1
```

**Output:**
```
54321
```

## Giải thích

Ở test ví dụ đầu, có 2 chữ số 1 và 4. Số tốt nhất có thể tạo là 41.

Ở test ví dụ sau, cả 5 chữ số đều xuất hiện. Số tốt nhất có thể tạo là 54321.