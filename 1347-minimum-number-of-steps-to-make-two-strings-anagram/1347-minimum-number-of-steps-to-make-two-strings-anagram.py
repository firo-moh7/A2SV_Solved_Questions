class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s=Counter(s)
        freq_t=Counter(t)

        count=0
        for key in freq_s:
            if freq_s[key]>freq_t[key]:
                count+=(freq_s[key]-freq_t[key])
        return count



        