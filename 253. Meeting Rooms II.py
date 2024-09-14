class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([intervals[i][0] for i in range(len(intervals))])
        end = sorted([intervals[i][1] for i in range(len(intervals))])
        
        res, count = 0,0
        s, e = 0,0
        while s < len(intervals):
            if starts[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res
        
