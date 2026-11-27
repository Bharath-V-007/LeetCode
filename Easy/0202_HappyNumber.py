class Solution:
    def isHappy(self, n: int) -> bool:
        result = 0
        seen = set()
        while result != 1:
            value = 0
            while n > 0:
                value += (n % 10) ** 2
                n //= 10
            if value in seen:
                return False
            seen.add(value)
            n = value
            result = value
        return True
