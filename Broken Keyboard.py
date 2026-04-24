t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)
    
    i = 0
    working = set()
    
    while i < n:
        j = i
        
        # count length of this block
        while j < n and s[j] == s[i]:
            j += 1
        
        length = j - i
        
        # if odd → definitely working
        if length % 2 == 1:
            working.add(s[i])
        
        i = j  # move to next block
    
    # print sorted result
    print("".join(sorted(working)))
