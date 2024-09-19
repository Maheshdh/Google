class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      res = []
      st = []
      def backtrack(openN,closed):
        if openN == closed == n:
          res.append("".join(st))
          return
        if openN < n:
          st.append('(')
          backtrack(openN+1,closed)
          st.pop()
        if closed < openN:
          st.append(')')
          backtrack(openN,closed+1)
          st.pop()
      backtrack(0,0)
      return res
        
