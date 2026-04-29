class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0:-1}
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            rem = cur_sum % k

            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False


        