class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1 = grid[0]
        r2 = [1-i for i in grid[0]]
        for row in grid[1:]:
            if row != r1 and row != r2:
                return False
        return True
