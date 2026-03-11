class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        freq=defaultdict(int)
        freq[0]=1
        ans=0
        for num in nums:
            prefix_sum+=num
            rem=prefix_sum%k
            ans+=freq[rem]
            freq[rem]+=1
        return ans



        