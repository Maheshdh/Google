class StockPrice:

    def __init__(self):
        self.prices = {}
        self.cur_time = 0
        self.max_price, self.min_price = [],[]

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        heapq.heappush(self.max_price,(-price,timestamp))
        heapq.heappush(self.min_price, (price, timestamp))
        self.cur_time = max(self.cur_time, timestamp)
        

    def current(self) -> int:
        return self.prices[self.cur_time]
        

    def maximum(self) -> int:
        if not self.max_price:
            return 0
        while self.max_price:
            price, timestamp = self.max_price[0]
            price = -price
            if self.prices[timestamp] == price:
                return price
            else:
                heapq.heappop(self.max_price)


    def minimum(self) -> int:
        if not self.min_price:
            return 0
        while self.min_price:
            price, timestamp = self.min_price[0]
            if self.prices[timestamp] == price:
                return price
            else:
                heapq.heappop(self.min_price)
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
