class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = collections.defaultdict(list)
        moves = {} # map to store already computed moves for a number
        for num in range(lo,hi+1):
            power = self.findPower(num,moves)
            powers[power].append(num)
        for key in sorted(powers.keys()):
            nums = sorted(powers[key])
            if len(nums) >= k:
                return nums[k-1]
            else:
                k -= len(nums)
                
    def findPower(self,num,moves):
        if num == 1:
            return 0
        if num in moves:
            return moves[num]
        power = 0
        while num > 1:
            # num is even
            if num % 2 == 0:
                num = num // 2
                power += 1
            else:
                num = (num * 3) + 1
                power += 1
        moves[num] = power
        return moves[num]
        

        
