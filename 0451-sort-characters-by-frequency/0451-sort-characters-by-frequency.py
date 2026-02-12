class Solution:
    def frequencySort(self, s: str) -> str:
        dict_=Counter(s)
        freq=sorted(dict_.items(),key=lambda x:x[1],reverse=True)
        ans=""
        
        for key,val in freq:
            for j in range(val):
                ans+=key
        return ans

        