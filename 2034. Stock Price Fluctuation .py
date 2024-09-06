class StockPrice:

    def __init__(self):
        self.time_map = collections.defaultdict(int)
        self.cur_time = 0
        self.max_heap = []
        self.min_heap = []       

    def update(self, timestamp: int, price: int) -> None:
        self.time_map[timestamp] = price
        self.cur_time = max(self.cur_time, timestamp)
        heapq.heappush(self.min_heap,(price,timestamp))
        heapq.heappush(self.max_heap,(-price,timestamp))
        

    def current(self) -> int:
        return self.time_map[self.cur_time]

    def maximum(self) -> int:
        if self.cur_time == 0:
            return 0
        while True:
            probable_price, probable_time = heapq.heappop(self.max_heap)
            probable_price = - 1 * probable_price
            if self.time_map[probable_time] == probable_price:
                heapq.heappush(self.max_heap,(-probable_price, probable_time))
                return probable_price

    def minimum(self) -> int:
        if self.cur_time == 0:
            return 0
        while True:
            p, t = heapq.heappop(self.min_heap)
            if self.time_map[t] == p:
                heapq.heappush(self.min_heap,(p,t))
                return p
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
