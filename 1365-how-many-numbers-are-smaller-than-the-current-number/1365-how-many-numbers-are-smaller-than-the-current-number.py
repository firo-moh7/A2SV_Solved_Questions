class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(n):
            count=0
            for j in range(n):
                if i==j:
                    continue
                elif nums[i]>nums[j]:
                    count+=1
            ans.append(count)
        return ans
        