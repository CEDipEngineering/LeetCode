from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = dict()
        indegree = [0]*numCourses
        output = []

        for course, dependency in prerequisites:
            graph.setdefault(dependency, []).append(course)
            indegree[course] += 1
        
        def search(node):
            output.append(node)
            indegree[node] -= 1
            for next in graph.get(node, []):
                indegree[next] -= 1
                if indegree[next] == 0:
                    search(next)
                    
        for node in range(numCourses):
            if indegree[node] == 0: search(node)

        if len(output) == numCourses: return output # If all courses were able to be scheduled, return order
        return [] # Return empty otherwise
                


if __name__ == "__main__":
    S = Solution()
    print_test = lambda n, l: print("<{}, {}>: {}".format(n, l, S.findOrder(n, l)))

    print_test(3, [[0,1],[0,2],[1,2]])
    print_test(2, [[0,1],[1,0]])
    exit(0)
    print_test(4, [[1,0],[2,0],[3,1],[3,2]])
    print_test(2, [[1,0]])
    print_test(6, [[5,4],[4,3],[3,2],[2,1],[1,0]])