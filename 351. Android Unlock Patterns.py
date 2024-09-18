class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def backtrack(num,j):
            if j == 0:
                return 1
            ans = 0
            for next_num in range(1,10):
                if (next_num not in seen) and (((num,next_num) not in skip) or skip[(num,next_num)] in seen):
                    seen.add(next_num)
                    ans += backtrack(next_num,j-1)
                    seen.discard(next_num)
            return ans

        skip = {
            (1,3) : 2,
            (3,1) : 2,
            (1,7) : 4,
            (3,9) : 6,
            (9,3) : 6,
            (7,9) : 8,
            (9,7) : 8,
            (7,1) : 4,
            (1,9) : 5,
            (9,1) : 5,
            (2,8) : 5,
            (8,2) : 5,
            (4,6) : 5,
            (6,4) : 5,
            (7,3) : 5,
            (3,7) : 5
        }    
        ans = 0
        for i in range(m,n+1):
            seen = set([1])
            ans += backtrack(1,i-1) * 4
            seen = set([2])
            ans += backtrack(2,i-1) * 4
            seen = set([5])
            ans += backtrack(5,i-1)
        return ans
        
