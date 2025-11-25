# Day 3: Cấu trúc điều khiển if-else

**Thời gian:** 195 phút (3h15')

---

## Phần 1: Câu lệnh if cơ bản (45')

### 📚 Lý thuyết (15')

#### Cú pháp if cơ bản

```python
# Cấu trúc if đơn giản
if điều_kiện:
    # Khối lệnh thực hiện khi điều kiện True
    lệnh1
    lệnh2
```

#### Ví dụ cơ bản

```python
age = 18

if age >= 18:
    print("Bạn đã đủ tuổi bầu cử")
    print("Chúc mừng!")

# Lưu ý về indentation
score = 85
if score >= 80:
    print("Điểm cao")  # 4 spaces hoặc 1 tab
    print("Xuất sắc")  # Cùng mức thụt lề
```

#### Boolean expressions

```python
# Điều kiện đơn giản
x = 10
if x > 5:
    print("x lớn hơn 5")

# Điều kiện phức tạp
temperature = 25
humidity = 60
if temperature > 20 and humidity < 70:
    print("Thời tiết dễ chịu")

# Kiểm tra giá trị trong list/string
name = "Alice"
if "A" in name:
    print("Tên có chứa chữ A")

numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("Số 3 có trong danh sách")
```

#### Truthy và Falsy values

```python
# Falsy values (được coi là False)
if 0:           # False
    print("Không in")
if "":          # False
    print("Không in")
if []:          # False
    print("Không in")
if None:        # False
    print("Không in")

# Truthy values (được coi là True)
if 1:           # True
    print("Sẽ in")
if "hello":     # True
    print("Sẽ in")
if [1, 2]:      # True
    print("Sẽ in")
```

### 💻 Thực hành (30')

#### Bài tập 1: Kiểm tra điều kiện đơn giản

**Yêu cầu:** Kiểm tra các điều kiện về tuổi, điểm số và tính chất của số (chẵn/lẻ, dương/âm).

**File thực hành:** [problem030101.py](problem030101.py)

#### Bài tập 2: Kiểm tra tính hợp lệ

**Yêu cầu:** Kiểm tra tính hợp lệ của mật khẩu, email và số điện thoại.

**File thực hành:** [problem030102.py](problem030102.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 2: if-else và elif (45')

### 📚 Lý thuyết (20')

#### Cấu trúc if-else

```python
# if-else cơ bản
age = 16

if age >= 18:
    print("Được phép lái xe")
else:
    print("Chưa được phép lái xe")

# Có thể viết trên một dòng (ternary operator)
status = "adult" if age >= 18 else "minor"
print(status)
```

#### Cấu trúc elif (else if)

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Điểm: {score}, Xếp loại: {grade}")
```

#### Nhiều điều kiện phức tạp

```python
temperature = 25
weather = "sunny"
wind_speed = 10

if temperature > 30:
    if weather == "sunny":
        print("Nóng và nắng - nên ở trong nhà")
    else:
        print("Nóng nhưng không nắng")
elif temperature > 20:
    if wind_speed < 15:
        print("Thời tiết dễ chịu")
    else:
        print("Hơi mát nhưng có gió")
else:
    print("Trời lạnh")
```

#### So sánh chuỗi và xử lý case

```python
# So sánh chuỗi (case sensitive)
name = input("Nhập tên: ")

if name == "Admin":
    print("Chào admin!")
elif name.lower() == "guest":  # Không phân biệt hoa thường
    print("Chào khách!")
else:
    print(f"Chào {name}!")

# Kiểm tra nhiều giá trị
day = input("Nhập thứ trong tuần: ").lower()

if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Ngày làm việc")
elif day in ["saturday", "sunday"]:
    print("Cuối tuần")
else:
    print("Ngày không hợp lệ")
```

### 💻 Thực hành (25')

#### Bài tập 1: Hệ thống xếp loại

**Yêu cầu:** Xếp loại học sinh dựa trên điểm trung bình và xác định học bổng.

**File thực hành:** [problem030201.py](problem030201.py)

#### Bài tập 2: Máy tính thuế

**Yêu cầu:** Tính thuế thu nhập cá nhân theo bậc thang thuế Việt Nam.

**File thực hành:** [problem030202.py](problem030202.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 3: Nested if và logic phức tạp (45')

### 📚 Lý thuyết (15')

#### If lồng nhau (Nested if)

```python
# Ví dụ về nested if
age = 20
has_license = True
has_car = False

if age >= 18:
    print("Đủ tuổi lái xe")
    if has_license:
        print("Có bằng lái")
        if has_car:
            print("Có thể lái xe ngay")
        else:
            print("Cần mượn xe hoặc thuê xe")
    else:
        print("Cần thi bằng lái")
else:
    print("Chưa đủ tuổi lái xe")
```

#### Kết hợp điều kiện phức tạp

```python
# Kiểm tra tam giác hợp lệ
a, b, c = 3, 4, 5

if a > 0 and b > 0 and c > 0:
    if a + b > c and b + c > a and a + c > b:
        print("Là tam giác hợp lệ")

        # Phân loại tam giác
        if a == b == c:
            print("Tam giác đều")
        elif a == b or b == c or a == c:
            print("Tam giác cân")
        elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
            print("Tam giác vuông")
        else:
            print("Tam giác thường")
    else:
        print("Không phải tam giác hợp lệ")
else:
    print("Độ dài cạnh phải dương")
```

#### Short-circuit evaluation

```python
# Python đánh giá từ trái sang phải và dừng sớm
x = 0

# An toàn với short-circuit
if x != 0 and 10 / x > 2:
    print("x lớn hơn 5")

# Tương tự với or
if x == 0 or 10 / x < 2:
    print("x bằng 0 hoặc x > 5")

# Sử dụng trong validation
def safe_divide(a, b):
    if b != 0 and a / b > 1:
        return a / b
    else:
        return 0
```

### 💻 Thực hành (30')

#### Bài tập 1: Kiểm tra năm nhuận

**Yêu cầu:** Kiểm tra năm nhuận sử dụng nested if và giải thích lý do.

**File thực hành:** [problem030301.py](problem030301.py)

#### Bài tập 2: Game đoán số nâng cao

**Yêu cầu:** Tạo game đoán số với gợi ý thông minh và đánh giá hiệu suất.

**File thực hành:** [problem030302.py](problem030302.py)

---

☕ **Nghỉ giải lao 5 phút** ☕

---

## Phần 4: Conditional expressions và best practices (45')

### 📚 Lý thuyết (15')

#### Conditional expressions (Ternary operator)

```python
# Cú pháp: giá_trị_nếu_true if điều_kiện else giá_trị_nếu_false

age = 20
status = "adult" if age >= 18 else "minor"

# So sánh với if-else thông thường
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ví dụ khác
score = 85
grade = "Pass" if score >= 60 else "Fail"
message = "Excellent!" if score >= 90 else "Good job!" if score >= 80 else "Keep trying!"

# Trong function calls
print("Passed" if score >= 60 else "Failed")
max_value = a if a > b else b  # Tương đương max(a, b)
```

#### Best practices cho if statements

```python
# 1. Tránh so sánh với True/False
# Không tốt
if is_valid == True:
    pass

# Tốt
if is_valid:
    pass

# 2. Sử dụng in cho multiple values
# Không tốt
if day == "Saturday" or day == "Sunday":
    pass

# Tốt
if day in ["Saturday", "Sunday"]:
    pass

# 3. Sử dụng not in
if status not in ["pending", "processing"]:
    pass

# 4. Tránh nested if quá sâu
# Không tốt
if condition1:
    if condition2:
        if condition3:
            do_something()

# Tốt hơn - early return
if not condition1:
    return
if not condition2:
    return
if not condition3:
    return
do_something()
```

#### Xử lý lỗi với if

```python
# Kiểm tra input hợp lệ
def safe_divide(a, b):
    if b == 0:
        print("Lỗi: Không thể chia cho 0")
        return None
    return a / b

# Kiểm tra kiểu dữ liệu
def process_number(value):
    if not isinstance(value, (int, float)):
        print("Lỗi: Giá trị phải là số")
        return None

    if value < 0:
        print("Cảnh báo: Giá trị âm")

    return value * 2

# Validation input
def get_valid_age():
    while True:
        try:
            age = int(input("Nhập tuổi: "))
            if 0 <= age <= 150:
                return age
            else:
                print("Tuổi phải từ 0 đến 150")
        except ValueError:
            print("Vui lòng nhập số nguyên")
```

### 💻 Thực hành (30')

#### Bài tập 1: Hệ thống login

**Yêu cầu:** Tạo hệ thống đăng nhập với phân quyền và giới hạn số lần thử.

**File thực hành:** [problem030401.py](problem030401.py)

#### Bài tập 2: Máy tính BMI và tư vấn sức khỏe

**Yêu cầu:** Tính BMI và đưa ra lời khuyên sức khỏe dựa trên tuổi và giới tính.

**File thực hành:** [problem030402.py](problem030402.py)

---

## Bài tập về nhà

### Bài 1: Máy tính tiền điện

Viết chương trình tính tiền điện theo bậc thang:

- Bậc 1 (0-50 kWh): 1.678 đ/kWh
- Bậc 2 (51-100 kWh): 1.734 đ/kWh
- Bậc 3 (101-200 kWh): 2.014 đ/kWh
- Bậc 4 (201-300 kWh): 2.536 đ/kWh
- Bậc 5 (301-400 kWh): 2.834 đ/kWh
- Bậc 6 (>400 kWh): 2.927 đ/kWh

### Bài 2: Kiểm tra số hoàn hảo

Viết chương trình kiểm tra số hoàn hảo (số bằng tổng các ước số thực sự):

- Tìm tất cả ước số của n (trừ chính n)
- Tính tổng các ước số
- So sánh với n
- In ra các ước số nếu là số hoàn hảo

### Bài 3: Game "Kéo Búa Bao"

Viết game kéo búa bao với máy:

- Máy chọn ngẫu nhiên
- Người chơi nhập lựa chọn
- Xác định thắng/thua/hòa
- Đếm điểm và chơi nhiều lượt
- Hiển thị thống kê cuối game

### Gợi ý làm bài

1. Sử dụng elif cho các khoảng giá trị (bài 1)
2. Sử dụng vòng lặp để tìm ước số (bài 2)
3. Sử dụng random module và dictionary (bài 3)
4. Chú ý validation input cho tất cả bài

---

## Tổng kết Day 3

**Đã học:**

- Câu lệnh if cơ bản và boolean expressions
- Cấu trúc if-else và elif
- If lồng nhau (nested if)
- Conditional expressions (ternary operator)
- Best practices cho if statements
- Xử lý validation và error handling
- Ứng dụng thực tế: login system, health advisor

**Chuẩn bị cho Day 4:**

- Ôn lại cấu trúc if-else
- Thực hành với điều kiện phức tạp
- Làm xong bài tập về nhà
- Chuẩn bị học vòng lặp for
