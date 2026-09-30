class Solution:
    def toLowerCase(self, s: str) -> str:
        result=[]
        for ch in s:
            asci=ord(ch)
            if 65<=asci<=90:
                result.append(chr(asci+32))
            else:
                result.append(ch)
        return ''.join(result)
