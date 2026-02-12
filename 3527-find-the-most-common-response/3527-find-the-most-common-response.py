class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ans=[]
        for i in responses:
            ans.append(list(set(i)))
        
        freq=[]
        for i in ans:
            freq.extend(i)
        count=Counter(freq)
        max_count=0
        for key,val in count.items():
            if val > max_count:
                max_count=val
                final_ans=key
            elif val==max_count:
                final_ans=min(final_ans,key)
        return final_ans
        
       
