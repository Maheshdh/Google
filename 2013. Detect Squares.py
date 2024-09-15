class DetectSquares:

    def __init__(self):
        self.points = collections.defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[x][y] += 1
        

    def count(self, point: List[int]) -> int:

        x, new_y = point
        count = 0
        for y in self.points[x]:
            edge = abs(new_y - y)
            if edge:
                count += self.points[x][y] * self.points[x-edge][y] * self.points[x-edge][new_y]
                count += self.points[x][y] * self.points[x+edge][y] * self.points[x+edge][new_y]
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
