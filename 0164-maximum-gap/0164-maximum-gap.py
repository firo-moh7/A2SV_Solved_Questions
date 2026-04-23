class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()

        dif = 0
        for i in range(len(nums)-1):
            dif = max(dif,nums[i+1]-nums[i])

        return dif


        