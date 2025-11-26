# BeginnerFreeContest 55 - PALINARRAY

**Thể loại:** Dynamic Programming  
**Độ khó:** 500

## Đề bài

Cho dãy a gồm n số nguyên. Hãy xác định xem dãy a có bao gồm bất kỳ dãy con có ít nhất 3 phần tử lập thành dãy palindrome.

Lưu ý, một dãy b được gọi là dãy con của dãy a nếu từ dãy a ta có thể xóa đi một vài phần tử (hoặc không xóa phần tử nào) để có được dãy b (và không mất tính thứ tự).

Ví dụ, [2], [1, 2, 1, 3], và [2, 3] là dãy con của [1, 2, 1, 3], nhưng [1, 1, 2] và [4] thì không.

Đồng thời, một dãy là dãy palindrome khi dãy đó đọc xuôi hay đọc ngược đều như nhau. Hay nói cách khác, một dãy a₁, a₂, ..., aₙ là một dãy palindrome nếu aᵢ = aₙ₋ᵢ₊₁ với mọi i từ 1 đến n.

Ví dụ, dãy [1234], [1, 2, 1], [1, 3, 2, 2, 3, 1], và [10, 10, 10] là dãy palindrome, nhưng dãy [1, 2] và [1, 2, 3, 1] thì không.

## Dữ liệu

Dòng đầu tiên gồm một số nguyên t (1 ≤ t ≤ 10⁴) — số lượng test case bạn phải trả lời.

2t dòng tiếp theo mô tả test case:
- Dòng đầu tiên của mỗi test case gồm một số nguyên n (3 ≤ n ≤ 10⁵) - độ dài của dãy a.
- Dòng thứ hai của test case gồm n số nguyên a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ n), với aᵢ là phần tử thứ i của a.

Dữ liệu đầu vào đảm bảo tổng của n trên tất cả các test không vượt quá 10⁵ (∑n ≤ 10⁵).

## Kết quả

Với mỗi test case, in "YES" (không bao gồm dấu ngoặc) nếu a có ít nhất một dãy con có ít nhất 3 phần tử lập thành dãy palindrome và "NO" nếu ngược lại.

## Ví dụ

**Input:**
```
5
3
1 2 1
5
1 2 3 4 5
3
2 3 2
4
3 4 4 3
5
1 2 2 3 3
```

**Output:**
```
YES
YES
NO
YES
NO
```

## Chấm điểm

- Subtask 1 (30% số test): n ≤ 5000
- Subtask 2 (70% số test): Không có ràng buộc gì thêm.