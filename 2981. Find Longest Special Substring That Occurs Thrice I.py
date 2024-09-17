class Solution:
    def maximumLength(self, s: str) -> int:
        hm = {}  # Dictionary to store substrings and their counts
        j = 0

        # Traverse the string to find special substrings
        i = 0
        while i < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1
            substring = s[i:j]
            # Update the count of the current special substring
            hm[substring] = hm.get(substring, 0) + 1
            i = j

        ans = -1

        # Check the conditions for each substring
        for substring, count in hm.items():
            length = len(substring)
            if length == 1 and count >= 3:
                ans = max(ans, 1)
            elif length >= 2:
                if count >= 3:
                    ans = max(ans, length)
                elif count == 2:
                    ans = max(ans, length - 1)
                elif count == 1 and substring[:-1] in hm:
                    ans = max(ans, length - 1)
                elif length >= 3:
                    ans = max(ans, length - 2)

        return ans


        
