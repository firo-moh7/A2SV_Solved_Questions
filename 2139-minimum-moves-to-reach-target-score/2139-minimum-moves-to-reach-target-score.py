class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        x=0
        while target > 1:
            if target%2==0 and maxDoubles>0:
                target//=2
                x+=1
                maxDoubles-=1
            
            elif maxDoubles==0:
                x+=target-1
                break
            
            else:
                x+=1
                target-=1

        return x
        
