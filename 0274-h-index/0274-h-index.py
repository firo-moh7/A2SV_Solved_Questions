class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_idx=0
        n=len(citations)
        for i in range(n):
            min_idx=min(citations[i],i+1)
            h_idx=max(h_idx,min_idx)
        return h_idx
