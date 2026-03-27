class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l=set(nums)
        if len(l)==1 and 0 in l:
            return "0"

        temp=[]
        for i in nums:
            temp.append(str(i))
        from functools import cmp_to_key
        temp.sort(key=cmp_to_key(lambda x,y: -1 if x+y > y+x else 1))
        return "".join(temp)
        