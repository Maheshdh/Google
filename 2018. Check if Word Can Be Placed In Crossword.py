class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        return self.canPlace(board,word) or self.canPlace(zip(*board),word)
    
    def canPlace(self,board,word):
        # T : O(len(word))
        words = [word,word[::-1]]
        print("words ",words)
        # T O(rows)
        for row in board:
            #print("row = ",row)
            segs = "".join(row).split("#")
            #print("Segs = ",segs)
            for w in words:
                # O(cols)
                for seg in segs:
                    if len(seg) == len(w):
                        # O(len(word))
                        if all(seg[i] == w[i] or seg[i] == " " for i in range(len(w))):
                            return True
        return False

        
