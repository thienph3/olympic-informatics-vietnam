# BeginnerFreeContest 43 - TRICKLES

**Thể loại:** Brute Force  
**Độ khó:** 500

## Đề bài

Cho một mảng gồm N phần tử a₁, a₂, ..., aₙ. Một bộ 3 số aᵢ, aⱼ, aₖ được gọi là đẹp nếu aᵢ < aⱼ < aₖ < aᵢ + aⱼ và 3 × aᵢ + 3 × aⱼ + 5 × aₖ là một số chia hết cho 3, 5 hoặc 8.

Hai bộ 3 được gọi là khác nhau nếu tồn tại một vị trí xuất hiện trong bộ này nhưng không xuất hiện trong bộ còn lại.

Ta định nghĩa độ đẹp của bộ 3 số đẹp aᵢ, aⱼ, aₖ là biểu thức: aᵢ + aⱼ - aₖ.

Hãy tính tích độ đẹp của tất cả các bộ ba số đẹp, nếu không tồn tại bất kì một bộ ba nào đẹp in ra 0.

Do kết quả có thể rất lớn nên hãy in ra kết quả modulo 10⁹ + 7.

## Dữ liệu

- Dòng đầu tiên gồm 1 số duy nhất N (1 ≤ N ≤ 2 × 10⁵).
- Dòng thứ hai gồm các số nguyên trong mảng a₁, a₂, ..., aₙ (0 ≤ aᵢ ≤ 2 × 10³).

## Kết quả

In ra một số nguyên duy nhất là tích của tất cả bộ ba số đẹp modulo 10⁹ + 7.

## Ví dụ

**Input:**
```
5
3 4 5 2 3
```

**Output:**
```
7
```

**Input:**
```
3
7 8 4
```

**Output:**
```
3
```

**Input:**
```
4
1 1 2 0
```

**Output:**
```
0
```

## Chấm điểm

- Subtask 1: N ≤ 10² (20% số điểm)
- Subtask 2: N ≤ 2 × 10⁵ (80% số điểm)