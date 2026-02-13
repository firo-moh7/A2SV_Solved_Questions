class Solution:
    def intToRoman(self, num: int) -> str:
        value_symb = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        ans=[]
        for key , val in value_symb:
            if num==0:
                break
            count=num//key
            ans.append(val*count)
            num-=count*key

        return "".join(ans)
                


        