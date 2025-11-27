# BWTREE - Solution

## Phân tích

Cây nhị phân với quy tắc:
- Gốc: đỉnh 1
- Đỉnh i có 2 con: 2i và 2i+1
- Cha của đỉnh i: i//2

Cần tìm LCA (Lowest Common Ancestor) của 2 đỉnh.

## Thuật toán

1. Đưa 2 đỉnh về cùng độ sâu bằng cách chia 2
2. Đồng thời đi lên cho đến khi gặp nhau

## Code

```python
def find_lca(u, v):
    """Tìm tổ tiên chung gần nhất của u và v"""
    # Đưa về cùng độ sâu
    while u != v:
        if u > v:
            u //= 2
        else:
            v //= 2
    return u

t = int(input())
for _ in range(t):
    u, v = map(int, input().split())
    print(find_lca(u, v))
```

## Code tối ưu hơn

```python
def find_lca(u, v):
    """Tìm LCA bằng bit manipulation"""
    # Tìm độ sâu của mỗi node
    def depth(x):
        return x.bit_length() - 1
    
    # Đưa về cùng độ sâu
    depth_u = depth(u)
    depth_v = depth(v)
    
    # Đưa node sâu hơn lên cùng độ sâu
    while depth_u > depth_v:
        u //= 2
        depth_u -= 1
    
    while depth_v > depth_u:
        v //= 2
        depth_v -= 1
    
    # Đồng thời đi lên cho đến khi gặp nhau
    while u != v:
        u //= 2
        v //= 2
    
    return u

t = int(input())
for _ in range(t):
    u, v = map(int, input().split())
    print(find_lca(u, v))
```

## Giải thích

1. Trong cây nhị phân này, cha của node i là i//2
2. Để tìm LCA, ta đưa 2 node về cùng độ sâu
3. Sau đó đồng thời đi lên cho đến khi gặp nhau
4. Độ phức tạp: O(log max(u,v))

**Độ phức tạp:** O(T × log(max(u,v)))