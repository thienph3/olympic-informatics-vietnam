# BeginnerFreeContest 52 - TOYS

**Thể loại:** Greedy  
**Độ khó:** 300

## Đề bài

Cửa hàng FreeContest hiện đang mở cửa và bán rất nhiều món đồ chơi thú vị. Đồ chơi loại i (i ≤ 10⁹) có giá là i đồng.

Tèo đã có sẵn N món đồ chơi a₁, a₂, ..., aₙ, và tất cả đều khác loại. Sắp tới đây là sinh nhật Tèo, và mẹ cho Tèo được chọn quà cho mình, miễn sao tổng giá tiền không vượt quá M đồng.

Tèo được chọn nhiều hơn một món đồ chơi, nhưng Tèo không thích chọn lại món mà mình đã có rồi. Tèo muốn có được nhiều loại đồ chơi nhất có thể bằng tiền của mẹ cho.

Tuy nhiên Tèo chưa học giải thuật và lập trình nên đã nhờ bạn giúp.

## Dữ liệu

- Dòng đầu tiên gồm 2 số nguyên N và M (1 ≤ N ≤ 10⁵, 1 ≤ M ≤ 10⁹) lần lượt là số món quà Tèo đang có và số tiền mà mẹ cho.
- Dòng tiếp theo gồm N số nguyên dương khác nhau a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 10⁹) là các loại đồ chơi mà Tèo đang có.

## Kết quả

- Dòng đầu tiên gồm số nguyên dương K là số món quà mà Tèo sẽ mua.
- Dòng tiếp theo gồm K số nguyên dương khác nhau t₁, t₂, ..., tₖ là các loại đồ chơi mà Tèo sẽ mua.
- Còn nhiều kết quả khác nhau và bạn có thể in bất kỳ cách nào (thứ tự in ra cũng không quan trọng).

## Ví dụ

**Input:**
```
4 14
3 6 11 5
```

**Output:**
```
3
7 1 2
```

**Input:**
```
2 4
7 1
```

**Output:**
```
2
2 3
```

**Input:**
```
1 5
4
```

**Output:**
```
2
1 3
```