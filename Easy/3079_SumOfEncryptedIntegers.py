class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            largest = 0
            count = 0
            while num > 0:
                digit = num % 10
                largest = max(largest,digit)
                count = count * 10 + 1
                num //= 10
            result += largest * count
        return result
