class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1 
        res = 0

        temp = skill[left] + skill[right]
        while left < right:
            if temp == skill[left] + skill[right]:
                res+=(skill[left] * skill[right])
            else:
                return -1
            left+=1
            right-=1
        return res
    

       

        