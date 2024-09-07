class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for id, src, replace in sorted(zip(indices,sources,targets),reverse = True):
            if s[id:id+len(src)] == src:
                s = s[:id] + replace + s[id+len(src):]
        return s
        
