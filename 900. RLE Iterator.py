class RLEIterator:

    def __init__(self, encoding: List[int]):
        #self.q = collections.deque()
        # for i in range(0,len(encoding),2):
        #     times = encoding[i]
        #     val = encoding[i+1]
        #     for time in range(times):
        #         self.q.append(val)
        self.encoded = encoding
        self.index = 0

    def next(self, n: int) -> int:
        # we have processed all the elements in the encoded array
        if self.index >= len(self.encoded):
            return -1
        while self.index < len(self.encoded):
            if n <= self.encoded[self.index]:
                self.encoded[self.index] -= n
                return self.encoded[self.index+1]
            n -= self.encoded[self.index]
            self.index += 2
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
