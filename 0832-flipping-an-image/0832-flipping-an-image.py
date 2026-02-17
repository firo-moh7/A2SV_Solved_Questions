class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        ans=[]
        for i in image:
            i.reverse()
            ans.append([abs(j-1) for j in i])
        return ans