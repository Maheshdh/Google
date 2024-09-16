class Solution:
    def validStrings(self, n: int) -> List[str]:
        def generate(id,s):
            if id == n:
                return [s]
            res = []
            if not s or s[-1] == "1":
                res += generate(id+1, s + "0")
            res += generate(id+1, s + "1")
            return res
        return generate(0,"")
        
