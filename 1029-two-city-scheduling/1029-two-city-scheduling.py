class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans=0
        s=sorted(costs,key=lambda x: x[0]-x[1])
        print(s)
        for j in range (len(costs)):
            if j<len(costs)//2:
                ans+=s[j][0]
            else:
                ans+=s[j][1]
        return ans

        