class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        cur_height = 0
        while left < right:
            width = right - left
            h = min(height[left],height[right])
            cur_height = max(cur_height,h * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return cur_height



