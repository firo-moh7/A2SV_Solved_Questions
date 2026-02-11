class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict_s=Counter(s)
        dict_t=Counter(t)

        count=0
        for key in dict_s:
            if dict_s[key]>dict_t[key]:
                count+=(dict_s[key]-dict_t[key])
        return count



        