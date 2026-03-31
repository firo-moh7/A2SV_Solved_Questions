class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_starting_pos(target,nums):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1
                else: 
                    right = mid - 1
            
            return -1

        def get_ending_pos(target,nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    left = mid + 1

                    
                elif nums[mid] < target:
                    left = mid + 1
                else: 
                    right = mid - 1
            return -1

        first=get_starting_pos(target,nums)
        last=get_ending_pos(target,nums)

        return [first,last]


        