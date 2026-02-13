matrix=[]
for _ in range(5):
    y=[int(i) for i in input().split()]
    matrix.append(y)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]==1:
            op=abs(i-2)+abs(j-2)
print(op)
