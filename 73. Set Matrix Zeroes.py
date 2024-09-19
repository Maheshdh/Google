class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        moves = [(1,0),(0,1),(0,-1),(-1,0)]
        def dfs(x,y):
            for col in range(cols):
                if(matrix[x][col] != 0):
                    matrix[x][col] = 0
                    visited.add((x,col))
            for row in range(rows):
                if matrix[row][y] != 0:
                    matrix[row][y] = 0
                    visited.add((row,y))
        visited = set()
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0 and (r,c) not in visited:
                    dfs(r,c)
                    
