class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()
        def dfs(start):
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
                    
        
