class Solution:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)
        min_cost = float('inf')
        current , count = nums[0] , 1
        start = 0
        for i in range(1,n):
            if nums[i] == current:
                count += 1
            else:
                end = start + count - 1
                if end >= 1 and start <= n-2:
                    cost = (n - count) * current
                    min_cost = min(min_cost,cost)
                current = nums[i]
                count = 1
                start = i
        end = start + count - 1
        if end >= 1 and start <= n-2:
            cost = (n - count) * current
            min_cost = min(min_cost,cost)
        return min_cost
