class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        visited = [False] * len(strs)
        groups = 0
        for i in range(len(strs)):
            if visited[i]:
                continue
            groups += 1
            self.dfs(i,strs,visited)
        return groups

    def dfs(self,i,strs,vis):
        vis[i] = True
        for j in range(len(strs)):
            if vis[j]:
                continue
            if self.is_similar(strs[i],strs[j]):
                self.dfs(j,strs,vis)

    def is_similar(self,a,b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 2 or count == 0
