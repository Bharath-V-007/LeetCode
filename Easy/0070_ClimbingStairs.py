class Solution:
    def climbStairs(self, n: int) -> int:
        current , prev = 1 , 1
        for i in range(1,n):
            current , prev = current+prev , current
        return current
