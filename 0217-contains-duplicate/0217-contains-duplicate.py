class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_=Counter(nums)
        for i,j in dict_.items():
            if j>=2:
                return True
        return False
        