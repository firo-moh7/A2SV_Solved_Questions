class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)
        freq = sorted(freq.items() , key = lambda x : x[0])
        k = 0
        
        for i ,j in freq:
            for n in range(j):
                nums[k] = i
                k += 1
        