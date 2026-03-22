t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()
    
    pos = x
    first_hit = -1
    
    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            first_hit = i + 1
            break
    
   
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
  
    pos = 0
    cycle_len = -1
    
    for i in range(n):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1
        
        if pos == 0:
            cycle_len = i + 1
            break
    
    
    if cycle_len == -1:
        print(1)
        continue
    
    remaining = k - first_hit
    answer = 1 + (remaining // cycle_len)
    
    print(answer)
