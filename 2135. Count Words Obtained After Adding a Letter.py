class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # start words set in sorted order
        start_words_set = set()
        for word in startWords:
            start_words_set.add("".join(sorted(word)))
        
        res = 0
        for word in targetWords:
            sorted_word = "".join(sorted(word))
            for i in range(len(sorted_word)):
                test_word = sorted_word[:i] + sorted_word[i+1:]
                if test_word in start_words_set:
                    res += 1
                    break
        return res

    # Time complexity : O(N)
    # Space complexity : O(N)

        
