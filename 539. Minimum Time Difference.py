class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for time in timePoints:
            hour, mins = time.split(":")
            time_in_minutes = int(hour) * 60 + int(mins)
            times.append(time_in_minutes)
        times.sort()
        res = 1440 + times[0] - times[-1]
        for i in range(1,len(times)):
            res = min(res, times[i] - times[i-1])
        return res

        
