class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_=Counter(nums)
        for i in dict_:
            if dict_[i]>=2:
                return True
        return False
        