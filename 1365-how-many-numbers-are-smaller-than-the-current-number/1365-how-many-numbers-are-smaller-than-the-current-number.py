class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        temp=sorted(nums)
        ans=[]
        dict_={}
        for i in range(n):
            if temp[i] not in dict_:
                dict_[temp[i]]=i
        for i in range(n):
            ans.append(dict_[nums[i]])
        return ans
        