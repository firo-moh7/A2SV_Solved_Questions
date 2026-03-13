class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count={}
        for cp in cpdomains:
            visit,domain = cp.split()
            visit=int(visit)
            domain=domain.split('.')
            
            for i in range(len(domain)):
                sub=".".join(domain[i:])
                count[sub]=count.get(sub,0)+visit

        return [f"{val} {key}" for key,val in count.items()]