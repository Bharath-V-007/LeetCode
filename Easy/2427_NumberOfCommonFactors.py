class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        while a % b:
            a , b = b , a % b
        factors = 0
        for i in range(1,b+1):
            if b % i == 0:
                factors += 1
        return factors
