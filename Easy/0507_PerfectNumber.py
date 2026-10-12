class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        if num == 1:
            return False
        for i in range(1,int(num**0.5)+1):
            if num%i == 0:
                sum += i
                div = num//i
                if div != num and div != i:
                    sum += div
        return sum == num
