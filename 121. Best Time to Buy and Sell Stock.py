class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = inf
        largestProfit = 0
        for num in prices:
            if num < minSoFar:
                minSoFar = num
            else:
                largestProfit = max(largestProfit,num - minSoFar)
        return largestProfit
