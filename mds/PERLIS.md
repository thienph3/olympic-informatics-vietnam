# BeginnerFreeContest 22 - PERLIS

**Thể loại:** Greedy  
**Độ khó:** 650

## Đề bài

Cho hai dãy A và B gồm N phần tử, bao gồm:
- Dãy A: A₁, A₂, A₃, ..., Aₙ là một hoán vị của các số nguyên liên tiếp từ 1 đến N. Phần tử thứ i của dãy được gọi là Aᵢ.
- Dãy B: B₁, B₂, ..., Bₙ. Trong đó, Bᵢ là số lượng phần tử của dãy con tăng dài nhất bắt đầu từ phần tử thứ i của dãy A cho trước.

Yêu cầu: Cho dãy B, hãy tìm lại dãy A. Nếu còn nhiều dãy A thỏa mãn, tìm ra dãy A có thứ tự từ điển nhỏ nhất.

## Dữ liệu

- Dòng đầu tiên chứa số nguyên dương N.
- Dòng tiếp theo chứa N số B₁, B₂, ..., Bₙ.

## Kết quả

In ra N số A₁, A₂, ..., Aₙ là hoán vị các số từ 1 đến N thỏa mãn yêu cầu đề bài.

## Ví dụ

**Input:**
```
4
1 2 2 1
```

**Output:**
```
4 2 3 1
```

**Input:**
```
5
5 4 3 2 1
```

**Output:**
```
1 2 3 4 5
```

## Giải thích

- Với ví dụ thứ nhất:
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 4 là [3]. Do đó, B₄ = 1.
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 3 là [1, 3]. Do đó, B₃ = 2.
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 2 là [2, 3]. Do đó, B₂ = 2.
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 1 là [1]. Do đó, B₁ = 1.

- Với ví dụ thứ hai:
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 5 là [5]. Do đó, B₅ = 1.
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 4 là [4, 5]. Do đó, B₄ = 2.
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 3 là [3, 4, 5]. Do đó, B₃ = 3.
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 2 là [2, 3, 4, 5]. Do đó, B₂ = 4.
  - Dãy con tăng dài nhất bắt đầu từ phần tử thứ 1 là [1, 2, 3, 4, 5]. Do đó, B₁ = 5.

## Giới hạn

Trong tất cả các test, 1 ≤ Bᵢ ≤ N.
- Subtask 1 (30%): 1 ≤ N ≤ 10.
- Subtask 2 (70%): 1 ≤ N ≤ 10⁵.