class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        fre=Counter(nums)
        res = []
        n = len(nums)
        for key,val in fre.items():
            if val > n/3:
                res.append(key)
        return res