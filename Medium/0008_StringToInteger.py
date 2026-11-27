class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        sign = 1
        more = False
        num_seen = False
        for ch in s:
            if not num_seen and ch == ' ':
                if more:
                    break
                continue
            elif not num_seen and ch == '-':
                if more:
                    break
                more = True
                sign = -1
            elif not num_seen and ch == '+':
                if more:
                    break
                more = True
                sign = 1
            elif ch < '0' or ch > '9':
                break
            else:
                num_seen = True
                num = num * 10 + (ord(ch) - ord('0'))
        num *= sign
        if num < -2 ** 31:
            return -2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return num
