class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        ans=[]
        sorted_=sorted(freq.items(),key=lambda x:x[1], reverse=True)
        for i in range(k):
          ans.append(sorted_[i][0])
        return ans
