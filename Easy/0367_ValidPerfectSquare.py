class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low , high = 1 , num//2 + 1
        while low <= high:
            i = (low+high)//2
            if i*i == num:
                return True
            elif i*i < num:
                low = i+1
            else:
                high = i-1
        return False
