class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        if n == 1:
            return 1
        for i in range(n):
            if (i == 0 or nums[i] >= nums[i-1]) and (i == n - 1 or nums[i] >= nums[i+1]):
                count += 1
            elif i != 0 and i != n - 1:
                if nums[i] >= (nums[i-1] + nums[i+1]) / 2:
                    count += 1
        return count
