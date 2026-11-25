class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n > 1 and n % 2 == 1:
            return n
        else:
            return n // 2
