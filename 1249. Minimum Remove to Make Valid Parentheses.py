class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_copy = list(s)
        open_count = 0
        for i,c in enumerate(s):
            if c == "(":
                open_count += 1
            elif c == ")" and open_count == 0:
                s_copy[i] = ""
            elif c == ")" and open_count > 0:
                open_count -= 1
        closed_count = 0
        for j in range(len(s_copy)-1,-1,-1):
            if s_copy[j] == "(" and closed_count == 0:
                s_copy[j] = ""
            elif s_copy[j] == "(" and closed_count > 0:
                closed_count -= 1
            elif s_copy[j] == ")":
                closed_count += 1
        return "".join(s_copy)



        
