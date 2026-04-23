from collections import Counter
x = int(input())
for _ in range(x):
    n , k = map(int,input().split())
    l = input()
    m = 0
    for i in range(k):
        if l[i] == 'W':
            m += 1

    min_m = m
    
    left = 0
    for i in range(k , n):
        if l[i] == 'W':
            m += 1
        elif l[left] == 'W':
            m -= 1
        left += 1
        min_m = min(m,min_m)
        
    print(min_m)

