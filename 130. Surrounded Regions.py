class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        # run dfs on border cells to convert O's to T's
        def dfs(x,y):
            if x < 0 or y < 0 or x == rows or y== cols or board[x][y] != 'O':
                return 
            board[x][y] = "T"
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r== rows-1) or (c== 0 or c== cols-1):
                    dfs(r,c)

        # convert remaining O's to X's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
