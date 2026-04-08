class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        
        for key , value in freq.items():
            bucket[value].append(key)

        res = []

        for num in range(len(bucket)-1,0,-1):
            for i in bucket[num]:
                res.append(i)
                if len(res) == k:
                    return res
        

       





