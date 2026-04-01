class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m=len(img)
        n=len(img[0])
        result=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                tot_sum=0
                count=0
                for x in range(max(i-1,0),min(m,i+2)):
                    for y in range(max(j-1,0),min(n,j+2)):
                        tot_sum+=img[x][y]
                        count+=1
                result[i][j]=tot_sum//count
        return result

    


        

        