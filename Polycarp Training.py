x=int(input())
li=[int(i) for i in input().split()]
li.sort()
count=1
for i in range(len(li)):
    if li[i]>=count:
        count+=1
    

print(count-1)
