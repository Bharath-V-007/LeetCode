class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0:
            return -1
        rem = 0
        count = 0
        while True:
            rem = (rem*10 + 1)%k
            count += 1
            if rem == 0:
                break
        return count
