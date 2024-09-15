class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i == 0 and j == 0:
                        count += 1
                    elif i == 0 and board[i][j-1] != 'X':
                        count += 1
                    elif j == 0 and board[i-1][j] !='X':
                        count +=1
                    elif board[i-1][j] =='.' and board[i][j-1] == '.':
                        count += 1
        return count
        
