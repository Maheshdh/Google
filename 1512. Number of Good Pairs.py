class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = collections.defaultdict(int)
        count = 0
        for num in nums:
            count += seen[num]
            seen[num] += 1
        return count

        
