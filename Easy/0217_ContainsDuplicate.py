class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for ch in nums:
            if ch in seen:
                return True 
            else:
                seen.add(ch)
        return False  
