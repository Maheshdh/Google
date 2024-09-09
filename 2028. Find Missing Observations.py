class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # find total sum
        # mean = total_sum // (m+n)
        total_sum = mean * (len(rolls) + n)
        missing_sum = total_sum - sum(rolls)
        if missing_sum / n > 6 or missing_sum < n:
            return []

        res = []
        while n > 0:
            # place values in n slots in a greedy way
            # max we can put is 6, or the value after placing one in remaining n-1 slots
            dice = min(6,missing_sum - (n-1))
            res.append(dice)
            missing_sum -= dice
            n -= 1
        return res
