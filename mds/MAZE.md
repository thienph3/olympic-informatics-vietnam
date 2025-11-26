# Beginner Free Contest 24 - MAZE

**Thể loại:** Simulation  
**Độ khó:** 400

## Đề bài

Long đang trên đường đi học thì không may bị một kẻ xấu bắt nhốt vào trong một mê cung. Mê cung gồm n + 1 căn phòng xếp nối tiếp nhau theo thứ tự phòng 1, phòng 2, ..., phòng n + 1. Long hiện đang ở phòng 1, và lối thoát ở phòng n + 1.

Giữa n + 1 căn phòng còn các cánh cửa. Ban đầu tại thời điểm 0, tất cả các cánh cửa đều đóng. Sau đó, cánh cửa thứ i sẽ chỉ mở ra mỗi aᵢ giây. Do Long khá nhanh nhẹn nên cậu có thể di chuyển giữa 2 căn phòng mà không mất thời gian nào.

Long bắt đầu di chuyển tại phòng 1 từ thời điểm 0. Câu hỏi đặt ra cho bạn đó là hãy tìm thời điểm sớm nhất mà Long sẽ thoát khỏi mê cung.

## Dữ liệu

- Dòng đầu tiên gồm một số nguyên n (1 ≤ n ≤ 10⁵) - số lượng phòng có trong mê cung.
- Dòng thứ hai gồm n số nguyên aᵢ (1 ≤ aᵢ ≤ 10⁹) - Cánh cửa thứ i sẽ mở ra mỗi aᵢ giây.

## Kết quả

In ra một số nguyên duy nhất là thời điểm sớm nhất mà Long sẽ thoát khỏi mê cung.

## Ví dụ

**Input:**
```
4
3 4 2 2
```

**Output:**
```
8
```

**Input:**
```
5
2 4 6 8 10
```

**Output:**
```
20
```

## Giải thích

Ở ví dụ 1, Long sẽ thoát ra khỏi mê cung như sau:
- Long ở phòng 1 tại thời điểm 0, cửa 1 đóng, đợi qua 3 giây để cửa 1 mở, Long đi qua phòng 2.
- Long ở phòng 2 tại thời điểm 3, cửa 2 đóng, đợi qua 1 giây để cửa 2 mở, Long đi qua phòng 3.
- Long ở phòng 3 tại thời điểm 4, cửa 3 đóng, đợi qua 2 giây để cửa 3 mở, Long đi qua phòng 4.
- Long ở phòng 4 tại thời điểm 6, cửa 4 đóng, đợi qua 2 giây để cửa 4 mở, Long đi qua phòng 5, và thoát ra mê cung.

Vì tổng thời gian ít nhất cần để thoát mê cung là 8 giây, nên ta in ra 8.