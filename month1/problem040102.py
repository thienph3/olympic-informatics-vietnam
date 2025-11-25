# Problem 04.01.02: Bảng cửu chương

print("=== BẢNG CỬU CHƯƠNG ===")

# In bảng cửu chương từ 1 đến 9
for table in range(1, 10):
    print(f"\nBảng cửu chương {table}:")
    for i in range(1, 11):
        result = table * i
        print(f"{table} × {i} = {result}")

print("\n" + "="*30)

# In bảng cửu chương dạng ngang
print("BẢNG CỬU CHƯƠNG DẠNG NGANG:")
for i in range(1, 11):
    for table in range(1, 10):
        result = table * i
        print(f"{table}×{i}={result:2d}", end="  ")
    print()  # Xuống dòng sau mỗi hàng