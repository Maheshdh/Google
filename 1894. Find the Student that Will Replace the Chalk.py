class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        rem_chalks =  k % sum(chalk)
        for s in range(len(chalk)):
            if chalk[s] <= rem_chalks:
                rem_chalks -= chalk[s]
                print(rem_chalks)
            else:
                return s



        
