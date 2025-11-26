# Beginner Free Contest 40 - KMEMORY

**Thể loại:** Array  
**Độ khó:** 350

## Đề bài

Trong ca khúc Lối Nhỏ, rapper Đen Vâu có viết "Kỉ niệm sẽ là thứ duy nhất đi theo anh cả cuộc đời dài". Vì là một Đồng Âm chân chính, thầy Yeh đã quyết định sẽ chụp nhiều hình ảnh nhất có thể cho lớp mà ông đang chủ nhiệm.

Và là người cầm máy, ông muốn đảm bảo rằng những bức hình mình chụp phải là oneshot (chụp một lần duy nhất) và xinh đẹp tuyệt vời.

Một bức hình xinh đẹp tuyệt vời là khi trong bức ảnh đó độ chênh lệch giữa chiều cao của học sinh cao nhất và học sinh thấp nhất không vượt quá K.

Lớp của ông có n học sinh. Khi các học sinh đã đứng vào vị trí mà chúng thích, học sinh thứ i sẽ có chiều cao là aᵢ.

Bây giờ đây bạn hãy cho thầy Yeh biết ông có thể chụp tối đa bao nhiêu bức hình xinh đẹp tuyệt vời của lớp này nhé.

## Dữ liệu

- Dòng thứ nhất gồm hai số nguyên N, K (1 ≤ N ≤ 5 × 10⁵; 0 ≤ K ≤ 10⁹).
- Dòng thứ hai gồm N số nguyên a₁, a₂, ..., aₙ (0 ≤ aᵢ ≤ 10⁹).

## Kết quả

Số lượng bức hình tối đa mà thầy Yeh có thể chụp.

## Ví dụ

**Input:**
```
4 3
10 5 6 2
```

**Output:**
```
5
```

## Giải thích

Các dãy học sinh thỏa mãn độ chênh lệch giữa học sinh cao nhất và học sinh thấp nhất ≤ K:
- {10} có độ chênh lệch là 0.
- {5} có độ chênh lệch là 0.
- {6} có độ chênh lệch là 0.
- {2} có độ chênh lệch là 0.
- {5, 6} có độ chênh lệch là 1.