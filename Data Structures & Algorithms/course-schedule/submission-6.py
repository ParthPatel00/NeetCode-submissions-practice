class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        taken = set()
        path = set()

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)


        def dfs(i): # Return False if cycle is found
            if i in path:
                return False
            if adj_list[i] == []:
                return True
            
            path.add(i)
            for pre in adj_list[i]:
                if not dfs(pre):
                    return False
            
            path.remove(i)
            adj_list[i] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
