n,k = map(int,input().split())
m = [int(i) for i in input().split()]
gaps =[]
for i in range(n-1):
    gaps.append(m[i+1]-m[i])
gaps.sort(reverse=True)
ans = m[-1] - m[0]
for i in range(k-1):
    ans-=gaps[i]

print(ans)
