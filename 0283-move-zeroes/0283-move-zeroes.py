class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder=0
        seeker=0
        while holder<len(nums) and seeker<len(nums):
            
            if nums[seeker]==0:
                seeker+=1
            elif nums[holder]!=0:
                holder+=1
            elif holder>seeker:
                holder,seeker=seeker,holder
            else:
                nums[holder],nums[seeker]=nums[seeker],nums[holder]

        