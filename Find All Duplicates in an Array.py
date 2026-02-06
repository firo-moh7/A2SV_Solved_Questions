class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        dict_c=Counter(nums)
        ans=[]
        for key,val in dict_c.items():
            if val==2:
                ans.append(key)
        return ans
