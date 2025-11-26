# Beginner Free Contest 23 - BRIDGES

**Thể loại:** Geometry  
**Độ khó:** 550

## Đề bài

Tại một vương quốc xa xăm nào đó có một dòng sông cắt ngang và chia vương quốc này thành hai bờ, bờ trái và bờ phải. Ở mỗi bờ sẽ có 10⁹ ngôi làng. Trong bài toán này ta sẽ xem mỗi ngôi làng là một điểm trên mặt phẳng tọa độ Descartes, ngôi làng thứ x ở bờ trái sẽ có tọa độ là (0, x), ngôi làng thứ y ở bờ phải sẽ có tọa độ là (1, y) (1 ≤ x, y ≤ 10⁹, x, y ∈ N*).

Để tăng trưởng kinh tế nhà vua của vương quốc đã quyết định xây dựng N cây cầu bắt ngang qua dòng sông để nối các ngôi làng lại với nhau. Cây cầu có dạng (u, v) có nghĩa là người dân ở làng thứ u ở bờ trái và người dân ở ngôi làng thứ v ở bờ phải có thể đi lại bằng cây cầu này. Với một cây cầu (u, v) bất kì, những người dân sử dụng cây cầu này sẽ cảm thấy không hài lòng nếu tồn tại một cây cầu (x, y) (x ≠ u và y ≠ v) bất kì cắt với cây cầu này.

Hai cây cầu là (u, v) và (x, y) được gọi là cắt nhau nếu như đoạn thẳng nối hai điểm (0, u) và (1, v) cắt với đoạn thẳng nối hai điểm (0, x) và (1, y). Bạn hãy tính tổng độ không hài lòng của người dân ở vương quốc với tổng độ không hài lòng được định nghĩa là: tổng số cặp (u, v) và (x, y) thỏa mãn điều kiện trên. Chú ý: cặp {(u, v), (x, y)} và {(x, y), (u, v)} chỉ tính là một. Hãy tính tổng độ không hài lòng của người dân.

## Dữ liệu

- Dòng đầu tiên gồm một số nguyên N (1 ≤ N ≤ 10⁵)
- N dòng tiếp theo, mỗi dòng gồm hai số tự nhiên u, v (1 ≤ u, v ≤ 10⁹)

## Kết quả

Một số duy nhất là kết quả của bài toán.

## Ví dụ

**Input:**
```
3
1 3
2 2
3 1
```

**Output:**
```
3
```

## Giải thích

Các cặp cây cầu cắt nhau là:
- (1, 3), (2, 2)
- (1, 3), (3, 1)
- (2, 2), (3, 1)

## Chấm điểm

- Subtask 1 (50% số test): N ≤ 5 × 10³
- Subtask 2 (50% số test): Không có ràng buộc gì thêm