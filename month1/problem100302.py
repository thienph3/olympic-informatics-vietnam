"""
Problem 100302: Quản lý state với global variables
Sử dụng global variables để quản lý trạng thái chương trình

Bài 1: Game State Management
- Quản lý trạng thái game
- Player stats và inventory

Bài 2: Application Configuration
- Settings management
- User preferences và session data
"""

# Game State Variables
game_state = {
    "level": 1,
    "score": 0,
    "lives": 3,
    "game_over": False,
    "paused": False
}

player_stats = {
    "name": "Player",
    "health": 100,
    "mana": 50,
    "experience": 0,
    "gold": 100
}

inventory = []
achievements = []

# Game Functions
def start_new_game(player_name="Player"):
    """Bắt đầu game mới"""
    global game_state, player_stats, inventory, achievements
    
    game_state = {
        "level": 1,
        "score": 0,
        "lives": 3,
        "game_over": False,
        "paused": False
    }
    
    player_stats = {
        "name": player_name,
        "health": 100,
        "mana": 50,
        "experience": 0,
        "gold": 100
    }
    
    inventory.clear()
    achievements.clear()
    
    print(f"New game started for {player_name}!")

def add_score(points):
    """Thêm điểm"""
    global game_state
    game_state["score"] += points
    
    # Level up every 1000 points
    new_level = (game_state["score"] // 1000) + 1
    if new_level > game_state["level"]:
        level_up(new_level)

def level_up(new_level):
    """Tăng level"""
    global game_state, player_stats
    
    old_level = game_state["level"]
    game_state["level"] = new_level
    
    # Bonus stats
    player_stats["health"] += 20
    player_stats["mana"] += 10
    player_stats["gold"] += 50
    
    print(f"Level up! {old_level} -> {new_level}")
    check_achievement("level_up", new_level)

def take_damage(damage):
    """Nhận damage"""
    global player_stats, game_state
    
    player_stats["health"] -= damage
    if player_stats["health"] <= 0:
        player_stats["health"] = 0
        lose_life()

def lose_life():
    """Mất mạng"""
    global game_state, player_stats
    
    game_state["lives"] -= 1
    player_stats["health"] = 100  # Respawn with full health
    
    if game_state["lives"] <= 0:
        game_over()
    else:
        print(f"Life lost! {game_state['lives']} lives remaining")

def game_over():
    """Game over"""
    global game_state
    game_state["game_over"] = True
    print("GAME OVER!")
    print(f"Final Score: {game_state['score']}")
    print(f"Level Reached: {game_state['level']}")

def add_item(item_name, quantity=1):
    """Thêm item vào inventory"""
    global inventory
    
    # Tìm item existing
    for item in inventory:
        if item["name"] == item_name:
            item["quantity"] += quantity
            return
    
    # Thêm item mới
    inventory.append({"name": item_name, "quantity": quantity})
    print(f"Added {quantity} {item_name} to inventory")

def use_item(item_name, quantity=1):
    """Sử dụng item"""
    global inventory, player_stats
    
    for item in inventory:
        if item["name"] == item_name:
            if item["quantity"] >= quantity:
                item["quantity"] -= quantity
                
                # Item effects
                if item_name == "Health Potion":
                    player_stats["health"] = min(100, player_stats["health"] + 30)
                elif item_name == "Mana Potion":
                    player_stats["mana"] = min(100, player_stats["mana"] + 20)
                
                # Remove if quantity is 0
                if item["quantity"] == 0:
                    inventory.remove(item)
                
                print(f"Used {quantity} {item_name}")
                return True
    
    print(f"Not enough {item_name} in inventory")
    return False

def check_achievement(achievement_type, value):
    """Kiểm tra achievement"""
    global achievements
    
    achievement_name = None
    
    if achievement_type == "level_up":
        if value == 5:
            achievement_name = "Novice Explorer"
        elif value == 10:
            achievement_name = "Experienced Adventurer"
        elif value == 20:
            achievement_name = "Master Explorer"
    
    elif achievement_type == "score":
        if value >= 10000:
            achievement_name = "High Scorer"
        elif value >= 50000:
            achievement_name = "Score Master"
    
    if achievement_name and achievement_name not in achievements:
        achievements.append(achievement_name)
        print(f"🏆 Achievement Unlocked: {achievement_name}")

# Application Configuration
app_config = {
    "theme": "light",
    "language": "en",
    "auto_save": True,
    "sound_enabled": True,
    "difficulty": "normal"
}

user_preferences = {
    "username": "guest",
    "email": "",
    "notifications": True,
    "privacy_mode": False
}

session_data = {
    "login_time": None,
    "last_activity": None,
    "session_id": None,
    "is_authenticated": False
}

# Configuration Functions
def load_config(config_dict):
    """Load configuration từ dictionary"""
    global app_config
    app_config.update(config_dict)
    print("Configuration loaded")

def update_setting(key, value):
    """Cập nhật setting"""
    global app_config
    if key in app_config:
        app_config[key] = value
        print(f"Setting updated: {key} = {value}")
        return True
    return False

def get_setting(key, default=None):
    """Lấy setting value"""
    return app_config.get(key, default)

def reset_settings():
    """Reset về default settings"""
    global app_config
    app_config = {
        "theme": "light",
        "language": "en",
        "auto_save": True,
        "sound_enabled": True,
        "difficulty": "normal"
    }
    print("Settings reset to default")

def login_user(username, email=""):
    """User login"""
    global user_preferences, session_data
    import datetime
    import uuid
    
    user_preferences["username"] = username
    user_preferences["email"] = email
    
    session_data["login_time"] = datetime.datetime.now()
    session_data["last_activity"] = datetime.datetime.now()
    session_data["session_id"] = str(uuid.uuid4())[:8]
    session_data["is_authenticated"] = True
    
    print(f"User {username} logged in")

def logout_user():
    """User logout"""
    global session_data
    
    username = user_preferences["username"]
    session_data = {
        "login_time": None,
        "last_activity": None,
        "session_id": None,
        "is_authenticated": False
    }
    
    print(f"User {username} logged out")

def update_activity():
    """Cập nhật last activity"""
    global session_data
    import datetime
    
    if session_data["is_authenticated"]:
        session_data["last_activity"] = datetime.datetime.now()

def get_session_info():
    """Lấy thông tin session"""
    if session_data["is_authenticated"]:
        return {
            "username": user_preferences["username"],
            "session_id": session_data["session_id"],
            "login_time": session_data["login_time"],
            "last_activity": session_data["last_activity"]
        }
    return None

# Test functions
if __name__ == "__main__":
    print("=== Bài 1: Game State Management ===")
    
    # Start new game
    start_new_game("Alice")
    
    # Game actions
    print(f"\nInitial state: {game_state}")
    print(f"Player stats: {player_stats}")
    
    # Add score and level up
    add_score(500)
    add_score(600)  # Should trigger level up
    
    # Add items
    add_item("Health Potion", 3)
    add_item("Mana Potion", 2)
    add_item("Sword", 1)
    
    print(f"Inventory: {inventory}")
    
    # Take damage and use potion
    print(f"\nHealth before damage: {player_stats['health']}")
    take_damage(40)
    print(f"Health after damage: {player_stats['health']}")
    
    use_item("Health Potion")
    print(f"Health after potion: {player_stats['health']}")
    
    # More scoring for achievements
    add_score(9000)  # Should unlock achievement
    
    print(f"Final game state: {game_state}")
    print(f"Achievements: {achievements}")
    
    print("\n=== Bài 2: Application Configuration ===")
    
    # Test configuration
    print(f"Initial config: {app_config}")
    
    # Update settings
    update_setting("theme", "dark")
    update_setting("difficulty", "hard")
    
    print(f"Theme: {get_setting('theme')}")
    print(f"Sound: {get_setting('sound_enabled')}")
    
    # User login
    login_user("john_doe", "john@example.com")
    print(f"User preferences: {user_preferences}")
    
    # Session info
    import time
    time.sleep(1)  # Simulate activity
    update_activity()
    
    session_info = get_session_info()
    print(f"Session info: {session_info}")
    
    # Logout
    logout_user()
    print(f"Session after logout: {get_session_info()}")
    
    # Reset settings
    reset_settings()
    print(f"Config after reset: {app_config}")

    print("\n=== Bài tập thực hành ===")
    print("1. Tạo shopping cart management system")
    print("2. Implement simple chat room với user states")
    print("3. Tạo todo list với categories và priorities")
    print("4. Build simple banking system với account states")