class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        co=Counter(chars)
        count_word=0
        for i in words:
            temp=Counter(i)
            for key in temp:
                if key not in co or temp[key] >co[key]:
                    break
            else:
                count_word+=len(i)
        return count_word
