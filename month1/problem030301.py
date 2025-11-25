# Problem 03.03.01: Kiểm tra năm nhuận

print("=== KIỂM TRA NĂM NHUẬN ===")

year = int(input("Nhập năm: "))

# Quy tắc năm nhuận:
# - Chia hết cho 4 VÀ (không chia hết cho 100 HOẶC chia hết cho 400)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
            reason = "Chia hết cho 400"
        else:
            is_leap = False
            reason = "Chia hết cho 100 nhưng không chia hết cho 400"
    else:
        is_leap = True
        reason = "Chia hết cho 4 và không chia hết cho 100"
else:
    is_leap = False
    reason = "Không chia hết cho 4"

print(f"\nNăm {year}: {'Năm nhuận' if is_leap else 'Không phải năm nhuận'}")
print(f"Lý do: {reason}")

# Tính số ngày trong tháng 2
days_in_feb = 29 if is_leap else 28
print(f"Tháng 2 năm {year} có {days_in_feb} ngày")

# Kiểm tra thêm một số năm
test_years = [1900, 2000, 2004, 2100, 2024]
print(f"\nKiểm tra nhanh:")
for test_year in test_years:
    if test_year % 4 == 0 and (test_year % 100 != 0 or test_year % 400 == 0):
        print(f"{test_year}: Năm nhuận")
    else:
        print(f"{test_year}: Không phải năm nhuận")