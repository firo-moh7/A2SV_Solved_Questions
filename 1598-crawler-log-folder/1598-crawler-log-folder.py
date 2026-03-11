class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if stack and i=="../":
                stack.pop()
                continue
            elif i=="./":
                continue
            elif i!="../":
                stack.append(i)
        print(stack)
        return len(stack)
        