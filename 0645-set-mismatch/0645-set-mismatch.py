class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            count = nums.count(i)
            if count == 2:
                res.append(i)
                break
        for i in range(1,len(nums)+1):
            count = nums.count(i)
            if count == 0:
                res.append(i)
                break
          

        return res