class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx=0
       
        for i in range(len(nums)):
            step=max(mx,nums[i]+i)

            if i>mx :
                return False
            mx =  max(step,mx)
        return True
        