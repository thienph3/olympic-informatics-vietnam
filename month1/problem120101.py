"""
Problem 120101: Standard library modules
Sử dụng các standard modules: os, sys, datetime, random, collections

Bài 1: OS và System Operations
- File system operations
- Environment variables
- System information

Bài 2: Date/Time và Random Operations
- Date/time manipulation
- Random number generation
- Collections utilities
"""

import os
import sys
import datetime
import random
import collections
from pathlib import Path

# OS Module Operations
def explore_os_module():
    """Explore os module functionality"""
    print("=== OS Module Operations ===")
    
    # Current directory operations
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    
    # List directory contents
    try:
        files = os.listdir('.')
        print(f"Files in current directory: {len(files)}")
        for file in files[:5]:  # Show first 5
            print(f"  {file}")
        if len(files) > 5:
            print(f"  ... and {len(files) - 5} more")
    except PermissionError:
        print("Permission denied to list directory")
    
    # Environment variables
    print(f"\nEnvironment variables:")
    print(f"PATH exists: {'PATH' in os.environ}")
    print(f"HOME/USERPROFILE: {os.environ.get('HOME', os.environ.get('USERPROFILE', 'Not found'))}")
    
    # File path operations
    file_path = os.path.join("folder", "subfolder", "file.txt")
    print(f"Joined path: {file_path}")
    print(f"Directory name: {os.path.dirname(file_path)}")
    print(f"Base name: {os.path.basename(file_path)}")
    print(f"Split extension: {os.path.splitext(file_path)}")
    
    # File existence and properties
    current_file = __file__
    print(f"\nCurrent file: {current_file}")
    print(f"File exists: {os.path.exists(current_file)}")
    print(f"Is file: {os.path.isfile(current_file)}")
    print(f"Is directory: {os.path.isdir(current_file)}")
    
    if os.path.exists(current_file):
        stat_info = os.stat(current_file)
        print(f"File size: {stat_info.st_size} bytes")
        print(f"Last modified: {datetime.datetime.fromtimestamp(stat_info.st_mtime)}")

def explore_sys_module():
    """Explore sys module functionality"""
    print("\n=== SYS Module Operations ===")
    
    # Python version info
    print(f"Python version: {sys.version}")
    print(f"Version info: {sys.version_info}")
    print(f"Platform: {sys.platform}")
    
    # Command line arguments
    print(f"Script name: {sys.argv[0]}")
    print(f"Arguments: {sys.argv[1:] if len(sys.argv) > 1 else 'None'}")
    
    # Module search path
    print(f"Module search paths ({len(sys.path)} total):")
    for i, path in enumerate(sys.path[:3]):
        print(f"  {i+1}. {path}")
    if len(sys.path) > 3:
        print(f"  ... and {len(sys.path) - 3} more paths")
    
    # Memory and performance info
    print(f"Recursion limit: {sys.getrecursionlimit()}")
    
    # Standard streams
    print(f"stdin: {type(sys.stdin)}")
    print(f"stdout: {type(sys.stdout)}")
    print(f"stderr: {type(sys.stderr)}")

def pathlib_examples():
    """Modern path handling with pathlib"""
    print("\n=== Pathlib Examples ===")
    
    # Create Path objects
    current_path = Path('.')
    file_path = Path(__file__)
    
    print(f"Current path: {current_path.absolute()}")
    print(f"File path: {file_path}")
    print(f"File name: {file_path.name}")
    print(f"File stem: {file_path.stem}")
    print(f"File suffix: {file_path.suffix}")
    print(f"Parent directory: {file_path.parent}")
    
    # Path operations
    new_path = current_path / "subfolder" / "file.txt"
    print(f"Joined path: {new_path}")
    
    # Check path properties
    print(f"File exists: {file_path.exists()}")
    print(f"Is file: {file_path.is_file()}")
    print(f"Is directory: {file_path.is_dir()}")
    
    # List directory contents
    try:
        python_files = list(current_path.glob("*.py"))
        print(f"Python files: {len(python_files)}")
        for py_file in python_files[:3]:
            print(f"  {py_file.name}")
    except Exception as e:
        print(f"Error listing files: {e}")

# DateTime Module Operations
def explore_datetime_module():
    """Explore datetime module functionality"""
    print("\n=== DateTime Module Operations ===")
    
    # Current date and time
    now = datetime.datetime.now()
    today = datetime.date.today()
    current_time = datetime.datetime.now().time()
    
    print(f"Current datetime: {now}")
    print(f"Today's date: {today}")
    print(f"Current time: {current_time}")
    
    # Formatting dates
    print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Formatted date: {now.strftime('%B %d, %Y')}")
    print(f"Formatted date: {now.strftime('%A, %I:%M %p')}")
    
    # Date arithmetic
    tomorrow = today + datetime.timedelta(days=1)
    last_week = today - datetime.timedelta(weeks=1)
    next_month = today + datetime.timedelta(days=30)
    
    print(f"Tomorrow: {tomorrow}")
    print(f"Last week: {last_week}")
    print(f"Next month (approx): {next_month}")
    
    # Time differences
    future_date = datetime.datetime(2025, 1, 1)
    time_diff = future_date - now
    print(f"Days until 2025: {time_diff.days}")
    
    # Parse date strings
    date_string = "2024-12-25"
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    print(f"Parsed date: {parsed_date}")
    
    # Weekday operations
    print(f"Today is: {today.strftime('%A')}")
    print(f"Day of week (0=Monday): {today.weekday()}")
    print(f"Day of week (1=Monday): {today.isoweekday()}")

def time_calculations():
    """Various time calculations"""
    print("\n=== Time Calculations ===")
    
    # Age calculation
    def calculate_age(birth_date):
        today = datetime.date.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age
    
    birth_date = datetime.date(2000, 5, 15)
    age = calculate_age(birth_date)
    print(f"Age for birth date {birth_date}: {age} years")
    
    # Working days calculation
    def count_working_days(start_date, end_date):
        current = start_date
        working_days = 0
        while current <= end_date:
            if current.weekday() < 5:  # Monday = 0, Friday = 4
                working_days += 1
            current += datetime.timedelta(days=1)
        return working_days
    
    start = datetime.date(2024, 1, 1)
    end = datetime.date(2024, 1, 31)
    working_days = count_working_days(start, end)
    print(f"Working days in January 2024: {working_days}")
    
    # Time zones (basic)
    utc_now = datetime.datetime.utcnow()
    print(f"UTC time: {utc_now}")
    print(f"Local time: {datetime.datetime.now()}")

# Random Module Operations
def explore_random_module():
    """Explore random module functionality"""
    print("\n=== Random Module Operations ===")
    
    # Set seed for reproducible results
    random.seed(42)
    
    # Basic random numbers
    print(f"Random float [0,1): {random.random()}")
    print(f"Random int [1,10]: {random.randint(1, 10)}")
    print(f"Random int [0,10): {random.randrange(10)}")
    print(f"Random int [2,10) step 2: {random.randrange(2, 10, 2)}")
    
    # Random choices
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    print(f"Random choice: {random.choice(colors)}")
    print(f"Random sample (3): {random.sample(colors, 3)}")
    
    # Weighted choices (Python 3.6+)
    weights = [1, 2, 3, 2, 1]  # Higher weight = more likely
    weighted_choices = random.choices(colors, weights=weights, k=5)
    print(f"Weighted choices: {weighted_choices}")
    
    # Shuffle
    deck = list(range(1, 14))  # Cards 1-13
    print(f"Original deck: {deck}")
    random.shuffle(deck)
    print(f"Shuffled deck: {deck}")
    
    # Random distributions
    print(f"Gaussian (μ=0, σ=1): {random.gauss(0, 1):.3f}")
    print(f"Uniform [5,15]: {random.uniform(5, 15):.3f}")
    
    # Generate random data
    def generate_random_data(n=10):
        return {
            'integers': [random.randint(1, 100) for _ in range(n)],
            'floats': [round(random.uniform(0, 1), 3) for _ in range(n)],
            'choices': [random.choice(['A', 'B', 'C']) for _ in range(n)]
        }
    
    data = generate_random_data(5)
    print(f"Random data sample: {data}")

# Collections Module Operations
def explore_collections_module():
    """Explore collections module functionality"""
    print("\n=== Collections Module Operations ===")
    
    # Counter
    text = "hello world programming"
    char_count = collections.Counter(text)
    print(f"Character frequency: {char_count}")
    print(f"Most common 3: {char_count.most_common(3)}")
    
    word_list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    word_count = collections.Counter(word_list)
    print(f"Word frequency: {word_count}")
    
    # defaultdict
    dd = collections.defaultdict(list)
    data = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'cherry')]
    
    for category, item in data:
        dd[category].append(item)
    
    print(f"Grouped data: {dict(dd)}")
    
    # defaultdict with int (for counting)
    counter_dd = collections.defaultdict(int)
    for char in "programming":
        counter_dd[char] += 1
    print(f"Character count with defaultdict: {dict(counter_dd)}")
    
    # deque (double-ended queue)
    dq = collections.deque([1, 2, 3, 4, 5])
    print(f"Original deque: {dq}")
    
    dq.appendleft(0)
    dq.append(6)
    print(f"After append operations: {dq}")
    
    left_item = dq.popleft()
    right_item = dq.pop()
    print(f"Popped items: left={left_item}, right={right_item}")
    print(f"Final deque: {dq}")
    
    # deque with maxlen (circular buffer)
    circular = collections.deque(maxlen=3)
    for i in range(5):
        circular.append(i)
        print(f"After adding {i}: {circular}")
    
    # namedtuple
    Point = collections.namedtuple('Point', ['x', 'y'])
    p1 = Point(1, 2)
    p2 = Point(x=3, y=4)
    
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Access by name: p1.x = {p1.x}, p1.y = {p1.y}")
    print(f"Access by index: p1[0] = {p1[0]}, p1[1] = {p1[1]}")
    
    # namedtuple methods
    print(f"Point fields: {p1._fields}")
    p3 = p1._replace(x=10)
    print(f"Replaced point: {p3}")

# Test all functions
if __name__ == "__main__":
    explore_os_module()
    explore_sys_module()
    pathlib_examples()
    explore_datetime_module()
    time_calculations()
    explore_random_module()
    explore_collections_module()
    
    print("\n=== Bài tập thực hành ===")
    print("1. Tạo file manager với os operations")
    print("2. Build date calculator application")
    print("3. Create random data generator")
    print("4. Implement text analysis với collections")