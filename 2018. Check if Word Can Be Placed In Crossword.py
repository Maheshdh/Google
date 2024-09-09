class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        words = [word, word[::-1]]
        for B in board,zip(*board):
            for row in B:
                segs = "".join(row).split("#")
                for w in words:
                    for seg in segs:
                        if len(seg) == len(w):
                            if all(seg[i] == w[i] or seg[i] == ' ' for i in range(len(w))):
                                return True
        return False
        
