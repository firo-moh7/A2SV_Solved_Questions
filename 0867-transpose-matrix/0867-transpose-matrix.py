class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        column=len(matrix[0])
        new_matrix=[]
        
        for i in range(column):
            l=[]
            for j in range(row):
                l.append(matrix[j][i])
            new_matrix.append(l)
                
        return new_matrix
        
      
        