class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        sum_even=sum(num for num in nums if num%2==0 )
        for i,j in queries:
            
            if nums[j]%2==0:
                sum_even-=nums[j]
            nums[j]+=i
            if nums[j]%2==0:
                sum_even+=nums[j]
            ans.append(sum_even)
        return ans
