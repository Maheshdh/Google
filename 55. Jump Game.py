class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = -1
        for i in range(len(nums)):
            # if you are at last position, return True
            if i == len(nums) -1 :
                return True
            # determine the max index you can go from the current index
            # if you can reach the last index, return True
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
            # if the max index you can reach is the current index, that means you cannot go further return False
            if i == max_reach:
                return False
        return True
