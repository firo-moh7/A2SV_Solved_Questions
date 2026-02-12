class Solution:
    def findValidPair(self, s: str) -> str:
        freq=Counter(s)
        if len(set(s))==1:
            return ""
        ans=""

        for i in range(len(s)):
            if freq[s[i]]==int(s[i]):
                if s[i] not in ans:
                    ans+=s[i]
        if len(ans)==1:
            return ""            
        return ans

        