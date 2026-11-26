class Solution:
    def canAliceWin(self, n: int) -> bool:
        result = False
        dec = 10
        while n >= dec:
            n -= dec
            result ^= True
            dec -= 1
        return result
