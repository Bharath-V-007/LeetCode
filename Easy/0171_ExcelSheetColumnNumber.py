class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result *= 26
            result += ord(ch) - 64
        return result
