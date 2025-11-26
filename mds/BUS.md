# Beginner Free Contest 46 - BUS

**Thể loại:** Greedy  
**Độ khó:** 500

## Đề bài

Nam là một tài xế xe buýt đi từ trạm 1 đến trạm thứ p. Thời gian để di chuyển qua các trạm là 1 phút. Cho biết thời gian và địa điểm chờ của n hành khách đón xe buýt, hãy giúp Nam xác định thời gian xuất phát từ trạm thứ 1 sớm nhất để có thể đón ít nhất m hành khách.

Biết rằng xe buýt có sức chứa không giới hạn.

## Dữ liệu

- Dòng thứ nhất ghi hai số nguyên dương n, m, p (1 ≤ n, p ≤ 10⁵, 1 ≤ m ≤ n) - số hành khách chờ xe buýt, số hành khách ít nhất Nam phải đón và số trạm xe buýt.
- n dòng tiếp theo, dòng thứ i gồm hai số nguyên dương ai và bi (1 ≤ ai ≤ p, bi ≤ 10⁹) - khách hàng thứ i bắt đầu chờ tại trạm ai tại thời điểm bi.

## Kết quả

In ra thời điểm xuất phát từ trạm 1 sớm nhất để Nam có thể đón ít nhất m hành khách.

## Ví dụ

**Input:**
```
7 4 5
1 1
2 4
4 10
5 5
6 4
7 3
```

**Output:**
```
3
```

## Giải thích

Nếu Nam xuất phát tại thời điểm 3 thì sẽ đón được hành khách thứ 1, 2, 5 và 6.