# Beginner Free Contest 55 - FIBOXOR

**Thể loại:** Math  
**Độ khó:** 400

## Đề bài

Sau buổi học môn toán ở trường, Anh được biết đến dãy số Fibonacci. Cụ thể dãy số được xây dựng như thế này:

- F(0) = 1
- F(1) = 1  
- F(n) = F(n-1) + F(n-2) với n > 1

Cảm thấy dãy số rất thú vị, anh muốn thay đổi dãy số một chút. Anh muốn thay vì sử dụng phép toán cộng sẽ sử dụng phép toán XOR. Cụ thể, anh sẽ chọn ra 2 số nguyên dương a, b và xây dựng một dãy Fibonacci của mình như sau:

- F(0) = a
- F(1) = b
- F(n) = F(n-1) ⊕ F(n-2) với n > 1

Anh nghĩ, với một số n bất kì, anh có thể biết kết quả chính xác của F(n) là bao nhiêu hay không?

## Dữ liệu

Dữ liệu bao gồm 3 số nguyên a, b, n (1 ≤ a, b, n ≤ 10⁹).

## Kết quả

Giá trị F(n) theo hàm mà Anh thay đổi.

## Ví dụ

**Input:**
```
1 2 2
```

**Output:**
```
3
```

**Input:**
```
325 265 1231232
```

**Output:**
```
76
```

**Input:**
```
4 5 1
```

**Output:**
```
5
```