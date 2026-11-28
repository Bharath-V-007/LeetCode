class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                pos1 , pos2 = i + j , i + j + 1
                total = result[pos2] + int(num1[i]) * int(num2[j])
                result[pos2] = total % 10
                result[pos1] += total // 10
        result = ''.join(map(str, result))
        return result.lstrip('0')
