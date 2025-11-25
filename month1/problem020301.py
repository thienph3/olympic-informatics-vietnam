# Problem 02.03.01: Thao tác gán
print("=== THAO TÁC GÁN ===")

# Khởi tạo
score = 100
lives = 3
multiplier = 1

print(f"Điểm ban đầu: {score}")
print(f"Mạng: {lives}")
print(f"Hệ số nhân: {multiplier}")

# Mô phỏng game
print("\n--- Vòng 1: Được 50 điểm ---")
score += 50
print(f"Điểm hiện tại: {score}")

print("\n--- Vòng 2: Mất 1 mạng, điểm x2 ---")
lives -= 1
multiplier *= 2
score *= multiplier
print(f"Mạng còn lại: {lives}")
print(f"Hệ số nhân: {multiplier}")
print(f"Điểm sau khi nhân: {score}")

print("\n--- Vòng 3: Chia đôi điểm ---")
score //= 2
print(f"Điểm cuối: {score}")