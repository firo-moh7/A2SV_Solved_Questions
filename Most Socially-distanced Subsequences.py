x = int(input())
for _ in range(x):
    y = int(input())
    l = [int(i) for i in input().split()]
    res = [l[0]]

    for i in range(1,len(l)-1):
        prev_diff = l[i] - l[i - 1]
        cur_diff = l[i + 1] - l[i]
        
        if prev_diff * cur_diff < 0:
            res.append(l[i])

    res.append(l[-1])

    print(len(res))
    print(*res)
