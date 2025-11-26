# Beginner Free Contest 37 - BWTREE

**Thể loại:** Tree  
**Độ khó:** 400

## Đề bài

Cho một cây lớn vô hạn, có gốc là đỉnh 1. Mọi đỉnh i ở trên cây đều có hai đỉnh con trực tiếp là 2i và 2i + 1. Bạn được hỏi T câu hỏi, câu hỏi thứ i sẽ gồm hai đỉnh ui, vi. Bạn cần tìm tổ tiên chung gần nhất của hai đỉnh này.

## Dữ liệu

- Dòng đầu tiên chứa số T (1 ≤ T ≤ 10⁵)
- T dòng tiếp theo, dòng thứ i chứa hai số ui, vi (1 ≤ ui, vi ≤ 10¹²)

## Kết quả

In ra T dòng, dòng thứ i là đáp án của câu hỏi thứ i.

## Ví dụ

**Input:**
```
3
2 13
4 3
1 1
```

**Output:**
```
1
1
1
```

## Giới hạn

- 30% số điểm có T ≤ 10³; ui, vi ≤ 10³
- 30% số điểm có T ≤ 10⁵; ui, vi ≤ 10⁶
- 40% số điểm có điều kiện gốc