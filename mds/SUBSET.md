# BeginnerFreeContest 47 - SUBSET

**Thể loại:** Dynamic Programming  
**Độ khó:** 650

## Đề bài

Cho dãy n số nguyên aᵢ. Một đoạn con liên tiếp từ l đến r gọi là hoàn hảo nếu như có thể chọn ra một tập con sao cho tổng của nó bằng s. Hãy tìm đoạn con hoàn hảo ngắn nhất trong dãy trên.

## Dữ liệu

- Dòng thứ nhất chứa hai số nguyên n, s (1 ≤ n ≤ 10⁵, 1 ≤ s ≤ 10⁹)
- Dòng tiếp theo chứa n số nguyên aᵢ (1 ≤ aᵢ ≤ s).

## Kết quả

Xuất ra độ dài dãy con hoàn hảo ngắn nhất. Nếu không có dãy con nào là hoàn hảo, in ra -1.

## Ví dụ

**Input:**
```
10 100
14 33 22 21 11 5 13 28 61 2
```

**Output:**
```
5
```

## Chấm điểm

- Subtask 1 (50% số test): n ≤ 10²
- Subtask 2 (50% số test): Không có ràng buộc gì thêm