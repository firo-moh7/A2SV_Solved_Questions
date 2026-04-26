class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        sub_num = {0:1}
        count = 0
        for n in nums:
            cur_sum += n

            if cur_sum - k in sub_num:
                count += sub_num[cur_sum - k]

            sub_num[cur_sum] = sub_num.get(cur_sum,0) + 1

        return count

        
            

        