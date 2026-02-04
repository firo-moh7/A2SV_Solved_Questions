class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=sorted(strs)
        first=l[0]
        last=l[-1]
        ans=""
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans
