from collections import defaultdict
a,b=map(int,input().split())
x=[int(i) for i in input().split()]
left=0
distinict=0
best_r=0
best_l=0
best_len=0
dict_x=defaultdict(int)
for i in range(a):
    if dict_x[x[i]]==0:
        distinict+=1
    dict_x[x[i]]+=1
    
    while distinict>b:
        dict_x[x[left]]-=1
        if dict_x[x[left]]==0:
            distinict-=1
        left+=1
    if i-left+1>best_len:
        best_len=i-left+1
        best_r=i
        best_l=left
print(best_l+1,best_r+1)
    
