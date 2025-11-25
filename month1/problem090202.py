# Problem 09.02.02: Xử lý văn bản và parsing

print("=== XỬ LÝ VĂN BẢN VÀ PARSING ===")

# Bài 1: Phân tích văn bản
print("1. Phân tích văn bản:")

text = """
Python is a high-level programming language. 
It is easy to learn and powerful to use.
Python supports multiple programming paradigms.
Many companies use Python for web development, data science, and automation.
"""

print(f"Văn bản gốc:\n{text}")

# Làm sạch văn bản
cleaned_text = text.strip()
print(f"Sau khi làm sạch: {len(cleaned_text)} ký tự")

# Đếm câu (dựa vào dấu chấm)
sentences = [s.strip() for s in cleaned_text.split('.') if s.strip()]
print(f"Số câu: {len(sentences)}")

# Đếm từ
words = cleaned_text.split()
print(f"Số từ: {len(words)}")

# Đếm ký tự (không kể khoảng trắng)
chars_no_space = len(cleaned_text.replace(' ', '').replace('\n', ''))
print(f"Số ký tự (không kể space): {chars_no_space}")

# Từ dài nhất và ngắn nhất
word_lengths = [(word.strip('.,'), len(word.strip('.,'))) for word in words]
longest_word = max(word_lengths, key=lambda x: x[1])
shortest_word = min(word_lengths, key=lambda x: x[1])
print(f"Từ dài nhất: '{longest_word[0]}' ({longest_word[1]} ký tự)")
print(f"Từ ngắn nhất: '{shortest_word[0]}' ({shortest_word[1]} ký tự)")

# Bài 2: Parsing CSV data
print("\n2. Parsing CSV data:")

csv_data = """Name,Age,City,Salary
Alice,25,New York,50000
Bob,30,Los Angeles,60000
Charlie,35,Chicago,55000
Diana,28,Houston,52000"""

print("Dữ liệu CSV:")
print(csv_data)

lines = csv_data.strip().split('\n')
header = lines[0].split(',')
print(f"\nHeader: {header}")

# Parse từng dòng
employees = []
for line in lines[1:]:
    values = line.split(',')
    employee = {}
    for i, value in enumerate(values):
        if header[i] in ['Age', 'Salary']:
            employee[header[i]] = int(value)
        else:
            employee[header[i]] = value
    employees.append(employee)

print("\nDữ liệu đã parse:")
for emp in employees:
    print(f"  {emp}")

# Thống kê
total_salary = sum(emp['Salary'] for emp in employees)
avg_salary = total_salary / len(employees)
print(f"\nTổng lương: ${total_salary:,}")
print(f"Lương trung bình: ${avg_salary:,.2f}")

# Bài 3: Xử lý log files
print("\n3. Xử lý log files:")

log_data = """
2024-01-15 10:30:25 INFO User login successful: alice@example.com
2024-01-15 10:31:12 ERROR Database connection failed
2024-01-15 10:32:05 INFO User logout: alice@example.com
2024-01-15 10:33:18 WARNING Low disk space: 85% used
2024-01-15 10:34:22 INFO User login successful: bob@example.com
2024-01-15 10:35:45 ERROR File not found: /path/to/file.txt
"""

print("Log data:")
print(log_data.strip())

# Parse log entries
log_entries = []
for line in log_data.strip().split('\n'):
    if line.strip():
        parts = line.split(' ', 3)  # Split thành 4 phần: date, time, level, message
        if len(parts) >= 4:
            date, time, level, message = parts
            log_entries.append({
                'date': date,
                'time': time,
                'level': level,
                'message': message
            })

print(f"\nĐã parse {len(log_entries)} log entries")

# Thống kê theo level
level_counts = {}
for entry in log_entries:
    level = entry['level']
    level_counts[level] = level_counts.get(level, 0) + 1

print("Thống kê theo level:")
for level, count in level_counts.items():
    print(f"  {level}: {count}")

# Tìm lỗi
errors = [entry for entry in log_entries if entry['level'] == 'ERROR']
print(f"\nCác lỗi ({len(errors)}):")
for error in errors:
    print(f"  {error['time']}: {error['message']}")

# Bài 4: URL parsing
print("\n4. URL parsing:")

urls = [
    "https://www.example.com/path/to/page?param1=value1&param2=value2",
    "http://subdomain.site.org:8080/api/users/123",
    "ftp://files.company.com/documents/report.pdf",
    "https://search.engine.com/search?q=python+programming&lang=en"
]

def parse_url(url):
    """Parse URL thành các thành phần"""
    result = {}
    
    # Protocol
    if '://' in url:
        protocol, rest = url.split('://', 1)
        result['protocol'] = protocol
    else:
        rest = url
        result['protocol'] = None
    
    # Query parameters
    if '?' in rest:
        rest, query_string = rest.split('?', 1)
        params = {}
        for param in query_string.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                params[key] = value
        result['params'] = params
    else:
        result['params'] = {}
    
    # Host và path
    if '/' in rest:
        host_part, path = rest.split('/', 1)
        result['path'] = '/' + path
    else:
        host_part = rest
        result['path'] = '/'
    
    # Port
    if ':' in host_part and not host_part.count(':') > 1:
        host, port = host_part.split(':')
        result['host'] = host
        result['port'] = int(port)
    else:
        result['host'] = host_part
        result['port'] = None
    
    return result

print("URL parsing:")
for url in urls:
    print(f"\nURL: {url}")
    parsed = parse_url(url)
    for key, value in parsed.items():
        print(f"  {key}: {value}")

# Bài 5: Configuration file parsing
print("\n5. Configuration file parsing:")

config_text = """
# Database configuration
db_host = localhost
db_port = 5432
db_name = myapp
db_user = admin

# Server settings
server_port = 8080
debug_mode = true
max_connections = 100

# Features
enable_logging = true
log_level = INFO
"""

print("Config file:")
print(config_text)

def parse_config(config_text):
    """Parse simple config file"""
    config = {}
    
    for line in config_text.split('\n'):
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            continue
        
        # Parse key = value
        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            # Convert types
            if value.lower() in ['true', 'false']:
                value = value.lower() == 'true'
            elif value.isdigit():
                value = int(value)
            
            config[key] = value
    
    return config

config = parse_config(config_text)
print("\nParsed configuration:")
for key, value in config.items():
    print(f"  {key}: {value} ({type(value).__name__})")

# Bài 6: Template processing
print("\n6. Template processing:")

template = """
Hello {name},

Thank you for your order #{order_id}.
Your order total is ${total:.2f}.

Items ordered:
{items}

Estimated delivery: {delivery_date}

Best regards,
{company_name}
"""

# Dữ liệu để fill template
order_data = {
    'name': 'John Doe',
    'order_id': '12345',
    'total': 99.99,
    'items': '- Python Programming Book\n- Wireless Mouse\n- Coffee Mug',
    'delivery_date': '2024-01-20',
    'company_name': 'TechStore Inc.'
}

print("Template:")
print(template)

print("Filled template:")
filled_template = template.format(**order_data)
print(filled_template)

# Bài 7: Word frequency analysis
print("\n7. Word frequency analysis:")

sample_text = """
Python is a programming language that lets you work quickly and integrate systems more effectively.
Python is powerful and fast, plays well with others, runs everywhere, is friendly and easy to learn.
Python is open source and free to use, even for commercial products.
"""

print("Sample text for analysis:")
print(sample_text)

# Làm sạch và tách từ
words = sample_text.lower().replace(',', '').replace('.', '').split()
print(f"Total words: {len(words)}")

# Đếm tần suất
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Sắp xếp theo tần suất
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

print("\nTop 10 most frequent words:")
for i, (word, freq) in enumerate(sorted_words[:10], 1):
    print(f"  {i:2d}. '{word}': {freq} times")

# Từ duy nhất (xuất hiện 1 lần)
unique_words = [word for word, freq in word_freq.items() if freq == 1]
print(f"\nUnique words ({len(unique_words)}): {unique_words[:10]}...")

# Bài 8: Data validation
print("\n8. Data validation:")

def validate_email(email):
    """Validate email format"""
    if '@' not in email:
        return False, "Missing @ symbol"
    
    parts = email.split('@')
    if len(parts) != 2:
        return False, "Multiple @ symbols"
    
    username, domain = parts
    
    if not username:
        return False, "Empty username"
    
    if '.' not in domain:
        return False, "Domain missing TLD"
    
    return True, "Valid email"

def validate_phone(phone):
    """Validate phone number"""
    # Remove common separators
    cleaned = phone.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    
    if not cleaned.isdigit():
        return False, "Contains non-digit characters"
    
    if len(cleaned) < 10:
        return False, "Too short"
    
    if len(cleaned) > 15:
        return False, "Too long"
    
    return True, "Valid phone number"

# Test validation
test_data = [
    ("emails", ["user@example.com", "invalid-email", "test@", "@domain.com"], validate_email),
    ("phones", ["123-456-7890", "(555) 123-4567", "12345", "abc-def-ghij"], validate_phone)
]

for data_type, test_values, validator in test_data:
    print(f"\nValidating {data_type}:")
    for value in test_values:
        is_valid, message = validator(value)
        status = "✓" if is_valid else "✗"
        print(f"  {status} '{value}': {message}")