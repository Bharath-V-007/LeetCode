class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        total = sum(nums)
        n = len(nums)
        actual_total = n*(n+1)//2
        return actual_total - total
