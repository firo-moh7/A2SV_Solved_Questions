class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        b.sort()
        a.sort()
        
        x=0
        y=0
        while x<len(b) and y<len(a):
            if b[x]==a[y]:
                x+=1
                y+=1
            elif b[x]>a[y]:
                y+=1
            else:
                return False
                
        if x==len(b) and y<=len(a):
            return True
