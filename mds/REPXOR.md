# BeginnerFreeContest 54 - REPXOR

**Thể loại:** Bit Manipulation  
**Độ khó:** 600

## Đề bài

Anh có một dãy số gồm N phần tử, bao gồm a₁, a₂, ..., aₙ, aᵢ ≤ aᵢ₊₁ ∀ i < N. Đây là một dãy không giảm, và Anh thì không thích việc đó.

Anh có thể thay đổi dãy số này bằng cách chọn 2 số liên tiếp để loại khỏi dãy, và thay vào đó một số mới có giá trị bằng XOR của giá trị 2 số được chọn. Cụ thể, anh sẽ chọn một 2 số x, y liền kề trong dãy, xóa khỏi dãy và chèn vào vị trí đó giá trị là x ⊕ y, trong đó ⊕ là phép toán XOR. Thao tác này được gọi là REPXOR.

Anh muốn dãy số của mình không còn là một dãy không giảm nữa, và anh có thể thực hiện nhiều lần thao tác REPXOR. Tuy nhiên, anh muốn thực hiện ít lần REPXOR nhất có thể. Hãy giúp Anh tìm ra số lần thực hiện REPXOR ít nhất để dãy số không còn là dãy không giảm.

## Dữ liệu

Dữ liệu đầu vào bao gồm:
- Dòng đầu bao gồm 1 số nguyên dương N trong đó N là độ lớn của dãy. (1 ≤ N ≤ 5 × 10⁵).
- Dòng tiếp theo, bao gồm N số nguyên dương a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 10⁹, aᵢ ≤ aᵢ₊₁ ∀ i).

## Kết quả

Gồm một số nguyên duy nhất là số thao tác mà Anh thực hiện ít nhất để dãy không còn là dãy không giảm. Nếu như không có cách nào để thay đổi thì xuất -1.

## Ví dụ

**Input:**
```
4
2 5 6 8
```

**Output:**
```
1
```

**Input:**
```
3
1 2 3
```

**Output:**
```
-1
```

**Input:**
```
5
1 2 4 6 20
```

**Output:**
```
2
```

## Giải thích

- Ở ví dụ thứ nhất, Anh có thể chọn 2, 5 để thực hiện REPXOR, dãy mới được tạo thành là 7, 6, 8.
- Ở ví dụ thứ hai, các dãy có thể tạo ra từ việc thực hiện các thao tác REPXOR là 1, 2, 3, 3, 3, 1, 1, 0.
- Ở ví dụ thứ ba, đầu tiên anh chọn 1, 2 để thực hiện REPXOR, dãy mới được tạo thành là 3, 4, 6, 20. Sau đó, Anh thực hiện REPXOR cho 2 số là 3, 4 và tạo được một dãy mới là 7, 6, 20. Anh chỉ cần dùng 2 thao tác để khiến dãy không còn là dãy không giảm. Đây cũng là cách tốt nhất.