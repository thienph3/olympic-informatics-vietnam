# BeginnerFreeContest 10 - TRAVELAB

**Thể loại:** Dynamic Programming  
**Độ khó:** 550

## Đề bài

Đoàn thanh tra gồm hai thành viên A và B cần lần lượt đi kiểm tra n công ty trong thành phố FreeContest. Để có thể sử dụng các thông tin của một số công ty trong việc kiểm tra các công ty quan trọng và việc thanh tra được tiến hành nhanh chóng, họ sẽ phân công các công ty cho nhau sao cho:

- Mỗi công ty chỉ được kiểm tra bởi đúng một thanh tra.
- Các thanh tra có thể kiểm tra các công ty theo thứ tự lần lượt từ công ty 1 đến công ty n.
- Tổng quãng đường di chuyển của hai thanh tra là ít nhất.

Lưu ý do tính chất đặc thù của ngành thanh tra, để di chuyển đến công ty t sau khi vừa kiểm tra xong công ty s, các thanh tra sẽ phải đi theo một đường đi đã được quy định trước. Đường đi này chưa chắc đã là đường đi ngắn nhất giữa hai công ty s và t.

Cụ thể hơn, gọi các giao điểm theo thứ tự mà A thanh tra là a₁, a₂, ..., aₓ và các giao điểm theo thứ tự mà B thanh tra là b₁, b₂, ..., bᵧ, ta có:

- Mỗi số nguyên từ 1 đến n xuất hiện trong dãy a₁, a₂, ..., aₓ, b₁, b₂, ..., bᵧ đúng một lần.
- a₁ < a₂ < ... < aₓ
- b₁ < b₂ < ... < bᵧ
- Gọi d(s, t) là quãng đường di chuyển từ công ty s đến công ty t theo đường đi đã được quy định trước, ta có tổng d(a₁, a₂) + d(a₂, a₃) + ... + d(aₓ₋₁, aₓ) + d(b₁, b₂) + d(b₂, b₃) + ... + d(bᵧ₋₁, bᵧ) nhỏ nhất có thể.

## Yêu cầu

Viết chương trình giúp đoàn thanh tra tính tổng quãng đường di chuyển ngắn nhất có thể của cả hai thanh tra.

## Dữ liệu

- Dòng đầu tiên gồm một số nguyên dương n (1 ≤ n ≤ 10²).
- n dòng tiếp theo, mỗi dòng gồm một số nguyên có giá trị từ 1 đến 10³. Ở dòng thứ i, số nguyên thứ j là quãng đường di chuyển từ công ty i đến công ty j theo đường đi đã được quy định trước.

Dữ liệu vào đảm bảo nếu i = j thì aᵢⱼ = 0.

## Kết quả

Gồm một dòng duy nhất chứa một số nguyên là tổng quãng đường di chuyển ngắn nhất của cả hai thanh tra.

## Ví dụ

**Input:**
```
4
0 2 3 4
2 0 1 5
3 1 0 3
4 5 3 0
```

**Output:**
```
3
```

## Giải thích

- Thanh tra A sẽ đi kiểm tra các công ty 1, 2, 3. Tổng quãng đường di chuyển của thanh tra A là 3.
- Thanh tra B sẽ đi kiểm tra công ty 4. Tổng quãng đường di chuyển của thanh tra B là 0.