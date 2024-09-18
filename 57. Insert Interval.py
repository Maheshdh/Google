class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        low = 0
        high = len(intervals)-1
        while low <= high:
            mid = (low+high) // 2
            if intervals[mid][0] < newInterval[0]:
                low = mid + 1
            else:
                high = mid - 1
        intervals.insert(low, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],interval[1])
        return res
        
