class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inOrder = [0 for _ in range(numCourses)]
        q = deque()
        order = []

        for course , pre in prerequisites:
            graph[pre].append(course)

            inOrder[course] += 1

        for course in range(numCourses):
            if inOrder[course] == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            order.append(course)

            for i in graph[course]:
                inOrder[i] -= 1

                if inOrder[i] == 0:
                    q.append(i)
        
        if len(order) == numCourses:
            return order
        
        return []
        