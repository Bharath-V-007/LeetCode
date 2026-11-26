class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        target = max(nums)
        for num in nums:
            moves += target - num
        return moves
