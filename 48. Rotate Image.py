class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        rows = len(matrix)
        cols = len(matrix)
        def transpose(matrix):
            rows, cols = len(matrix), len(matrix)
            for r in range(rows-1):
                for c in range(r+1,cols):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        transpose(matrix)

        # reverse
        def reverse(row):
            left, right = 0, cols-1
            while left < right:
                row[left],row[right] = row[right], row[left]
                left += 1
                right -= 1
            
        for r in range(rows):
            reverse(matrix[r])

        
        
