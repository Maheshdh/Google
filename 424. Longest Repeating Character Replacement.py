class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        maxLength = 1
        left = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            while right - left + 1 - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength
        
