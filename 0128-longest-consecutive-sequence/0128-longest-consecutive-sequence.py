class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        count=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i]+1==nums[i+1]:
                count+=1

        return count+1
        