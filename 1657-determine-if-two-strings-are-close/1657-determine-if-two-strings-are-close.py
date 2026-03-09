class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq_w1=Counter(word1)
        freq_w2=Counter(word2)
        if len(word1)!=len(word2):
            return False
        for i in word1:
            if i not in word2:
                return False
        sorted_w1=[]
        sorted_w2=[]
        for i,j in freq_w1.items():
            sorted_w1.append(j)
        for i,j in freq_w2.items():
            sorted_w2.append(j)
        sorted_w1.sort(reverse=True)
        sorted_w2.sort(reverse=True)
        for i in range(len(sorted_w1)):
            if sorted_w1[i]!=sorted_w2[i]:
                return False
        return True
        
        
        