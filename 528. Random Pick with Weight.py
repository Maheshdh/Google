class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        self.total = 0
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum

        

    def pickIndex(self) -> int:
        target = random.random() * self.total
        low = 0
        high = len(self.prefix_sums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target > self.prefix_sums[mid]:
                low += 1
            elif mid!=0 and target < self.prefix_sums[mid] and self.prefix_sums[mid-1] < target:
                return mid
            else:
                high = mid - 1
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
