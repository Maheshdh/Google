class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        max_length = 0
        for num in nums:
            if num-1 in all_nums:
                continue
            x = num
            cur_length = 1
            while x+1 in all_nums:
                cur_length += 1
                x = x+1
            max_length = max(max_length , cur_length)
            
        return max_length
