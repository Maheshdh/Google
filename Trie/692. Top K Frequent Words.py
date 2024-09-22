class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.num_words = 0

class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        bucket = [TrieNode() for i in range(len(words)+1)]
        self.k = k

        def add_word(root, word):
            cur = root
            cur.num_words = 1
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.endOfWord = True

        def get_words(root,prefix):
            if self.k == 0:
                return []
            res = []
            if root.endOfWord:
                self.k -= 1
                res.append(prefix)
            for i in range(26):
                c = chr(ord('a') + i)
                if c in root.children:
                    res += get_words(root.children[c],prefix+c)
            return res

        for word,freq in cnt.items():
            add_word(bucket[freq], word)
        
        res = []
        for i in range(len(words),0,-1):
            if self.k == 0:
                return res
            if bucket[i].num_words:
                res += get_words(bucket[i],'')
            
        return res

        
