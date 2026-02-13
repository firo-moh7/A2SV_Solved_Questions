class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        column=len(matrix[0])
        new_matrix=[[0]*row for i in range(column)]
        
        for i in range(column):
            for j in range(row):
                new_matrix[i][j]=matrix[j][i]
        return new_matrix
        
      
        