class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=defaultdict(lambda:-1)
        for i in nums2:
            while stack and stack[-1]<i:
                res[stack[-1]]=i
                stack.pop()
            stack.append(i)

        return [res[i] for i in nums1]
        