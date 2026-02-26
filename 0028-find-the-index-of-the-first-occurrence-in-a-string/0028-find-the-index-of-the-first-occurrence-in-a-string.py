class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x=0
        y=0
        while x<len(haystack):
            if haystack[x]==needle[y]:
                temp=haystack[x:x+len(needle)]
                if temp==needle:
                    return x
            x+=1
        return -1