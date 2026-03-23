class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        if not matrix:
            return []

        n=len(matrix)
        m=len(matrix[0])
        zeros_row=[False]*n
        zeros_column=[False]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    zeros_row[i]=True
                    zeros_column[j]=True
        for i in range(n):
            for j in range(m):
                if zeros_row[i] or zeros_column[j]:
                    matrix[i][j]=0
            
    
        