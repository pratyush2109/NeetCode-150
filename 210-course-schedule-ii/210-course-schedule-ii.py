class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i:[] for i in range(numCourses)}
        visited=set()
        res=[]
        
        for c,p in prerequisites:
            preMap[c].append(p)
            
        def dfs(course):
            if course in visited:
                return False
            
            if len(preMap[course])==0:
                if course not in res:
                    res.append(course)
                return True
            
            visited.add(course)
            for crs in preMap[course]:
                if not dfs(crs):
                    return False
            
            visited.remove(course)
            preMap[course]=[]
            if course not in res:
                res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res