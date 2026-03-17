class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=defaultdict(list)

        for i in paths:
            s=i.split(' ')
            path=s.pop(0)

            for n in s:
                idx=n.index('(')
                d[n[idx:]].append(path+ '/' + n[:idx])
        return [d[i] for i in d.keys() if len(d[i])>1]
