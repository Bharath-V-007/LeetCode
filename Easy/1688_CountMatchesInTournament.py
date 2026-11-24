class Solution:
    def numberOfMatches(self, n: int) -> int:
        #Each match exactly eliminates one team and after N-1 matches, exactly one team wins
        return n - 1
