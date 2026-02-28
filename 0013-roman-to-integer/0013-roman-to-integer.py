class Solution:
    def romanToInt(self, s: str) -> int:
        value_symb = {'M':1000, 'CM':900,'D':500, 'CD':400,'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10,'IX':9,'V':5, 'IV':4, 'I':1}
        x=0
        ans=0
        while x<len(s):
            if s[x:x+2] in value_symb:
                ans+=value_symb[s[x:x+2]]
                x+=2
            else:
                ans+=value_symb[s[x]]
                x+=1
        return ans
