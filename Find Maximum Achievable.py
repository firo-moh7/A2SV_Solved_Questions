class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3==0:
            num_div=num//3
            return [num_div-1,num_div,num_div+1]
        else:
            return []
