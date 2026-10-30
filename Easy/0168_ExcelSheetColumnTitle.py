class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            num = columnNumber % 26
            result = chr(num + 65) + result
            columnNumber //= 26
        return result
