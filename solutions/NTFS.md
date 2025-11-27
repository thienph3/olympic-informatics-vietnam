# NTFS - Math (150 points)

## Phân tích bài toán

Bài toán yêu cầu tính số lượng file tối đa có thể lưu trữ trên ổ đĩa NTFS.

### Input
- Dung lượng ổ đĩa (GB)
- Kích thước file trung bình (MB)

### Output
- Số lượng file tối đa

### Ý tưởng
1. Chuyển đổi đơn vị: GB → MB
2. Chia dung lượng tổng cho kích thước file trung bình
3. Lấy phần nguyên

## Solution

```python
# Đọc input
disk_size_gb = int(input())  # Dung lượng ổ đĩa (GB)
file_size_mb = int(input())  # Kích thước file (MB)

# Chuyển đổi GB sang MB
disk_size_mb = disk_size_gb * 1024

# Tính số file tối đa
max_files = disk_size_mb // file_size_mb

print(max_files)
```

## Độ phức tạp
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Test cases
```
Input:
1
10

Output:
102

Giải thích: 1GB = 1024MB, 1024/10 = 102 files
```