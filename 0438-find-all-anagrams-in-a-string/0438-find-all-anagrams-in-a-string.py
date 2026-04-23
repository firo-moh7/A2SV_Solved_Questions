class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        count_anag = Counter()
        n = len(p)
        res = []
        
        if n > len(s):
            return []
        for i in range(n):
            count_anag[s[i]] += 1
        
        if count_p == count_anag:
            res.append(0)

        left = 0
        for i in range(n,len(s)):
            count_anag[s[i]] += 1
            count_anag[s[left]] -= 1

            if count_anag[s[left]] == 0:
                del count_anag[s[left]]
            
            left += 1

            if count_p == count_anag:
                res.append(left)
        
        return res
        

        