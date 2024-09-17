class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        i = 0
        ans = 0
        while i < len(s):
            l,r = i,i
            while l>=0 and r <len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if len(s[l:r+1]) > ans:
                res = s[l:r+1]
                ans = len(s[l:r+1])
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if len(s[l:r+1]) > ans:
                res = s[l:r+1]
                ans = len(res)
            i += 1
        return res
        
