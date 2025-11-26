# Beginner Free Contest 50 - IMPOSSIBOR

**Thể loại:** Bit Manipulation  
**Độ khó:** 600

## Đề bài

Bạn được cho mảng a gồm N số nguyên dương đánh số từ 1. Số x được gọi là đẹp nếu x có thể biểu diễn dưới dạng tổng OR của một dãy con không liên tiếp của a.

Cụ thể hơn, x là số đẹp nếu tồn tại các chỉ số 1 ≤ index₁ < index₂ < ... < indexₖ ≤ N thỏa a[index₁] OR a[index₂] OR ... OR a[indexₖ] = x, trong đó OR là toán tử bitwise OR.

Tìm số nguyên dương nhỏ nhất không phải số đẹp.

## Dữ liệu

- Dòng đầu tiên chứa số nguyên dương N (1 ≤ N ≤ 10⁵) là độ dài mảng a.
- Dòng thứ hai chứa N số nguyên dương a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 10⁹).

## Kết quả

In ra số nguyên dương nhỏ nhất không phải số đẹp.

## Ví dụ

**Input:**
```
2
2 1
```

**Output:**
```
4
```

**Input:**
```
3
5 3 2
```

**Output:**
```
1
```