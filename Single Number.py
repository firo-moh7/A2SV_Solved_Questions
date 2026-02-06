class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        dict=Counter(nums)
        for key,val in dict.items():
            if val==1:
                return key
