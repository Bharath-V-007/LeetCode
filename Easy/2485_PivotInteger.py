import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = math.isqrt(n*(n+1)//2)
        if pivot*pivot == n*(n+1)//2:
            return pivot
        return -1
