class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        freq = sorted(freq.items(),key = lambda x:x[1] , reverse = True)
        for i , j in freq:
            return i