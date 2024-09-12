class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = {}
        for num in hand:
            counts[num] = counts.get(num,0) + 1
        minH = list(counts.keys())
        heapq.heapify(minH)
        while minH:
            start = minH[0]
            for i in range(start, start+groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
                    
