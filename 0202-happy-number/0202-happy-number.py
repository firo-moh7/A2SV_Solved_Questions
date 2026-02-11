class Solution:
    def isHappy(self, n: int) -> bool:
        string=str(n)
        for i in range(1,10):
            count=0
            for i in string:
                count+=int(i)**2
            if count==1 or count==7:
                return True
            elif count==n:
                return False
            string=str(count)
        return False

        