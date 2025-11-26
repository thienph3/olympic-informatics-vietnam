# Beginner Free Contest 40 - CARDGAME

**Thể loại:** Greedy  
**Độ khó:** 450

## Đề bài

Bảo bay Bổng vừa nghĩ ra một trò chơi mới dành cho k bạn nhỏ ở một ngôi trường nọ. Cậu đặt n tấm thẻ lên bàn, trên tấm thẻ thứ i có ghi số ai. Mặt có ghi số của các tấm thẻ được đặt úp xuống mặt bàn. Mỗi lượt chơi, Bảo gọi một bạn nhỏ chưa từng được chơi lượt nào trước đó lên rút ra hai tấm thẻ bất kì mà bạn nhỏ muốn. Sau khi chọn xong bạn nhỏ sẽ để tấm thẻ có ghi số lớn hơn lại trên bàn (bạn lên sau không biết được tấm thẻ mà bạn lên trước chọn) và mang tấm thẻ có giá trị nhỏ hơn về cho mình.

Nếu hai tấm thẻ mà bạn nhỏ chọn có ghi hai số bằng nhau, bạn nhỏ có thể lựa chọn mang về một tấm thẻ bất kì trong hai tấm thẻ đó.

Đặt S là tổng các số ghi trên k tấm thẻ mà các bạn nhỏ mang về. Hãy cho biết S có thể đạt giá trị nhỏ nhất và lớn nhất là bao nhiêu.

## Dữ liệu

- Dòng đầu tiên chứa hai số nguyên dương n, k (1 ≤ k < n ≤ 10⁵).
- Dòng thứ hai chứa n số nguyên dương a₁, a₂, ..., aₙ (1 ≤ ai ≤ 10⁹).

## Kết quả

In ra hai số nguyên dương cách nhau bởi một dấu cách là giá trị S nhỏ nhất và lớn nhất có thể đạt được.

## Ví dụ

**Input:**
```
5 3
1 2 3 4 5
```

**Output:**
```
6 9
```

## Giải thích

Trong trường hợp xấu nhất:
- Bạn thứ nhất bốc tấm thẻ thứ 1 và 2, mang tấm thứ 1 về và để lại tấm thứ 2.
- Bạn thứ hai bốc tấm thẻ thứ 2 và 3, mang tấm thứ 2 về và để lại tấm thứ 3.
- Bạn thứ ba bốc tấm thẻ thứ 3 và 4, mang tấm thứ 3 về và để lại tấm thứ 4.

Tổng các số trên các tấm thẻ của các bạn nhận được: 1 + 2 + 3 = 6.

Trong trường hợp tốt nhất:
- Bạn thứ nhất bốc tấm thẻ thứ 2 và 3, mang tấm thứ 2 về và để lại tấm thứ 3.
- Bạn thứ hai bốc tấm thẻ thứ 3 và 4, mang tấm thứ 3 về và để lại tấm thứ 4.
- Bạn thứ ba bốc tấm thẻ thứ 4 và 5, mang tấm thứ 4 về và để lại tấm thứ 5.

Tổng các số trên các tấm thẻ của các bạn nhận được: 2 + 3 + 4 = 9.

## Chấm điểm

- Subtask 1 (20% số test): n ≤ 5
- Subtask 2 (80% số test): Không có ràng buộc gì thêm