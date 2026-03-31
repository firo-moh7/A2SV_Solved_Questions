class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            day = 0
            current_sum = 0
            for i in range(len(weights)):
                if weights[i] + current_sum > capacity:
                    day+= 1
                    current_sum = weights[i]
                else:
                    current_sum+= weights[i]
            if current_sum > 0:
                day+=1
            return day <= days
                
        left= max(weights)
        right = sum(weights)
        ans= -1
        while left <= right:
            mid = (left + right)//2
            if check(mid):
                ans=mid
                right = mid - 1

            else:
                left = mid + 1
        return ans
