class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        
        cur_sum = 0
        counter = 2
        ans = []
        while cur_sum + counter <= finalSum:
            ans.append(counter)
            cur_sum += counter
            counter += 2
        if finalSum - cur_sum > 0 :
            ans[-1] += finalSum - cur_sum
        return ans
        
