class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            a=nums2.index(i)
            if a+1<len(nums2) and i<nums2[a+1]:
                ans.append(nums2[a+1])
            else:
                ans.append(-1)
        return ans
        