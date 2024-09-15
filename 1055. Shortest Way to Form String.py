class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def is_subsequence(to_check, src):
            i , j = 0,0
            while i < len(to_check) and j < len(src):
                if to_check[i] == src[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(to_check)
            
        source_chars = set(source)
        for char in target:
            if char not in source_chars:
                return -1
            
        concat_source = source
        count = 1
        while not is_subsequence(target,concat_source):
            concat_source += source
            count += 1
        return count

    

        
