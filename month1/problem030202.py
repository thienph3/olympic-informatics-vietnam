# Problem 03.02.02: Máy tính thuế

print("=== MÁY TÍNH THUẾ THU NHẬP ===")

# Nhập thông tin
income = float(input("Nhập thu nhập hàng tháng (triệu VNĐ): "))
dependents = int(input("Số người phụ thuộc: "))

# Tính thu nhập chịu thuế
personal_deduction = 11  # 11 triệu
dependent_deduction = dependents * 4.4  # 4.4 triệu/người
taxable_income = income - personal_deduction - dependent_deduction

print(f"\nThu nhập chịu thuế: {taxable_income:.1f} triệu VNĐ")

if taxable_income <= 0:
    tax = 0
    tax_rate = "0%"
elif taxable_income <= 5:
    tax = taxable_income * 0.05
    tax_rate = "5%"
elif taxable_income <= 10:
    tax = 5 * 0.05 + (taxable_income - 5) * 0.10
    tax_rate = "10%"
elif taxable_income <= 18:
    tax = 5 * 0.05 + 5 * 0.10 + (taxable_income - 10) * 0.15
    tax_rate = "15%"
elif taxable_income <= 32:
    tax = 5 * 0.05 + 5 * 0.10 + 8 * 0.15 + (taxable_income - 18) * 0.20
    tax_rate = "20%"
else:
    tax = 5 * 0.05 + 5 * 0.10 + 8 * 0.15 + 14 * 0.20 + (taxable_income - 32) * 0.25
    tax_rate = "25%"

net_income = income - tax

print(f"Thuế phải nộp: {tax:.2f} triệu VNĐ (thuế suất cao nhất: {tax_rate})")
print(f"Thu nhập sau thuế: {net_income:.2f} triệu VNĐ")