import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i , j = 0 , math.isqrt(c)
        while i <= j:
            eqn = i*i + j*j
            if eqn == c:
                return True
            elif eqn < c:
                i += 1
            else:
                j -= 1
        return False
