m , k = map(int,input().split())
l = [int(i) for i in input().split()]
n = len(l)
freq = {}
left = 0
tot = 0
distinict = 0
for i in range(n):
    if l[i] not in freq or freq[l[i]] == 0:
        distinict += 1

    freq[l[i]] = freq.get(l[i] , 0) + 1
    
    while distinict > k:
        freq[l[left]] -= 1
        if freq[l[left]] == 0:
            distinict -= 1
        left += 1
       
    tot += (i - left + 1)
print(tot)
