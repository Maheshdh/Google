class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        row = points[0]
        for r in range(1,rows):
            next_row = points[r].copy()
            left_row = [0] * cols
            right_row = [0] * cols
            left_row[0] = row[0]
            for c in range(1,cols):
                left_row[c] = max(row[c], left_row[c-1] -1 )
            right_row[-1] = row[-1]
            for c in range(cols-2,-1,-1):
                right_row[c] = max(row[c], right_row[c+1] -1 )
            for c in range(cols):
                next_row[c] += max(left_row[c], right_row[c])
            row = next_row
        return max(row)

        
