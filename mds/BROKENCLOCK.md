# Beginner Free Contest 42 - BROKENCLOCK

**Thể loại:** Implementation  
**Độ khó:** 350

## Đề bài

Tổ chức FC có một chiếc đồng hồ bị hỏng. Như các bạn đã biết, đồng hồ có 2 loại:

- Đồng hồ loại 12: số chỉ giờ nằm trong khoảng từ 1 tới 12
- Đồng hồ loại 24: số chỉ giờ nằm trong khoảng từ 0 tới 23

Số chỉ phút của cả 2 loại đồng hồ đều nằm trong khoảng từ 0 tới 59.

Do nhân viên của tổ chức quá lười để sửa đồng hồ, nên tổ chức đã thuê bạn sửa đồng hồ với yêu cầu như sau:

Họ cho bạn biết đồng hồ là loại gì, và giờ mà đồng hồ đang hiển thị. Họ yêu cầu bạn thay đổi ít chữ số nhất để giờ được hiển thị sau khi sửa đúng với format của đồng hồ.

## Dữ liệu

- Dòng thứ nhất ghi loại đồng hồ (12 hoặc 24)
- Dòng thứ hai ghi giờ đang hiển thị với format HH:MM:
  - 2 ký tự HH biểu thị giờ
  - 2 ký tự MM biểu thị phút

## Kết quả

In ra giờ được hiển thị sau khi đã sửa.

## Ví dụ

**Input:**
```
24
17:30
```

**Output:**
```
17:30
```

**Input:**
```
12
17:30
```

**Output:**
```
07:30
```

**Input:**
```
24
99:99
```

**Output:**
```
09:09
```

## Chấm điểm

Không có Subtask cụ thể.