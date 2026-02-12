class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        doubled_num=[]
        changed.sort()
        freq=Counter(changed)
        for num in changed:
            if freq[num]>=1:
                freq[num]-=1
                if freq[2*num]>=1:
                    doubled_num.append(num)
                    freq[2*num]-=1

            if len(doubled_num)==len(changed)//2:  
                return doubled_num

        return []
        
        
        