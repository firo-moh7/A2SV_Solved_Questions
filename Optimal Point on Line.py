x = int(input())
n=[int(i) for i in input().split()]
n.sort()
print(n[(x-1)//2])

