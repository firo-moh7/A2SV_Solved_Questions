class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        n=len(mat)
        m=len(mat[0])
        ans=[]
        r=0
        c=0
        for i in range(n*m):
            ans.append(mat[r][c])
            if (r+c) % 2==0:
                if c==m-1:
                    r+=1
                elif r==0:
                    c+=1
                else:
                    r-=1
                    c+=1

            else:
                if r==n-1:
                    c+=1
                elif c==0:
                    r+=1
                else:
                    r+=1
                    c-=1
        return ans

                
                

        
        