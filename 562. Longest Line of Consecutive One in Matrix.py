class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        # move map
        self.moves = {

            'U' : (-1,0),
            'R' : (0,1),
            'D' : (1,0),
            'L' : (0,-1),
            'UR': (-1,1),
            'DR' :(1,1),
            'DL' : (1,-1),
            'UL' : (-1,-1)
        }

        rows, cols = len(mat), len(mat[0])
        self.cache = {}
        max_ones = 0
        res = 0
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]:
                    for move in self.moves:
                        res = self.dfs(mat, row,col,move)
                        max_ones = max(max_ones, res)
        return max_ones
    
    def dfs(self,mat,row,col,move):
        if (row,col,move) in self.cache:
            return self.cache[(row,col,move)]
        
        self.cache[(row,col,move)] = 0

        if (0<=row<len(mat)) and (0<=col<len(mat[0])) and mat[row][col]:
            self.cache[(row,col,move)] = 1 + self.dfs(mat,row + self.moves[move][0],col+self.moves[move][1],move)
        return self.cache[(row,col,move)]

    # Time complexity : O(rows * cols)
    # Space complexity : O(rows* cols)
