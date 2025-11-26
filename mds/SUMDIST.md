# FreeContest 132 - SUMDIST

**Thể loại:** Geometry  
**Độ khó:** 750

## Đề bài

Trên mặt phẳng tọa độ Oxy cho N điểm. Tìm một điểm có tọa độ thực trên mặt phẳng, sao cho tổng khoảng cách Euclid từ điểm tìm được đến từng điểm đã cho là nhỏ nhất có thể.

## Dữ liệu

- Dòng đầu tiên chứa một số nguyên dương N (1 ≤ N ≤ 10⁵) là số điểm.
- N dòng sau đó, mỗi dòng chứa 2 số nguyên Xᵢ và Yᵢ ứng với tọa độ một điểm. (-10⁴ ≤ Xᵢ, Yᵢ ≤ 10⁴).

## Kết quả

Một dòng duy nhất chứa 2 số thực lần lượt là hoành độ và tung độ của điểm mà bạn tìm được.

Gọi S là tổng khoảng cách từ điểm bạn tìm được đến các điểm đề bài cho, còn J là tổng khoảng cách mà giám khảo tìm được. Gọi ε = |S - J| / max(1, J).

Điểm của một test sẽ được tính như sau:
- Nếu ε ≤ 10⁻⁷, bạn được 100% số điểm của test (5 điểm).
- Ngược lại, bạn được max(0, -log₁₀(ε) / 10 - 0.5) điểm, làm tròn đến số nguyên gần nhất.

## Ví dụ

**Input:**
```
4
4 6
4 -2
-2 -2
-2 6
```

**Output:**
```
1.0000000 2.0000000
```