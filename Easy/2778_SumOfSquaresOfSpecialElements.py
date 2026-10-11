class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        count = 0
        for i,x in enumerate(nums):
            if len(nums)%(i+1)==0:
                count += x*x
        return count
