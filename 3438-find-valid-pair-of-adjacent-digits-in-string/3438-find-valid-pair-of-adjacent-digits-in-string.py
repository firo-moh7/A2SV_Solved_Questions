class Solution:
    def findValidPair(self, s: str) -> str:
        if len(set(s))==1:
            return ""
        freq=Counter(s)
        temp=[]
        ans=""

        for i in range(len(s)):
             temp.append(freq[s[i]])
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                continue
            elif int(s[i])==temp[i] and int(s[i+1])==temp[i+1]:
                ans+=s[i]
                ans+=s[i+1]
                return ans

                 
        return ans

        