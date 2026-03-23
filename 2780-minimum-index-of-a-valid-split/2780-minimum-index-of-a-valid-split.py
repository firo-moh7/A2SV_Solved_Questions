class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        first_freq=Counter(nums)
        second_freq=defaultdict(int)
        n=len(nums)

        for index in range(n):
            num=nums[index]
            first_freq[num]-=1
            second_freq[num]+=1

            if second_freq[num] * 2 > index + 1 and first_freq[num] * 2 > n - index -1:
                return index
        
        return -1

        
