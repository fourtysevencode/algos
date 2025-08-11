def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 = down, -1 = up
    
    for char in text:
        fence[rail].append(char)
        rail += direction
        
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    return ''.join(''.join(row) for row in fence)