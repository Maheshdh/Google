class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        for i in range(1,len(intervals)):
            meet_start = intervals[i][0]
            prev_meet_end = intervals[i-1][1]
            if meet_start < prev_meet_end:
                return False
        return True
        
