class Solution:
    def checkString(self, s: str) -> bool:
        found = False
        for ch in s:
            if found and ch == 'a':
                return False
            if not found and ch == 'b':
                found = True
        return True
