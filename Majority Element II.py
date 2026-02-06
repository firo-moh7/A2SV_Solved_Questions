class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        ans=[]
        n=len(nums)
        dict_=Counter(nums)
        for key , val in dict_.items():
            if val>n/3:
                ans.append(key)
        return ans
