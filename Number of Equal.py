from collections import Counter
a,b=map(int,input().split())
arr1=[int(i) for i in input().split()]
arr2=[int(i) for i in input().split()]
freq=Counter(arr1)
count=0
for i in arr2:
    if i in freq:
        count+=freq[i]
print(count)
