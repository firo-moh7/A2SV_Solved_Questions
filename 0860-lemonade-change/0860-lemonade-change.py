class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten_dol=0
        five_dol=0
        for i in bills:
            if i==5:
               five_dol+=1
            elif i==10:
                if five_dol>0:
                    five_dol-=1
                    ten_dol+=1
                else:
                    return False
            
            else:
                if ten_dol>0 and five_dol>0:
                    five_dol-=1
                    ten_dol-=1
                elif five_dol>=3:
                    five_dol-=3
                else:
                    return False

        return True



