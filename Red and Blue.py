x = int(input())
for _ in range(x):
    y = int(input())
    l = [int(i) for i in input().split()]

    sum_l = 0
    max_l = 0
    for i in l:
        sum_l += i
        max_l = max(max_l , sum_l)
    
    m = int(input())
    n = [int(i) for i in input().split()]

    sum_n = 0
    max_n = 0

    for j in n:
        sum_n += j
        max_n = max(sum_n , max_n)

    print(max_n + max_l)
