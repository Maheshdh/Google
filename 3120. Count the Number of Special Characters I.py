class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small_chars = [0 for i in range(26)]
        for char in word:
            if 0 <= ord(char) - ord('a') < 26:
                small_chars[ord(char)-ord('a')] = 1
        count = 0
        for char in word:
            if 'A'<=char<='Z' and small_chars[ord(char) - ord('A')]:
                count += 1
                small_chars[ord(char)-ord('A')] = 0
        return count
                
        
