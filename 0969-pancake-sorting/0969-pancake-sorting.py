class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result=[]
        for i in range(len(arr),1,-1):
            n=arr.index(i)
            if i==n+1:
                continue
            
            if n!=0:
                result.append(n+1)
            result.append(i)

            arr[:n+1] = reversed(arr[:n+1])
            arr[:i] = reversed(arr[:i])
        return result
            
        