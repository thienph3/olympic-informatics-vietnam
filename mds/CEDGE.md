# Beginner Free Contest 23 - CEDGE

**Thể loại:** Graph  
**Độ khó:** 500

## Đề bài

Cho một cây (đồ thị liên thông vô hướng không chu trình) gồm N nút. Các nút được đánh số từ 1 đến N. Nhiệm vụ của bạn là tô màu các cạnh trên cây, sao cho với mỗi nút, không có hai cạnh bất kì kề với nút đó được tô cùng một màu.

Trong các cách tô màu thỏa mãn, hãy tìm cách tô dùng ít màu phân biệt nhất.

Lưu ý: nếu có nhiều cách tô dùng ít màu phân biệt nhất và thỏa mãn điều kiện, bạn có thể in ra một cách bất kì.

## Dữ liệu

- Dòng đầu tiên gồm một số nguyên N (2 ≤ N ≤ 10⁵).
- N - 1 dòng tiếp theo, dòng thứ i chứa hai số nguyên ai và bi (1 ≤ ai, bi ≤ N) biểu diễn cạnh nối giữa nút ai và bi.

## Kết quả

- Dòng đầu tiên in ra một số nguyên K là số lượng màu phân biệt ít nhất được dùng để tô.
- N - 1 dòng tiếp theo, dòng thứ i in ra một số nguyên ci (1 ≤ ci ≤ K) biểu diễn màu của cạnh thứ i trong cách cho ban đầu.

## Ví dụ

**Input:**
```
3
1 2
2 3
```

**Output:**
```
2
1
2
```