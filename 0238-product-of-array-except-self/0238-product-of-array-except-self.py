class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
       
        res=[0] * n
        temp = 1
        for i in range(n):
            res[i] = temp
            temp *= nums[i] 

        temp2 = 1
        for i in range(n-1 , -1 , -1):
            res[i] *= temp2
            temp2 *= nums[i]

        return res
            
            