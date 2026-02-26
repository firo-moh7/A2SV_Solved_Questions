class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i]==needle[0]:
                temp=haystack[i:i+n]
                if temp==needle:
                    return i
        return -1