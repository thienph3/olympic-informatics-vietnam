# BeginnerFreeContest 55 - ROOT

**Thể loại:** Graph  
**Độ khó:** 500

## Đề bài

Peter kể rằng cậu ấy có một mô hình cây đặc biệt, từ một nút chỉ có thể đi xuống nút thấp hơn nó. Tuy nhiên trong lúc chuyển chỗ mô hình này, Peter đã vô tình vấp ngã làm thay đổi hình dạng của cây.

Peter chỉ nhớ một vài đặc điểm của mô hình, đặc điểm thứ i cho biết từ nút uᵢ có thể đi đến nút vᵢ. Peter không cần xác định chính xác hình dạng ban đầu của cây, chỉ cần biết được nút nào là gốc của cây.

Hãy giúp Peter xác định xem có bao nhiêu nút có khả năng làm gốc của cây.

## Dữ liệu

- Dòng đầu tiên chứa 2 số nguyên dương n, m (1 ≤ n, m ≤ 10⁵) lần lượt là số lượng nút của cây và số đặc điểm mà Peter nhớ.
- n - 1 dòng tiếp theo, dòng thứ i chứa 2 số nguyên dương aᵢ và bᵢ (1 ≤ aᵢ, bᵢ ≤ n), cho biết có một cạnh nối giữa aᵢ và bᵢ.
- m dòng tiếp theo, dòng thứ i chứa 2 số nguyên dương uᵢ và vᵢ (1 ≤ uᵢ, vᵢ ≤ n), cho biết có đường đi từ nút uᵢ đến nút vᵢ.

## Kết quả

In ra một số duy nhất là số nút có khả năng làm gốc của cây.

Dữ liệu đảm bảo rằng có ít nhất một nút có thể làm gốc.

## Ví dụ

**Input:**
```
7 2
2 3
3 5
4 6
1 2
4 7
2 3
4 7
```

**Output:**
```
2
```

## Giải thích

- Ở ví dụ thứ nhất, có thể chọn các nút 1, 2.
- Ở ví dụ thứ hai, có thể chọn các nút 2, 4, 5.

## Chấm điểm

- Subtask 1 (50% số test): n, m ≤ 10².
- Subtask 2 (50% số test): không có ràng buộc gì thêm.