# Beginner Free Contest 18 - FINDPER

**Thể loại:** Simulation  
**Độ khó:** 400

## Đề bài

Cho một dãy gồm N số nguyên: a₁, a₂, ..., aₙ và dãy B rỗng. Trên dãy B, bạn hãy thực hiện N phép biến đổi. Với phép biến đổi thứ i:

- Thêm aᵢ vào cuối dãy B.
- Đảo ngược thứ tự các phần tử của dãy B.

Bạn hãy tìm kết quả của dãy B sau khi thực hiện N phép biến đổi.

## Dữ liệu

- Dòng đầu tiên, chứa số nguyên dương N.
- Dòng tiếp theo, chứa N số nguyên a₁, a₂, ..., aₙ.

## Giới hạn

- 1 ≤ N ≤ 2 × 10⁵
- 0 ≤ aᵢ ≤ 10⁹

## Kết quả

Gồm một dòng duy nhất là kết quả bài toán.

## Ví dụ

**Input:**
```
4
1 2 3 4
```

**Output:**
```
4 2 1 3
```

**Input:**
```
3
3 1 2
```

**Output:**
```
2 1 3
```

## Giải thích ví dụ

Ở ví dụ 2:
- Sau phép toán 1, B = {3}.
- Sau phép toán 2, B = {1, 3}.
- Sau phép toán 3, B = {2, 1, 3}.