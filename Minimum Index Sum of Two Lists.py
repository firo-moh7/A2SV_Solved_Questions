class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_ans={}
        for i ,j in enumerate(list1):
            for s,k in enumerate(list2):
                if j==k:
                    dict_ans[j]=i+s
                    temp=min(dict_ans.values())
            ans=[]

            if len(dict_ans)==1:
                for key in dict_ans:
                    ans.append(key)
            else:
                for key,value in dict_ans.items():
                    if value<=temp:
                        ans.append(key)
        return ans
