class Solution:
    def findGCD(self, nums: list[int]) -> int:
        small , large = min(nums) , max(nums)
        while large % small:
            large , small = small , large % small
        return small
