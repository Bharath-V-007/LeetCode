class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            count = 0
            div = 0
            for i in range(1,int(num**0.5) + 1):
                if num % i == 0:
                    count += 1
                    div += i
                    if i*i != num:
                        count += 1
                        div += num//i
            if count == 4:
                result += div
        return result
