class SnapshotArray:

    def __init__(self, length: int):
        self.records = [[(0,0)] for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.records[index].append((self.snap_id,val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        record = self.records[index]
        low = 1
        high = len(record) - 1
        ans = None
        while low <= high:
            mid = (low + high)//2
            if snap_id >= record[mid][0]:
                ans = record[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return record[high][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
