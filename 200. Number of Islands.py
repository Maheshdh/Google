class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            grid[x][y] = "0"
            for move in moves:
                x_new,y_new = x+move[0], y+move[1]
                if 0<=x_new<rows and 0<=y_new<cols and grid[x_new][y_new] == "1":
                    dfs(x_new,y_new)
                    
        rows,cols = len(grid), len(grid[0])
        count = 0
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count
        
