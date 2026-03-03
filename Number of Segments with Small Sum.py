a,b=map(int,input().split())
n=list(map(int,input().split()))
seg=0
left=0
cur_sum=0
for i in range(a):
    cur_sum+=n[i]
    
    while cur_sum>b:
        cur_sum-=n[left]
        left+=1
    seg+=(i-left+1)
    
print(seg)
