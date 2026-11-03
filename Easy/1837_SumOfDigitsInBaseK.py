class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n > 0:
            rem = n%k
            result += rem
            n //= k
        return result
