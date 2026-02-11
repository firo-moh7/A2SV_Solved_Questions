class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            temp=str(i)
            for num in temp:
                ans.append(num)
        for i in range(len(ans)):
            ans[i]=int(ans[i])
        return ans
        