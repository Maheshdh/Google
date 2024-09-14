class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        can_detonate = {}
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]
                dist = sqrt((x1-x2)**2 + (y1-y2)**2)
                if dist <= r1:
                    if i in can_detonate:
                        can_detonate[i].append(j)
                    else:
                        can_detonate[i] = [j]
                if dist <= r2:
                    if j in can_detonate:
                        can_detonate[j].append(i)
                    else:
                        can_detonate[j] = [i]
        res = 0
        def dfs(s, visit):
            if s in visit:
                return 0
            visit.add(s)
            bombs_detonated = 1
            for neighbor in can_detonate.get(s,[]):
                bombs_detonated += dfs(neighbor,visit)
            return bombs_detonated

        for i in range(len(bombs)):
            res = max(res, dfs(i,set()))
        
        return res
        
