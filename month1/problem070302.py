# Problem 07.03.02: Quản lý danh sách học sinh

print("=== QUẢN LÝ DANH SÁCH HỌC SINH ===")

# Khởi tạo danh sách học sinh
students = []

def display_menu():
    print("\n=== MENU QUẢN LÝ HỌC SINH ===")
    print("1. Thêm học sinh")
    print("2. Hiển thị danh sách")
    print("3. Tìm kiếm học sinh")
    print("4. Xóa học sinh")
    print("5. Sắp xếp danh sách")
    print("6. Thống kê")
    print("0. Thoát")

def add_student():
    name = input("Nhập tên học sinh: ").strip()
    if name:
        if name not in students:
            students.append(name)
            print(f"✅ Đã thêm {name} vào danh sách")
        else:
            print(f"❌ {name} đã có trong danh sách")
    else:
        print("❌ Tên không được để trống")

def display_students():
    if not students:
        print("📝 Danh sách trống")
        return
    
    print(f"\n📋 DANH SÁCH HỌC SINH ({len(students)} học sinh):")
    for i, student in enumerate(students, 1):
        print(f"{i:2d}. {student}")

def search_student():
    if not students:
        print("📝 Danh sách trống")
        return
    
    name = input("Nhập tên cần tìm: ").strip()
    if name in students:
        position = students.index(name) + 1
        print(f"✅ Tìm thấy {name} ở vị trí {position}")
    else:
        print(f"❌ Không tìm thấy {name}")
        
        # Tìm kiếm gần đúng
        similar = []
        for student in students:
            if name.lower() in student.lower():
                similar.append(student)
        
        if similar:
            print(f"🔍 Có thể bạn muốn tìm: {', '.join(similar)}")

def remove_student():
    if not students:
        print("📝 Danh sách trống")
        return
    
    display_students()
    
    try:
        choice = input("Nhập tên hoặc số thứ tự cần xóa: ").strip()
        
        # Thử xóa theo số thứ tự
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(students):
                removed = students.pop(index)
                print(f"✅ Đã xóa {removed}")
            else:
                print("❌ Số thứ tự không hợp lệ")
        # Xóa theo tên
        elif choice in students:
            students.remove(choice)
            print(f"✅ Đã xóa {choice}")
        else:
            print(f"❌ Không tìm thấy {choice}")
            
    except ValueError:
        print("❌ Lựa chọn không hợp lệ")

def sort_students():
    if not students:
        print("📝 Danh sách trống")
        return
    
    print("Chọn cách sắp xếp:")
    print("1. A-Z (tăng dần)")
    print("2. Z-A (giảm dần)")
    
    choice = input("Lựa chọn (1-2): ").strip()
    
    if choice == "1":
        students.sort()
        print("✅ Đã sắp xếp A-Z")
    elif choice == "2":
        students.sort(reverse=True)
        print("✅ Đã sắp xếp Z-A")
    else:
        print("❌ Lựa chọn không hợp lệ")

def show_statistics():
    if not students:
        print("📝 Danh sách trống")
        return
    
    print(f"\n📊 THỐNG KÊ:")
    print(f"Tổng số học sinh: {len(students)}")
    
    if students:
        # Học sinh đầu tiên và cuối cùng (theo alphabet)
        sorted_students = sorted(students)
        print(f"Học sinh đầu tiên (A-Z): {sorted_students[0]}")
        print(f"Học sinh cuối cùng (A-Z): {sorted_students[-1]}")
        
        # Độ dài tên
        name_lengths = [len(name) for name in students]
        avg_length = sum(name_lengths) / len(name_lengths)
        print(f"Độ dài tên trung bình: {avg_length:.1f} ký tự")
        
        # Tên dài nhất và ngắn nhất
        longest_name = max(students, key=len)
        shortest_name = min(students, key=len)
        print(f"Tên dài nhất: {longest_name} ({len(longest_name)} ký tự)")
        print(f"Tên ngắn nhất: {shortest_name} ({len(shortest_name)} ký tự)")
        
        # Phân tích chữ cái đầu
        first_letters = {}
        for student in students:
            first_letter = student[0].upper()
            first_letters[first_letter] = first_letters.get(first_letter, 0) + 1
        
        print(f"Phân bố chữ cái đầu:")
        for letter in sorted(first_letters.keys()):
            print(f"  {letter}: {first_letters[letter]} học sinh")

# Chương trình chính
def main():
    print("🎓 CHƯƠNG TRÌNH QUẢN LÝ DANH SÁCH HỌC SINH")
    
    # Thêm một số học sinh mẫu
    sample_students = ["Nguyễn Văn An", "Trần Thị Bình", "Lê Văn Cường"]
    students.extend(sample_students)
    print(f"📝 Đã thêm {len(sample_students)} học sinh mẫu")
    
    while True:
        display_menu()
        choice = input("\nNhập lựa chọn: ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            sort_students()
        elif choice == "6":
            show_statistics()
        elif choice == "0":
            print("👋 Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

# Chạy chương trình
if __name__ == "__main__":
    main()