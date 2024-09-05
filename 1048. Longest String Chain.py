class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        longest_chain = 1
        cache = {}
        def dfs(cur_word):
            if cur_word == "":
                return 0
            if cur_word in cache:
                return cache[cur_word]
            res = 1
            for i in range(len(cur_word)):
                prefix_word = cur_word[:i] + cur_word[i+1:]
                if prefix_word in word_set:
                    res = max(res, 1+dfs(prefix_word))
            cache[cur_word] = res
            return res
        for word in words:
            longest_chain = max(longest_chain,dfs(word))
        return longest_chain
        
