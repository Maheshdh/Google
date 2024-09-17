class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_left = defaultdict(lambda:inf)
        prefix_sum = 0
        res = -inf
        for x in nums:
            prefix_left[x] = min(prefix_left[x],prefix_sum)
            prefix_sum += x
            if x-k in prefix_left:
                res = max(res, prefix_sum - prefix_left[x-k])
            if x+k in prefix_left:
                res = max(res, prefix_sum - prefix_left[x+k])
        return res if res!= -inf else 0
