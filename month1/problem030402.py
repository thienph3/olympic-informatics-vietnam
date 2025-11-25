# Problem 03.04.02: Máy tính BMI và tư vấn sức khỏe

print("=== TƯ VẤN SỨC KHỎE - BMI ===")

# Nhập thông tin
try:
    weight = float(input("Cân nặng (kg): "))
    height = float(input("Chiều cao (cm): "))
    age = int(input("Tuổi: "))
    gender = input("Giới tính (M/F): ").upper().strip()
    
    # Validation
    if weight <= 0 or weight > 500:
        print("❌ Cân nặng không hợp lệ!")
    elif height <= 0 or height > 300:
        print("❌ Chiều cao không hợp lệ!")
    elif age <= 0 or age > 150:
        print("❌ Tuổi không hợp lệ!")
    elif gender not in ["M", "F"]:
        print("❌ Giới tính phải là M hoặc F!")
    else:
        # Tính BMI
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        
        print(f"\n📊 KẾT QUẢ PHÂN TÍCH:")
        print(f"BMI: {bmi:.2f}")
        
        # Phân loại BMI
        if bmi < 16:
            category = "Gầy độ III (rất nguy hiểm)"
            color = "🔴"
        elif bmi < 17:
            category = "Gầy độ II (nguy hiểm)"
            color = "🟠"
        elif bmi < 18.5:
            category = "Gầy độ I (thiếu cân)"
            color = "🟡"
        elif bmi < 25:
            category = "Bình thường"
            color = "🟢"
        elif bmi < 30:
            category = "Thừa cân"
            color = "🟡"
        elif bmi < 35:
            category = "Béo phì độ I"
            color = "🟠"
        elif bmi < 40:
            category = "Béo phì độ II"
            color = "🔴"
        else:
            category = "Béo phì độ III (rất nguy hiểm)"
            color = "🔴"
        
        print(f"Phân loại: {color} {category}")
        
        # Tư vấn theo tuổi và giới tính
        print(f"\n💡 TƯ VẤN:")
        
        if bmi < 18.5:
            print("• Cần tăng cân một cách lành mạnh")
            print("• Ăn nhiều protein, carbs phức tạp")
            print("• Tập gym để tăng cơ bắp")
            
            if age < 25:
                print("• Ở tuổi trẻ, cơ thể dễ hấp thụ dinh dưỡng")
            elif age > 50:
                print("• Cần bổ sung canxi và vitamin D")
                
        elif bmi > 25:
            print("• Cần giảm cân để cải thiện sức khỏe")
            print("• Giảm calories, tăng hoạt động thể chất")
            print("• Ăn nhiều rau xanh, hạn chế đường")
            
            if age > 40:
                print("• Cần kiểm tra đường huyết và huyết áp định kỳ")
            if gender == "F" and age > 45:
                print("• Phụ nữ trung niên cần chú ý hormone")
                
        else:
            print("• Duy trì lối sống lành mạnh hiện tại")
            print("• Tập thể dục đều đặn 150 phút/tuần")
            print("• Ăn uống cân bằng, đủ chất")
        
        # Tính cân nặng lý tưởng
        ideal_bmi = 22  # BMI lý tưởng
        ideal_weight = ideal_bmi * (height_m ** 2)
        weight_diff = weight - ideal_weight
        
        print(f"\n🎯 CÂN NẶNG LÝ TƯỞNG:")
        print(f"Cân nặng lý tưởng: {ideal_weight:.1f} kg")
        
        if abs(weight_diff) < 2:
            print("✅ Cân nặng của bạn rất lý tưởng!")
        elif weight_diff > 0:
            print(f"📉 Cần giảm {weight_diff:.1f} kg")
        else:
            print(f"📈 Cần tăng {abs(weight_diff):.1f} kg")
            
except ValueError:
    print("❌ Vui lòng nhập đúng định dạng số!")