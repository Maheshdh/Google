class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp_str = ""
        for i in s:
            temp_str += str(ord(i) - ord('a') + 1)
        list_digits = list(temp_str)
        while k > 0:
            temp_num = sum(int(i) for i in list_digits)
            k -= 1
            list_digits = list(str(temp_num))
        return temp_num
        
