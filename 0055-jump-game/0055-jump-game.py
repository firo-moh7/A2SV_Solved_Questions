class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx=0
        gas=0
        for i in nums:
            if gas<0:
                return False

            elif gas < i:
                gas=i
            gas-=1
        return True
        