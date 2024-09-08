class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @lru_cache(None)
        def dp(pos, room):
            if pos == len(nums): return 0

            res = 0
            for slot in range(1, numSlots+1):
                # if slot is 3, then 1 item in it worth 100 = 10 ** 2
                base = 10 ** (slot-1) # value of 1 item of this slot

                # how many spots are available in this slot.
                # if we had room encoded as 1211,
                # and we want to see how much room is available in slot 3:
                # then base = 10 * (slot-1) = 100
                # then left = 1211 // base % 10 = 1211 // 100 %12 = 12 % 10 = 2
                left = room // base % 10
                if left > 0:
                    res = max(res, (nums[pos]&slot) + dp(pos+1, room - base))
            return res

        # initially every slot has room for 2 items. for example:
        # if we have 3 slots we make string '222' converted to int: 222
        return dp(0, int('2'*numSlots))
