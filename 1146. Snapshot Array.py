class SnapshotArray:

    def __init__(self, length: int):
        self.snap_array = [[(0,0)] for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snap_array[index].append((self.snap_id,val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1       

    def get(self, index: int, snap_id: int) -> int:
        record = self.snap_array[index]
        low = 0
        high = len(record) - 1
        while low <= high:
            mid = (low + high)//2
            if snap_id >= record[mid][0]:
                low = mid + 1
            else:
                high = mid - 1
        return record[high][1]
    

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
