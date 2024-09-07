class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        all_starts, all_ends = [],[]
        for interval in intervals:
            all_starts.append(interval[0])
            all_ends.append(interval[1])
        all_starts.sort()
        all_ends.sort()
        used_rooms = 0
        end_ptr = 0
        for i in range(len(all_starts)):
            if all_starts[i] < all_ends[end_ptr]:
                used_rooms += 1
            else:
                end_ptr += 1
        return used_rooms

        
