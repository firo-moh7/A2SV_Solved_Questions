class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        max_count=0
        set_nums=set(nums)
        
        for i in set_nums:
            if (i-1) not in set_nums:
                current=i
                count=1
                while current+1 in set_nums:
                    count+=1
                    current+=1
                max_count=max(max_count,count)

        return max_count
        