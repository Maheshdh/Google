class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        if k >= rows + cols - 2:
            return rows + cols - 2
        queue = deque([(0,(0,0,k))])
        seen = set((0,0,k))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        target = (rows-1,cols-1)
        while queue:
            print(queue[0])
            steps, (x,y, removals_left) = queue.popleft()
            if (x,y) == target:
                return steps
            for move in directions:
                x_new,y_new = x+move[0], y+move[1]
                if 0 <= x_new < rows and 0 <= y_new < cols:
                    removals = removals_left - grid[x_new][y_new]
                    if removals >= 0 and (x_new,y_new,removals) not in seen:
                        seen.add((x_new,y_new,removals))
                        queue.append((steps+1, (x_new,y_new,removals)))
        return -1
