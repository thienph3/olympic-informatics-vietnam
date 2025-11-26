# Beginner Free Contest 28 - AGRTREE

**Thể loại:** Tree  
**Độ khó:** 550

## Đề bài

Ngày xửa ngày xưa, có một vương quốc tên là DH. Vương quốc gồm có N thành phố. Các thành phố được đánh số từ 1 đến N. Để cho dễ quản lý, nhà vua đã tổ chức vương quốc theo dạng cây với N - 1 con đường nối giữa các thành phố và thành phố gốc là thành phố 1. Thành phố v được xem là con của thành phố u nếu u nằm trên đường đi từ v đến thành phố 1.

Nhà vua muốn phát triển vương quốc theo hướng nông nghiệp nên mỗi thành phố của vương quốc sẽ được trồng duy nhất một loại lương thực. Các loại lương thực được đánh số từ 1 đến M. Thành phố thứ i sẽ trồng loại lương thực là Ai (1 ≤ Ai ≤ M). Một thành phố được gọi là phát triển nếu tất cả các loại lương thực từ 1 đến M đều được trồng trong ít nhất một trong các thành phố con của thành phố đó hoặc trong chính thành phố đó.

Với mỗi thành phố từ 1 đến N, bạn hãy giúp nhà vua xác định xem thành phố đó có phải là thành phố phát triển hay không.

## Dữ liệu

- Dòng đầu tiên chứa hai số nguyên N và M (M ≤ N).
- Dòng thứ hai gồm N số nguyên A₁, A₂, ..., Aₙ (1 ≤ Ai ≤ M).
- N - 1 dòng tiếp theo, mỗi dòng gồm hai số nguyên u, v (1 ≤ u, v ≤ N) tương ứng với một con đường hai chiều nối hai thành phố u và v.

## Kết quả

Gồm một dòng duy nhất chứa xâu S với Si (1 ≤ i ≤ N) là 1 nếu thành phố thứ i là thành phố phát triển, là 0 nếu ngược lại.

## Ví dụ

**Input:**
```
7 2
2 1 1 2 1 2 1
1 2
2 3
1 4
1 5
5 6
4 7
```

**Output:**
```
1100100
```

**Giới hạn:**
- 30% số test tương ứng với N ≤ 1000
- 70% số test tương ứng với N ≤ 100000