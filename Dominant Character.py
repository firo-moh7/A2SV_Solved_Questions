x=int(input())
for _ in range(x):
    y=int(input())
    st=input()
    min_ans=float('inf')

    for i in range(y-1):
        if st[i:i+2] in 'aa':
            min_ans=min(min_ans,2)
    
    for i in range(y-2):
        if st[i:i+3] in ['aba','aca']:
            min_ans=min(min_ans,3)
    
    for i in range(y-3):
        if st[i:i+4] in ['abca','acba']:
            min_ans=min(min_ans,4)
    
    for i in range(y-6):
        if st[i:i+7] in ['abbacca','accabba']:
            min_ans=min(min_ans,7)
    
    print(min_ans if min_ans!=float('inf') else -1)
