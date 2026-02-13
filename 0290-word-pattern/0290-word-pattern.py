class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(s)!=len(pattern):
            return False
        
        freq={}
        hash_=set()
        for ch,word in zip(pattern,s):
            if ch in freq:
                if freq[ch]!=word:
                    return False
            else:
                if word in hash_:
                    return False
                freq[ch]=word
                hash_.add(word)
        return True


        
        


       
        