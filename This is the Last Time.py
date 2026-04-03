import heapq
x=int(input())
for i in range(x):
    n , k = map(int,input().split())
    casinos=[]

    for _ in range(n):
        l , r , real = map(int, input().split())
        casinos.append((l,r,real))

    casinos.sort()

    i=0
    cur=k
    heap=[]

    while True:
        while i<n and casinos[i][0] <= cur:
            l , r, real = casinos[i]
            heapq.heappush(heap,(-real,r))
            i+=1
        while heap and heap[0][1] < cur:
            heapq.heappop(heap)

        if not heap:
            break

        best_real = -heap[0][0]

        if best_real <= cur:
            break

        heapq.heappop(heap)
        cur = best_real

    print(cur)
    


