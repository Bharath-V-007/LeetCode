class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low , high = 0 , x//2
        while low <= high:
            i = (low + high) // 2
            if i*i == x:
                return i
            elif i*i < x:
                low = i + 1
            else:
                high = i - 1
        return high
