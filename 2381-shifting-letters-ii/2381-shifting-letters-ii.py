class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr=[0]*(len(s)+1)
        a=96
        for l,r,k in shifts:
            if k==0:
                arr[l]-=1
                arr[r+1]+=1
            else:
                arr[l]+=1
                arr[r+1]-=1
        
        cur=0
        res=[0]*len(s)
        for i in range(len(s)):
            cur+=arr[i]
            res[i]=cur
        fin_ans=""
        for i in range (len(s)):
            ans=ord(s[i])-ord('a')
            ans=(ans+res[i])%26
            fin_ans+=chr(ans+ord('a'))
        return fin_ans


            

            

            
        