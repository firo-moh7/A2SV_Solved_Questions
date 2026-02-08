class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            dict_[key].append(i)
        return list(dict_.values())
