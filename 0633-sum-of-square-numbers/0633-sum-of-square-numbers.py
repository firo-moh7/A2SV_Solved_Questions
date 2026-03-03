class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        hash_={}
        
        for i in range(int(sqrt(c))+1):
            if i*i==c or i*i ==c-i*i or c-i*i in hash_:
                return True
            else:
                hash_[i*i]=hash_.get(i*i,0)+1
        return False

        