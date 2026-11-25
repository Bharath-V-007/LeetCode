class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for n in range(1,num+1):
            temp = n
            digit_sum = 0
            while temp > 0:
                rem = temp % 10
                digit_sum += rem
                temp //= 10
            if digit_sum % 2 == 0:
                count += 1
        return count
