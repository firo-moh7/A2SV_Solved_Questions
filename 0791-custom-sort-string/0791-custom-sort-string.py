class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        result=[]
        mp={}
        for i in s:
            mp[i]=mp.get(i,0)+1
        
        for i in order:
            if i in mp:
                result.append(i*mp[i])
                del mp[i]

        for key , val in mp.items():
            result.append(key * val)

        return "".join(result)