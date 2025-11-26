# Beginner Free Contest 52 - NTFS

**Thể loại:** Math  
**Độ khó:** 150

## Đề bài

Nếu đĩa cứng máy tính được format theo chế độ NTFS thì bộ nhớ được phân phối cho các file chứa trong đĩa cứng theo đơn vị cluster, mỗi cluster là một vùng nhớ có kích thước 4KB (1KB = 1024 byte). Như vậy dù tập tin có kích thước nhỏ hơn hoặc bằng 4KB thì nó cũng chiếm một vùng nhớ 4KB trên đĩa.

**Yêu cầu:** Cho một số nguyên dương n (n ≤ 10⁹) là kích thước của một tập tin theo đơn vị byte. Hãy xác định kích thước theo KB mà tập tin chiếm trên đĩa cứng NTFS.

## Dữ liệu

Dòng duy nhất chứa số nguyên dương n.

## Kết quả

In ra kích thước theo KB mà tập tin chiếm giữ.

## Ví dụ

**Input:**
```
4097
```

**Output:**
```
8
```