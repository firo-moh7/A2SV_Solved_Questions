class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ransom=Counter(ransomNote)
        freq_magazine=Counter(magazine)
        for i in freq_ransom:
            if freq_ransom[i]>freq_magazine[i]:
                return False
        return True
        