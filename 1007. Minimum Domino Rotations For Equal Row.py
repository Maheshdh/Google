class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        values = [tops[0],bottoms[0]]
        ans = float('inf')
        for value in values:
            flag = True
            top_flips, bottom_flips = 0, 0
            for i in range(len(tops)):
                if tops[i] != value and bottoms[i] != value:
                    flag = False
                    break
                elif tops[i] != value:
                    top_flips += 1
                elif bottoms[i] != value:
                    bottom_flips += 1
            if flag:
                ans = min(ans, min(top_flips, bottom_flips))
        if ans == float('inf'):
            return -1
        return ans
                
