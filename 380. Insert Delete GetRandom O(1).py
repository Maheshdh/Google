class RandomizedSet:

    def __init__(self):
      self.numMap = {}
      self.numList = []

    def insert(self, val: int) -> bool:
      if not val in self.numMap:
        ans = True
        self.numMap[val] = len(self.numList)
        self.numList.append(val)
      else:
        ans = False
      return ans
        

    def remove(self, val: int) -> bool:
      if val in self.numMap:
        ans = True
        id = self.numMap[val]
        self.numList[id] = self.numList[-1]
        self.numMap[self.numList[-1]] = id
        self.numList.pop()
        del self.numMap[val]
      else:
        ans = False
      return ans
        

    def getRandom(self) -> int:
      #print(self.numList)
      return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
