# BeginnerFreeContest 42 - RAINBOW

**Thể loại:** Graph  
**Độ khó:** 750

## Đề bài

Một vị vua đang trên đường trở về vương quốc của mình thì chợt nhận ra mình đã lạc vào một bàn cờ có chiều dài 10⁹ và chiều rộng 10⁹. Bàn cờ được đánh số từ 1 đến 10⁹ theo từng hàng từ trên xuống và theo từng cột từ trái sang. Vị trí tại dòng i và cột j được định nghĩa là tọa độ (i, j).

Nhà vua được biết một số ô trên bàn cờ "allow". Những ô này được xác định bằng n đoạn con. Mỗi đoạn con biểu diễn ba số nguyên rᵢ, aᵢ, bᵢ (aᵢ ≤ bᵢ) cho biết rằng các ô của các cột liên tiếp từ aᵢ đến bᵢ tại dòng rᵢ là các ô "allow".

Nhà vua đang đứng ở ô x₀, y₀ và rất gấp rút để trở về. Bạn hãy giúp nhà vua tìm một đường đi qua ít ô nhất để có thể tới vị trí x₁, y₁. Biết nhà vua chỉ có thể di chuyển trong các ô "allow". Nhà vua có thể di chuyển tới bất kì ô "allow" nào đó nếu ô đó có ít nhất một điểm chung với ô đang đứng.

Dữ liệu được đảm bảo rằng điểm đầu và cuối của nhà vua nằm trong bàn cờ, trên các ô cho phép và không trùng nhau. Thêm vào đó, tổng số ô "allow" trong bộ dữ liệu không vượt quá 10⁵.

## Dữ liệu

- Dòng thứ nhất chứa bốn số tự nhiên x₀, y₀, x₁, y₁ (1 ≤ x₀, y₀, x₁, y₁ ≤ 10⁹) - vị trí ban đầu và kết thúc của nhà vua.
- Dòng thứ hai chứa duy nhất một số n (1 ≤ n ≤ 10⁵) - số đoạn con của bộ dữ liệu.
- n dòng tiếp theo, mỗi dòng chứa ba số rᵢ, aᵢ, bᵢ (1 ≤ rᵢ, aᵢ, bᵢ ≤ 10⁹, aᵢ ≤ bᵢ) - các cột từ aᵢ đến bᵢ trên dòng rᵢ có thể đi được.

## Kết quả

Nếu như không có đường đi, in ra -1. Ngược lại, in ra số bước đi ít nhất để nhà vua ở vị trí bắt đầu có thể tới được vị trí kết thúc.

## Ví dụ

**Input:**
```
5 7 6 11
3
5 3 8
6 7 11
1 1 1
```

**Output:**
```
1
```

**Input:**
```
1 1 1 1
1
2 6 10
```

**Output:**
```
-1
```